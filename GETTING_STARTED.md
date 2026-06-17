# Getting started

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
