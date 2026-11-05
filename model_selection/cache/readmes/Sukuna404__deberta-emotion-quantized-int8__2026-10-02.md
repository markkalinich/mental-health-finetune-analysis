---
language: en
license: apache-2.0
base_model: microsoft/deberta-v3-base
tags:
  - text-classification
  - emotion-detection
  - quantization
  - int8
  - torchao
datasets:
  - dair-ai/emotion
metrics:
  - accuracy
  - f1
---

# DeBERTa Emotion Detection — INT8 Quantized

Fine-tuned and quantized version of DeBERTa for 6-class emotion classification.

## Usage
```python
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

repo_id = "Sukuna404/deberta-emotion-quantized-int8"
tokenizer = AutoTokenizer.from_pretrained(repo_id)
model = AutoModelForSequenceClassification.from_pretrained(repo_id).to("cpu")
model.eval()

def predict(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding="longest")
    with torch.no_grad():
        outputs = model(**inputs)
    pred_id = outputs.logits.argmax().item()
    return model.config.id2label[pred_id]

print(predict("I am so happy today!"))  # joy
```
