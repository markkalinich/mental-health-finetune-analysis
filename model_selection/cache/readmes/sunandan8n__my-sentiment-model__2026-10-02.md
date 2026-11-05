---
language: en
tags:
- sentiment-analysis
- text-classification
license: mit
datasets: 
- custom
widget:
- text: "I love this product! It's amazing."
- text: "This is the worst experience ever."
---

# My Sentiment Model

This is a fine-tuned **sentiment analysis model** created by [sunandan8n](https://huggingface.co/sunandan8n).  
It classifies text into **positive** or **negative** sentiment.

## Model Details
- **Base Model**: DistilBERT (uncased)
- **Framework**: Transformers (PyTorch)
- **File Format**: SafeTensors

## Intended Use
- Sentiment classification for short English texts.  
- Can be used in chatbots, customer feedback analysis, or product reviews.  

## Example Usage

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline

model_name = "sunandan8n/my-sentiment-model"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

classifier = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)

print(classifier("I am very happy with this!"))
print(classifier("This is terrible."))

