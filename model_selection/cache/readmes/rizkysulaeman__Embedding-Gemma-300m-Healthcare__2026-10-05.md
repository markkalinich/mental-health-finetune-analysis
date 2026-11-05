---
tags:
- gguf
- llama.cpp
- unsloth
- sentence-transformers
license: mit
datasets:
- qiaojin/PubMedQA
language:
- en
- id
base_model:
- unsloth/embeddinggemma-300m
pipeline_tag: sentence-similarity
---

# Embedding-Gemma-300m-Healthcare - GGUF

This sentence-transformers model was finetuned and converted to GGUF format using [Unsloth](https://github.com/unslothai/unsloth).

## Available Model files:
- `embeddinggemma-300m.Q5_K_M.gguf`
- `embeddinggemma-300m.Q8_0.gguf`
- `embeddinggemma-300m.Q4_K_M.gguf`

This was trained 2x faster with [Unsloth](https://github.com/unslothai/unsloth)
[<img src="https://raw.githubusercontent.com/unslothai/unsloth/main/images/unsloth%20made%20with%20love.png" width="200"/>](https://github.com/unslothai/unsloth)