---
license: apache-2.0
language:
- en
pipeline_tag: text-classification
tags:
- yelp
- sentiment-analysis
- roberta
---

# Yelp 5-class Star Rating Classifier (RoBERTa-base)

Fine-tuned `roberta-base` for predicting Yelp star ratings (1–5) from review text. Trained on 50k sampled Yelp reviews.

**Validation accuracy:** 0.6856 · **Macro-F1:** 0.6849

Used by the Yelp Business Intelligence Agent for the optional `classify_review` tool.
