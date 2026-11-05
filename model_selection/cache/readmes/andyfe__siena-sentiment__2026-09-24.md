---
language: en
tags:
- text-classification
- sentiment-analysis
- customer-support
- distilbert
license: mit
datasets:
- synthetic
metrics:
- accuracy
model-index:
- name: siena-sentiment
  results:
  - task:
      type: text-classification
      name: Text Classification
    dataset:
      type: synthetic
      name: Customer Support Tickets
    metrics:
    - type: accuracy
      value: 0.95
base_model:
- distilbert/distilbert-base-uncased
---

# Siena Sentiment Analysis Model

This model is a fine-tuned version of `distilbert-base-uncased` for sentiment analysis on customer support tickets, capable of classifying text into five sentiment categories.

## Model Description

- **Model Architecture**: DistilBERT (66M parameters)
- **Task**: Multi-class Sentiment Classification
- **Language**: English
- **Training Data**: 5,000 synthetic customer support tickets generated using GPT-4
- **Input**: Customer support tickets or similar text (50-200 words)
- **Output**: Sentiment classification into one of five categories:
  - Strong Negative (0)
  - Mild Negative (1)
  - Neutral (2)
  - Mild Positive (3)
  - Strong Positive (4)

### Limitations

- Model is trained on synthetic data, which may not capture all real-world nuances
- Best suited for customer support context; may not generalize well to other domains
- Input text should be between 50-200 words for optimal performance

## Training Procedure

### Training Data

The model was trained on 5,000 synthetic customer support tickets:
- 1,000 samples per sentiment category
- Generated using GPT-4o-mini for balanced representation
- Text length between 50-200 words
- Focus on product and service-related issues

### Training Hyperparameters

- Optimizer: AdamW
- Learning rate: 2e-5
- Batch size: 16
- Training epochs: 3
- Max sequence length: 128 tokens

## How to Use

Here's how to use the model with the Transformers library:

```python
from transformers import pipeline

# Load the sentiment analysis pipeline
classifier = pipeline("text-classification", model="andyfe/siena-sentiment")

# Example text
text = """I am extremely disappointed with the customer service I received today. I've been waiting for a response for over a week, and when I finally got one, it didn't address my issue at all. This is unacceptable."""

# Get prediction
result = classifier(text)
print(result)
```

For more detailed usage with the model directly:

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Load model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("andyfe/siena-sentiment")
model = AutoModelForSequenceClassification.from_pretrained("andyfe/siena-sentiment")

# Prepare input text
text = "Your customer service team was incredibly helpful and resolved my issue quickly!"
inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=128)

# Get prediction
outputs = model(**inputs)
predictions = torch.nn.functional.softmax(outputs.logits, dim=-1)
predicted_label = torch.argmax(predictions).item()

# Map prediction to sentiment label
id2label = {
    0: "Strong Negative",
    1: "Mild Negative",
    2: "Neutral",
    3: "Mild Positive",
    4: "Strong Positive"
}

print(f"Predicted sentiment: {id2label[predicted_label]}")
```