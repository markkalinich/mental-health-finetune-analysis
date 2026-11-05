---
language:
- vi
base_model:
- ZycckZ/Simple_VieQA
pipeline_tag: text-classification
datasets:
- ura-hcmut/UIT-VSFC
- anotherpolarbear/vietnamese-sentiment-analysis
license: mit
metrics:
- accuracy
- f1
- precision
- recall
library_name: transformers
tags:
- sentiment-analysis
- fine-tuned
- bert
- vietnamese
- text-classification
---
# Simple_VieQA Sentiment (ZycckZ)

Fine-tuned version of [Simple_VieQA](https://huggingface.co/ZycckZ/Simple_VieQA)  
for Vietnamese sentiment analysis on `UIT-VSFC` dataset.

## 🧠 Performance
| Metric | Score |
|--------|--------|
| Accuracy | 0.936 |
| F1-weighted | 0.930 |

## 🚀 How to use
```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

model_name = "ZycckZ/Simple_VieQA-sentiment"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

text = "Sản phẩm rất tốt, pin trâu"
inputs = tokenizer(text, return_tensors="pt")
with torch.no_grad():
    logits = model(**inputs).logits
pred = torch.argmax(logits, dim=-1).item()
print(pred)