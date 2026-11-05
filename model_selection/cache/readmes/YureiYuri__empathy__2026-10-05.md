---
language:
- en
license: apache-2.0
tags:
- mental-health
- therapy
- chatbot
- text-classification
- distilbert
pipeline_tag: text-classification
library_name: transformers
---

# Therapy Chatbot - Mental Health Intent Classification

This model classifies mental health-related text into 11 different intent categories.

## Model Description

- **Model type:** DistilBERT for Sequence Classification
- **Language:** English
- **Training data:** 3,508 therapy context-response pairs
- **Task:** Intent classification for mental health chatbot

## Intent Categories

The model classifies text into these 11 intents:
- `depression` - Feelings of sadness, hopelessness, worthlessness
- `anxiety` - Worry, panic, nervousness
- `self_esteem` - Issues with self-worth and confidence
- `relationship` - Relationship problems and conflicts
- `family` - Family-related concerns
- `sleep_issues` - Insomnia and sleep problems
- `anger` - Anger management issues
- `suicide` - Suicidal thoughts (crisis detection)
- `trauma` - PTSD and trauma-related issues
- `grief` - Loss and bereavement
- `general_support` - General emotional support needs

## Usage
```python
from transformers import DistilBertTokenizerFast, DistilBertForSequenceClassification
import torch

# Load model and tokenizer
model = DistilBertForSequenceClassification.from_pretrained("YOUR-USERNAME/therapy-chatbot")
tokenizer = DistilBertTokenizerFast.from_pretrained("YOUR-USERNAME/therapy-chatbot")

# Make prediction
text = "I feel worthless and can't sleep at night"
inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)

with torch.no_grad():
    outputs = model(**inputs)

prediction = torch.argmax(outputs.logits, dim=1).item()
print(f"Predicted intent: {prediction}")
```

## Training

- **Epochs:** 6
- **Batch size:** 16
- **Learning rate:** 3e-5
- **Validation loss:** ~0.030

## Limitations

⚠️ **Important:** This model is NOT a replacement for professional mental health care. It's designed to assist in categorizing user messages for appropriate responses.

## Disclaimer

This is an AI model for educational and support purposes only. In case of mental health emergencies, please contact:
- National Suicide Prevention Lifeline: 988
- Crisis Text Line: Text HOME to 741741