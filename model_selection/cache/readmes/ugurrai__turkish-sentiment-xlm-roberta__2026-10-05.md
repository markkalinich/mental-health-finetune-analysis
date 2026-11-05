---
language: tr
license: apache-2.0
tags:
- sentiment-analysis
- turkish
- xlm-roberta
- nlp
metrics:
- accuracy
pipeline_tag: text-classification
---

# 🚀 Turkish Sentiment Analysis | XLM-RoBERTa

Bu model, Fırat Üniversitesi bünyesinde düzenlenen **FÜB3V CodeNight Hackathon** kapsamında geliştirilmiştir. Türkçe metinler üzerinde duygu analizi (olumlu, olumsuz, nötr) yapabilmek için **XLM-RoBERTa-Large** mimarisi kullanılarak fine-tune edilmiştir.

## 🏆 Yarışma Başarısı
- **Sıralama:** 6. Sırada tamamlandı.
- **Doğruluk (Accuracy):** %83.86
- **Süreç:** Yarışma süresince kısıtlı zamanda saf PyTorch ile özel eğitim döngüsü (custom training loop) yazılarak eğitilmiştir.

## 📊 Model Detayları
- **Model Tipi:** XLM-RoBERTa (Multilingual Transformer)
- **Görev:** Çok sınıflı sınıflandırma (3-class classification)
- **Eğitim Platformu:** Kaggle (GPU T4 x2)

## 💻 Kullanım (How to Use)

Modeli `transformers` kütüphanesi ile hızlıca kullanabilirsiniz:

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

model_name = "ugurrai/turkish-sentiment-xlm-roberta"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

text = "Bu proje gerçekten harika olmuş, ellerinize sağlık!"
inputs = tokenizer(text, return_tensors="pt")

with torch.no_grad():
    logits = model(**inputs).logits
    predicted_class_id = logits.argmax().item()

print(predicted_class_id)