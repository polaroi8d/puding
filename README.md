# puding 🥣

tldr; 

I have access to an Nvidia Spark GX10 with 128GB unified memory and in this AI chaos my friends always ask about the performance, and how it can be used for agentic coding tasks, so I created this small repo to showcase them what and how it performs. 

My plan is to add more models & prompts to test the ability of those models. 

LLM benchmark on GB10 (Nvidia Spark GX10 with 128GB unified memory). Sends a coding task to any OpenAI-compatible API, measures speed and token usage, and extracts the generated `index.html` per model.

Running the models with with vLLM, but planning to add more inference engine.

The [benchmark.py script](benchmark.py) generated mainly by using Opus 4.8

See [Getting started](docs/getting-started.md) for usage, output layout, metrics, and requirements.

## Results

Full results: [summary.md](summary.md)

## Tested models

| Model | Release | Hugging Face | Website / resources | Benchmarks |
|-------|------------|--------------|---------------------|------------|
| [Qwen3.6-35B-A3B](https://huggingface.co/Qwen/Qwen3.6-35B-A3B) | 2026-04-15 | [Qwen/Qwen3.6-35B-A3B](https://huggingface.co/Qwen/Qwen3.6-35B-A3B) | [Blog](https://qwen.ai/blog?id=qwen3.6-35b-a3b) · [GitHub](https://github.com/QwenLM/Qwen3.6) · [ModelScope](https://modelscope.cn/collections/Qwen/Qwen36) | [results](models/Qwen-Qwen3.6-35B-A3B/) |
| [Qwen3-Coder-30B-A3B-Instruct-FP8](https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8) | 2025-07-31 | [Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8](https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8) | [GitHub](https://github.com/QwenLM/Qwen3-Coder) · [Qwen](https://qwen.ai) | [results](models/Qwen-Qwen3-Coder-30B-A3B-Instruct-FP8/) |
| [Qwen3-Coder-Next-FP8](https://huggingface.co/Qwen/Qwen3-Coder-Next-FP8) | 2026-02-01 | [Qwen/Qwen3-Coder-Next-FP8](https://huggingface.co/Qwen/Qwen3-Coder-Next-FP8) | [GitHub](https://github.com/QwenLM/Qwen3-Coder) · [Tech report](https://github.com/QwenLM/Qwen3-Coder/blob/main/qwen3_coder_next_tech_report.pdf) | [results](models/Qwen3-Coder-Next-FP8/) |
| [Codestral-22B-v0.1](https://huggingface.co/mistralai/Codestral-22B-v0.1) | 2024-05-29 | [mistralai/Codestral-22B-v0.1](https://huggingface.co/mistralai/Codestral-22B-v0.1) | [Blog](https://mistral.ai/news/codestral) · [Mistral](https://mistral.ai) | [results](models/mistralai-Codestral-22B-v0.1/) |
