---
license: mit
language:
- en
tags:
- medical-qa
- distilbert
- multiple-choice
---

# 🩺 WMHDS-Medical QA Model

This model is fine-tuned on medical multiple-choice questions to assist with educational and diagnostic reasoning.

## 📌 Model Details
- Base: `distilbert-base-uncased`
- Task: Multiple Choice QA
- Intended use: Educational support, medical training

## 🧪 How to Use
```python
from transformers import AutoTokenizer, AutoModelForMultipleChoice

tokenizer = AutoTokenizer.from_pretrained("LeduBaSK/wmhds-medical")
model = AutoModelForMultipleChoice.from_pretrained("LeduBaSK/wmhds-medical")

## 🏁 Created by: @LeduBaSK