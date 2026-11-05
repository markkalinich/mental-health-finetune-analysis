---
language: en
license: apache-2.0
tags:
- text-classification
- sentiment-analysis
datasets:
- imdb
metrics:
- accuracy
pipeline_tag: text-classification
---

# DistilBERT Fine-Tuned on IMDb for Sentiment Analysis

This model is a fine-tuned version of `distilbert-base-uncased` on the IMDb movie reviews dataset. It was developed during Week 3 of the AI Internship to perform binary sentiment classification (Positive/Negative).

## Model Description
- **Developed by:** Shah Jahan SHEIKH (AI Intern)
- **Model Type:** Text Classification (Sentiment Analysis)
- **Language:** English
- **Base Model:** `distilbert-base-uncased`

## Training Results
The model was trained on a downsampled subset of 1,000 training examples and evaluated on 200 test examples over 2 epochs.

- **Final Test Accuracy:** 74.50%
- **Training Loss:** 0.4456
- **Validation Loss:** 0.5367

## How to Use
You can easily load and use this model for inference using the Hugging Face `pipeline`:

```python
from transformers import pipeline

# Load the model from the Hub
classifier = pipeline("text-classification", model="ShahJahan-del/imdb-sentiment-analysis")

# Test with custom reviews
reviews = [
    "This movie was an absolute masterpiece, the acting was phenomenal!",
    "I fell asleep after 20 minutes. Total waste of time and money."
]

results = classifier(reviews)
for review, res in zip(reviews, results):
    sentiment = "POSITIVE" if res['label'] == "LABEL_1" else "NEGATIVE"
    print(f"Review: '{review}' -> {sentiment} ({res['score']:.2%})")