---
language: en
license: apache-2.0
tags:
- safety
- text-classification
- indian-context
- hinglish
- moderation
---

# SafeOrNot Safety Classification Model

This model detects whether a given text is **safe or unsafe** based on
context-aware classification with a focus on **Indian and Hinglish language usage**.

## Use Case
- Community safety moderation
- Location/place safety scoring (e.g. Maps-style apps)
- Harassment and abuse detection in Indian contexts

## Model Details
- Architecture: Transformer-based (BERT family)
- Task: Binary text classification (Safe / Unsafe)
- Trained on: Custom curated Indian safety dataset

## How to Use

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification

model_id = "aryaman1222/safeornot-safety-model"

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForSequenceClassification.from_pretrained(model_id)
