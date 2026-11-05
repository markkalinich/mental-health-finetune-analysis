---
tags:
- gguf
- llama.cpp
- unsloth
license: gemma
datasets:
- aldsouza/health-agent-dataset
language:
- id
- en
pipeline_tag: any-to-any
---

# FunctionGemma-270M-Healthcare : GGUF

This model was finetuned and converted to GGUF format using [Unsloth](https://github.com/unslothai/unsloth).

**Example usage**:
- For text only LLMs:    `./llama.cpp/llama-cli -hf rizkysulaeman/FunctionGemma-270M-Healthcare --jinja`
- For multimodal models: `./llama.cpp/llama-mtmd-cli -hf rizkysulaeman/FunctionGemma-270M-Healthcare --jinja`

## Available Model files:
- `functiongemma-270m-it.F16.gguf`

## Note
The model's BOS token behavior was adjusted for GGUF compatibility.
This was trained 2x faster with [Unsloth](https://github.com/unslothai/unsloth)
[<img src="https://raw.githubusercontent.com/unslothai/unsloth/main/images/unsloth%20made%20with%20love.png" width="200"/>](https://github.com/unslothai/unsloth)