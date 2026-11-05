---
library_name: transformers
tags:
  - text-classification
  - distilbert
  - sentiment-analysis
  - new-closed-neutral
  - colab
---

# 📌 Model Card: distil-bert-classifier

This model is a fine-tuned DistilBERT model for sequence classification, designed to identify whether a place (e.g., restaurants, businesses) is **NEW**, **CLOSED**, or **NEUTRAL** based on short text snippets.

---

## 🧠 Model Details

### Model Description

- **Base Model:** `distilbert-base-uncased`  
- **Task:** Sequence Classification  
- **Classes:** `NEW`, `CLOSED`, `NEUTRAL`  
- **Language:** English  
- **License:** MIT *(confirm if needed)*  
- **Developer:** virustechhacks  

This model helps extract signals about business status from textual data such as reviews, posts, or headlines.

---

## 🔗 Model Sources

- **Repository:** https://huggingface.co/virustechhacks/distil-bert-classifier  

---

## 🚀 Uses

### ✅ Direct Use

Classify short text snippets into:
- `NEW` → Newly opened places  
- `CLOSED` → Shut down or no longer operating  
- `NEUTRAL` → No clear status signal  

### 🔄 Downstream Use

Outputs can be aggregated into features like:
- `closed_signal_ratio`
- `new_signal_ratio`
- `mention_count`

These can feed into larger ML pipelines (e.g., XGBoost models).

### ⚠️ Out-of-Scope

- General sentiment analysis beyond defined labels  
- Non-English text  
- Long documents (>128 tokens)  
- High-stakes decision-making systems  

---

## ⚠️ Bias, Risks, and Limitations

- **Synthetic Data Bias:**  
  Trained on rule-based synthetic data → may not generalize well to real-world language.

- **No Time Awareness:**  
  Cannot distinguish *recent vs outdated* signals.

- **Token Limit:**  
  Inputs >128 tokens are truncated.

---

## 💡 Recommendations

For production use:
- Fine-tune on real-world datasets  
- Add timestamp-based features  
- Evaluate thoroughly on live data  

---

## 🛠️ How to Use

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import torch.nn.functional as F

repo_name = "virustechhacks/distil-bert-classifier"

tokenizer = AutoTokenizer.from_pretrained(repo_name)
model = AutoModelForSequenceClassification.from_pretrained(repo_name)

id_to_label = {0: "NEW", 1: "CLOSED", 2: "NEUTRAL"}

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

def predict_status(text):
    inputs = tokenizer(
        text,
        truncation=True,
        padding="max_length",
        max_length=128,
        return_tensors="pt"
    )
    inputs = {k: v.to(device) for k, v in inputs.items()}

    with torch.no_grad():
        outputs = model(**inputs)

    probs = F.softmax(outputs.logits, dim=-1)
    confidence, pred = torch.max(probs, dim=1)

    return id_to_label[pred.item()], confidence.item()

# Example
print(predict_status("Grand opening this weekend!"))
print(predict_status("The store ceased operations."))