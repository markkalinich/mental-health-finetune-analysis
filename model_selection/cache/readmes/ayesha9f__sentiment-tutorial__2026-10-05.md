---
datasets:
- imdb
language: en
license: apache-2.0
metrics:
- accuracy
- f1
pipeline_tag: text-classification
tags:
- sentiment-analysis
- text-classification
- distilbert
---

# sentiment-tutorial

Fine-tuned distilbert-base-uncased for binary sentiment classification.

## Intended Use
Classify English text as positive or negative.

## Training Procedure
- Base model: distilbert-base-uncased
- Epochs: 2
- Learning rate: 2e-5
- Batch size: 32
- Max length: 128

## Evaluation Results

Accuracy: 0.870

Precision: 0.879

Recall: 0.858

F1: 0.868

## Limitations
- Binary classification only
- English only
- Movie reviews domain

## Usage

from transformers import pipeline

classifier = pipeline(
    "sentiment-analysis",
    model="ayesha9f/sentiment-tutorial"
)

classifier("This was a great experience!")
