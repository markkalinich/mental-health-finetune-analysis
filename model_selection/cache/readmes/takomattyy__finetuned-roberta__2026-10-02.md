---
language: 
- en
- tl
tags:
- sentiment-analysis
- filipino
- english
- roberta
- service-reviews
license: mit
datasets:
- custom
metrics:
- accuracy
- f1
pipeline_tag: text-classification
---

# HandyHome Sentiment Analysis

This model classifies sentiment in Filipino-English service reviews.

## Model Details

- **Base Model**: RoBERTa
- **Task**: Sentiment Classification (3 classes)
- **Languages**: Filipino, English (mixed)
- **Classes**: 
  - 0: Negative
  - 1: Neutral  
  - 2: Positive

## Usage

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Load model and tokenizer
model_name = "YOUR_USERNAME/handyhome-sentiment-roberta"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# Predict sentiment
text = "Magaling yung service, very professional!"
inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=512)

with torch.no_grad():
    outputs = model(**inputs)
    predictions = torch.softmax(outputs.logits, dim=1)
    predicted_class = torch.argmax(predictions, dim=1).item()

labels = ["negative", "neutral", "positive"]
print(f"Sentiment: {labels[predicted_class]}")
```

## Training Data

Trained on HandyHome service reviews dataset containing Filipino-English mixed language reviews.