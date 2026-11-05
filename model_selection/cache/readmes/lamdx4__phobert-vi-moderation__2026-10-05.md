---
license: agpl-3.0      # đổi nếu base là phobert-base (MIT)
base_model: [vinai/phobert-base-v2]
language: [vi]
task_categories: [text-classification]
tags: [vietnamese, moderation, phobert, finetune, transformers]
---

# phoBERT Vietnamese Moderation (binary)

## How to use
```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
repo = "lamdx4/phobert-vi-moderation"
tok  = AutoTokenizer.from_pretrained(repo, use_fast=False)
mdl  = AutoModelForSequenceClassification.from_pretrained(repo)
probs = mdl(**tok("bình luận ...", return_tensors="pt", truncation=True, max_length=192)).logits.softmax(-1)
print({"valid": float(probs[0,0]), "invalid": float(probs[0,1])})
