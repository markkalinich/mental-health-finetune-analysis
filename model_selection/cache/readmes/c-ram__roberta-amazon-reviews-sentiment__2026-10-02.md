---
language: en
license: mit
base_model: roberta-base
tags:
  - text-classification
  - sentiment-analysis
  - roberta
  - amazon-reviews
---

# RoBERTa Amazon Reviews Sentiment Classifier

Fine-tuned version of `roberta-base` for 3-class sentiment classification (negative / neutral / positive) on Amazon product reviews.

## Model Details

- **Base model:** roberta-base
- **Task:** Sentiment classification (3-class)
- **Dataset:** Amazon product reviews (balanced sample)
- **Language:** English
- **Repository:** [amazon-review-classifier-roberta-sentiment-finetuning](https://github.com/chandlershortlidge/amazon-review-classifier-roberta-sentiment-finetuning)

## Performance

Evaluated on a held-out test set of 1,086 reviews:

| Class    | Precision | Recall | F1-Score | Support |
|----------|-----------|--------|----------|---------|
| Negative | 0.84      | 0.85   | 0.85     | 361     |
| Neutral  | 0.77      | 0.71   | 0.74     | 350     |
| Positive | 0.86      | 0.91   | 0.89     | 375     |
| **Macro avg** | **0.82** | **0.82** | **0.82** | 1086 |
| **Weighted avg** | **0.82** | **0.83** | **0.83** | 1086 |

**Overall accuracy: 83%**

## Usage

```python
from transformers import pipeline

classifier = pipeline("text-classification", model="c-ram/roberta-amazon-reviews-sentiment")
classifier("This product exceeded my expectations!")
```