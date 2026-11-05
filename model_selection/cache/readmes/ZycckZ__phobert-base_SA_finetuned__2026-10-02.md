---
language:
- vi
base_model:
- vinai/phobert-base
task_categories:
- text-classification
tags:
- sentiment-analysis
- pytorch
- transformers
- phobert
---

# PhoBERT Base for Sentiment Analysis (Vietnamese)

## 1. Model Description
This model is a fine-tuned version of [vinai/phobert-base](https://huggingface.co/vinai/phobert-base) for general **Sentiment Analysis (SA)** on Vietnamese text. It is designed to classify sentences into three emotional categories: **Negative**, **Neutral**, and **Positive**.

- **Language:** Vietnamese
- **Model Type:** Transformer-based Encoder
- **Base Model:** vinai/phobert-base
- **Task:** Sentiment Analysis (3-class classification)

## 2. Training Data
The model was trained on a comprehensive collection of Vietnamese sentiment datasets to ensure robustness:
- [UIT-VSFC (ura-hcmut/UIT-VSFC)](https://huggingface.co/datasets/ura-hcmut/UIT-VSFC)
- [Vietnamese Sentiment Analysis (anotherpolarbear/vietnamese-sentiment-analysis)](https://huggingface.co/datasets/anotherpolarbear/vietnamese-sentiment-analysis)
- [Kaggle Vietnamese Sentiment Analyst (linhlpv)](https://www.kaggle.com/datasets/linhlpv/vietnamese-sentiment-analyst)

## 3. Training Procedure
### Hyperparameters:
- **Learning Rate:** 5e-5
- **Batch Size:** 32
- **Precision:** Mixed precision (fp16)
- **Epochs:** 3
- **Optimizer:** AdamW

## 4. Evaluation Results
The model was evaluated on a dedicated test set (3166 samples).

- **Accuracy:** 93.90%
- **F1-Macro (Average):** 83.00%
- **F1-Weighted:** 93.59%

### Classification Report:
| Class | Precision | Recall | F1-Score | Support |
| :--- | :--- | :--- | :--- | :--- |
| **Negative** | 0.94 | 0.97 | 0.96 | 1409 |
| **Neutral** | 0.73 | 0.49 | 0.59 | 167 |
| **Positive** | 0.95 | 0.96 | 0.95 | 1590 |

**Observations:**
- The model performs exceptionally well on **Negative** (F1: 0.96) and **Positive** (F1: 0.95) sentiments.
- The **Neutral** class remains a challenge (F1: 0.59) due to the inherent ambiguity of neutral expressions in Vietnamese reviews and smaller support size.

## 5. How to Use
```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

tokenizer = AutoTokenizer.from_pretrained("ZycckZ/phobert-base_SA_finetuned")
model = AutoModelForSequenceClassification.from_pretrained("ZycckZ/phobert-base_SA_finetuned")

text = "Sản phẩm dùng rất tốt, giao hàng nhanh chóng."
inputs = tokenizer(text, return_tensors="pt")

with torch.no_grad():
    logits = model(**inputs).logits

predicted_class_id = logits.argmax().item()
# Map: 0: Negative, 1: Neutral, 2: Positive