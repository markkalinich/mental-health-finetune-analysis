---
language:
  - en
tags:
- distilbert
- sentiment-analysis
datasets:
- generated_reviews_enth
---

# DistilBERT — Product Review Sentiment Analysis

A DistilBERT model fine-tuned for sentiment analysis on English-language product reviews.

> **Video walkthrough**: [ML Hyperproductivity with Hugging Face — part 1: AutoML with AutoNLP](https://youtube.com/watch?v=s-6V6HlwX98)

## Model Details

| Detail | Value |
|--------|-------|
| **Base model** | [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) |
| **Task** | Sentiment analysis (text classification) |
| **Language** | English |
| **Dataset** | [generated_reviews_enth](https://huggingface.co/datasets/generated_reviews_enth) |

## Usage

```python
from transformers import pipeline

classifier = pipeline("sentiment-analysis", model="juliensimon/reviews-sentiment-analysis")
classifier("This product is amazing, best purchase I've made!")
```

## Resources

- A notebook for **Amazon SageMaker** is available in the `code` subfolder.
