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

`92amineee/distilbert-sentiment`

## Dataset

`cornell-movie-review-data/rotten_tomatoes`

Classes:
- NEGATIVE
- POSITIVE

## Evaluation

- Accuracy: 0.8433395872420263
- Evaluation loss: 0.42508700489997864

## Base model

`distilbert-base-uncased`

## MLOps workflow

Dataset → tokenization → fine-tuning → evaluation → Hugging Face Hub → Model Card → Space.

## Limitations

Educational binary sentiment classifier fine-tuned specifically on Rotten Tomatoes.
