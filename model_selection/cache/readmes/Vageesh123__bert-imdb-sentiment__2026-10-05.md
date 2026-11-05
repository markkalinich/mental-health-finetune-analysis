---
license: apache-2.0
tags:
- sentiment-analysis
- imdb
- bert
---

# BERT IMDB Sentiment Classifier

This is a fine-tuned BERT model for binary sentiment classification (Positive/Negative) on the IMDB movie reviews dataset.

## Model Description

- **Base Model:** BERT (bert-base-uncased)
- **Dataset:** IMDB Movie Reviews
- **Task:** Sentiment Analysis
- **Fine-tuning:** Trained for 1 epoch on a small subset (2000 samples)

## Usage

```python
from transformers import pipeline

classifier = pipeline("sentiment-analysis", model="Vageesh123/bert-imdb-sentiment")

result = classifier("This movie was absolutely fantastic!")
print(result)
