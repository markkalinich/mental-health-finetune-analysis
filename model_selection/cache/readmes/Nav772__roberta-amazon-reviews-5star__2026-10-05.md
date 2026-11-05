
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
- roberta
- multi-class-classification
---

# RoBERTa Fine-tuned on Amazon Reviews (5-Star Rating)

## Model Description

This model is a fine-tuned version of `roberta-base` for 5-class sentiment classification, predicting star ratings (1-5) from Amazon product reviews.

## Comparison with DistilBERT

This model was trained as part of a model comparison study:

| Model | Parameters | Accuracy | Off-by-one Accuracy | Inference Speed |
|-------|------------|----------|---------------------|-----------------|
| DistilBERT | 67M | 54.95% | 92.45% | 1.83x faster |
| **RoBERTa** | **125M** | **59.90%** | **95.10%** | Baseline |

RoBERTa provides ~5 percentage points higher accuracy at the cost of slower inference.

## Training Data

- **Dataset**: SetFit/amazon_reviews_multi_en
- **Train samples**: 20,000 (subset)
- **Test samples**: 2,000 (subset)
- **Classes**: 1 star, 2 stars, 3 stars, 4 stars, 5 stars

## Training Procedure

- **Base model**: roberta-base
- **Epochs**: 3
- **Batch size**: 16
- **Learning rate**: 2e-5
- **Max sequence length**: 256

## Usage
```python
from transformers import pipeline

classifier = pipeline("text-classification", model="Nav772/roberta-amazon-reviews-5star")
result = classifier("This product exceeded my expectations! Great quality.")
print(result)
```

## When to Use This Model

- Choose **RoBERTa** when accuracy is the priority and latency is less critical
- Choose **DistilBERT** when you need faster inference or have resource constraints

## Demo

Try the model comparison demo: [sentiment-model-comparison](https://huggingface.co/spaces/Nav772/sentiment-model-comparison)

## Limitations

- Trained on Amazon product reviews; may not generalize to other review domains
- Adjacent star ratings (e.g., 2 vs 3 stars) are inherently difficult to distinguish
- English language only
