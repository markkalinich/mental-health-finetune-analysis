---
language: en
license: apache-2.0
library_name: transformers
pipeline_tag: text-classification
base_model: distilbert-base-uncased
datasets:
- dair-ai/emotion
tags:
- emotion-classification
- distilbert
- text-classification
metrics:
- accuracy
- f1
model-index:
- name: distilbert-emotion
  results:
  - task:
      type: text-classification
      name: Emotion Classification
    dataset:
      name: dair-ai/emotion
      type: dair-ai/emotion
    metrics:
    - type: accuracy
      value: 0.9335
    - type: f1
      value: 0.9329
      name: Weighted F1
---

# DistilBERT — Emotion Classification

Fine-tuned `distilbert-base-uncased` on the [dair-ai/emotion](https://huggingface.co/datasets/dair-ai/emotion)
dataset to classify English text into six emotions: **sadness, joy, love,
anger, fear, surprise**.

This model was produced as part of an end-to-end MLOps pipeline project
(data prep → training with Weights & Biases tracking → Hub publishing →
containerised inference → CI/CD).

## Intended use

Single-label emotion classification of short English text (e.g. tweets,
messages). Not intended for clinical, safety-critical, or high-stakes use.

## Training

- **Base model:** distilbert-base-uncased
- **Dataset:** dair-ai/emotion (`split` config — 16k/2k/2k)
- **Max sequence length:** 64 (95th-percentile text length was 41 words)
- **Best hyperparameters:** learning rate 5e-5, batch size 16, 3 epochs,
  weight decay 0.01
- **Tracking:** Weights & Biases (loss, accuracy, weighted/macro F1, system metrics)

## Evaluation (held-out test split)

| Metric | Score |
|--------|-------|
| Accuracy | 0.9335 |
| Weighted F1 | 0.9329 |
| Macro F1 | 0.8924 |

The gap between weighted and macro F1 reflects class imbalance in the dataset
(joy and sadness dominate; love and surprise are rare).

## Usage

```python
from transformers import pipeline
clf = pipeline("text-classification", model="G25AIT2134/distilbert-emotion")
clf("I can't believe how happy this makes me!")
```

## Limitations

- English only; informal/tweet-style text.
- Lower accuracy on under-represented classes (love, surprise).
- Inherits any biases present in the training data.
