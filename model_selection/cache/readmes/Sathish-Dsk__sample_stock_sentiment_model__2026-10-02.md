---
language: en
tags:
- text-classification
- sentiment-analysis
- finance
license: mit
datasets:
- custom
metrics:
- accuracy
model-index:
- name: sample_stock_sentiment_model
  results:
  - task:
      type: text-classification
      name: Sentiment Analysis
    dataset:
      name: custom-dataset
      type: custom
    metrics:
    - type: accuracy
      value: 0.92
---

# My Text Classification Model

This is a BERT-based text classification model trained on custom CSV data.

## Model Details
- **Base Model**: `bert-base-uncased`
- **Task**: Text Classification
- **Languages**: English
- **Labels**: Positive (1), Negative (0)
- **Dataset**: Private CSV dataset (`data.csv`)
- **Framework**: Hugging Face Transformers (PyTorch)

## Usage
```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from transformers import pipeline

# Hugging Face Hub model ID (online)
model_id = "Sathish-Dsk/sample_stock_sentiment_model"

# Load model and tokenizer directly from Hugging Face
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForSequenceClassification.from_pretrained(model_id)

# Create sentiment analysis pipeline
nlp = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)

# Test input
result = nlp("Stock prices of Reliance are expected to rise tomorrow.")
print(result)
