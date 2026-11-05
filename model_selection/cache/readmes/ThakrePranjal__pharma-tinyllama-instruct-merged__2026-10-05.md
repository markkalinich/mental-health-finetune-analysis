---
base_model: TinyLlama/TinyLlama-1.1B-intermediate-step-1431k-3T
tags:
- instruction-tuning
- pharma
- causal-lm
- merged
datasets:
- ThakrePranjal/pharma-instruction-dataset
---

# Pharma TinyLlama — Instruction Merged Model (Stage 2)

This is the **fully merged standalone instruction-tuned model**:
`TinyLlama/TinyLlama-1.1B-intermediate-step-1431k-3T` with both:

1. Stage 1 domain LoRA merged in (pharma-domain pretraining)
2. Stage 2 instruction LoRA merged in (pharma instruction tuning)

No PEFT/LoRA library needed at inference time — load directly with 🤗 Transformers.

## Usage

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model     = AutoModelForCausalLM.from_pretrained("ThakrePranjal/pharma-tinyllama-instruct-merged")
tokenizer = AutoTokenizer.from_pretrained("ThakrePranjal/pharma-tinyllama-instruct-merged")
model.eval()

def generate(instruction, input_text="", max_new_tokens=150):
    if input_text.strip():
        prompt = (
            f"### Instruction:\n{instruction}\n\n"
            f"### Input:\n{input_text}\n\n"
            f"### Response:\n"
        )
    else:
        prompt = (
            f"### Instruction:\n{instruction}\n\n"
            f"### Response:\n"
        )
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    with torch.no_grad():
        out = model.generate(
            **inputs,
            max_new_tokens=max_new_tokens,
            do_sample=True,
            temperature=0.7,
            top_p=0.9,
            repetition_penalty=1.1,
            pad_token_id=tokenizer.eos_token_id,
        )
    return tokenizer.decode(out[0], skip_special_tokens=True)

print(generate("Explain the primary mechanism of action of metformin."))
```

## Full training pipeline

```
TinyLlama (base)
    → Stage 1: Domain Pretraining LoRA    [ThakrePranjal/pharma-tinyllama-domain-lora]
    → Merge  → Stage 1 Merged Model       [ThakrePranjal/pharma-tinyllama-domain-lora]
    → Stage 2: Instruction LoRA           [ThakrePranjal/pharma-tinyllama-instruct-lora]
    → Merge  → THIS MODEL (Stage 2 Merged)
    → Stage 3: Preference Tuning (DPO)    (upcoming)
```

## Dataset

[ThakrePranjal/pharma-instruction-dataset](https://huggingface.co/datasets/ThakrePranjal/pharma-instruction-dataset)

## Limitations

Trained on a small pharma corpus. Not validated for clinical or production use.
Intended for educational/research purposes only.
