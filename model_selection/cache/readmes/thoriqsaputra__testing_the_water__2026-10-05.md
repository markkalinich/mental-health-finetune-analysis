---
tags:
  - text-classification
  - sentiment-analysis
  - distilbert
license: apache-2.0
---

# My Awesome Model

This is a fine-tuned DistilBERT model for sentiment analysis on the IMDb dataset. It classifies movie reviews as positive or negative.

## Usage

```python
from transformers import AutoModelForSequenceClassification, AutoTokenizer
model = AutoModelForSequenceClassification.from_pretrained("your_username/testing_the_water")
tokenizer = AutoTokenizer.from_pretrained("your_username/testing_the_water")
```

## Training

- Dataset: IMDb (subset of 1,000 samples)
- Epochs: 1
- Batch Size: 8
