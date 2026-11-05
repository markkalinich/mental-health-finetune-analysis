---
base_model: TinyLlama/TinyLlama-1.1B-Chat-v1.0
library_name: peft
model_name: tinyllama-medical-assistant-final
tags:
  - base_model:adapter:TinyLlama/TinyLlama-1.1B-Chat-v1.0
  - lora
  - sft
  - transformers
  - trl
licence: license
pipeline_tag: text-generation
---

# Model Card for tinyllama-medical-assistant-final

This model is a fine-tuned version of [TinyLlama/TinyLlama-1.1B-Chat-v1.0](https://huggingface.co/TinyLlama/TinyLlama-1.1B-Chat-v1.0).
It has been trained using [TRL](https://github.com/huggingface/trl).

## Training procedure

[<img src="https://raw.githubusercontent.com/wandb/assets/main/wandb-github-badge-28.svg" alt="Visualize in Weights & Biases" width="150" height="24"/>]

This model was trained with SFT.

### Framework versions

- PEFT 0.17.1
- TRL: 0.23.1
- Transformers: 4.57.0
- Pytorch: 2.6.0+cu124
- Datasets: 4.1.1
- Tokenizers: 0.22.1
