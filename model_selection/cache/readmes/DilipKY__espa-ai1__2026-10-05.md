---
title: ESPA AI
emoji: 🤖
colorFrom: blue
colorTo: green
sdk: transformers
sdk_version: 4.21.1
app_file: app.py
license: mit
tags:
- text-classification
- distilbert
- NLP
- sentiment-analysis
short_description: A DistilBERT-based model fine-tuned on IMDb for text classification.
---
# Model Card for ESPA AI

ESPA AI is a text classification model fine-tuned on the IMDb dataset using DistilBERT. It is designed to classify movie reviews as either positive or negative.

## Model Details

### Model Description

This model uses the DistilBERT architecture, a smaller, faster version of BERT, to perform sentiment analysis on text data. It has been fine-tuned on the IMDb dataset for binary classification (positive or negative reviews).

- **Developed by:** DilipKY
- **Funded by:** [Optional Information]
- **Model type:** Transformer-based model (DistilBERT)
- **Language(s):** English
- **License:** MIT License
- **Finetuned from model:** distilbert-base-uncased

### Model Sources

- **Repository:** [DilipKY/espa-ai](https://huggingface.co/DilipKY/espa-ai)
- **Paper:** [DistilBERT: A smaller, faster, cheaper version of BERT](https://arxiv.org/abs/1910.01108)

## Uses

### Direct Use

This model can be used to classify text data into positive or negative categories. It is useful for sentiment analysis in applications like customer feedback analysis, review classification, etc.

```python
from transformers import pipeline

# Load pre-trained model from Hugging Face
classifier = pipeline("text-classification", model="DilipKY/espa-ai")

# Test on a sample review
sample_text = "This movie was amazing! The plot was so engaging and the acting was superb."
result = classifier(sample_text)
print(result)
