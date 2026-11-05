---
language: vi
license: mit
tags:
- vietnamese
- sentiment-analysis
- phobert
- text-classification
datasets:
- custom
metrics:
- f1
---

# Vietnamese Sentiment Analysis Model

This model is fine-tuned from [vinai/phobert-base](https://huggingface.co/vinai/phobert-base) for Vietnamese sentiment analysis with entity context.

## Model description

The model classifies text sentiment into three categories:
- NEGATIVE (0)
- NEUTRAL (1)
- POSITIVE (2)

It is specifically designed to analyze sentiment toward a specific entity mentioned in the text.

## Intended uses & limitations

The model is intended to be used for Vietnamese sentiment analysis, specifically when analyzing sentiment toward a named entity.

### How to use

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Load model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("Khoa/vietnamese-sentiment-analysis-with-entity")
model = AutoModelForSequenceClassification.from_pretrained("Khoa/vietnamese-sentiment-analysis-with-entity")

# Function to predict sentiment
def predict_sentiment(text, entity, model, tokenizer):
    combined_text = f"Đối với {entity}, {text}"
    inputs = tokenizer(combined_text, return_tensors="pt", truncation=True, padding=True)

    with torch.no_grad():
        outputs = model(**inputs)
        predictions = torch.nn.functional.softmax(outputs.logits, dim=-1)
        predicted_class = torch.argmax(predictions, dim=-1).item()

    sentiment_labels = {0: "NEGATIVE", 1: "NEUTRAL", 2: "POSITIVE"}
    return sentiment_labels[predicted_class], predictions[0].tolist()

# Example usage
text = "Món ăn rất ngon nhưng giá hơi đắt"
entity = "Nhà hàng ABC"
sentiment, confidence = predict_sentiment(text, entity, model, tokenizer)
print(f"Sentiment: {sentiment}")
```

## Training procedure

The model was fine-tuned on a custom Vietnamese dataset with entity-specific sentiment annotations.


This model was fine-tuned on a custom Vietnamese sentiment analysis dataset.
It achieves the following metrics on the test set:
- Accuracy: 0.0000
- F1 Score: 0.0000
- Precision: 0.0000
- Recall: 0.0000

