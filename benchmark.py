#!/usr/bin/env python3
"""
LLM Benchmark — sends PRD.md to models via OpenAI-compatible API, measures
token usage and speed, and extracts generated source files.

Usage:
    python benchmark.py --models gpt-4o llama-3-70b
    python benchmark.py --models gpt-4o --url http://localhost:9999
    python benchmark.py --list-models
"""

import argparse
import json
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

from openai import OpenAI
from rich.console import Console
from rich.progress import (
    BarColumn,
    Progress,
    SpinnerColumn,
    TextColumn,
    TimeElapsedColumn,
)
from rich.table import Table

SCRIPT_DIR = Path(__file__).parent
PROMPTS_DIR = SCRIPT_DIR / "prompts"
MODELS_DIR = SCRIPT_DIR / "models"
SUMMARY_PATH = SCRIPT_DIR / "summary.md"

DEFAULT_SYSTEM = (
    "You are an expert web developer. "
    "Implement exactly what the spec says. "
    "Output the file as a fenced html code block. No extra commentary."
)


def load_prompt(slug_or_path: str) -> tuple[str, dict]:
    path = Path(slug_or_path)
    if not path.exists():
        path = PROMPTS_DIR / f"{slug_or_path}.md"
    text = path.read_text(encoding="utf-8")
    meta: dict = {}
    if text.startswith("---\n"):
        end = text.index("\n---\n", 4)
        for line in text[4:end].splitlines():
            if ": " in line:
                k, v = line.split(": ", 1)
                meta[k.strip()] = v.strip()
        text = text[end + 5 :]
    return text, meta


console = Console()

# ── File extraction ────────────────────────────────────────────────────────────

KNOWN_FILES = [
    "index.html",
]

FILENAME_COMMENT_RE = re.compile(
    r"^(?://|<!--|#|/\*)\s*([\w./\-]+\.\w+)(?:\s*-->|\s*\*/)?\s*$",
    re.MULTILINE,
)
FENCED_BLOCK_RE = re.compile(r"```(?P<lang>\w*)\n(?P<body>.*?)```", re.DOTALL)
BRACKET_FILENAME_RE = re.compile(r"\[([^\]]+\.\w+)\]")


def extract_files(response_text: str) -> dict[str, str]:
    files: dict[str, str] = {}
    used_known: set[str] = set()

    for match in FENCED_BLOCK_RE.finditer(response_text):
        lang = match.group("lang").lower()
        body = match.group("body")
        preceding = response_text[max(0, match.start() - 200) : match.start()]
        fname = None

        bracket = BRACKET_FILENAME_RE.findall(preceding)
        if bracket:
            fname = bracket[-1]

        if not fname:
            heading = re.findall(
                r"(?:\*\*|`)?([^\s`*\n]+\.[a-z]+)(?:\*\*|`)?\s*$", preceding.strip()
            )
            if heading:
                fname = heading[-1]

        if not fname:
            first_line = body.split("\n")[0]
            cm = FILENAME_COMMENT_RE.match(first_line)
            if cm:
                fname = cm.group(1)
                body = "\n".join(body.split("\n")[1:])

        if not fname:
            if (
                lang == "html"
                and "index.html" not in used_known
                and "<!DOCTYPE" in body
            ):
                fname = "index.html"

        if fname:
            fname = fname.lstrip("./").replace("\\", "/")
            files[fname] = body.rstrip("\n")
            used_known.add(fname)

    return files


# ── Benchmark runner ───────────────────────────────────────────────────────────


def sanitize_model_name(model: str) -> str:
    return re.sub(r"[/:]+", "-", model).strip("-")


def run_benchmark(
    model: str, prd: str, api_url: str, system_prompt: str = DEFAULT_SYSTEM
) -> dict:
    client = OpenAI(base_url=f"{api_url.rstrip('/')}/v1", api_key="benchmark")

    metrics: dict = {
        "model": model,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "api_url": api_url,
        "ttft": None,
        "total_time": None,
        "prompt_tokens": None,
        "completion_tokens": None,
        "total_tokens": None,
        "tokens_per_sec": None,
        "response_chars": 0,
        "error": None,
    }

    full_text = ""
    t_first_token = None

    progress = Progress(
        SpinnerColumn(),
        TextColumn("[bold blue]{task.description}"),
        BarColumn(bar_width=30),
        TextColumn("{task.fields[tokens]} tok"),
        TimeElapsedColumn(),
        console=console,
        transient=True,
    )
    task_id = progress.add_task(f"[cyan]{model}", total=None, tokens=0)

    try:
        t_start = time.perf_counter()
        stream = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prd},
            ],
            stream=True,
            stream_options={"include_usage": True},
        )

        completion_tokens = 0
        with progress:
            for chunk in stream:
                content = ""
                if chunk.choices:
                    delta = chunk.choices[0].delta
                    if delta and delta.content:
                        content = delta.content
                if content:
                    if t_first_token is None:
                        t_first_token = time.perf_counter()
                    full_text += content
                    completion_tokens += 1
                    progress.update(task_id, tokens=completion_tokens)
                if hasattr(chunk, "usage") and chunk.usage:
                    u = chunk.usage
                    metrics["prompt_tokens"] = u.prompt_tokens
                    metrics["completion_tokens"] = u.completion_tokens
                    metrics["total_tokens"] = u.total_tokens

        t_end = time.perf_counter()
        metrics["ttft"] = round(t_first_token - t_start, 3) if t_first_token else None
        metrics["total_time"] = round(t_end - t_start, 3)
        metrics["response_chars"] = len(full_text)
        ct = metrics["completion_tokens"] or completion_tokens
        if ct and metrics["total_time"]:
            metrics["tokens_per_sec"] = round(ct / metrics["total_time"], 1)

    except Exception as exc:
        metrics["error"] = str(exc)
        console.print(f"[red]Error: {exc}[/red]")

    metrics["_response"] = full_text
    return metrics


# ── Output writers ─────────────────────────────────────────────────────────────


def write_app_files(
    model_slug: str, files: dict[str, str], prompt_slug: str = ""
) -> Path:
    app_dir = (
        MODELS_DIR / model_slug / prompt_slug / "app"
        if prompt_slug
        else MODELS_DIR / model_slug / "app"
    )
    for rel_path, content in files.items():
        dest = app_dir / rel_path
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(content, encoding="utf-8")
    return app_dir


def fmt(val, suffix="", precision=2):
    if val is None:
        return "—"
    if isinstance(val, float):
        return f"{val:.{precision}f}{suffix}"
    return f"{val}{suffix}"


def write_summary(all_metrics: list[dict], prompt_slug: str, prompt_title: str) -> Path:
    existing: dict[str, dict] = {}
    if SUMMARY_PATH.exists():
        hit = re.search(
            r"<!--BENCHMARK_DATA:(.*?)-->", SUMMARY_PATH.read_text(), re.DOTALL
        )
        if hit:
            existing = {e["_key"]: e for e in json.loads(hit.group(1))}

    for m in all_metrics:
        m["prompt"] = prompt_slug
        m["prompt_title"] = prompt_title
        m["_key"] = f"{m['model']}||{prompt_slug}"
    existing.update({m["_key"]: m for m in all_metrics})

    sorted_m = sorted(
        existing.values(),
        key=lambda m: (
            m.get("prompt", ""),
            m.get("total_time") is None,
            m.get("total_time") or 0,
        ),
    )

    rows = ""
    for m in sorted_m:
        rows += (
            f"| {m.get('prompt_title', m.get('prompt', '—'))} "
            f"| {m['model']} "
            f"| {fmt(m['ttft'], 's')} "
            f"| {fmt(m['total_time'], 's')} "
            f"| {fmt(m['prompt_tokens'])} "
            f"| {fmt(m['completion_tokens'])} "
            f"| {fmt(m['total_tokens'])} "
            f"| {fmt(m['tokens_per_sec'], ' tok/s', 1)} |\n"
        )

    run_date = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    content = f"""# LLM Benchmark Results

**Last run date:** {run_date}
**Entries:** {len(sorted_m)}

## Results

| Prompt | Model | TTFT | Total Time | Prompt Tok | Completion Tok | Total Tok | Speed |
|--------|-------|------|------------|------------|----------------|-----------|-------|
{rows}
## Metric Definitions

| Metric | Description |
|--------|-------------|
| **TTFT** | Time to First Token — latency before output starts |
| **Total Time** | Wall-clock generation time (request → last token) |
| **Prompt Tok** | Tokens consumed by the prompt + system message |
| **Completion Tok** | Tokens the model generated |
| **Speed** | Completion tokens ÷ total time |

"""
    content += f"\n<!--BENCHMARK_DATA:{json.dumps(list(existing.values()))}-->\n"
    SUMMARY_PATH.write_text(content, encoding="utf-8")
    return SUMMARY_PATH


# ── Rich terminal table ────────────────────────────────────────────────────────


def print_summary_table(all_metrics: list[dict]):
    table = Table(
        title="Benchmark Results", show_header=True, header_style="bold magenta"
    )
    table.add_column("Prompt", style="yellow", no_wrap=True)
    table.add_column("Model", style="cyan", no_wrap=True)
    table.add_column("TTFT", justify="right")
    table.add_column("Total", justify="right")
    table.add_column("Prompt tok", justify="right")
    table.add_column("Compl tok", justify="right")
    table.add_column("tok/s", justify="right")

    for m in sorted(
        all_metrics,
        key=lambda x: (x.get("total_time") is None, x.get("total_time") or 0),
    ):
        table.add_row(
            m.get("prompt_title", m.get("prompt", "—")),
            m["model"],
            fmt(m["ttft"], "s"),
            fmt(m["total_time"], "s"),
            fmt(m["prompt_tokens"]),
            fmt(m["completion_tokens"]),
            fmt(m["tokens_per_sec"], "", 1),
        )

    console.print(table)


# ── List ───────────────────────────────────────────────────────────────────────


def list_models():
    if not MODELS_DIR.exists():
        console.print(
            "[yellow]No models directory yet — run a benchmark first.[/yellow]"
        )
        return
    models = [d.name for d in MODELS_DIR.iterdir() if d.is_dir()]
    if not models:
        console.print("[yellow]No model results found.[/yellow]")
        return
    console.print("[bold]Previously benchmarked models:[/bold]")
    for m in sorted(models):
        console.print(f"  • {m}")


def list_prompts():
    if not PROMPTS_DIR.exists():
        console.print("[yellow]No prompts directory found.[/yellow]")
        return
    files = sorted(PROMPTS_DIR.glob("*.md"))
    if not files:
        console.print("[yellow]No prompts found in prompts/.[/yellow]")
        return
    console.print("[bold]Available prompts:[/bold]")
    for f in files:
        _, meta = load_prompt(str(f))
        title = meta.get("title", f.stem)
        console.print(f"  • [cyan]{f.stem}[/cyan]  {title}")


# ── CLI ────────────────────────────────────────────────────────────────────────


def main():
    parser = argparse.ArgumentParser(
        description="LLM benchmark — runs a prompt against one or more models"
    )
    parser.add_argument(
        "--models", nargs="+", metavar="MODEL", help="Model IDs to benchmark"
    )
    parser.add_argument(
        "--prompt",
        metavar="SLUG",
        help="Prompt to use (slug from prompts/, e.g. todo-app)",
    )
    parser.add_argument(
        "--url", default="http://localhost:9999", help="OpenAI-compatible API base URL"
    )
    parser.add_argument(
        "--list-models", action="store_true", help="List previously benchmarked models"
    )
    parser.add_argument(
        "--list-prompts", action="store_true", help="List available prompts"
    )
    parser.add_argument(
        "--no-extract", action="store_true", help="Skip file extraction"
    )
    args = parser.parse_args()

    if args.list_models:
        list_models()
        return

    if args.list_prompts:
        list_prompts()
        return

    if not args.models:
        parser.print_help()
        sys.exit(1)

    if not args.prompt:
        console.print(
            "[red]--prompt is required. Use --list-prompts to see available options.[/red]"
        )
        list_prompts()
        sys.exit(1)

    try:
        prd, meta = load_prompt(args.prompt)
    except FileNotFoundError:
        console.print(f"[red]Prompt not found: {args.prompt}[/red]")
        list_prompts()
        sys.exit(1)

    prompt_slug = Path(args.prompt).stem if Path(args.prompt).exists() else args.prompt
    prompt_title = meta.get("title", prompt_slug)
    system_prompt = meta.get("system", DEFAULT_SYSTEM)

    all_metrics: list[dict] = []

    for model in args.models:
        slug = sanitize_model_name(model)
        console.rule(f"[bold cyan]{model}[/bold cyan]")

        metrics = run_benchmark(model, prd, args.url, system_prompt)

        files: dict[str, str] = {}
        if not args.no_extract and not metrics.get("error"):
            files = extract_files(metrics.get("_response", ""))

        if files and not args.no_extract:
            app_dir = write_app_files(slug, files, prompt_slug)
            console.print(
                f"[green]Extracted {len(files)} file(s) → {app_dir.relative_to(SCRIPT_DIR)}[/green]"
            )

        summary_metrics = {k: v for k, v in metrics.items() if k != "_response"}
        all_metrics.append(summary_metrics)

    if all_metrics:
        summary_path = write_summary(all_metrics, prompt_slug, prompt_title)
        console.print(
            f"\n[dim]Summary → {summary_path.relative_to(SCRIPT_DIR)}[/dim]\n"
        )
        print_summary_table(all_metrics)


if __name__ == "__main__":
    main()
