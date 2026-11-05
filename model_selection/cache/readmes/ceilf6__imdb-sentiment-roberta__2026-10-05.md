---
license: mit
language:
- en
tags:
- sentiment-analysis
- imdb
- roberta
- text-classification
pipeline_tag: text-classification
base_model: textattack/roberta-base-imdb
---

# IMDB Sentiment RoBERTa

This repository contains a high-accuracy IMDB sentiment classifier for the 2026 machine learning course task.

The model is based on `textattack/roberta-base-imdb`, a RoBERTa sequence-classification model fine-tuned for IMDB sentiment analysis.

## Evaluation

- Dataset: `imdb_top_500.csv`
- Accuracy: 98.40%
- Correct: 492 / 500
- Required minimum accuracy: 0.92
- Labels: `0 = negative`, `1 = positive`

## Usage

```python
from transformers import pipeline

classifier = pipeline(
    "sentiment-analysis",
    model="ceilf6/imdb-sentiment-roberta",
    tokenizer="ceilf6/imdb-sentiment-roberta",
)
print(classifier("This movie is great and deeply moving."))
```

## CI/CD

GitHub Actions evaluates the model and uploads this repository only when accuracy is at least `0.92`.
