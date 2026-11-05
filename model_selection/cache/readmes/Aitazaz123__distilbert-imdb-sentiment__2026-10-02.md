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
Fine-tuned from `distilbert-base-uncased` on 5,000 IMDb movie reviews for 3 epochs.
Classifies text as POSITIVE or NEGATIVE sentiment.

## Training Data
- **Source**: IMDb Large Movie Review Dataset
- **Train**: 5,000 samples | **Validation**: 1,000 samples
- Label balance: approximately 50% positive, 50% negative

## Evaluation Results
| Metric   | Score |
|----------|-------|
| Accuracy | 88.6% |
| F1 Score | 0.886 |

## Baseline Comparison
| Model                        | Accuracy |
|------------------------------|----------|
| TF-IDF + Logistic Regression | 89.4%    |
| DistilBERT (this model)      | 88.6%    |

## How to Use
```python
from transformers import pipeline
classifier = pipeline('text-classification', model='Aitazaz123/distilbert-imdb-sentiment')
result = classifier('This movie was absolutely incredible!')
# Output: [{'label': 'POSITIVE', 'score': 0.997}]
```

## Limitations
- Trained only on English movie reviews — other domains may vary
- May not handle Urdu, Roman Urdu, or code-switched text well
- Sarcasm may be misclassified
