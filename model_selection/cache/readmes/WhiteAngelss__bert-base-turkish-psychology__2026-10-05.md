---
license: apache-2.0
---

# WhiteAngels BERT Modeli - Türkçe Psikolojik Metin Sınıflandırma

## Açıklama
Bu proje, Türkçe metinlerde psikolojik temaları sınıflandırmak için eğitilmiş bir BERT modelini içerir. Model, metinleri dört ana sınıfa ayırır:
- Psikolojik Baskılar
- Irkçılık
- Kaba Konuşma
- Nötr
- positive

Model, Hugging Face Transformers kütüphanesi kullanılarak geliştirilmiştir.

## Kullanım
Modeli yüklemek ve metin sınıflandırması yapmak için aşağıdaki adımları izleyebilirsiniz:

### Gerekli Kütüphaneler
```bash
pip install transformers
pip install torch
pip install matplotlib



from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification
import torch
import matplotlib.pyplot as plt

# Pipeline'ı kullanarak modeli yükleyin
pipe = pipeline("text-classification", model="WhiteAngelss/bert-base-turkish-psychology")

# Örnek bir metin
text = "Bu proje çok heyecan verici!"

# Metni sınıflandırın
result = pipe(text)

# Sonuçları yazdırın
print(f"Tahmin edilen sınıf: {result[0]['label']}")
print(f"Sonuç olasılığı: {result[0]['score']:.4f}")

# Görselleştirme
labels = ["Psikolojik Baskılar", "Irkçılık", "Kaba Konuşma", "Nötr"]
scores = [result[0]['score'] if label == result[0]['label'] else 0 for label in labels]

plt.bar(labels, scores)
plt.xlabel('Sınıf')
plt.ylabel('Olasılık')
plt.title('Tahmin Sonuçları')
plt.xticks(rotation=45)
plt.show()

![bert-base-turkish-psychology-model-testing.png](https://cdn-uploads.huggingface.co/production/uploads/66a0d312cc3ba5f65843d3b4/FN1_Sjb4mJ5WPoQzXZGJy.png)