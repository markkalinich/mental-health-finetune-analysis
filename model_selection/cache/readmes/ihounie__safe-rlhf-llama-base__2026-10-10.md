---
base_model: PKU-Alignment/alpaca-7b-reproduced
library_name: transformers
tags:
  - llama
  - alpaca
  - safety
  - sft
  - safe-rlhf
license: other
---

# ihounie/safe-rlhf-llama-base

SFT fine-tune of `PKU-Alignment/alpaca-7b-reproduced` on the
[PKU-Alignment/PKU-SafeRLHF-30K](https://huggingface.co/datasets/PKU-Alignment/PKU-SafeRLHF-30K)
dataset (preferred-safe SFT mode), trained with LoRA (r=64, alpha=128, dropout=0.05) for 3 epochs
and then **merged** back into the base model. Weights are stored in bf16.

- Base model: `PKU-Alignment/alpaca-7b-reproduced`
- Source W&B run: [hounie/SAFE-RLHF-point/kd7z6emv](https://wandb.ai/hounie/SAFE-RLHF-point/runs/kd7z6emv)
- Source adapter artifact: `hounie/SAFE-RLHF-point/kd7z6emv-lora_adapters:v0`
- Training config: `configs/train/safe/sft_safeRLHF.yaml` from
  [constrained-sft](https://github.com/) (loss_type=sft, sft_data=preferred_safe).

## Usage

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

tok = AutoTokenizer.from_pretrained("ihounie/safe-rlhf-llama-base")
model = AutoModelForCausalLM.from_pretrained(
    "ihounie/safe-rlhf-llama-base",
    torch_dtype=torch.bfloat16,
    device_map="auto",
)
```
