---
license: apache-2.0
datasets:
- cogsci13/Amazon-Reviews-2023-Books-Review
language:
- en
metrics:
- mae
- rmse
- accuracy
- f1
base_model:
- answerdotai/ModernBERT-large
pipeline_tag: text-classification
tags:
- sentiment-analysis
- ordinal-regression
- amazon-reviews
- modernbert
- text-classification
- rating-prediction
library_name: transformers
---
