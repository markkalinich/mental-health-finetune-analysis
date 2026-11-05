---
pipeline_tag: text-classification
tags:
- text-classification
- sentiment-analysis
language: hi
license: mit
---

# 🇮🇳 Hindi Sentiment Analysis Model

This repository contains a fine-tuned Hindi Sentiment Analysis model built using the HuggingFace Transformers library.
It predicts sentiment for Hindi text and classifies it into:

- **Positive**
- **Neutral**
- **Negative**

This model is suitable for Hindi tweets, reviews, comments, and general Hindi language sentiment tasks.

---


## 🚀 Model Overview

- **Model type:** Sequence Classification  
- **Base model:** Multilingual Transformer  
- **Framework:** HuggingFace Transformers  
- **Language:** Hindi (hi)  
- **Task:** Sentiment Classification  

This model was fine-tuned using a labeled Hindi dataset containing user-generated text such as tweets/comments.

---

## 🧠 Intended Usage

You can use this model for:

- Hindi sentiment analysis  
- Social media monitoring  
- Review classification  
- Feedback analysis  
- Tweet polarity detection  

---

## 🔍 Example Inference (Python)

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

model_name = "ShivamSharma8168/hindi-sentiment-model"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

labels = ["negative", "neutral", "positive"]

def predict_sentiment(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    outputs = model(**inputs)
    pred = torch.argmax(outputs.logits, dim=1).item()
    return labels[pred]

print(predict_sentiment("यह फ़िल्म बहुत अच्छी है"))   # positive
print(predict_sentiment("मुझे यह पसंद नहीं आया"))      # negative
