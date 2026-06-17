# LLM Benchmark Results

**Task:** [Todo App PRD](../PRD.md) — vanilla JS single-file app
**Last run date:** 2026-06-17 10:42 UTC
**Models tested:** 3

## Results (sorted by total generation time)

| Model | TTFT | Total Time | Prompt Tok | Completion Tok | Total Tok | Speed |
|-------|------|------------|------------|----------------|-----------|-------|
| Qwen3-Coder-Next-FP8 | 2.77s | 53.65s | 1086 | 2423 | 3509 | 45.2 tok/s |
| Qwen/Qwen3.6-35B-A3B | 2.16s | 76.09s | 1127 | 2242 | 3369 | 29.5 tok/s |

## Metric Definitions

| Metric | Description |
|--------|-------------|
| **TTFT** | Time to First Token — latency before output starts |
| **Total Time** | Wall-clock generation time (request → last token) |
| **Prompt Tok** | Tokens consumed by PRD + system message |
| **Completion Tok** | Tokens the model generated |
| **Speed** | Completion tokens ÷ total time |


<!--BENCHMARK_DATA:[
  {
    "model": "Qwen/Qwen3.6-35B-A3B",
    "timestamp": "2026-06-17T10:34:39.495163+00:00",
    "api_url": "http://localhost:9999",
    "ttft": 2.163,
    "total_time": 76.093,
    "prompt_tokens": 1127,
    "completion_tokens": 2242,
    "total_tokens": 3369,
    "tokens_per_sec": 29.5,
    "response_chars": 7584,
    "error": null
  },
  {
    "model": "Qwen3-Coder-Next-FP8",
    "timestamp": "2026-06-17T10:41:33.218370+00:00",
    "api_url": "http://localhost:9999",
    "ttft": 2.769,
    "total_time": 53.648,
    "prompt_tokens": 1086,
    "completion_tokens": 2423,
    "total_tokens": 3509,
    "tokens_per_sec": 45.2,
    "response_chars": 11618,
    "error": null
  }
]-->
