---
base_model: unsloth/tinyllama-bnb-4bit
tags:
- unsloth
- pharma
- causal-lm
- dpo
- preference-tuning
- instruction-tuning
- domain-adaptive-pretraining
- merged
- final
datasets:
- ThakrePranjal/pharma-instruction-dataset-unsloth
- ThakrePranjal/pharma-preference-dataset-unsloth
---

# Pharma TinyLlama — Final Model (Unsloth 3-Stage Complete)

This is the **final fully merged standalone model** — complete output of the
Unsloth 3-stage pharma fine-tuning pipeline applied to
`unsloth/tinyllama-bnb-4bit`.

## 3-Stage Pipeline Summary

| Stage | Type | Data | What model learned |
|---|---|---|---|
| 1 | Domain Pretraining (SFT) | Raw pharma PDF paragraphs | Pharma vocabulary, facts, terminology |
| 2 | Instruction Fine-Tuning (SFT) | 48 Alpaca-format QA pairs | How to follow pharma instructions |
| 3 | Preference Tuning (DPO) | 48 chosen/rejected pairs | Which pharma answers are better |

Built with **Unsloth** (2x faster, lower VRAM) + HuggingFace TRL.
Total GPU time: ~353 seconds on Tesla T4.

## Quick Start

```python
from unsloth import FastLanguageModel
import torch

model, tokenizer = FastLanguageModel.from_pretrained(
    model_name="ThakrePranjal/pharma-tinyllama-unsloth-final",
    max_seq_length=512,
    load_in_4bit=True,
)
FastLanguageModel.for_inference(model)

def ask(question, max_new_tokens=150):
    prompt = f"### Instruction:\n{question}\n\n### Response:\n"
    inputs = tokenizer(prompt, return_tensors="pt").to("cuda")
    with torch.inference_mode():
        out = model.generate(
            **inputs,
            max_new_tokens=max_new_tokens,
            do_sample=True,
            temperature=0.7,
            top_p=0.9,
            repetition_penalty=1.1,
            pad_token_id=tokenizer.eos_token_id,
        )
    input_len = inputs["input_ids"].shape[-1]
    return tokenizer.decode(out[0][input_len:], skip_special_tokens=True).strip()

# Test
questions = [
    "Explain the primary mechanism of action of metformin.",
    "Why should AI predictions in drug discovery be experimentally validated?",
    "Define pharmacovigilance.",
    "Why should atorvastatin and ezetimibe be used together?",
]
for q in questions:
    print(f"Q: {q}")
    print(f"A: {ask(q)}\n")
```

## Complete Pipeline Repos

| Stage | Dataset | LoRA Adapter | Merged Model |
|---|---|---|---|
| 1 — Domain Pretraining | — | [ThakrePranjal/pharma-tinyllama-unsloth-stage1-lora](https://huggingface.co/ThakrePranjal/pharma-tinyllama-unsloth-stage1-lora) | [ThakrePranjal/pharma-tinyllama-unsloth-stage1-merged](https://huggingface.co/ThakrePranjal/pharma-tinyllama-unsloth-stage1-merged) |
| 2 — Instruction SFT | [ThakrePranjal/pharma-instruction-dataset-unsloth](https://huggingface.co/datasets/ThakrePranjal/pharma-instruction-dataset-unsloth) | [ThakrePranjal/pharma-tinyllama-unsloth-stage2-lora](https://huggingface.co/ThakrePranjal/pharma-tinyllama-unsloth-stage2-lora) | [ThakrePranjal/pharma-tinyllama-unsloth-stage2-merged](https://huggingface.co/ThakrePranjal/pharma-tinyllama-unsloth-stage2-merged) |
| 3 — DPO Preference | [ThakrePranjal/pharma-preference-dataset-unsloth](https://huggingface.co/datasets/ThakrePranjal/pharma-preference-dataset-unsloth) | [ThakrePranjal/pharma-tinyllama-unsloth-stage3-dpo-lora](https://huggingface.co/ThakrePranjal/pharma-tinyllama-unsloth-stage3-dpo-lora) | **THIS MODEL** |

## Limitations

Trained on a small pharma corpus (1 PDF, 48 instruction/preference pairs).
Not validated for clinical or production use. Intended for
educational/research purposes only.
