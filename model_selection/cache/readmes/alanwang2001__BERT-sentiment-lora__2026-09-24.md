---
library_name: transformers
license: apache-2.0
base_model: google-bert/bert-base-uncased
tags:
- bert
- sentiment-analysis
- text-classification
- transformers
pipeline_tag: text-classification
---

# BERT-sentiment-lora

This model is a fine-tuned version of [google-bert/bert-base-uncased](https://huggingface.co/google-bert/bert-base-uncased) for 3-class movie review sentiment classification.

## Labels

- `0` → negative (−1)
- `1` → mixed (0)
- `2` → positive (+1)

## Training details

- Architecture: BertForSequenceClassification
- Hidden size: 768, Layers: 12, Heads: 12
- Framework: Transformers 5.3.0
