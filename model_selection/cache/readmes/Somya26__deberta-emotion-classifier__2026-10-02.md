---
language: en
tags:
- emotion-classification
- text-classification
- deberta
license: apache-2.0
---

# DeBERTa Emotion Classifier

This model classifies text into 5 emotions:
- 😠 Anger
- 😨 Fear  
- 😊 Joy
- 😢 Sadness
- 😲 Surprise

## Usage
```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

model_name = "Somya26/deberta-emotion-classifier"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

text = "I am so happy today!"
inputs = tokenizer(text, return_tensors="pt")
outputs = model(**inputs)
probs = torch.sigmoid(outputs.logits).squeeze()

emotions = ['anger', 'fear', 'joy', 'sadness', 'surprise']
for emotion, prob in zip(emotions, probs):
    print(f"{emotion}: {prob:.2%}")
```

## Training

Trained on emotion classification dataset using DeBERTa-v3-base.
