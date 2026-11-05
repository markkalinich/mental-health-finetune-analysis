---
language: en
license: apache-2.0
tags:
- sentiment-analysis
- text-classification
- distilbert
datasets:
- imdb
metrics:
- accuracy
- f1
pipeline_tag: text-classification
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

Accuracy: 0.869

Precision: 0.878

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
    model="Rameen191/sentiment-tutorial"
)

classifier("This was a great experience!")
