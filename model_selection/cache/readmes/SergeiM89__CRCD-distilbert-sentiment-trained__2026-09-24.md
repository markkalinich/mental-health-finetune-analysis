---
language:
- en
library_name: transformers
pipeline_tag: text-classification
tags:
- sentiment-analysis
- distilbert
- text-classification
- customer-reviews
base_model: distilbert/distilbert-base-uncased
datasets:
- SergeiM89/CRCD-sentiment-balanced-3class
---

# CRCD DistilBERT Sentiment Classifier

A fine-tuned DistilBERT model for sentiment analysis of English
customer and product reviews.

## Task

The model classifies reviews into three sentiment classes:

| Label ID | Sentiment |
|---:|---|
| 0 | negative |
| 1 | neutral |
| 2 | positive |

## Model architecture

- Base model: distilbert/distilbert-base-uncased
- Model type: DistilBertForSequenceClassification
- Encoder: DistilBERT
- Number of output classes: 3
- Task: English sentiment classification
- Maximum input length: 256 tokens

The model contains a DistilBERT encoder and a classification head
with three output neurons.

## Training dataset

The model was fine-tuned on the CRCD Balanced Sentiment Dataset:

https://huggingface.co/datasets/SergeiM89/CRCD-sentiment-balanced-3class

The dataset contains English customer and product reviews
with negative, neutral, and positive sentiment labels.

The data was cleaned, balanced, and divided into training,
validation, and test splits before fine-tuning.

## Related resources

Base model:

https://huggingface.co/distilbert/distilbert-base-uncased

Training dataset:

https://huggingface.co/datasets/SergeiM89/CRCD-sentiment-balanced-3class