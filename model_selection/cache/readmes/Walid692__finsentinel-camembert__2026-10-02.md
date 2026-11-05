---
language: fr
license: mit
tags:
- text-classification
- sentiment-analysis
- finance
- camembert
- french
datasets:
- zeroshot/twitter-financial-news-sentiment
- pauri32/fiqa-2018
metrics:
- accuracy
- f1
---

# FinSentinel — French Financial Sentiment Analysis

CamemBERT fine-tuned for financial sentiment classification.

## Model Description

This model classifies financial text into 3 categories:
- **Bearish** (negative sentiment)
- **Bullish** (positive sentiment)
- **Neutral**

Fine-tuned from `camembert-base` on 12,816 financial sentences.

## Training Results

| Epoch | Accuracy | F1 Score |
|-------|----------|----------|
| 1     | 70.67%   | 0.641    |
| 2     | 76.83%   | 0.756    |
| 3     | 78.00%   | 0.772    |

## Test Results

| Metric   | Score  |
|----------|--------|
| Accuracy | 78.08% |
| F1 Score | 0.7759 |

## Per-class Results

| Class   | Precision | Recall | F1   |
|---------|-----------|--------|------|
| Bearish | 0.60      | 0.52   | 0.55 |
| Bullish | 0.69      | 0.64   | 0.66 |
| Neutral | 0.84      | 0.89   | 0.87 |

## Training Details

- Base model: camembert-base
- Epochs: 3
- Batch size: 32
- Learning rate: 2e-5
- Max length: 128
- Train samples: 10,252
- Val samples: 1,282
- Test samples: 1,282

## Usage

```python
from transformers import pipeline

classifier = pipeline(
    "text-classification",
    model="Walid692/finsentinel-camembert"
)

result = classifier("La hausse des taux d'interet inquiete les investisseurs institutionnels.")
print(result)
```

## Author

Ahmed Walid BOUANZOUL — AI Engineer
GitHub: https://github.com/AhmedWalidbou/FinSentinel
