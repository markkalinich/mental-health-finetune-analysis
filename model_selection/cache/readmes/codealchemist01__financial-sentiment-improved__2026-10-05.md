---
language: en
license: apache-2.0
tags:
- financial-sentiment
- sentiment-analysis
- finance
- nlp
- transformers
datasets:
- zeroshot/twitter-financial-news-sentiment
metrics:
- accuracy
- f1
model-index:
- name: financial-sentiment-improved
  results:
  - task:
      type: text-classification
      name: Financial Sentiment Analysis
    dataset:
      name: Twitter Financial News Sentiment
      type: zeroshot/twitter-financial-news-sentiment
    metrics:
    - type: accuracy
      value: 0.847
    - type: f1
      value: 0.845
---

# financial-sentiment-improved

This model is a fine-tuned version of DistilBERT for financial sentiment analysis. It has been trained on financial news and social media data to classify text into three sentiment categories: Bearish (negative), Neutral, and Bullish (positive).

## Model Performance

- **Accuracy**: 0.847
- **F1 Score**: 0.845

## Usage

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

tokenizer = AutoTokenizer.from_pretrained("codealchemist01/financial-sentiment-improved")
model = AutoModelForSequenceClassification.from_pretrained("codealchemist01/financial-sentiment-improved")

def predict_sentiment(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=512)
    
    with torch.no_grad():
        outputs = model(**inputs)
        predictions = torch.nn.functional.softmax(outputs.logits, dim=-1)
    
    labels = ["Bearish", "Neutral", "Bullish"]
    predicted_class = torch.argmax(predictions, dim=-1).item()
    confidence = predictions[0][predicted_class].item()
    
    return {
        "label": labels[predicted_class],
        "confidence": confidence
    }

# Example
result = predict_sentiment("The stock market is showing strong growth today")
print(result)
```

## Training Details

This model was trained using advanced techniques including:
- Balanced dataset sampling
- Custom loss functions
- Learning rate scheduling
- Early stopping

## Intended Use

This model is designed for financial sentiment analysis tasks, including:
- Social media sentiment monitoring
- News sentiment analysis
- Market sentiment tracking
- Financial document analysis
