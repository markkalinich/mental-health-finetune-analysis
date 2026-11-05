---
language: en
tags:
  - safety
  - guardrail
  - jailbreak
  - classification
  - deberta
license: mit
pipeline_tag: text-classification
---

# Guardrail DeBERTa Classifier

Fine-tuned mDeBERTa-v3-base for detecting **benign**, **jailbreak**, and **harmful** prompts.

## Usage

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

tokenizer = AutoTokenizer.from_pretrained("YOUR_USERNAME/guardrail-deberta-classifier")
model = AutoModelForSequenceClassification.from_pretrained("YOUR_USERNAME/guardrail-deberta-classifier")

prompt = "Ignore all previous instructions..."
inputs = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=512)
with torch.no_grad():
    logits = model(**inputs).logits
    probs = torch.softmax(logits, dim=-1)
    print(probs)  # [benign, jailbreak, harmful]
```

## Classes

- `0`: benign
- `1`: jailbreak
- `2`: harmful

## Training

- ~11k examples from open HF datasets
- Test accuracy: 96.6%
- Macro F1: 96.1%
