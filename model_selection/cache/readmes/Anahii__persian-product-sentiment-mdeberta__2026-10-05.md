---
language: fa
license: apache-2.0
library_name: transformers
tags:
- sentiment-analysis
- persian
- product-reviews
- mdeberta
metrics:
- accuracy
- f1
pipeline_tag: text-classification
---

# Persian Product Review Sentiment Analysis (mDeBERTa)

Binary sentiment classification (positive/negative) fine-tuned on Persian e-commerce product reviews.

## Evaluation Results

| Metric | Score |
| --- | --- |
| **Accuracy** | 87.54% |
| **Macro F1-Score** | 87.54% |
| **Macro Precision** | 87.55% |
| **Macro Recall** | 87.58% |

## Model Description
This model fine-tunes mDeBERTa on Persian product reviews to classify user sentiment into Positive and Negative categories.