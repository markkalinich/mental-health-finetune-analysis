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
- name: financial-sentiment-bert-large
  results:
  - task:
      type: text-classification
      name: Financial Sentiment Analysis
    dataset:
      name: Twitter Financial News Sentiment
      type: zeroshot/twitter-financial-news-sentiment
    metrics:
    - type: accuracy
      value: 0.843
      name: Accuracy
---

# financial-sentiment-bert-large

## Model Description

BERT-Large financial sentiment analysis model with high accuracy

This model is fine-tuned from `bert-large-uncased` for financial sentiment analysis, capable of classifying financial text into three categories:
- **Bearish** (0): Negative financial sentiment
- **Neutral** (1): Neutral financial sentiment  
- **Bullish** (2): Positive financial sentiment

## Model Performance

- **Accuracy**: 0.843
- **Dataset**: Twitter Financial News Sentiment
- **Base Model**: bert-large-uncased

## Usage

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Load model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("codealchemist01/financial-sentiment-bert-large")
model = AutoModelForSequenceClassification.from_pretrained("codealchemist01/financial-sentiment-bert-large")

# Example usage
text = "Apple stock is showing strong growth potential"
inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)

with torch.no_grad():
    outputs = model(**inputs)
    predictions = torch.nn.functional.softmax(outputs.logits, dim=-1)
    predicted_class = torch.argmax(predictions, dim=-1).item()

# Labels: 0=Bearish, 1=Neutral, 2=Bullish
labels = ["Bearish", "Neutral", "Bullish"]
print(f"Prediction: {labels[predicted_class]}")
```

## Training Details

- **Training Dataset**: Twitter Financial News Sentiment
- **Training Framework**: Transformers
- **Optimization**: AdamW
- **Hardware**: RTX GPU

## Limitations

This model is specifically trained for financial sentiment analysis and may not perform well on general sentiment analysis tasks.

## Citation

If you use this model, please cite:

```bibtex
@misc{financial-sentiment-large,
  author = {CodeAlchemist01},
  title = {financial-sentiment-bert-large},
  year = {2024},
  publisher = {Hugging Face},
  url = {https://huggingface.co/codealchemist01/financial-sentiment-bert-large}
}
```
