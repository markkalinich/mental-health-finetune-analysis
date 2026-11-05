---
language: en
license: mit
tags:
- sentiment-analysis
- text-classification
- yelp
- transformers
- distilbert
---

# Yelp Reviews Sentiment Analyzer

## Model Overview
This is a DistilBERT-based sentiment analysis model fine-tuned on a subset of the Yelp Open Dataset. It classifies restaurant reviews into three categories: Negative, Neutral, and Positive.

## Intended Use
- Sentiment classification of restaurant reviews for business insights, customer feedback analysis, or academic research.
- Can be integrated into applications to provide real-time sentiment detection.

## Training Data
- Yelp Open Dataset (restaurant reviews subset).
- Labels derived from star ratings converted into sentiment classes.

## Model Architecture
- Based on `distilbert-base-uncased`.
- Fine-tuned using Hugging Face's `AutoModelForSequenceClassification`.

## Performance
- Accuracy: ~78.5%
- F1 Score: ~78.4%
- Precision: ~78.3%
- Recall: ~78.5%

## Limitations
- Performance may vary on reviews from domains outside Yelp restaurants.
- Model is trained only on English-language reviews.
- Neutral class can be subjective, and borderline cases may be misclassified.

## How to Use
Use Hugging Face Transformers pipeline:

```python
from transformers import pipeline

sentiment_analyzer = pipeline("sentiment-analysis", model="fitsblb/YelpReviewsAnalyzer")

result = sentiment_analyzer("The food was amazing but the service was slow.")
print(result)
