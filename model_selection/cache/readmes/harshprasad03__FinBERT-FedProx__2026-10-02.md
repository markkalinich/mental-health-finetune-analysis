---
language: en
license: mit
tags:
- federated-learning
- finance
- sentiment-analysis
- bert
- finbert
- fedprox
library_name: transformers
pipeline_tag: text-classification
authors: 
- Harsh Prasad
- Sai Dhole
---

## FinBERT–FedProx: Federated Proximal Optimization for Financial Sentiment Analysis

---

### 📌 Model Summary

This model is a **federated version of FinBERT** fine-tuned for
**financial sentiment classification (Positive / Negative / Neutral)**.

Training is performed across **three clients**:

* Financial Twitter posts  
* Financial news headlines  
* Financial reports & statements  

Unlike standard FedAvg, this model uses **FedProx optimization**,
which adds a **proximal penalty term** to stabilize client training when
data across clients is **non-identically distributed (non-IID)**.

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
FedProx (µ = 0.05)

````

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

| Method  | Final Avg F1-Score |
| ------- | ------------------ |
| FedProx | **0.855**          |

FedProx provided **slightly better stability and performance**
compared to standard FedAvg under client data imbalance.

---

### 🚀 Example Usage

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

model = AutoModelForSequenceClassification.from_pretrained(
    "harshprasad03/FinBERT-FedProx"
)
tokenizer = AutoTokenizer.from_pretrained(
    "harshprasad03/FinBERT-FedProx"
)

text = "Oil stocks rose after strong quarterly performance."

inputs = tokenizer(text, return_tensors="pt")
outputs = model(**inputs)

prob = torch.softmax(outputs.logits, dim=1)
print(prob)
````

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
FedProx-based Federated FinBERT for Financial Sentiment Analysis.
```

---

### 👨‍💻 Authors

**Harsh Prasad**
AI and ML Research

**Sai Dhole**
AI and ML Research

---