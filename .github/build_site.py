#!/usr/bin/env python3
"""Build the GitHub Pages site for puding.

Layout on disk: models/{model}/{prompt}/ — each folder is one self-contained
result: an artifact (pelican.svg | index.html) and/or a result.json with that
run's metrics. Add/remove/edit a result by adding/removing/editing its folder.

Produces _site/index.html: repo description, then one section per model with a
metrics table whose Prompt column links to that model's generated result.
"""
import html
import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / "_site"

DESCRIPTION = (
    "LLM benchmark on a GB10 (Nvidia Spark GX10, 128GB unified memory). "
    "Each model gets the same coding prompts via an OpenAI-compatible API; "
    "I record speed and token usage, and keep the generated artifact "
    "(an SVG or a single-file app) so you can open it below."
    " Github: https://github.com/polaroi8d/puding"
)

COLS = [
    ("ttft", "TTFT", "s"),
    ("total_time", "Total Time", "s"),
    ("prompt_tokens", "Prompt Tok", ""),
    ("completion_tokens", "Completion Tok", ""),
    ("total_tokens", "Total Tok", ""),
    ("tokens_per_sec", "Speed", " tok/s"),
]


def cell(val, suffix):
    if val is None:
        return "—"
    return f"{val}{suffix}" if suffix else str(val)


def copy_artifact(src, dst):
    """Copy a result file. For SVGs, inject a full-bleed black background as the
    first child so the pelican renders on black when opened directly."""
    if src.suffix != ".svg":
        shutil.copy(src, dst)
        return
    import re
    svg = re.sub(r"(<svg\b[^>]*>)",
                 r'\1<rect width="100%" height="100%" fill="#000"/>',
                 src.read_text(), count=1, flags=re.IGNORECASE)
    dst.write_text(svg)


def main():
    import re  # noqa: F401  (used by copy_artifact)
    assert '<rect/>' in re.sub(r"(<svg\b[^>]*>)", r'\1<rect/>',
                               '<svg x="0"><g/></svg>', count=1), "svg bg regex broke"
    if SITE.exists():
        shutil.rmtree(SITE)
    SITE.mkdir(parents=True)

    # One pass over the folder tree: copy artifacts, read metrics.
    # models: folder_name -> {"display": str, "prompts": {prompt: {link, metrics}}}
    models, titles = {}, {}
    for prompt_dir in sorted((ROOT / "models").glob("*/*")):
        if not prompt_dir.is_dir():
            continue
        model, prompt = prompt_dir.parent.name, prompt_dir.name
        entry = next((f for f in sorted(prompt_dir.iterdir())
                      if f.suffix in (".html", ".svg")), None)
        link = None
        if entry:
            dest = SITE / model / prompt
            dest.mkdir(parents=True, exist_ok=True)
            copy_artifact(entry, dest / entry.name)
            link = f"{model}/{prompt}/{entry.name}"

        rj = prompt_dir / "result.json"
        metrics = json.loads(rj.read_text()) if rj.exists() else None

        m = models.setdefault(model, {"display": model, "prompts": {}})
        if metrics:
            m["display"] = metrics.get("model") or model
            titles[prompt] = metrics.get("prompt_title") or prompt
        m["prompts"][prompt] = {"link": link, "metrics": metrics}

    out = [
        "<!doctype html><html><head><meta charset=utf-8>",
        "<title>puding — model results</title>",
        "<style>body{font-family:system-ui,sans-serif;max-width:900px;margin:2rem auto;padding:0 1rem;line-height:1.5}",
        "h2{margin-top:2.5rem}table{border-collapse:collapse;width:100%;font-size:.9rem}",
        "th,td{border:1px solid #ddd;padding:.4rem .6rem;text-align:left}",
        "th{background:#f5f5f5}.muted{color:#999}</style></head><body>",
        "<h1>puding 🥣 — model results</h1>",
        f"<p>{html.escape(DESCRIPTION)}</p>",
    ]

    for model in sorted(models):
        out.append(f"<h2>{html.escape(models[model]['display'])}</h2><table><tr><th>Prompt</th>"
                   + "".join(f"<th>{label}</th>" for _, label, _ in COLS) + "</tr>")
        for prompt in sorted(models[model]["prompts"]):
            rec = models[model]["prompts"][prompt]
            link, e = rec["link"], rec["metrics"]
            title = html.escape(titles.get(prompt, prompt))
            name = f'<a href="{link}">{title}</a>' if link else f'<span class="muted">{title}</span>'
            if e and e.get("error"):
                cells = f'<td colspan="{len(COLS)}" class="muted">{html.escape(e["error"])}</td>'
            elif e:
                cells = "".join(f"<td>{cell(e.get(k), suf)}</td>" for k, _, suf in COLS)
            else:
                cells = f'<td colspan="{len(COLS)}" class="muted">no run recorded</td>'
            out.append(f"<tr><td>{name}</td>{cells}</tr>")
        out.append("</table>")

    out.append("</body></html>")
    (SITE / "index.html").write_text("\n".join(out))
    print(f"Built _site/index.html: {len(models)} models")


if __name__ == "__main__":
    main()
