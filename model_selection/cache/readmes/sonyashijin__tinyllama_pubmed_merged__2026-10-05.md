---
base_model: unsloth/tinyllama-bnb-4bit
tags:
- text-generation-inference
- transformers
- unsloth
- llama
- trl
- sft
license: apache-2.0
language:
- en
---

# Uploaded  model

- **Developed by:** sonyashijin
- **License:** apache-2.0
- **Finetuned from model :** unsloth/tinyllama-bnb-4bit

This llama model was trained 2x faster with [Unsloth](https://github.com/unslothai/unsloth) and Huggingface's TRL library.

[<img src="https://raw.githubusercontent.com/unslothai/unsloth/main/images/unsloth%20made%20with%20love.png" width="200"/>](https://github.com/unslothai/unsloth)

# Evaluation

| Tasks  |Version|Filter|n-shot|Metric|   |Value|   |Stderr|
|--------|------:|------|-----:|------|---|----:|---|-----:|
|pubmedqa|      1|none  |     0|acc   |↑  |0.716|±  |0.0202|

Base model (unsloth/tinyllama-bnb-4bit)
| Tasks  |Version|Filter|n-shot|Metric|   |Value|   |Stderr|
|--------|------:|------|-----:|------|---|----:|---|-----:|
|pubmedqa|      1|none  |     0|acc   |↑  |0.636|±  |0.0215|