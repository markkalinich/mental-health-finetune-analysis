---
language: en
pipeline_tag: text-classification
library_name: transformers
tags:
- text-classification
- content-safety
- guardex
base_model: s-nlp/roberta_toxicity_classifier
metrics:
- f1
---

# GuardEx RoBERTa Safety Classifier

Binary classifier that labels a piece of text as `safe` or `unsafe`. Used by
[GuardEx](https://github.com/atliq/guardex), an LLM guardrail library, as one of
its content-safety models.

## Labels

| id | label |
|----|--------|
| 0  | safe   |
| 1  | unsafe |

## Performance

Held-out evaluation:

- F1: 0.938
- Unsafe recall: 95.7%
- Safe recall: 91.5%

## Usage

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

repo = "AtliQ-Technologies/guardex-roberta-safety"
tok = AutoTokenizer.from_pretrained(repo)
model = AutoModelForSequenceClassification.from_pretrained(repo)

enc = tok("text to check", return_tensors="pt", truncation=True, max_length=128)
with torch.no_grad():
    logits = model(**enc).logits
print(model.config.id2label[int(logits.argmax())])  # "safe" or "unsafe"
```

## Details

Fine-tuned from `s-nlp/roberta_toxicity_classifier` with hyperparameter
optimization. Max sequence length 128.
