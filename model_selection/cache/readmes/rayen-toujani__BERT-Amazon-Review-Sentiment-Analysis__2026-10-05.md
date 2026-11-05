---
language: en
tags:
- bert
- text-classification
- sentiment-analysis
- amazon-reviews
datasets:
- amazon_fine_food_reviews
metrics:
- accuracy
---

# BERT Amazon Review Sentiment Analysis

## Model Description
Fine-tuned BERT-base model for classifying Amazon food reviews as positive (4-5 stars) or negative (1-2 stars).

## Usage
```python
from transformers import pipeline
classifier = pipeline("text-classification", model="rayen-toujani/BERT-Amazon-Review-Sentiment-Analysis")
classifier("This product is amazing!")
