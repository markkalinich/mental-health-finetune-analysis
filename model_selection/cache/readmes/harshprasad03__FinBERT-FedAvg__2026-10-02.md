---
language: en
license: mit
tags:
- federated-learning
- finance
- sentiment-analysis
- bert
- finbert
- fedavg
library_name: transformers
pipeline_tag: text-classification
authors: 
- Harsh Prasad
- Sai Dhole
---

## FinBERT–FedAvg: Federated Averaging for Financial Sentiment Analysis

---

### 📌 Model Summary

This model is a **federated version of FinBERT** fine-tuned for
**financial sentiment classification (Positive / Negative / Neutral)**.

Training is performed across **three clients**:

* Financial Twitter posts  
* Financial news headlines  
* Financial reports & statements  

This model is trained using the **Federated Averaging (FedAvg)** algorithm,
where each client trains locally on its own data and only **model weights** are shared.
No raw data is exchanged, supporting privacy-preserving learning.

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
FedAvg aggregation

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

| Method | Final Avg F1-Score |
| ------ | ------------------ |
| FedAvg | **0.846**          |

FedAvg provided **strong and stable global performance**
across heterogeneous financial text sources.

---

### 🚀 Example Usage

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

model = AutoModelForSequenceClassification.from_pretrained(
    "harshprasad03/FinBERT-FedAvg"
)
tokenizer = AutoTokenizer.from_pretrained(
    "harshprasad03/FinBERT-FedAvg"
)

text = "Tech stocks fell after negative earnings guidance."

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
FedAvg-based Federated FinBERT for Financial Sentiment Analysis.
```

---

### 👨‍💻 Authors

**Harsh Prasad**
AI and ML Research

**Sai Dhole**
AI and ML Research

---