---
license: apache-2.0
language:
- en
- bn
metrics:
- accuracy
- f1
base_model:
- sagorsarker/bangla-bert-base
pipeline_tag: text-classification
tags:
- sentiment
- bengali
- machine-learning
- AI
- LLM
- Transformers
- Models
- bangla-sentiment-analysis
source: 
- name: BANEmo Paper 
- url: https://ieeexplore.ieee.org/document/11171926
---
# BanglaBERT Sentiment Classifier

This is a fine‑tuned BanglaBERT model trained on the BANEmo Dataset (https://ieeexplore.ieee.org/document/11171926) for **Bangla sentiment analysis**.  
It classifies Bangla comments into two categories:  
- **0 → Sadness 😢**  
- **1 → Happiness 😀**

---

## 📊 Model Details
- **Base model:** `sagorsharma/banglabert`
- **Task:** Sequence Classification (Sentiment Analysis)
- **Labels:** 2 (Sadness, Happiness)
- **Dataset:** BANEmo (https://ieeexplore.ieee.org/document/11171926)
- **Evaluation Metrics:** Accuracy, F1 Score
- **Validation Accuracy:** ~84%

---

## 🛠️ Training Setup
- **Framework:** Hugging Face Transformers
- **Optimizer:** AdamW
- **Learning Rate:** 5e‑5
- **Epochs:** 3
- **Batch Size:** 8
- **Loss Function:** CrossEntropyLoss

---

## 🚀 Usage

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Load model and tokenizer
model = AutoModelForSequenceClassification.from_pretrained("sakhawat-hossen/bangla-sentiment-banglabert")
tokenizer = AutoTokenizer.from_pretrained("sakhawat-hossen/bangla-sentiment-banglabert")

# Example prediction
text = "আজ আমি খুব খুশি।"
inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
with torch.no_grad():
    outputs = model(**inputs)
prediction = torch.argmax(outputs.logits, dim=-1).item()

print("Prediction:", "Happiness 😀" if prediction == 1 else "Sadness 😢")