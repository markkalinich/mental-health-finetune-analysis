---
language: en
license: mit
library_name: transformers
tags:
- text-classification
- sentiment-analysis
datasets:
- stanfordnlp/imdb
base_model: sentence-transformers/all-MiniLM-L6-v2
---

# Fine-tuned all-MiniLM-L6-v2 for IMDB Sentiment Classification

This is a sentence-transformer model (`sentence-transformers/all-MiniLM-L6-v2`) fine-tuned for sentiment classification on the IMDB movie reviews dataset. It classifies text as either **positive** (LABEL_1) or **negative** (LABEL_0).

## Model Description

This model was fine-tuned as part of a university assignment to demonstrate the effectiveness of transfer learning. By adapting a pre-trained sentence encoder to a specific downstream task, the model achieves high accuracy in predicting the sentiment of movie reviews.

