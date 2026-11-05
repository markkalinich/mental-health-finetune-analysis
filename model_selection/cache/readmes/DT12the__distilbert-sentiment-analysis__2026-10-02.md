---
language: "en"
license: "mit"
tags:
- distilbert
- sentiment-analysis
- multilingual
widgets:
- text: "I love this movie!"
---

# Model Name: DistilBERT for Sentiment Analysis

## Model Description

### Overview

This model is a fine-tuned version of `distilbert-base-uncased` on a social media dataset for the purpose of sentiment analysis. It can classify text into non-negative and negative sentiments.

### Intended Use

This model is intended for sentiment analysis tasks, particularly for analyzing social media texts.

### Model Architecture

This model is based on the `DistilBertForSequenceClassification` architecture, a distilled version of BERT that maintains comparable performance on downstream tasks while being more computationally efficient.

## Training

### Training Data

The model was trained on a dataset consisting of social media posts, surveys and interviews, labeled for sentiment (non-negative and negative). The dataset includes texts from a variety of sources and demographics.

### Training Procedure

The model was trained using the following parameters:
- Optimizer: AdamW
- Learning Rate: 5e-5
- Batch Size: 32
- Epochs: 30

Training was conducted on Kaggle, utilizing two GPUs for accelerated training.