---
language: 
- en
license: mit
tags:
- roberta
- text-classification
- esg
- sustainability
- environmental
- social
- governance
base_model: roberta-base
library_name: transformers
pipeline_tag: text-classification
datasets:
- salitahir/green-guard-esg-sentences
metrics:
- accuracy
- f1
---

# 🟣 Green-Guard — RoBERTa ESG *Category* Classifier (v1)

**Task:** Sentence-level classification for **Environmental (E)**, **Social (S)**, and **Governance (G)** categories.  
**Base model:** `roberta-base`, fine-tuned with **class-weighted loss** to address label imbalance.  
**Repository:** [GitHub → Green-Guard Project](https://github.com/salitahir/green_guard)

---

## 📊 Metrics (Test Set)

| Metric | Value |
|:-------|------:|
| Accuracy | **0.81** |
| Macro F1 | **0.81** |
| Weighted F1 | **0.81** |

> Metrics computed on the same held-out test split (`data/processed/splits/`)  
> using [`reports/category_metrics_v1.json`](https://github.com/salitahir/green_guard/tree/main/reports)

---

## 🧩 Labels
```json
{ "0": "E", "1": "S", "2": "G" }
```

## 🚀 Quick Inference

You can load and run the model directly:
```
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

model_id = "salitahir/roberta-esg-category-green-guard-v1"
tok = AutoTokenizer.from_pretrained(model_id)
mod = AutoModelForSequenceClassification.from_pretrained(model_id).eval()

text = "We invested in renewable energy sources for our operations."
inputs = tok(text, return_tensors="pt", truncation=True)
pred = torch.softmax(mod(**inputs).logits, dim=-1)
label_id = pred.argmax(-1).item()
label = mod.config.id2label[str(label_id)]
print(label, float(pred[0][label_id]))
```

--- 

## ✅ Expected output:

E 0.88

---

## 🧠 Intended Use

This model acts as Stage 2 in the Green-Guard pipeline — categorizing sustainability-related sentences identified by the Relevance Model.

---

## ⚖️ License

MIT License — open for research and commercial reuse with attribution.