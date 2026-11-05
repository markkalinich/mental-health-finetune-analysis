---
license: apache-2.0
base_model: distilbert-base-uncased
datasets:
  - amazon_polarity
language:
  - en
pipeline_tag: text-classification
tags:
  - sentiment-analysis
  - product-reviews
metrics:
  - accuracy
  - f1
---

# DistilBERT — Amazon Product Review Sentiment

`distilbert-base-uncased` fine-tuned on a subset of the
[amazon_polarity](https://huggingface.co/datasets/amazon_polarity) dataset for
binary **POSITIVE / NEGATIVE** sentiment classification of product reviews.

Motivation: the common off-the-shelf sentiment model is trained on movie
reviews (SST-2). This model adapts to the product-review domain.

## Results (1,000 held-out product reviews)

| Model | Accuracy | F1 |
|---|---|---|
| Baseline (movie-trained, SST-2) | 88.6% | 0.888 |
| **This model (product reviews)** | **89.7%** | **0.899** |

## Usage

```python
from transformers import pipeline
clf = pipeline("sentiment-analysis", model="rahiqr/distilbert-amazon-sentiment")
clf("Arrived quickly and works perfectly!")
```

- Live demo: https://huggingface.co/spaces/rahiqr/review-intelligence
- Source & training code: https://github.com/rahiqraees/review-intelligence
