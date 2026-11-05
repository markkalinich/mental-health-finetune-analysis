---
license: mit
datasets:
- ajaykarthick/imdb-movie-reviews
language:
- en
metrics:
- accuracy
- f1
- precision
- recall
base_model:
- google-bert/bert-base-uncased
pipeline_tag: text-classification
library_name: transformers
tags:
- sentiment-analysis
- imdb-dataset
---