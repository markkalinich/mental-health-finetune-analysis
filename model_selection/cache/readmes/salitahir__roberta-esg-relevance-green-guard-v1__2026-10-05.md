---
language: 
- en
license: mit
tags:
- roberta
- text-classification
- esg
- sustainability
- binary-classification
base_model: roberta-base
library_name: transformers
pipeline_tag: text-classification
datasets:
- salitahir/green-guard-esg-sentences
metrics:
- accuracy
- f1
---

# 🟢 Green-Guard — RoBERTa ESG *Relevance* Classifier (v1)

**Task:** Sentence-level classification — determine if a sentence is *Sustainability-Related* (`Yes` / `No`).  
**Base model:** `roberta-base`, fine-tuned on a labeled ESG corpus from the Green-Guard dataset.  
**Repository:** [GitHub → Green-Guard Project](https://github.com/salitahir/green_guard)

---

## 📊 Metrics (Test Set)

| Metric | Value |
|:-------|------:|
| Accuracy | **0.90** |
| Macro F1 | **0.89** |
| Weighted F1 | **0.90** |

> Metrics computed on a held-out test split (`data/processed/splits/`)  
> using the JSON logs → [`reports/relevance_metrics_v1.json`](https://github.com/salitahir/green_guard/tree/main/reports)

---

## 🧩 Labels
```json
{ "0": "No", "1": "Yes" }
```

## 🚀 Quick Inference

You can load and run the model directly:
```
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

model_id = "salitahir/roberta-esg-relevance-green-guard-v1"
tok = AutoTokenizer.from_pretrained(model_id)
mod = AutoModelForSequenceClassification.from_pretrained(model_id).eval()

text = "We reduced Scope 2 emissions by 24% in 2024."
inputs = tok(text, return_tensors="pt", truncation=True)
pred = torch.softmax(mod(**inputs).logits, dim=-1)
label_id = pred.argmax(-1).item()
label = mod.config.id2label[str(label_id)]
print(label, float(pred[0][label_id]))
```

--- 

## ✅ Expected output:

Yes 0.94

---

## 🧠 Intended Use

This model acts as Stage 1 in the two-stage Green-Guard ESG classifier, filtering sustainability-related sentences before ESG-type categorization.

---

## ⚖️ License

MIT License — open for research and commercial reuse with attribution.