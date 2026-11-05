---
license: mit
language:
- en
library_name: transformers
pipeline_tag: text-classification
tags:
- sentiment-analysis
- nlp
- amazon-reviews
- roberta
---

# Amazon Fine Food Reviews - RoBERTa Sentiment Analysis

## Model Description
This is a fine-tuned **RoBERTa** model for **Sentiment Analysis**, trained on the **Amazon Fine Food Reviews** dataset. It classifies English food reviews into three categories: `positive`, `neutral`, and `negative`.

This model is part of an academic Web Mining project developed at EMSI Marrakech.

### Performance
- **Accuracy:** ~84%
- **F1-Score (Macro):** ~0.84

### Intended Uses
- **Intended Use:** Analyzing customer sentiment in e-commerce food reviews.
- **Language:** English

### How to use
You can use this model directly with a pipeline for text classification:

```python
from transformers import pipeline

# Load the model
sentiment_classifier = pipeline("text-classification", model="aablaess/amazon-reviews-roberta")

# Analyze a review
result = sentiment_classifier("This product is absolutely delicious, I will buy it again!")
print(result)
# [{'label': 'positive', 'score': 0.98...}]