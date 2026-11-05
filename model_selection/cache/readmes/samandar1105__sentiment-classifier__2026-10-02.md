---
language: en
tags:
  - text-classification
  - sentiment-analysis
  - roberta
  - pytorch
datasets:
  - glue
  - imdb
metrics:
  - accuracy
  - f1
model-index:
  - name: sentiment-classifier
    results:
      - task:
          type: text-classification
          name: Sentiment Analysis
        dataset:
          name: SST-2 + IMDB
          type: mixed
        metrics:
          - type: accuracy
            value: 0.9292
          - type: f1
            value: 0.9413
---

# RoBERTa Fine-Tuned for Sentiment Analysis

This model classifies English text as either **Positive 😊** or **Negative 😞**.

Fine-tuned from `roberta-base` on a combination of SST-2 (Stanford Sentiment Treebank) and IMDB movie reviews.

## Performance

| Metric   | Score  |
|----------|--------|
| Accuracy | 0.9292 (92.92%) |
| F1 Score | 0.9413 |

*Evaluated on 20,000 held-out IMDB test samples.*

## How to Use

```python
from transformers import pipeline

classifier = pipeline(
    "text-classification",
    model="samandar1105/sentiment-classifier"
)

result = classifier("This movie was absolutely fantastic!")
print(result)
# [{'label': 'positive', 'score': 0.998}]
```

## Labels

| ID | Label    | Meaning |
|----|----------|---------|
| 0  | negative | Negative sentiment |
| 1  | positive | Positive sentiment |

## Training Details

| Parameter | Value |
|-----------|-------|
| Base model | roberta-base |
| Training data | SST-2 (67K) + IMDB (25K) = 92K samples |
| Epochs | 4 |
| Batch size | 32 |
| Learning rate | 2e-5 |
| Max sequence length | 256 |
| Warmup ratio | 0.1 |
| Weight decay | 0.01 |

## Limitations

- Trained on English text only
- Optimized for movie/review-style text
- Binary only (positive / negative) — no neutral class
