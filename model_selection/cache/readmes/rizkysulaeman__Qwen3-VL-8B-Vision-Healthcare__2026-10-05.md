---
tags:
- gguf
- llama.cpp
- unsloth
- vision-language-model
license: mit
datasets:
- unsloth/Radiology_mini
language:
- id
- en
metrics:
- accuracy
base_model:
- unsloth/Qwen3-VL-8B-Instruct-unsloth-bnb-4bit
pipeline_tag: image-text-to-text
---

# Qwen3-VL-8B-Vision-Healthcare : GGUF

This model was finetuned and converted to GGUF format using [Unsloth](https://github.com/unslothai/unsloth).

**Example usage**:
- For text only LLMs:    `./llama.cpp/llama-cli -hf rizkysulaeman/Qwen3-VL-8B-Vision-Healthcare --jinja`
- For multimodal models: `./llama.cpp/llama-mtmd-cli -hf rizkysulaeman/Qwen3-VL-8B-Vision-Healthcare --jinja`

## Available Model files:
- `qwen3-vl-8b-instruct.Q5_K_M.gguf`
- `qwen3-vl-8b-instruct.Q8_0.gguf`
- `qwen3-vl-8b-instruct.Q4_K_M.gguf`
- `qwen3-vl-8b-instruct.F16-mmproj.gguf`
This was trained 2x faster with [Unsloth](https://github.com/unslothai/unsloth)
[<img src="https://raw.githubusercontent.com/unslothai/unsloth/main/images/unsloth%20made%20with%20love.png" width="200"/>](https://github.com/unslothai/unsloth)