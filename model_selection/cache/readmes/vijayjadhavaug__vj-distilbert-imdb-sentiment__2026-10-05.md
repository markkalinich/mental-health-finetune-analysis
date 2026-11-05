---
tags:
- sentiment-analysis
- imdb
- transformers
- distilbert
license: apache-2.0
---

# 🏆 DistilBERT IMDB Sentiment Classifier

This is a **fine-tuned DistilBERT model** for **sentiment analysis** on the IMDB dataset.  
It classifies reviews into **Positive** or **Negative** sentiments.

## 📖 Model Details
- **Base Model:** `distilbert-base-uncased`
- **Dataset:** IMDB Reviews
- **Fine-Tuning Epochs:** 3
- **Batch Size:** 16
- **Evaluation Loss:** 0.291

## 🚀 Usage
```python
from transformers import pipeline

classifier = pipeline("sentiment-analysis", model="vj/distilbert-imdb-sentiment")

result = classifier("The movie was absolutely fantastic!")
print(result)  # [{'label': 'POSITIVE', 'score': 0.98}]
