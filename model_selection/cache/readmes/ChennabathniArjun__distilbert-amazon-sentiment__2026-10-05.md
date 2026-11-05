---
license: apache-2.0
datasets:
- PJ2005/amazon-fine-food-reviews
language:
- en
metrics:
- accuracy
- precision
- recall
- f1
base_model:
- distilbert/distilbert-base-uncased-finetuned-sst-2-english
- distilbert/distilbert-base-uncased-distilled-squad
pipeline_tag: text-classification
tags:
- sentiment-analysis
- text-classification
- distilbert
---