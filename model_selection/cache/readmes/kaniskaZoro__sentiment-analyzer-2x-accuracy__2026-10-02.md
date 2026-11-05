---
language: en
tags:
  - text-classification
  - sentiment-analysis
library_name: transformers
license: apache-2.0
datasets:
  - imdb
---


# Sentiment Analyzer

## Overview
This repository contains a sentiment analysis model trained on the IMDb dataset. The model is based on `distilbert-base-uncased` and fine-tuned for binary sentiment classification (positive/negative).

## Files
- `sentiment_model/` : Contains the trained model files.
- `results/checkpoint-125/` : Checkpoint directory from training.
- `sample_data/` : Sample dataset files used for training and evaluation.
- `wandb/` : Weights & Biases logs and run data.

## Installation
```bash
pip install transformers datasets sentence-transformers
```

## Usage
```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification

tokenizer = AutoTokenizer.from_pretrained('kaniskaZoro/sentiment-analyzer')
model = AutoModelForSequenceClassification.from_pretrained('kaniskaZoro/sentiment-analyzer-2x-accuracy')

text = "The movie was fantastic!"
inputs = tokenizer(text, return_tensors='pt', padding=True, truncation=True, max_length=256)
outputs = model(**inputs)
```

## Training
The model was trained using the `Trainer` API from Hugging Face Transformers with the following settings:
- Dataset: IMDb (subset of 2000 train, 500 test samples for demonstration)
- Batch size: 16
- Epochs: 1
- Logging and checkpointing integrated with Weights & Biases

## License
Specify license here (e.g., MIT, Apache 2.0).

