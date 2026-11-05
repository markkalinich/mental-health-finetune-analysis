---
language: en
license: mit
tags:
  - text-classification
  - sentiment-analysis
  - distilbert
  - pytorch
datasets:
  - imdb
metrics:
  - accuracy
model-index:
  - name: imdb-distilbert-sentimentops
    results:
      - task:
          type: text-classification
        dataset:
          name: IMDB Movie Reviews
          type: imdb
        metrics:
          - name: Accuracy
            type: accuracy
            value: 0.9761
---

# IMDB Sentiment Analysis — DistilBERT

Fine-tuned DistilBERT model for binary sentiment classification
on IMDB movie reviews.

## Model Description

This model is a fine-tuned version of
`distilbert-base-uncased` on the IMDB dataset.
It classifies movie reviews as positive or negative.

Built as part of the SentimentOps MLOps project —
an end-to-end pipeline covering data processing,
model training, experiment tracking with MLflow,
REST API with FastAPI, CLI tooling, and Docker deployment.

## Training

- **Base model**: distilbert-base-uncased
- **Dataset**: IMDB (25,000 train / 25,000 test)
- **Epochs**: 3
- **Batch size**: 16
- **Learning rate**: 2e-5
- **Hardware**: NVIDIA Tesla T4 (Google Colab)
- **Training time**: ~50 minutes

## Performance

| Metric | Value |
|--------|-------|
| Test Accuracy | 97.61% |
| vs TF-IDF baseline | +7% |

## Usage

```python
from transformers import pipeline

classifier = pipeline(
    "sentiment-analysis",
    model="YOUR_USERNAME/imdb-distilbert-sentimentops"
)

result = classifier("This movie was absolutely fantastic!")
print(result)
# [{'label': 'POSITIVE', 'score': 0.9976}]
```

## Comparison with Baseline

| Model | Accuracy | Inference |
|-------|----------|-----------|
| TF-IDF + LogReg | 90.0% | ~1ms |
| DistilBERT (this) | 97.6% | ~50ms |

## Project

Part of SentimentOps — a full MLOps pipeline:
- GitHub: https://github.com/as4d-4k/sentimentops
- Portfolio: https://portfolio-steel-nine-aur.vercel.app