---
language: ar
tags:
- arabic
- offensive-language
- text-classification
- content-moderation
- arabert
pipeline_tag: text-classification
---

# Arabic Speech Guard 🛡️

**Arabic-Speech-Guard** is an Arabic text classification model fine-tuned on AraBERT to detect offensive and harmful speech.

## Labels
- **0** → Neutral  
- **1** → Offensive  

## Model Details
- Base model: `aubmindlab/bert-base-arabertv2`
- Task: Arabic Offensive Speech Detection
- Language: Arabic

## Usage

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

model_name = "USERNAME/Arabic-Speech-Guard"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

text = "اكتب النص هنا"

inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
with torch.no_grad():
    outputs = model(**inputs)

prediction = torch.argmax(outputs.logits, dim=1).item()
print("Prediction:", "Danger" if prediction == 1 else "Safe")
