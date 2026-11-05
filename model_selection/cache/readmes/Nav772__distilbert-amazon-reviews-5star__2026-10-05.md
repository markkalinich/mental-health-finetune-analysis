
---
license: mit
language: en
datasets:
- SetFit/amazon_reviews_multi_en
metrics:
- accuracy
pipeline_tag: text-classification
tags:
- sentiment-analysis
- distilbert
- multi-class-classification
---

# DistilBERT Fine-tuned on Amazon Reviews (5-Star Rating)

## Model Description

This model is a fine-tuned version of `distilbert-base-uncased` for 5-class sentiment classification, predicting star ratings (1-5) from Amazon product reviews.

## Training Data

- **Dataset**: SetFit/amazon_reviews_multi_en
- **Train samples**: 20,000 (subset)
- **Test samples**: 2,000 (subset)
- **Classes**: 1 star, 2 stars, 3 stars, 4 stars, 5 stars

## Training Procedure

- **Base model**: distilbert-base-uncased
- **Epochs**: 3
- **Batch size**: 16
- **Learning rate**: 2e-5
- **Max sequence length**: 256

## Evaluation Results

- **Accuracy**: 54.95%
- **Off-by-one accuracy**: 92.45%

Note: 55% accuracy on a 5-class problem is 2.75x better than random chance (20%). The high off-by-one accuracy (92%) indicates the model rarely makes catastrophic errors.

## Usage
```python
from transformers import pipeline

classifier = pipeline("text-classification", model="Nav772/distilbert-amazon-reviews-5star")
result = classifier("This product exceeded my expectations! Great quality.")
print(result)
```

## Limitations

- Trained on Amazon product reviews; may not generalize to other review domains
- Adjacent star ratings (e.g., 2 vs 3 stars) are inherently difficult to distinguish due to subjective labeling
- English language only
