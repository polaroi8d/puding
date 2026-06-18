# LLM Benchmark Results

**Last run date:** 2026-06-18 06:38 UTC
**Entries:** 4

## Results

| Prompt | Model | TTFT | Total Time | Prompt Tok | Completion Tok | Total Tok | Speed |
|--------|-------|------|------------|------------|----------------|-----------|-------|
| SVG Pelican on a Bicycle | Qwen3-Coder-Next-FP8 | 0.39s | 38.39s | 63 | 1822 | 1885 | 47.5 tok/s |
| SVG Pelican on a Bicycle | Qwen/Qwen3.6-35B-A3B | 0.36s | 323.84s | 65 | 9686 | 9751 | 29.9 tok/s |
| Todo App | Qwen3-Coder-Next-FP8 | 0.84s | 50.05s | 1082 | 2346 | 3428 | 46.9 tok/s |
| Todo App | Qwen/Qwen3.6-35B-A3B | 2.13s | 87.11s | 1122 | 2560 | 3682 | 29.4 tok/s |

## Metric Definitions

| Metric | Description |
|--------|-------------|
| **TTFT** | Time to First Token — latency before output starts |
| **Total Time** | Wall-clock generation time (request → last token) |
| **Prompt Tok** | Tokens consumed by the prompt + system message |
| **Completion Tok** | Tokens the model generated |
| **Speed** | Completion tokens ÷ total time |


<!--BENCHMARK_DATA:[{"model": "Qwen3-Coder-Next-FP8", "timestamp": "2026-06-18T06:21:20.816936+00:00", "api_url": "http://localhost:9999", "ttft": 0.386, "total_time": 38.387, "prompt_tokens": 63, "completion_tokens": 1822, "total_tokens": 1885, "tokens_per_sec": 47.5, "response_chars": 4044, "error": null, "prompt": "svg-pelican", "prompt_title": "SVG Pelican on a Bicycle", "_key": "Qwen3-Coder-Next-FP8||svg-pelican"}, {"model": "Qwen3-Coder-Next-FP8", "timestamp": "2026-06-18T06:24:27.368567+00:00", "api_url": "http://localhost:9999", "ttft": 0.844, "total_time": 50.049, "prompt_tokens": 1082, "completion_tokens": 2346, "total_tokens": 3428, "tokens_per_sec": 46.9, "response_chars": 11180, "error": null, "prompt": "todo-app", "prompt_title": "Todo App", "_key": "Qwen3-Coder-Next-FP8||todo-app"}, {"model": "Qwen/Qwen3.6-35B-A3B", "timestamp": "2026-06-18T06:30:58.308019+00:00", "api_url": "http://localhost:9999", "ttft": 2.129, "total_time": 87.112, "prompt_tokens": 1122, "completion_tokens": 2560, "total_tokens": 3682, "tokens_per_sec": 29.4, "response_chars": 8718, "error": null, "prompt": "todo-app", "prompt_title": "Todo App", "_key": "Qwen/Qwen3.6-35B-A3B||todo-app"}, {"model": "Qwen/Qwen3.6-35B-A3B", "timestamp": "2026-06-18T06:32:42.497385+00:00", "api_url": "http://localhost:9999", "ttft": 0.365, "total_time": 323.839, "prompt_tokens": 65, "completion_tokens": 9686, "total_tokens": 9751, "tokens_per_sec": 29.9, "response_chars": 23775, "error": null, "prompt": "svg-pelican", "prompt_title": "SVG Pelican on a Bicycle", "_key": "Qwen/Qwen3.6-35B-A3B||svg-pelican"}]-->
