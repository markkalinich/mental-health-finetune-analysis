---
language:
- en
license: apache-2.0
base_model: distilbert-base-uncased
tags:
- text-classification
- emotion-classification
- distilbert
datasets:
- dair-ai/emotion
metrics:
- accuracy
- f1
---

# DistilBERT Emotion Classifier - HW2

This model is a fine-tuned `distilbert-base-uncased` text classifier for the
`dair-ai/emotion` dataset.

## Task

Tweet emotion classification with six labels:

- sadness
- joy
- love
- anger
- fear
- surprise

## Training Summary

- Base model: `distilbert-base-uncased`
- Dataset: `dair-ai/emotion`
- Epochs: 3
- Learning rate: 2e-5
- Batch size: 8
- Weight decay: 0.01
- Final validation accuracy: 0.9435
- Final weighted F1: 0.9436

## Hyperparameter Comparison

| Setting | Accuracy | Weighted F1 | Note |
|---|---:|---:|---|
| lr=2e-5, epochs=3, batch=8 | 0.9435 | 0.9436 | Final model |
| lr=5e-5, epochs=1, batch=8 | 0.9415 | 0.9420 | Comparison run |
| lr=1e-5, epochs=1, batch=8 | 0.9205 | 0.9202 | Comparison run |

## Usage

```python
from transformers import pipeline

classifier = pipeline(
    "text-classification",
    model="./model",
    tokenizer="./model",
)

classifier("I feel very happy today.", top_k=None)
```
