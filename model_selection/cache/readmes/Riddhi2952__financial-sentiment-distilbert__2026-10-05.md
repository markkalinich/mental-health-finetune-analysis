---
language: en
tags:
  - text-classification
  - financial
  - sentiment-analysis
  - distilbert
license: apache-2.0
datasets:
  - zeroshot/twitter-financial-news-sentiment
metrics:
  - accuracy
  - f1
---

# Financial Sentiment DistilBERT

Fine-tuned DistilBERT model for financial news sentiment classification.

## Model Description

This model classifies financial news headlines into three sentiment categories:
- **Bearish** (label 0) — Negative market sentiment
- **Bullish** (label 1) — Positive market sentiment  
- **Neutral** (label 2) — No clear directional sentiment

## Training Data

- Dataset: [zeroshot/twitter-financial-news-sentiment](https://huggingface.co/datasets/zeroshot/twitter-financial-news-sentiment)
- Training samples: 7,504 (after stratified split)
- Validation samples: 938
- Test samples: 938

## Performance

| Metric   | Score |
|----------|-------|
| Accuracy | 84.43% |
| Macro F1 | 0.80   |
| Bearish F1 | 0.74 |
| Bullish F1 | 0.77 |
| Neutral F1 | 0.90 |

## Usage

```python
from transformers import pipeline

classifier = pipeline(
    "text-classification",
    model="Riddhi2952/financial-sentiment-distilbert"
)

result = classifier("$AAPL beats earnings estimates revenue up 12%")
print(result)
# [{'label': 'Bullish', 'score': 0.99}]
```

## Training Details

- Base model: distilbert-base-uncased
- Max sequence length: 23 tokens
- Batch size: 16
- Learning rate: 2e-5
- Epochs: 3
- Class imbalance handling: Class weights (Bearish 2.19x, Bullish 1.64x)

## Limitations

- Negation handling: Complex negations like "not expected to miss" may be misclassified
- Domain specific: Trained on Twitter financial news, may not generalize to formal reports
- Short text: Optimized for headlines (avg 11.7 tokens), not long documents
