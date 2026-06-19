# LLM Benchmark Results

**Last run date:** 2026-06-19 06:34 UTC
**Entries:** 8

## Results

| Prompt | Model | TTFT | Total Time | Prompt Tok | Completion Tok | Total Tok | Speed |
|--------|-------|------|------------|------------|----------------|-----------|-------|
| SVG Pelican on a Bicycle | Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8 | 0.24s | 16.50s | 63 | 900 | 963 | 54.6 tok/s |
| SVG Pelican on a Bicycle | Qwen3-Coder-Next-FP8 | 0.39s | 38.39s | 63 | 1822 | 1885 | 47.5 tok/s |
| SVG Pelican on a Bicycle | mistralai/Codestral-22B-v0.1 | 0.83s | 80.33s | 65 | 431 | 496 | 5.4 tok/s |
| SVG Pelican on a Bicycle | Qwen/Qwen3.6-35B-A3B | 1.50s | 264.78s | 65 | 7720 | 7785 | 29.2 tok/s |
| Todo App | Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8 | 0.65s | 29.21s | 1082 | 1525 | 2607 | 52.2 tok/s |
| Todo App | Qwen3-Coder-Next-FP8 | 0.84s | 50.05s | 1082 | 2346 | 3428 | 46.9 tok/s |
| Todo App | mistralai/Codestral-22B-v0.1 | 1.12s | 61.13s | 1254 | 324 | 1578 | 5.3 tok/s |
| Todo App | Qwen/Qwen3.6-35B-A3B | 2.13s | 87.11s | 1122 | 2560 | 3682 | 29.4 tok/s |

## Metric Definitions

| Metric | Description |
|--------|-------------|
| **TTFT** | Time to First Token — latency before output starts |
| **Total Time** | Wall-clock generation time (request → last token) |
| **Prompt Tok** | Tokens consumed by the prompt + system message |
| **Completion Tok** | Tokens the model generated |
| **Speed** | Completion tokens ÷ total time |


<!--BENCHMARK_DATA:[{"model": "Qwen3-Coder-Next-FP8", "timestamp": "2026-06-18T06:21:20.816936+00:00", "api_url": "http://localhost:9999", "ttft": 0.386, "total_time": 38.387, "prompt_tokens": 63, "completion_tokens": 1822, "total_tokens": 1885, "tokens_per_sec": 47.5, "response_chars": 4044, "error": null, "prompt": "svg-pelican", "prompt_title": "SVG Pelican on a Bicycle", "_key": "Qwen3-Coder-Next-FP8||svg-pelican"}, {"model": "Qwen3-Coder-Next-FP8", "timestamp": "2026-06-18T06:24:27.368567+00:00", "api_url": "http://localhost:9999", "ttft": 0.844, "total_time": 50.049, "prompt_tokens": 1082, "completion_tokens": 2346, "total_tokens": 3428, "tokens_per_sec": 46.9, "response_chars": 11180, "error": null, "prompt": "todo-app", "prompt_title": "Todo App", "_key": "Qwen3-Coder-Next-FP8||todo-app"}, {"model": "Qwen/Qwen3.6-35B-A3B", "timestamp": "2026-06-18T06:30:58.308019+00:00", "api_url": "http://localhost:9999", "ttft": 2.129, "total_time": 87.112, "prompt_tokens": 1122, "completion_tokens": 2560, "total_tokens": 3682, "tokens_per_sec": 29.4, "response_chars": 8718, "error": null, "prompt": "todo-app", "prompt_title": "Todo App", "_key": "Qwen/Qwen3.6-35B-A3B||todo-app"}, {"model": "Qwen/Qwen3.6-35B-A3B", "timestamp": "2026-06-18T06:56:36.885333+00:00", "api_url": "http://localhost:9999", "ttft": 1.501, "total_time": 264.784, "prompt_tokens": 65, "completion_tokens": 7720, "total_tokens": 7785, "tokens_per_sec": 29.2, "response_chars": 18611, "error": null, "prompt": "svg-pelican", "prompt_title": "SVG Pelican on a Bicycle", "_key": "Qwen/Qwen3.6-35B-A3B||svg-pelican"}, {"model": "mistralai/Codestral-22B-v0.1", "timestamp": "2026-06-19T06:10:09.514524+00:00", "api_url": "http://localhost:9999", "ttft": 0.835, "total_time": 80.331, "prompt_tokens": 65, "completion_tokens": 431, "total_tokens": 496, "tokens_per_sec": 5.4, "response_chars": 749, "error": null, "prompt": "svg-pelican", "prompt_title": "SVG Pelican on a Bicycle", "_key": "mistralai/Codestral-22B-v0.1||svg-pelican"}, {"model": "mistralai/Codestral-22B-v0.1", "timestamp": "2026-06-19T06:11:49.991527+00:00", "api_url": "http://localhost:9999", "ttft": 1.117, "total_time": 61.132, "prompt_tokens": 1254, "completion_tokens": 324, "total_tokens": 1578, "tokens_per_sec": 5.3, "response_chars": 1026, "error": null, "prompt": "todo-app", "prompt_title": "Todo App", "_key": "mistralai/Codestral-22B-v0.1||todo-app"}, {"model": "Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8", "timestamp": "2026-06-19T06:24:19.604835+00:00", "api_url": "http://localhost:9999", "ttft": 0.645, "total_time": 29.208, "prompt_tokens": 1082, "completion_tokens": 1525, "total_tokens": 2607, "tokens_per_sec": 52.2, "response_chars": 6431, "error": null, "prompt": "todo-app", "prompt_title": "Todo App", "_key": "Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8||todo-app"}, {"model": "Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8", "timestamp": "2026-06-19T06:34:22.129355+00:00", "api_url": "http://localhost:9999", "ttft": 0.241, "total_time": 16.496, "prompt_tokens": 63, "completion_tokens": 900, "total_tokens": 963, "tokens_per_sec": 54.6, "response_chars": 1764, "error": null, "prompt": "svg-pelican", "prompt_title": "SVG Pelican on a Bicycle", "_key": "Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8||svg-pelican"}]-->
