---
base_model:
- merged_model
- mistralai/Mistral-7B-v0.3
tags:
- text-generation-inference
- transformers
- unsloth
- mistral
- trl
- sft
license: apache-2.0
language:
- en
---

# Uploaded  model

- **Developed by:** ahmadmirza17
- **License:** apache-2.0
- **Finetuned from model :** merged_model

This mistral model was trained 2x faster with [Unsloth](https://github.com/unslothai/unsloth) and Huggingface's TRL library.

Model was intially a Mistral 7b, conducted continual pre-training on medical-specific pdf content and then QnA finetuned for more defined conversation response.

[<img src="https://raw.githubusercontent.com/unslothai/unsloth/main/images/unsloth%20made%20with%20love.png" width="200"/>](https://github.com/unslothai/unsloth)