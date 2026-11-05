---
library_name: transformers
pipeline_tag: text-classification
tags:
- text-classification
- sentiment-analysis
- distilbert
datasets:
- cornell-movie-review-data/rotten_tomatoes
---

# DistilBERT Sentiment Classifier

DistilBERT fine-tuned for sentiment analysis on Rotten Tomatoes movie reviews.

## Repository

`sofiane-isi/distilbert-sentiment`

## Dataset

`cornell-movie-review-data/rotten_tomatoes`

Classes:
- NEGATIVE
- POSITIVE

## Evaluation

- Accuracy: 0.8461538461538461
- Evaluation loss: 0.42963317036628723

## Base model

`distilbert-base-uncased`

## MLOps workflow

Dataset → tokenization → fine-tuning → evaluation → Hugging Face Hub → Model Card → Space.

## Limitations

Educational binary sentiment classifier fine-tuned specifically on Rotten Tomatoes.
