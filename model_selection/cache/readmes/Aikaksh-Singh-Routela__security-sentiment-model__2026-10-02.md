---
language: en
license: mit
tags:
- sentiment-analysis
- cybersecurity
- bert
widget:
- text: "Security team successfully prevents major data breach"
  example_title: "Positive"
- text: "Ransomware attack shuts down hospital systems"
  example_title: "Negative"
- text: "New security guidelines published by agency"
  example_title: "Neutral"
---

# Security Sentiment Analyzer

Fine-tuned BERT model that analyzes sentiment of cybersecurity news headlines.

## Model Details

- **Base Model:** `bert-base-uncased`
- **Task:** Text Classification (Sentiment Analysis)
- **Labels:**
    - `0`: Positive 🟢
    - `1`: Negative 🔴
    - `2`: Neutral 🔵

## Accuracy

**87.5%** on test set

## How to Use

```python
from transformers import pipeline

classifier = pipeline("text-classification", model="Aikaksh-Singh-Routela/security-sentiment-model")

result = classifier("Ransomware attack shuts down hospital systems")
print(result)
