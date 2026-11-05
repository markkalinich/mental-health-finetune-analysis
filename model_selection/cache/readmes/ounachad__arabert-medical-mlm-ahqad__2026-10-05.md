---
language: ar
tags:
- arabic
- medical
- masked-language-modeling
- dapt
- arabert
license: apache-2.0
---

# AraBERT-MLM (DAPT on AHQAD/AHD)

This repository releases a **domain-adapted AraBERT** checkpoint continued with **masked language modeling (DAPT-MLM)** on the **AHQAD/AHD** Arabic health question–answer corpus.  
The model is intended for **constrained clinical question reformulation** via **mask filling** (e.g., replacing a placeholder with one or more `[MASK]` tokens and predicting only the masked positions).

## Model ID
`USERNAME/REPO_NAME`

## Training data
- **AHQAD/AHD** Arabic health QA corpus (≈808k Q–A pairs, ~90 specialties).  
- Used under the **original terms** of the dataset.

## Intended use
- Arabic clinical question **rewriting/reformulation** using **span completion** (mask filling).
- A front-end module for Arabic clinical QA pipelines (retrieval/generation) to improve question clarity and completeness.

## How to use (Transformers)
```python
from transformers import AutoTokenizer, AutoModelForMaskedLM
import torch

repo_id = "USERNAME/REPO_NAME"
tokenizer = AutoTokenizer.from_pretrained(repo_id)
model = AutoModelForMaskedLM.from_pretrained(repo_id)

text = "عندي ألم في ___ منذ أسبوع؟"
masked = text.replace("___", tokenizer.mask_token)

inputs = tokenizer(masked, return_tensors="pt")
with torch.no_grad():
    logits = model(**inputs).logits

mask_index = (inputs["input_ids"][0] == tokenizer.mask_token_id).nonzero(as_tuple=True)[0][0].item()
pred_id = logits[0, mask_index].argmax(-1).item()
print("Prediction:", tokenizer.decode([pred_id]))
