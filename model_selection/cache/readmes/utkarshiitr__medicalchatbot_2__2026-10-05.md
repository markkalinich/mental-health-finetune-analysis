---
tags:
- text-classification
pipeline_tag: text-classification
---

# Medical Diagnosis Chatbot

This model is trained to classify medical conditions based on input symptoms and provide appropriate recommendations.

## Supported Tasks

This model supports the following tasks:
- `text-classification`: Classify text into predefined medical conditions.

## Usage

Here is how you can use the model for text classification:

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification

tokenizer = AutoTokenizer.from_pretrained("utkarshiitr/medicalchatbot")
model = AutoModelForSequenceClassification.from_pretrained("utkarshiitr/medicalchatbot")

inputs = tokenizer("fever, cough", return_tensors="pt")
outputs = model(**inputs)
