---
language: en
tags:
- sentiment-analysis
base_model:
- ProsusAI/finbert
---

## Model Description

This is a fine-tuned version of [ProsusAI/finbert](https://huggingface.co/ProsusAI/finbert) for cryptocurrency news sentiment analysis. The model classifies text into three sentiment categories: **negative**, **neutral**, and **positive**.

### Key Features

- **Base Model**: ProsusAI/finbert
- **Task**: Sentiment Classification (3 classes)
- **Domain**: Cryptocurrency news and social media
- **Custom Tokens**: 520 crypto-specific tokens added to vocabulary


## Usage

```python
import torch 
from transformers import BertForSequenceClassification, AutoTokenizer
from torch.nn import functional as F


tokenizer = AutoTokenizer.from_pretrained('houmanrajabi/CoinPulse')
model = BertForSequenceClassification.from_pretrained('houmanrajabi/CoinPulse')
model.eval()

def predict_sentiment(text, temperature=2.0):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=512)
    with torch.no_grad():
        outputs = model(**inputs)
        label_map = {0: 'negative', 1: 'neutral', 2: 'positive'}
        logits = outputs.logits / temperature
        predicted_class_id = logits.argmax().item()
        confidence = F.softmax(logits, dim=1)[0, predicted_class_id].item()
        return label_map[predicted_class_id].capitalize() , confidence
    
sample_texts = [
    "The company reported record profits and exceeded all expectations.",
    "Stock prices plummeted after the disappointing earnings report.",
    "The quarterly results were in line with market forecasts."
]
for i, text in enumerate(sample_texts):
    sentiment, confidence = predict_sentiment(text)
    print(f"{i+1}) {text}\nSentiment: {sentiment}\nConfidence: {round(confidence,2)}\n")

```