---
language: en
license: mit
pipeline_tag: sentiment-analysis
tags:
- transformers
- pytorch
- distilbert
- sentiment-analysis
- imdb
---

# IMDB Sentiment Analysis using DistilBERT

This model is fine-tuned on the IMDB movie reviews dataset for sentiment analysis.

## Model Details
- Base Model: distilbert-base-uncased
- Framework: Hugging Face Transformers
- Task: Sentiment Analysis
- Dataset: IMDB Dataset

## Labels
- POSITIVE
- NEGATIVE

## Example Usage

```python
from transformers import pipeline

classifier = pipeline(
    "sentiment-analysis",
    model="NoureEzzA1arab/imdb-distilbert-sentiment"
)

result = classifier("This movie was fantastic and emotional.")
print(result)