---
language: en
license: apache-2.0
tags:
- sentiment-analysis
- text-classification
- distilbert
datasets:
- imdb
metrics:
- accuracy
- f1
pipeline_tag: text-classification
widget:
- text: I absolutely loved this movie!
- text: What a waste of time.
---

# my-sentiment-analyzer

Fine-tuned `distilbert-base-uncased` for binary sentiment classification.

## Evaluation Results

| Metric    | Score |
|-----------|-------|
| Accuracy  | 0.873 |
| F1        | 0.875 |
| Precision | 0.857 |
| Recall    | 0.894 |
