---
language: en
license: apache-2.0
tags:
  - sentiment analysis
  - text classification
  - bert
  - transformers
  - news
  - reviews
---

# SentimentBERT — Fine-tuned BERT for Sentiment Classification (Positive, Neutral, Negative)

**SentimentBERT** is a Finetuned BERT-based model specifically for **sentiment classification of sentences** into three categories: **Positive**, **Negative**, and **Neutral**.

This model has been trained on a ** 130K large and diverse dataset of news articles** across a wide range of categories. It achieves **over 86% accuracy** and demonstrates a strong understanding of sentence-level sentiment, even in nuanced or mixed-context cases.

---

## Model Highlights

- **Base model**: `bert-base-uncased`
- **Fine tuned for**: Sentiment classification (3-class)
- **Accuracy**: > 86%
- **Classes**: Positive, Neutral, Negative
- **Language**: English
- **Format**: `safetensors`
- **Tokenizer**: Compatible with `bert-base-uncased`

---

## Applications

This model is well-suited for:

- **News article sentiment analysis**
- **Amazon product review analysis**
- **Customer support or service feedback systems**
- **General-purpose opinion mining**



Thanks for visiting and downloading this model!
If this model helped you, please consider leaving a like. Your support helps this model reach more developers and encourages further improvements if any.
---

## How to use the model

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

model = AutoModelForSequenceClassification.from_pretrained("mervp/SentimentBERT")
tokenizer = AutoTokenizer.from_pretrained("mervp/SentimentBERT")

def predict_sentiment(text):
    model.eval()
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits
        prediction = torch.argmax(logits, dim=-1).item()
    label = model.config.id2label[prediction]
    return label

print(predict_sentiment("What a beautiful day."))               # positive
print(predict_sentiment("The service was excellent."))          # positive
print(predict_sentiment("He did a fantastic job."))             # positive
print(predict_sentiment("The experience was terrible."))        # negative
print(predict_sentiment("Everything went wrong."))              # negative
print(predict_sentiment("He opened the door and walked in."))   # neutral
print(predict_sentiment("They are meeting at 5 PM."))           # neutral
print(predict_sentiment("She has a cat."))                      # neutral
