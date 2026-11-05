---
language:
- en
license: apache-2.0
tags:
- sentiment-analysis
- distilbert
- imdb
- transformers
---

# IMDB Sentiment Analysis Model

This model is a fine-tuned version of `distilbert-base-uncased` on the IMDB movie reviews dataset.

## Model Details
- **Base Model**: distilbert-base-uncased
- **Dataset**: IMDB Movie Reviews  
- **Task**: Sentiment Classification - Positive / Negative

## Evaluation Results
- **Accuracy**: 0.893
- **Precision**: 0.8699
- **Recall**: 0.9180
- **F1-Score**: 0.8933
- **Loss**: 0.3018

## How to use
```python
from transformers import pipeline

classifier = pipeline("sentiment-analysis", model="ayeshayasir7543458/results")

print(classifier("This movie was amazing!"))
print(classifier("I hated this movie."))