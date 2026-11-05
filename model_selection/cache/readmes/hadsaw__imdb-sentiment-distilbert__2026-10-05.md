
---
language: en
tags:
- sentiment-analysis
- text-classification
- distilbert
- imdb
datasets:
- imdb
metrics:
- accuracy
- f1
- precision
- recall
---

# IMDB Sentiment Analysis Model

This model is a fine-tuned version of `distilbert-base-uncased` on the IMDB dataset for sentiment analysis.

## Model description

The model was trained on the IMDB movie reviews dataset to classify movie reviews as either positive (1) or negative (0).

## Training procedure

- Model: DistilBERT (distilbert-base-uncased)
- Training Data: IMDB Dataset (40,000 training samples)
- Validation Data: 5,000 samples
- Test Data: 5,000 samples
- Epochs: 2
- Batch Size: 32
- Learning Rate: 2e-5
- Max Sequence Length: 256 tokens

## Usage
