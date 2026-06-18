# puding 🥣

tldr; 

I have access to an Nvidia Spark GX10 with 128GB unified memory and in this AI chaos my friends always ask about the performance, and how it can be used for agentic coding tasks, so I created this small repo to showcase them what and how it performs. 

My plan is to add more models & prompts to test the ability of those models. 

LLM benchmark on GB10 (Nvidia Spark GX10 with 128GB unified memory). Sends a coding task to any OpenAI-compatible API, measures speed and token usage, and extracts the generated `index.html` per model.

Running the models with with vLLM, but planning to add more inference. If you have any other hw and want to contribute, feel free to add your benchmark tests. 

The [benchmark.py script](benchmark.py) generated mainly by using Opus 4.8

See [Getting started](docs/getting-started.md) for usage, output layout, metrics, and requirements.

## Results

Full results: [summary.md](summary.md)

**Tested models:**
- [Qwen3.6-35B-A3B](models/Qwen3.6-35B-A3B/)
- [Qwen3-Coder-Next-FP8](models/Qwen3-Coder-Next-FP8/)
