---
base_model: unsloth/tinyllama-bnb-4bit
tags:
- unsloth
- domain-adaptive-pretraining
- pharma
- causal-lm
- merged
---

# Pharma TinyLlama — Stage 1 Merged (Domain Pretraining) — Unsloth

Stage 1 merged model: `unsloth/tinyllama-bnb-4bit` with the Stage 1 domain
pretraining LoRA ([ThakrePranjal/pharma-tinyllama-unsloth-stage1-lora](https://huggingface.co/ThakrePranjal/pharma-tinyllama-unsloth-stage1-lora))
merged in using Unsloth's 16-bit merge. Load directly without PEFT.

This model was used as the **base for Stage 2 instruction fine-tuning**.

## Usage

```python
from unsloth import FastLanguageModel

model, tokenizer = FastLanguageModel.from_pretrained(
    model_name="ThakrePranjal/pharma-tinyllama-unsloth-stage1-merged",
    max_seq_length=512,
    load_in_4bit=True,
)
```

## Pipeline position

```
unsloth/tinyllama-bnb-4bit
    └── Stage 1 SFT LoRA → Merge → THIS MODEL
                                        └── Stage 2 SFT → [ThakrePranjal/pharma-tinyllama-unsloth-stage2-merged]
                                                └── Stage 3 DPO → [ThakrePranjal/pharma-tinyllama-unsloth-final]
```
