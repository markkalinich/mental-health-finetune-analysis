---
license: mit
tags:
- mental-health
- depression
- anxiety
- stress
language: en
---

# Mental Health Multiclass Classification

Fine-tuned for Depression/Anxiety/Stress classification.

## Performance
- Validation Loss: 0.4109
- Validation Accuracy: 0.8867
- F1 (Macro): 0.8701

## Usage
```python
import torch
from transformers import AutoTokenizer

model = torch.load("pytorch_model.bin")
tokenizer = AutoTokenizer.from_pretrained("alfiyahqthz/bert-multiclass-das")

text = "I feel depressed"
inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
logits = model(inputs['input_ids'], inputs['attention_mask'])
prediction = logits.argmax(dim=1).item()
# 0=Depression, 1=Anxiety, 2=Stress
```
