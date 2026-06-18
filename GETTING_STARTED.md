# Getting started

## What it does

1. Sends a prompt from `prompts/` to one or more models via streaming chat completion
2. Extracts generated files from the response
3. Writes extracted files to `models/<model>/<prompt>/` and appends a row to `summary.md` at the project root

## Usage

```sh
python3 benchmark.py --list-prompts               # show available prompts
python3 benchmark.py --list-models                # show past runs

python3 benchmark.py --prompt todo-app --models gpt-4o claude-sonnet-4-6
python3 benchmark.py --prompt svg-pelican --models qwen3 --url http://localhost:9999
```

Default API URL: `http://localhost:9999`

## Output structure

```
prompts/
  todo-app.md        # prompt + optional frontmatter
  svg-pelican.md
models/
  <model-slug>/
    <prompt-slug>/
      app/           # extracted source files
summary.md           # all runs, all prompts — one table
```

## Adding a new prompt

Create a `.md` file in `prompts/`. Frontmatter is optional:

```markdown
---
title: My Prompt
system: You are an expert... Output only a fenced code block.
---
Your prompt text here.
```

Without frontmatter, the default web-developer system prompt is used.

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
