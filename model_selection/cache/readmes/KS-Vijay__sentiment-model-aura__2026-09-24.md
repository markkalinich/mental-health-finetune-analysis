---
language: en
license: apache-2.0
base_model: distilbert-base-uncased
tags:
  - text-classification
  - sentiment-analysis
  - transformer
  - distilbert
  - huggingface
pipeline_tag: text-classification
widget:
  - text: "I love the way your startup handled my issue. Brilliant support!"
---

# 💫 Sentiment Model Aura (KS-Vijay)

This model is fine-tuned using **DistilBERT** to classify the **sentiment of startup grievance text** as either `Positive`, `Neutral`, or `Negative`.

## 💼 Use Case

Used in a smart Grievance Redressal System to analyze tone and emotion of user complaints, providing faster triage and better prioritization.

## 🔍 Model Summary

- **Task:** Sentiment Classification
- **Model:** DistilBERT
- **Labels:** `Positive`, `Neutral`, `Negative`
- **Format:** `safetensors`
- **Trained on:** Complaints from `complaints.csv` (custom dataset)
- **Framework:** PyTorch with 🤗 Transformers

## 🧪 Example Input

```text
"The support staff was helpful, but the delay was frustrating."
