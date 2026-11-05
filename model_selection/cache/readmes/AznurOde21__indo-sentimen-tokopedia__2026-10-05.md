---
license: mit
tags:
  - indobert
  - sentiment-analysis
  - tokopedia
  - indo
language:
  - id
---

# IndoBERT Tokopedia Sentiment Classifier

Model ini dilatih menggunakan IndoBERT (`indobenchmark/indobert-base-p1`) untuk klasifikasi sentimen komentar pelanggan Tokopedia (positif / negatif).

## Dataset
Dataset berupa komentar dari Tokopedia dengan label berdasarkan rating (≥4 = positif, ≤3 = negatif).

## Penggunaan

```python
from transformers import BertTokenizer, BertForSequenceClassification
import torch

tokenizer = BertTokenizer.from_pretrained("username/indo-sentimen-tokopedia")
model = BertForSequenceClassification.from_pretrained("username/indo-sentimen-tokopedia")

text = "Barang sangat buruk dan tidak sesuai"
inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)

with torch.no_grad():
    logits = model(**inputs).logits
    probs = torch.nn.functional.softmax(logits, dim=1)
    pred = torch.argmax(probs)

print("Sentimen:", "Positif" if pred.item() == 1 else "Negatif")
