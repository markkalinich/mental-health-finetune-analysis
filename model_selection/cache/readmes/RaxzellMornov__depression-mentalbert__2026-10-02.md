---
language: en
license: mit
tags:
  - text-classification
  - depression-detection
  - mental-health
  - bert
  - transformers
datasets:
  - custom
metrics:
  - f1
  - accuracy
model-index:
  - name: MentalBERT
    results:
      - task:
          type: text-classification
        metrics:
          - type: f1
            value: 0.9109
            name: F1 Score
---

# MentalBERT - SentiMind

Fine-tuned **MentalBERT** model for binary classification of depressive vs. non-depressive tweets.

## Model Description

Pre-trained on mental health corpora from Reddit and clinical forums.

| Label | ID |
|-------|----|
| Non-Depressive | 0 |
| Depressive     | 1 |

## Performance

| Metric | Value |
|--------|-------|
| F1 Score | 0.9109 |

## Usage

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

model_id = "RaxzellMornov/depression-mentalbert"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForSequenceClassification.from_pretrained(model_id)
model.eval()

text = "I feel so empty and hopeless."
inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=128)

with torch.no_grad():
    logits = model(**inputs).logits

predicted_class = logits.argmax(-1).item()
labels = {0: "Non-Depressive", 1: "Depressive"}
print(labels[predicted_class])
```

## Training Details

- **Task**: Binary sequence classification
- **Framework**: PyTorch + Hugging Face Transformers
- **Fine-tuned on**: Depressive Twitter dataset

## Disclaimer

SentiMind is intended for research and educational purposes only.
It should **not** be used as a substitute for professional mental health diagnosis.
