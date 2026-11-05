---
language: en
license: apache-2.0
base_model: distilbert/distilbert-base-uncased
tags:
  - text-classification
  - sentiment-analysis
  - distilbert
datasets:
  - imdb
metrics:
  - loss
---

# DistilBERT Sentiment Classifier (IMDB)

Fine-tuned [distilbert-base-uncased](https://huggingface.co/distilbert/distilbert-base-uncased) for binary sentiment classification (positive/negative) on a subset of the IMDB movie review dataset.

## Model Details

- **Base model:** distilbert/distilbert-base-uncased
- **Task:** Sentiment analysis (binary classification)
- **Labels:** `0` = negative, `1` = positive
- **Max sequence length:** 128 tokens

## Training

| Hyperparameter | Value |
|---|---|
| Dataset | IMDB (500 samples, 80/20 split) |
| Epochs | 2 |
| Batch size | 8 |
| Learning rate | 5e-5 (linear decay) |

**Final eval loss:** 0.0008

## Usage

```python
from transformers import pipeline

classifier = pipeline("text-classification", model="chinmaygarde/hello")
classifier("This movie was absolutely fantastic!")
# [{'label': 'LABEL_1', 'score': 0.999}]
```
