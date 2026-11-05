
---
license: mit
tags:
  - text-classification
  - sentiment-analysis
  - sequence-classification
  - roberta
  - lora
  - peft
language: en
library_name: transformers
base_model: FacebookAI/roberta-base
datasets:
  - glue
---

# 📘 RoBERTa Sentiment Analysis — LoRA Merged Model

This repository contains a **LoRA fine-tuned RoBERTa model** for **2-class sentiment analysis** (Negative, Positive).  
The base model is **`FacebookAI/roberta-base`**, and the LoRA adapters have been **merged into the base model** to produce a standalone model.

---

## 🚀 Model Overview

| Feature | Details |
|--------|---------|
| **Base Model** | `FacebookAI/roberta-base` |
| **Fine-tuning method** | LoRA (PEFT) |
| **Task** | Sentiment Classification |
| **Labels** | NEGATIVE (0), POSITIVE (1) |
| **Dataset** | GLUE SST-2 |
| **Merged** | Yes, LoRA adapter merged into base model |
| **Training Environment** | Auto-detect (Google Colab or local machine) |

---

## 🧠 How to Use the Merged Model

### 🔹 Inference Example

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# -----------------------------
# Load merged model and tokenizer
# -----------------------------
model_name = "mishrabp/roberta-sentiment-analysis-merged"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# Make sure model is on the correct device and in evaluation mode
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)
model.eval()

# -----------------------------
# Label mapping (same as training)
# -----------------------------
id2label = {0: "NEGATIVE", 1: "POSITIVE"}

# -----------------------------
# Texts for validation
# -----------------------------
text_list = [
    # Positive
    "I loved the new Batman movie!",
    "What an amazing experience!",
    "The service was surprisingly good, even though the restaurant was packed.",
    "Absolutely fantastic performance, though a bit too long for my taste.",
    "The concert had incredible energy, yet the sound quality was pleasing.",
    "The dessert was delightful.",
    "I loved the artwork.",
    "The new phone works well.",
    "The flight was smooth.",
    "I was thrilled by the surprise party.",
    
    # Negative
    "The food at that restaurant was terrible.",
    "I will never go back to that place again.",
    "I was disappointed that my favorite dish was sold out.",
    "The book was thrilling at first, but the ending left me mindblowing.",  # could be positive/negative, marking negative
    "The hotel room looked nothing like the photos online, but the staff were friendly.",  # neutral → marking negative
    "The movie had stunning visuals, but the plot was overly predictable.",
    "The customer support solved my issue quickly, though I had to wait on hold for a long time.",
    "I appreciated the thoughtful gift, but the packaging was damaged upon delivery."
]

# -----------------------------
# Inference
# -----------------------------
# Tokenize all texts as a batch (avoids inconsistencies and is faster)
inputs = tokenizer(
    text_list,
    return_tensors="pt",
    truncation=True,
    padding=True,
    max_length=512
)

# Move all inputs to device
inputs = {k: v.to(device) for k, v in inputs.items()}

# Run inference
with torch.no_grad():
    outputs = model(**inputs)
    predictions = torch.argmax(outputs.logits, dim=-1)

# Print results
for text, pred in zip(text_list, predictions):
    print(f"Text: {text}")
    print(f"Predicted Sentiment: {id2label[pred.item()]}")
    print("-" * 50)
```

---

## ⚙️ Model Details

- Merged LoRA adapters for efficient fine-tuning.  
- Fully compatible with `AutoModelForSequenceClassification`.  
- Trained on GLUE SST-2 dataset for 2-class sentiment analysis.  

---

## 📝 Citation

```
@model{mishrabp_roberta_sentiment_analysis_merged,
  author = {Mishra, Bibhu},
  title = {RoBERTa Sentiment Analysis - LoRA Merged},
  year = 2025,
  base_model = {FacebookAI/roberta-base}
}
```

---

## 🙌 Acknowledgements

- Hugging Face Transformers  
- Hugging Face PEFT  
- GLUE Benchmark  
- RoBERTa by Facebook AI  


