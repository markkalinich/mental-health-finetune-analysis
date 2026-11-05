---
base_model:
- google-bert/bert-base-uncased
tags:
- sentiment-analysis
- text-classification
- imdb
- bert
- fine-tuned
language:
- en
pipeline_tag: text-classification
---
# BERT IMDb Sentiment Classifier

## Dataset
- **IMDb Dataset** (50,000 reviews: 25k train + 25k test)  
- Source: [IMDB Dataset of 50K Movie Reviews Kaggle](https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews)
- Preprocessing: Tokenization via BERT tokenizer

## Model Architecture
- Base: `bert-base-uncased` from Hugging Face Transformers
- Fine-tuned with a classification head (linear layer)
- Trained with PyTorch using AdamW optimizer and scheduler
