---
language:
- vi
- en
tags:
- text-classification
- content-moderation
- tiktok
- pytorch
license: mit
datasets:
- custom
metrics:
- f1
- accuracy
---

# TikTok Content Safety - Text Classifier

This model classifies TikTok video text content (captions, comments) as **safe** or **harmful**.

## Usage

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification

tokenizer = AutoTokenizer.from_pretrained("KhoiBui/tiktok-text-safety-classifier")
model = AutoModelForSequenceClassification.from_pretrained("KhoiBui/tiktok-text-safety-classifier")

text = "your text here"
inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=512)
outputs = model(**inputs)
prediction = outputs.logits.argmax(-1).item()  # 0=safe, 1=harmful
```

## Model Details
- **Base Model**: XLM-RoBERTa / CafeBERT
- **Task**: Binary classification (safe/harmful)
- **Training Data**: TikTok video metadata (Vietnamese + English)
