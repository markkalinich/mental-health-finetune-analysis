---
tags:
- gguf
- llama.cpp
- unsloth
license: mit
language:
- en
- id
base_model:
- unsloth/Qwen2.5-1.5B-Instruct
pipeline_tag: reinforcement-learning
---

# Qwen-3-GRPO-Healthcare-Deep-Search : GGUF

This model was finetuned and converted to GGUF format using [Unsloth](https://github.com/unslothai/unsloth).

**Example usage**:
- For text only LLMs:    `./llama.cpp/llama-cli -hf rizkysulaeman/Qwen-3-GRPO-Healthcare-Deep-Search --jinja`
- For multimodal models: `./llama.cpp/llama-mtmd-cli -hf rizkysulaeman/Qwen-3-GRPO-Healthcare-Deep-Search --jinja`

## Available Model files:
- `Qwen-3-GRPO-Healthcare-Deep-Search.Q5_K_M.gguf`
- `Qwen-3-GRPO-Healthcare-Deep-Search.Q8_0.gguf`
- `Qwen-3-GRPO-Healthcare-Deep-Search.Q4_K_M.gguf`
This was trained 2x faster with [Unsloth](https://github.com/unslothai/unsloth)
[<img src="https://raw.githubusercontent.com/unslothai/unsloth/main/images/unsloth%20made%20with%20love.png" width="200"/>](https://github.com/unslothai/unsloth)