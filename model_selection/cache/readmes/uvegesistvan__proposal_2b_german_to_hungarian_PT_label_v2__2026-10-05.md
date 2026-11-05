---
language: 
  - de
  - hu
license: mit
tags:
  - text-classification
  - emotion-detection
  - machine-learning
  - german
  - hungarian
model_name: uvegesistvan/proposal_2b_german_to_hungarian_PT_label_v2
datasets: []
metrics:
  - precision
  - recall
  - f1-score
  - accuracy
---

# Proposal 2B: German to Hungarian Emotion Labeling (v2)

## Model Description

This model is designed for **emotion classification** in Hungarian texts. 
It was fine-tuned to recognize **nine emotion categories** and trained on a dataset with labeled examples.

## Labels and Their Meanings

| Label | Emotion      |
|--------|----------------|
| 0      | Anger        |
| 1      | Fear         |
| 2      | Disgust      |
| 3      | Sadness      |
| 4      | Joy          |
| 5      | None of them |
| 6      | Enthusiasm   |
| 7      | Hope         |
| 8      | Pride        |

## Evaluation Metrics

The model was evaluated using **precision, recall, f1-score, and accuracy**.

### Classification Report

| Label | Precision | Recall | F1-score | Support |
|--------|------------|--------|----------|---------|
| Anger (0)        | 0.53 | 0.57 | 0.55 | 777 |
| Fear (1)         | 0.89 | 0.73 | 0.80 | 776 |
| Disgust (2)      | 0.92 | 0.95 | 0.93 | 776 |
| Sadness (3)      | 0.86 | 0.85 | 0.86 | 775 |
| Joy (4)          | 0.84 | 0.80 | 0.82 | 736 |
| None of them (5) | 0.65 | 0.66 | 0.66 | 1594 |
| Enthusiasm (6)   | 0.62 | 0.64 | 0.63 | 776 |
| Hope (7)         | 0.52 | 0.52 | 0.52 | 777 |
| Pride (8)        | 0.76 | 0.79 | 0.77 | 776 |

#### Overall Performance:

- **Accuracy**: 72%
- **Macro Avg**: Precision: 0.73, Recall: 0.72, F1-score: 0.73
- **Weighted Avg**: Precision: 0.72, Recall: 0.72, F1-score: 0.72

## How to Use

To use this model for text classification in Python:

```python
from transformers import pipeline

classifier = pipeline("text-classification", model="uvegesistvan/proposal_2b_german_to_hungarian_PT_label_v2")

text = "Ich bin sehr glücklich, dass du hier bist!"  # German
result = classifier(text)
print(result)
