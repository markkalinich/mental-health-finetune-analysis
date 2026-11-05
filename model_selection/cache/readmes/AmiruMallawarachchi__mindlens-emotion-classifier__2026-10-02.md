---
language: en
license: apache-2.0
tags:
  - text-classification
  - emotion
  - roberta
datasets:
  - dair-ai/emotion
metrics:
  - accuracy
  - f1
pipeline_tag: text-classification
---

# MindLens Emotion Classifier (RoBERTa, dair-ai/emotion)

Fine-tuned `roberta-base` for 6-class emotion classification
as part of the MindLens mental-health support system.

**Classes:** sadness, joy, love, anger, fear, surprise

## Results (held-out test set, n=2000)
| Metric | Score |
|---|---|
| Accuracy | 0.9250 |
| Macro F1 | 0.8827 |
| 80% gate | PASS |

## Dataset
[dair-ai/emotion](https://huggingface.co/datasets/dair-ai/emotion) —
~16k English Twitter messages labelled with 6 basic emotions.
Train: 16,000 | Val: 2,000 | Test: 2,000

## Usage
```python
from transformers import pipeline
clf = pipeline("text-classification",
               model="AmiruMallawarachchi/mindlens-emotion-classifier")
clf("I feel completely overwhelmed and hopeless")
```

## Limitations
Twitter-domain training data. One signal among five in the MindLens
orchestrator — not a clinical mood assessment.
