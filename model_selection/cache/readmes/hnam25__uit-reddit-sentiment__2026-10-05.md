---
language: en
license: mit
pipeline_tag: text-classification
tags:
- sentiment-analysis
- reddit
- transformer
- roberta
- social-media
---

# Reddit Sentiment Transformer

Fine-tuned transformer model for 3-class sentiment classification on manually labeled Reddit posts about AI models.

## Labels

- negative
- neutral
- positive

## Base checkpoint

- cardiffnlp/twitter-roberta-base-sentiment-latest

## Test metrics

- accuracy: 0.7492
- macro_f1: 0.7498

## Training notes

This model was exported from `colab/sentiment_advanced_demo.ipynb`.
