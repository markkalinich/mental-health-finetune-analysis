---
datasets:
  - stanfordnlp/imdb
  - McAuley-Lab/Amazon-Reviews-2023
  - fancyzhx/yelp_polarity
language:
  - es
  - en
metrics:
  - accuracy
  - f1
  - precision
  - recall
base_model: google-bert/bert-base-uncased
library_name: transformers
tags:
  - NLP
  - Bert
  - sentiment-analysis
pipeline_tag: text-classification
license: mit
---
