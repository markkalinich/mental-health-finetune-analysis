---
base_model: TinyLlama/TinyLlama-1.1B-intermediate-step-1431k-3T
tags:
- pharma
- causal-lm
- dpo
- preference-tuning
- instruction-tuning
- domain-adaptive-pretraining
- merged
- final
datasets:
- ThakrePranjal/pharma-domain-corpus
- ThakrePranjal/pharma-instruction-dataset
- ThakrePranjal/pharma-preference-dataset
---

# Pharma TinyLlama — Final Model (Stage 3 Complete)

This is the **final fully merged standalone model** — the end result of
a complete 3-stage fine-tuning pipeline applied to
`TinyLlama/TinyLlama-1.1B-intermediate-step-1431k-3T`:

| Stage | Type | What it learned |
|---|---|---|
| 1 | Domain Adaptive Pretraining | Pharma vocabulary, concepts, terminology |
| 2 | Instruction Fine-Tuning (SFT) | Follow Alpaca-style instructions in pharma domain |
| 3 | Preference Tuning (DPO) | Prefer high-quality, accurate pharma responses |

No PEFT/LoRA library needed — load directly with 🤗 Transformers.

## Usage

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model     = AutoModelForCausalLM.from_pretrained("ThakrePranjal/pharma-tinyllama-final")
tokenizer = AutoTokenizer.from_pretrained("ThakrePranjal/pharma-tinyllama-final")
model.eval()

def generate(instruction, input_text="", max_new_tokens=150):
    if input_text.strip():
        prompt = (
            f"### Instruction:\n{instruction}\n\n"
            f"### Input:\n{input_text}\n\n"
            f"### Response:\n"
        )
    else:
        prompt = f"### Instruction:\n{instruction}\n\n### Response:\n"

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

# Test
questions = [
    "Explain the primary mechanism of action of metformin.",
    "Why should AI predictions in drug discovery be experimentally validated?",
    "Define pharmacovigilance.",
    "Why should atorvastatin and ezetimibe be used together?",
]
for q in questions:
    print("Q:", q)
    print("A:", generate(q))
    print()
```

## Complete pipeline repos

| Stage | Dataset | Adapter | Merged Model |
|---|---|---|---|
| 1 — Domain Pretraining | [ThakrePranjal/pharma-domain-corpus](https://huggingface.co/datasets/ThakrePranjal/pharma-domain-corpus) | [ThakrePranjal/pharma-tinyllama-domain-lora](https://huggingface.co/ThakrePranjal/pharma-tinyllama-domain-lora) | — |
| 2 — Instruction Tuning | [ThakrePranjal/pharma-instruction-dataset](https://huggingface.co/datasets/ThakrePranjal/pharma-instruction-dataset) | [ThakrePranjal/pharma-tinyllama-instruct-lora](https://huggingface.co/ThakrePranjal/pharma-tinyllama-instruct-lora) | [ThakrePranjal/pharma-tinyllama-instruct-merged](https://huggingface.co/ThakrePranjal/pharma-tinyllama-instruct-merged) |
| 3 — Preference Tuning (DPO) | [ThakrePranjal/pharma-preference-dataset](https://huggingface.co/datasets/ThakrePranjal/pharma-preference-dataset) | [ThakrePranjal/pharma-tinyllama-dpo-lora](https://huggingface.co/ThakrePranjal/pharma-tinyllama-dpo-lora) | **THIS MODEL** |

## Limitations

Trained on a small pharma corpus. Not validated for clinical or production use.
Intended for educational/research purposes only.
