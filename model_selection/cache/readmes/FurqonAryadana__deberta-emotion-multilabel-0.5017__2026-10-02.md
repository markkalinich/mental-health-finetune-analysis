---
tags:
- multilabel-classification
- emotion-detection
- text-classification
- transformers
- deberta
- huggingface
license: apache-2.0
datasets:
- custom
language:
- en
---

# DeBERTa-v3-Large for Multilabel Emotion Classification

This model is a fine-tuned version of [`microsoft/deberta-v3-large`](https://huggingface.co/microsoft/deberta-v3-large) for multilabel emotion classification.  
It was trained on a custom dataset where each text sample may contain multiple emotions.

## 📌 Model Card

- **Model**: `FurqonAryadana/deberta-emotion-multilabel-0.5007`
- **Base**: DeBERTa-v3-Large
- **Task**: Multilabel Emotion Classification
- **License**: Apache 2.0
- **Language**: English
- **Threshold Tuning**: Applied per label

## 📊 Evaluation (Validation Set)

**Detailed Classification Report (After Threshold Tuning)**:

| Emotion         | Precision | Recall | F1-score | Support |
|----------------|-----------|--------|----------|---------|
| amusement      | 0.62      | 0.70   | 0.66     | 851     |
| anger          | 0.41      | 0.61   | 0.49     | 999     |
| annoyance      | 0.33      | 0.77   | 0.46     | 1609    |
| caring         | 0.44      | 0.55   | 0.49     | 594     |
| confusion      | 0.46      | 0.71   | 0.56     | 800     |
| disappointment | 0.30      | 0.50   | 0.37     | 990     |
| disgust        | 0.28      | 0.46   | 0.35     | 584     |
| embarrassment  | 0.38      | 0.31   | 0.34     | 308     |
| excitement     | 0.42      | 0.52   | 0.47     | 632     |
| fear           | 0.51      | 0.52   | 0.51     | 321     |
| gratitude      | 0.82      | 0.74   | 0.78     | 955     |
| joy            | 0.45      | 0.58   | 0.50     | 876     |
| love           | 0.66      | 0.78   | 0.71     | 701     |
| sadness        | 0.44      | 0.51   | 0.47     | 714     |

- **F1 Micro**: `0.5104`
- **F1 Macro**: `0.5125`

## 🧠 Emotions (Label Order)

```python
[
  'amusement', 'anger', 'annoyance', 'caring', 'confusion', 'disappointment',
  'disgust', 'embarrassment', 'excitement', 'fear', 'gratitude', 'joy',
  'love', 'sadness'
]
