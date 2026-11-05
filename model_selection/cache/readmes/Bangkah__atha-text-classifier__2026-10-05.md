---
library_name: transformers
license: apache-2.0
base_model: indobenchmark/indobert-base-p1
language:
    - id
datasets:
    - Bangkah/atha-text-dataset
tags:
    - sentiment-analysis
    - text-classification
    - indonesian
metrics:
    - accuracy
    - f1
---

# atha-text-classifier

Model ini adalah fine-tuned indobenchmark/indobert-base-p1 untuk klasifikasi sentimen Bahasa Indonesia 3 kelas.

Label output:

- `negative`
- `neutral`
- `positive`

Training data: https://huggingface.co/datasets/Bangkah/atha-text-dataset

## Quick Use (Transformers)

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

model_id = "Bangkah/atha-text-classifier"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForSequenceClassification.from_pretrained(model_id)

text = "produk ini bagus dan pengirimannya cepat"
inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=128)
with torch.no_grad():
    logits = model(**inputs).logits

probs = torch.softmax(logits, dim=-1)[0]
label_id = int(torch.argmax(probs).item())
label = model.config.id2label[label_id]
score = float(probs[label_id].item())
print({"label": label, "confidence": round(score, 4)})
```

## Limitations

- Dataset training masih sintetis, sehingga metrik tinggi tidak langsung merepresentasikan performa produksi.
- Untuk use-case production, tetap lakukan fine-tuning ulang dengan data real domain aplikasi.

## Validation Metrics

- Loss: 0.0004
- Accuracy: 1.0000
- Macro F1: 1.0000

## Confusion Matrix

| true\pred | negative | neutral | positive |
|---|---:|---:|---:|
| negative | 100 | 0 | 0 |
| neutral | 0 | 100 | 0 |
| positive | 0 | 0 | 100 |

## Classification Report

```text
              precision    recall  f1-score   support

    negative     1.0000    1.0000    1.0000       100
     neutral     1.0000    1.0000    1.0000       100
    positive     1.0000    1.0000    1.0000       100

    accuracy                         1.0000       300
   macro avg     1.0000    1.0000    1.0000       300
weighted avg     1.0000    1.0000    1.0000       300

```
