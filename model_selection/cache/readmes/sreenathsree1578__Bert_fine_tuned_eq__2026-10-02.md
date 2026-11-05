---
language: en
license: mit
library_name: transformers
pipeline_tag: text-classification
tags:
- emotional-intelligence
- sentiment-analysis
- workplace-emotions
- distilbert
---

# EQ Detection Model

A fine-tuned **DistilBERT** model for detecting emotional intelligence levels in workplace-focused text data.

---

## Model Description

- **Task:** Text Classification  
- **Model Type:** Emotional Intelligence (EQ) Detection  
- **Base Model:** distilbert-base-uncased  
- **Language:** English  
- **Output Classes:** 3 (NEGATIVE / NEUTRAL / POSITIVE)  
- **Training Dataset Size:** 2,796 workplace communication samples  

The model is designed to evaluate emotional regulation, tone, and behavioral intelligence in professional communication.

---

## Label Schema

| Label | ID | Description |
|------|----|-------------|
| NEGATIVE | 0 | Poor emotional regulation, negative or aggressive expressions |
| NEUTRAL  | 1 | Emotionally neutral or factual statements |
| POSITIVE | 2 | High emotional intelligence and constructive emotional behavior |

---

## Training Performance

| Epoch | Training Loss | Validation Loss | Accuracy |
|------:|---------------|-----------------|----------|
| 1 | 0.188500 | 0.147850 | 94.89% |
| 2 | 0.055100 | 0.120229 | 96.39% |

**Final Validation Accuracy:** **96.39%**

---

## Training Configuration

- **Framework:** Hugging Face Transformers  
- **Optimizer:** AdamW  
- **Batch Size:** 16  
- **Learning Rate:** 2e-5  
- **Epochs:** 2  
- **Max Sequence Length:** 128 tokens  

---

## Intended Use

This model is intended for:

- Workplace communication analysis  
- Emotional intelligence assessment  
- HR analytics and employee development  
- Team interaction and behavioral insights  

---

## How to Use

### Load the Model
```python
from transformers import pipeline

classifier = pipeline(
    "text-classification",
    model="sreenathsree1578/Eq_funetuned"
)