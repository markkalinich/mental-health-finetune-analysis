---
language: en
license: mit
tags:
- federated-learning
- finance
- sentiment-analysis
- bert
- finbert
library_name: transformers
pipeline_tag: text-classification
authors: 
- Harsh Prasad
- Sai Dhole
---

## FinBERT–AdaptiveFedAvg: Adaptive Federated Aggregation for Financial Sentiment Analysis

---

### 📌 Model Summary

This model is a **federated version of FinBERT** fine-tuned for
**financial sentiment classification (Positive / Negative / Neutral)**.

Training is performed across **three clients**:

* Financial Twitter posts
* Financial news headlines
* Financial reports & statements

Unlike standard FedAvg, this model uses an **Adaptive Aggregation strategy**,
where client contributions are **weighted dynamically based on validation performance**,
allowing stronger clients to influence the global model more.

This model is part of a research project comparing:

* FedAvg
* FedProx
* Adaptive Aggregation

for federated financial NLP.

---

### 🧠 Intended Use

Designed for:

* Financial sentiment research
* Risk & market analytics
* Academic exploration of federated learning

Not intended for automated trading without expert oversight.

---

### 🏗 Model Architecture

Base Model:

```
ProsusAI/finbert
```

Task:

```
Sequence classification — 3 classes
```

Training Setup:

```
3 federation clients
10 global rounds
3 local epochs
Adaptive weighted aggregation
```

---

### 📊 Client Data Sources

| Client   | Data Type         |
| -------- | ----------------- |
| Client-1 | Financial Twitter |
| Client-2 | Financial News    |
| Client-3 | Financial Reports |

No raw data is shared between clients.

---

### 🔐 Privacy Advantage

Only model updates are exchanged — not text data.
This supports data governance and privacy-aware ML.

---

### 📈 Performance (Validation)

| Method          | Final Avg F1-Score |
| --------------- | ------------------ |
| Adaptive FedAvg | **0.823**          |

Adaptive aggregation showed **smooth convergence and stable performance**
while preserving privacy.

---

### 🚀 Example Usage

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

model = AutoModelForSequenceClassification.from_pretrained(
    "harshprasad03/FinBERT-Adaptive"
)
tokenizer = AutoTokenizer.from_pretrained(
    "harshprasad03/FinBERT-Adaptive"
)

text = "Global markets improved after positive earnings reports."

inputs = tokenizer(text, return_tensors="pt")
outputs = model(**inputs)

prob = torch.softmax(outputs.logits, dim=1)
print(prob)
```

---

### ⚠️ Limitations

* Trained only on finance-domain text
* Sentiment ≠ market prediction
* Model may inherit dataset biases
* Designed for research use

---

### 📚 Citation

```
Harsh Prasad, Sai Dhole (2025).
Adaptive Federated FinBERT for Financial Sentiment Analysis.
```

---

### 👨‍💻 Authors

**Harsh Prasad**
AI and ML Research

**Sai Dhole**
AI and ML Research

---