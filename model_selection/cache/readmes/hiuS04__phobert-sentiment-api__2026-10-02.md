---
language: vi
license: mit
tags:
- vietnamese
- sentiment-analysis
pipeline_tag: text-classification
---

# PhoBERT Sentiment Analysis 🇻🇳

Fine-tuned PhoBERT model for Vietnamese product review sentiment classification (Positive / Neutral / Negative).

## Usage

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

model_name = "hiuS04/phobert-sentiment-api"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

text = "Sản phẩm rất tốt và đáng tiền"
inputs = tokenizer(text, return_tensors="pt")
outputs = model(**inputs)
pred = torch.softmax(outputs.logits, dim=-1)
print(pred)