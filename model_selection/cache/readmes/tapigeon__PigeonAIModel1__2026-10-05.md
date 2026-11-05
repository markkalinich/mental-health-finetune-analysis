---
language: en
license: mit
tags:
- text-classification
- good-vs-bad
- sentiment
---

# 🐦 PigeonAIModel1

This is a simple text classification model trained to detect whether an input sentence is **positive (good)** or **negative (bad)**, based on labeled examples of common good and bad expressions.

## 🧠 How it works

- Fine-tuned on a synthetic dataset of 1000 labeled sentences.
- Uses `distilbert-base-uncased` architecture from Hugging Face Transformers.

## 🧪 Example Usage

```python
from transformers import pipeline

classifier = pipeline("text-classification", model="tapigeon/PigeonAIModel1")
print(classifier("You are amazing!"))      # → Good
print(classifier("You're so stupid!"))     # → Bad
