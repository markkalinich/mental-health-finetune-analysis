---
language: en
license: mit
base_model: roberta-base
tags:
  - sentiment-analysis
  - text-classification
  - roberta
  - besstie
  - english-varieties
pipeline_tag: text-classification
---

# BESSTIE RoBERTa Sentiment (en-AU, seed 42)

Fine-tuned `roberta-base` for binary sentiment classification on the
**BESSTIE** dataset, variety **en-AU**, training seed **42**.

## Labels

| id | label    |
|----|----------|
| 0  | Negative |
| 1  | Positive |

## Usage

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

repo = "vyshnav112233/BESSTIE-RoBERTa-en-AU-seed42"
tok = AutoTokenizer.from_pretrained(repo)
model = AutoModelForSequenceClassification.from_pretrained(repo)
model.eval()

inputs = tok("I loved this!", return_tensors="pt", truncation=True, max_length=128)
with torch.no_grad():
    logits = model(**inputs).logits
pred = int(logits.argmax(-1))
print(model.config.id2label[pred])
```

## Training details

- Base model: `roberta-base`
- Max sequence length: 128
- Task: binary sentiment classification (`num_labels=2`)
- Variety: `en-AU` (one of `en-AU`, `en-UK`, `en-IN`, `mixed`)
- Random seed: `42`

The raw training-state checkpoint is also included as `best_model.pt`
for users who want to reload the `state_dict` directly into a
`RobertaForSequenceClassification` instance.
