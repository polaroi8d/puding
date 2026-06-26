# LLM Benchmark Results

**Last run date:** 2026-06-26 13:38 UTC
**Entries:** 14

## Results

| Prompt | Model | TTFT | Total Time | Prompt Tok | Completion Tok | Total Tok | Speed |
|--------|-------|------|------------|------------|----------------|-----------|-------|
| SVG Pelican on a Bicycle | openai/gpt-oss-20b | 2.99s | 12.26s | 124 | 511 | 635 | 41.7 tok/s |
| SVG Pelican on a Bicycle | Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8 | 0.24s | 16.50s | 63 | 900 | 963 | 54.6 tok/s |
| SVG Pelican on a Bicycle | Qwen3-Coder-Next-FP8 | 0.39s | 38.39s | 63 | 1822 | 1885 | 47.5 tok/s |
| SVG Pelican on a Bicycle | mistralai/Codestral-22B-v0.1 | 0.83s | 80.33s | 65 | 431 | 496 | 5.4 tok/s |
| SVG Pelican on a Bicycle | Ornith-1.0-35B | 0.38s | 106.25s | 65 | 3168 | 3233 | 29.8 tok/s |
| SVG Pelican on a Bicycle | Qwen/Qwen3.6-35B-A3B | 1.50s | 264.78s | 65 | 7720 | 7785 | 29.2 tok/s |
| SVG Pelican on a Bicycle | Qwen/Qwen-AgentWorld-35B-A3B | 1.44s | 528.34s | 65 | 15552 | 15617 | 29.4 tok/s |
| Todo App | Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8 | 0.65s | 29.21s | 1082 | 1525 | 2607 | 52.2 tok/s |
| Todo App | openai/gpt-oss-20b | 9.48s | 36.04s | 1146 | 1613 | 2759 | 44.8 tok/s |
| Todo App | Qwen3-Coder-Next-FP8 | 0.84s | 50.05s | 1082 | 2346 | 3428 | 46.9 tok/s |
| Todo App | mistralai/Codestral-22B-v0.1 | 1.12s | 61.13s | 1254 | 324 | 1578 | 5.3 tok/s |
| Todo App | Ornith-1.0-35B | 0.70s | 77.96s | 1122 | 2305 | 3427 | 29.6 tok/s |
| Todo App | Qwen/Qwen3.6-35B-A3B | 2.13s | 87.11s | 1122 | 2560 | 3682 | 29.4 tok/s |
| Todo App | Qwen/Qwen-AgentWorld-35B-A3B | 1.92s | 336.83s | 1122 | 9909 | 11031 | 29.4 tok/s |

## Metric Definitions

| Metric | Description |
|--------|-------------|
| **TTFT** | Time to First Token — latency before output starts |
| **Total Time** | Wall-clock generation time (request → last token) |
| **Prompt Tok** | Tokens consumed by the prompt + system message |
| **Completion Tok** | Tokens the model generated |
| **Speed** | Completion tokens ÷ total time |

