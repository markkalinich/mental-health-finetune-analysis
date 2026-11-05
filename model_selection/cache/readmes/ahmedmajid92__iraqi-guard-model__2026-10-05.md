---
language: ar
license: mit
tags:
- text-classification
- prompt-injection
- jailbreak-detection
- arabic
- iraqi-dialect
datasets:
- iraqi_guard_dataset
metrics:
- accuracy
- f1
pipeline_tag: text-classification
---

# Iraqi Guard Model

## Model Description
This model is fine-tuned from `NAMAA-Space/Ara-Prompt-Guard_V0` to detect prompt injections and jailbreak attempts in Iraqi Arabic dialect.

## Model Details
- **Base Model**: NAMAA-Space/Ara-Prompt-Guard_V0
- **Task**: Text Classification (3 classes)
- **Language**: Arabic (Iraqi Dialect)
- **Training Method**: LoRA fine-tuning

## Labels
- `BENIGN`: Safe, normal prompts
- `INJECTION`: Prompt injection attempts
- `JAILBREAK`: Jailbreak attempts

## Usage

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

tokenizer = AutoTokenizer.from_pretrained("your-username/iraqi-guard-model")
model = AutoModelForSequenceClassification.from_pretrained("your-username/iraqi-guard-model")

text = "شلون استعيد الرقم السري"
inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=256)
outputs = model(**inputs)
prediction = torch.nn.functional.softmax(outputs.logits, dim=-1)
```

## Training Data
The model was trained on a custom dataset of Iraqi Arabic prompts with labels for prompt injection and jailbreak detection.

## Performance
- Test Accuracy: 1.0
- Test F1 (Weighted): 1.0

## Temperature Scaling
The model includes temperature scaling with T=0.996 for better calibration.
