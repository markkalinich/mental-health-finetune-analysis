---
language: ko
tags:
- medical
- bert
- korean
license: apache-2.0
datasets:
- other
model-index:
- name: Medical Chatbot
  results:
  - task:
      name: Medical Text Classification
      type: text-classification
    metrics:
      - type: accuracy
        value: 0.95
        name: Validation Accuracy
---

# Medical Chatbot Model

This model is a fine-tuned version of KLUE BERT base for medical symptom classification.

## Model description

The model uses KLUE BERT base architecture fine-tuned on a custom medical dataset. It performs classification for various diseases and provides treatment recommendations.

## Input Format
```python
{
    "text": "두통이 심하고 메스꺼워요"
}
```

## Output Format
```python
{
    "label": "편두통",
    "score": 0.95
}
```

## Training procedure
- Epochs: 5
- Batch size: 8
- Learning rate: 2e-5
- Maximum sequence length: 128

## Limitations and bias
This model should be used for reference only and not as a substitute for professional medical advice.