---
language: en
datasets:
- dair-ai/emotion
metrics:
- accuracy
- f1
tags:
- emotion-classification
- text-classification
- distilbert
license: apache-2.0
library_name: transformers
---

# DistilBERT Emotion Classifier 🎭

This is a fine-tuned DistilBERT model for emotion classification trained on the
[dair-ai/emotion](https://huggingface.co/datasets/dair-ai/emotion) dataset.

## 🧠 Model Details
- **Base model:** distilbert-base-uncased  
- **Task:** Text Classification (Emotion Detection)  
- **Languages:** English  
- **Labels:** sadness, joy, love, anger, fear, surprise  
- **Training epochs:** 2  
- **Batch size:** 64  

## 📊 Evaluation Metrics on Test Data
| Metric | Value |
|:--------|:-------|
| Accuracy | 0.919 |
| F1 Score | 0.918 |

## Usage
```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

model_name = "tsid7710/distillbert-emotion-model"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

text = "I am feeling great today!"
inputs = tokenizer(text, return_tensors="pt")
with torch.inference_mode():
    logits = model(**inputs).logits
pred = torch.argmax(logits, dim=-1).item()
print(pred)
