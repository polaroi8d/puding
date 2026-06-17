# LLM Benchmark Results

## Results

| Model | TTFT | Total Time | Prompt Tok | Completion Tok | Total Tok | Speed |
|-------|------|------------|------------|----------------|-----------|-------|
| Qwen3-Coder-Next-FP8 | 2.71s | 50.79s | 1086 | 2313 | 3399 | 45.5 tok/s |
| Qwen3.6-35B-A3B | 0.66s | 79.75s | 1127 | 2410 | 3537 | 30.2 tok/s |

### Metric Definitions

| Metric | Description |
|--------|-------------|
| **TTFT** | Time to First Token — latency before output starts |
| **Total Time** | Wall-clock generation time (request → last token) |
| **Prompt Tok** | Tokens consumed by PRD + system message |
| **Completion Tok** | Tokens the model generated |
| **Speed** | Completion tokens ÷ total time |
