---
language: en
license: apache-2.0
tags:
- bert
- sentiment-analysis
- text-classification
---





# BERT Movie Review Sentiment Analysis

A fine-tuned BERT model for binary sentiment classification on movie reviews.

## Project Overview

This project fine-tunes `bert-base-uncased` on the IMDB movie reviews dataset to classify reviews as Positive or Negative.

## Model Details

- **Base Model:** bert-base-uncased
- **Task:** Binary Sentiment Classification
- **Dataset:** IMDB Movie Reviews
- **Training Samples:** 2000
- **Test Samples:** 500
- **Epochs:** 2
- **Accuracy:** ~92%

## Files

- `model.safetensors` — fine-tuned model weights
- `config.json` — model configuration
- `tokenizer.json` — tokenizer
- `tokenizer_config.json` — tokenizer configuration
- `predict.py` — inference script
- `BERT_transformer_movie_review_project.ipynb` — full training notebook

## Usage

```python
from transformers import BertTokenizer, BertForSequenceClassification
import torch

model_name = "nitz0219/bert-movie-review"
tokenizer = BertTokenizer.from_pretrained(model_name)
model = BertForSequenceClassification.from_pretrained(model_name)
model.eval()

text = "This movie was absolutely fantastic!"
inputs = tokenizer(text, return_tensors="pt", padding="max_length", truncation=True, max_length=128)

with torch.no_grad():
    outputs = model(**inputs)
    prediction = torch.argmax(outputs.logits, dim=-1).item()

label = "Positive" if prediction == 1 else "Negative"
print(label)
```

## Built By

Nitesh — AI/ML Engineer