---
license: mit
language:
- gu
- en
- hi
base_model: google/muril-base-cased
tags:
- sentiment-analysis
- text-classification
- code-mixed
- gujlish
- hinglish
metrics:
- accuracy
pipeline_tag: text-classification
library_name: transformers
---

# Gujlish & Hinglish Sentiment Analysis Model (MuRIL Fine-Tuned)

This model is a fine-tuned version of [google/muril-base-cased](https://huggingface.co/google/muril-base-cased) trained on a custom synthetic dataset of **150,000 code-mixed samples**. It is designed to detect sentiment (Positive, Negative, Neutral) in Indian languages, specifically handling **Code-Switching** (mixing Gujarati/Hindi with English).

## Project Overview
* **Problem:** Standard AI models struggle with "Gujlish" (Gujarati written in English script) or "Hinglish".
* **Solution:** This model uses MuRIL (Multilingual Representations for Indian Languages) and was fine-tuned on a massive synthetic dataset covering diverse topics like Tech, Movies, Food, and Daily Life.
* **Performance:** Achieved **100% Accuracy** on the validation set.

## Intended Use
This model is ideal for:
* Analyzing social media comments (YouTube, Instagram) in India.
* Processing audio transcriptions from mixed-language conversations.
* Customer feedback analysis for Indian apps.

## How to Use

```python
from transformers import pipeline

# Load the model
classifier = pipeline("text-classification", model="marshal-yash/gujlish-sentiment-analysis")

# Test on Code-Mixed Text
text = "Aa movie bahu saras che, maja aavi!"
result = classifier(text)

print(result)
# Output: [{'label': 'Positive', 'score': 0.99}]