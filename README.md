# puding 🥣

LLM benchmark harness on GB10 (Nvidia Spark GX10 with 128GB unified memory). Sends a coding task to any OpenAI-compatible API, measures speed and token usage, and extracts the generated `index.html` per model.

## What it does

1. Sends `PRD.md` to one or more models via streaming chat completion
2. Extracts the generated `index.html` from the response
3. Writes extracted files to `models/<name>/app/` and a comparison table to `results/summary.md`

## Usage

```sh
python benchmark.py --models gpt-4o claude-sonnet-4-6
python benchmark.py --models gpt-4o --url http://localhost:9999
python benchmark.py --list-models                 # show past runs
```

Default API URL: `http://localhost:9999`

## Output structure

```
models/
  <model-slug>/
    app/           # extracted source files
results/
  summary.md       # cross-model comparison table
```

## Metrics captured

| Metric | Description |
|--------|-------------|
| TTFT | Time to first token |
| Total time | Wall-clock generation time |
| Tokens/sec | Completion throughput |

## Requirements

```sh
pip install openai rich
```

## Results

Full results: [results/summary.md](results/summary.md)

**Tested models:**
- [Qwen3.6-35B-A3B](models/Qwen3.6-35B-A3B/)
- [Qwen3-Coder-Next-FP8](models/Qwen3-Coder-Next-FP8/)
