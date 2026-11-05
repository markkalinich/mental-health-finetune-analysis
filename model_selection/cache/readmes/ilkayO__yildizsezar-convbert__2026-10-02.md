---
language:
- tr
pipeline_tag: text-classification
tags:
- sentiment-analysis
- convbert
- turkish
- ecommerce
license: apache-2.0
widget:
- text: Ürün elime çok hızlı ulaştı, paketleme harikaydı. Kesinlikle tavsiye ederim!
  example_title: 5 Yıldız (Positive)
- text: Biraz gecikmeli aktarıyor görüntüyü ama onun dışında fiyat performans ürünü.
  example_title: 3 Yıldız (Mixed)
- text: Kutu ezik geldi ve içindeki parça kırıktı. İade edeceğim.
  example_title: 1 Yıldız (Negative)
datasets:
- ilkayO/yildizsezar-turkish-reviews
base_model:
- dbmdz/convbert-base-turkish-mc4-uncased
---
<div align="center">
  <img src="https://huggingface.co/ilkayO/yildizsezar-convbert/resolve/main/yildizsezar.png" width="220" alt="YildizSezar Logo"/>
  <p style="color: #6b7280; font-size: 16px; font-style: italic; margin-top: 5px; font-family: sans-serif;">
    "Geldim, Gördüm, Yıldızladım."
  </p>
</div>

# 🌟 YıldızSezar: Turkish E-Commerce Review ConvBERT

[![Hugging Face Spaces](https://img.shields.io/badge/🤗%20Hugging%20Face-Live%20Demo-blue)](https://huggingface.co/spaces/ilkayO/YildizSezar-Demo)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ilkay-onay/YildizSezar-Review-Classifier/blob/main/YildizSezar_Demo.ipynb)
[![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-black?logo=github)](https://github.com/ilkay-onay/YildizSezar-Review-Classifier)

**YıldızSezar** is a fine-tuned version of `dbmdz/convbert-base-turkish-mc4-uncased`, specifically engineered to predict 1-to-5 star ratings directly from morphologically complex Turkish e-commerce customer reviews.

This model serves as the official implementation for my B.Sc. Thesis Project, which was successfully published in a peer-reviewed journal.
📄 **Paper:** [A Star Rating-Based Approach in BERT-Based Sentiment Analysis of Customer Feedback](https://dergipark.org.tr/tr/pub/ij3dptdi/article/1732179)

## 🚀 Model Details
- **Architecture:** ConvBERT (Turkish)
- **Task:** Multi-class Sentiment Analysis
- **Classes:** 5 (`1 Yildiz`, `2 Yildiz`, `3 Yildiz`, `4 Yildiz`, `5 Yildiz`)
- **Language:** Turkish
- **License:** Apache 2.0 (Commercially friendly)

## 📊 Performance & Training
Real-world e-commerce data often suffers from extreme class imbalance. To overcome this, the model was trained on a highly robust dataset augmented with a scalable synthetic data generation pipeline via **LLaMA-8B-DPO** (generating over 900,000 synthetic review samples).

- **Accuracy:** 89.96%
- **Macro F1-Score:** 0.799
- **Dataset:** [ilkayO/yildizsezar-turkish-reviews](https://huggingface.co/datasets/ilkayO/yildizsezar-turkish-reviews)

## 💻 Quick Usage
You can easily integrate this model into your Python projects:

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

model_id = "ilkayO/yildizsezar-convbert"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForSequenceClassification.from_pretrained(model_id)

text = "Ürünün kalitesi beklediğimden çok daha iyi çıktı."
inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=256)

with torch.no_grad():
    outputs = model(**inputs)
    predicted_class_id = torch.argmax(outputs.logits, dim=-1).item()

# Assuming id2label is properly configured in config.json
print(f"Predicted Rating: {model.config.id2label[str(predicted_class_id)]}")
```

## 🤝 Commercial Integration & Consulting
This model is open-sourced under the **Apache 2.0** license, meaning you are free to use, modify, and integrate it into your commercial products. 

If your company is looking to integrate advanced NLP systems, requires custom fine-tuning on internal data, or if you are interested in having me join your AI team, feel free to reach out!
📧 **Contact:** ilkayonay2001@gmail.com | [LinkedIn](https://linkedin.com/in/ilkay-onay-391905254)