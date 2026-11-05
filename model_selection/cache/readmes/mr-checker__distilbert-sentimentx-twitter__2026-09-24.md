---
license: apache-2.0
language:
- en
metrics:
- accuracy
- f1
base_model:
- distilbert/distilbert-base-uncased
tags:
- sentiment-analysis
- twitter
- nlp
- pytorch
---

# SentimentX-DistilBERT

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) trained on the **Sentiment140** dataset. It is designed to classify the sentiment of short-form text (specifically tweets) into two categories: **Positive** and **Negative**.

## Model Description

- **Developed by:** [Kalyan Sai]
- **Model type:** Transformer-based Text Classification
- **Language(s) (NLP):** English
- **License:** Apache 2.0
- **Finetuned from model:** distilbert-base-uncased

## Intended Uses & Limitations

### Intended Use
This model is intended for real-time sentiment monitoring of social media feeds, specifically Twitter (X). It is optimized for high-throughput inference environments.

### Limitations
- The model was trained on a binary dataset (Positive/Negative). It may not perform accurately on neutral text.
- Performance may decrease on text with heavy use of modern slang or emojis not present in the 2009 Sentiment140 dataset.

## Training and Evaluation Data

The model was trained on a sample of **100,000 tweets** from the Sentiment140 dataset, which contains 1.6 million tweets automatically labeled (0 = negative, 4 = positive) based on emoticons.

### Training Procedure
- **Hardware:** Trained on Kaggle NVIDIA Tesla T4 GPU.
- **Optimizer:** AdamW
- **Learning Rate:** Default (5e-5)
- **Epochs:** 2
- **Mixed Precision:** FP16 enabled for acceleration.

## Evaluation Results

The model achieved the following results on the evaluation set:

- **Accuracy:** 82.44%
- **F1-Score:** 82.50%
- **Precision:** 83.01%
- **Recall:** 81.99%

## How to Get Started with the Model

Use the code below to get started with the model locally:

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

tokenizer = AutoTokenizer.from_pretrained("mr-checker/sentimentX-distilbert")
model = AutoModelForSequenceClassification.from_pretrained("mr-checker/sentimentX-distilbert")

text = "SentimentX is working perfectly!"
inputs = tokenizer(text, return_tensors="pt")

with torch.no_grad():
    logits = model(**inputs).logits

predicted_class_id = logits.argmax().item()
# 0: Negative, 1: Positive
```
