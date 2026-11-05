---
language: tr
license: mit
tags:
- text-classification
- sentiment-analysis
metrics:
- accuracy
---

# Adanus: Türkçe Metin Duygu Analizi Modeli

## Model Açıklaması
Bu model, `dbmdz/bert-base-turkish-cased` mimarisi üzerine, Türkçe metinlerin pozitif veya negatif olduğunu tespit etmek amacıyla fine-tune edilmiştir. Eğitim sürecinde sentetik Türkçe yorum veri seti kullanılmıştır.

## Kullanım Senaryoları & Sınırlılıklar
- **Uygundur:** Kısa Türkçe e-ticaret yorumları, müşteri geri bildirimleri ve sosyal medya metinlerinin duygu analizi.
- **Sınırlılıklar:** Eğitim seti küçük tutulduğu için çok uzun veya edebi metinlerde kararlılığı değişebilir.

## Eğitim Verisi & Performans Metrikleri
- **Eğitim Seti:** 400 örnek
- **Test Seti:** 100 örnek
- **Eğitim Epoch Sayısı:** 2
- **Test Accuracy (eval_accuracy):** %100 (1.0)
- **Validation Loss (eval_loss):** 0.00039

## Örnek Kullanım (Inference)
```python
from transformers import pipeline

classifier = pipeline("text-classification", model="tosbaga/Adanus")
result = classifier("Bu ürünü gerçekten çok beğendim, harika.")
print(result) 
# Çıktı: [{'label': 'LABEL_1', 'score': 0.99}] -> LABEL_1: Pozitif, LABEL_0: Negatif