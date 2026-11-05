---
language:
- en
license: apache-2.0
tags:
- text-classification
- sentiment-analysis
- question-answering
- mobilebert
- lightweight
base_model: google/mobilebert-uncased
model_name: PRV AI 1.0
---

# PRV AI 1.0

## Model Description
PRV AI 1.0 is a lightweight and efficient AI model designed for natural language processing tasks.

## Model Details
- **Model Name:** PRV AI 1.0
- **Version:** 1.0
- **Parameters:** 24.5 Million
- **Developed by:** PRV
- **Language:** English
- **License:** Apache 2.0

## What Can PRV AI 1.0 Do?
- Text Classification
- Sentiment Analysis
- Question Answering
- Named Entity Recognition

## How to Use
```python
from transformers import MobileBertTokenizer, MobileBertModel

tokenizer = MobileBertTokenizer.from_pretrained("Prava1/PRV-AI-1.0")
model = MobileBertModel.from_pretrained("Prava1/PRV-AI-1.0")
```

## Base Model
PRV AI 1.0 is built on top of MobileBERT by Google Research.
Original model: google/mobilebert-uncased

## License
This model is licensed under the Apache 2.0 License.
Original MobileBERT credit goes to Google Research.