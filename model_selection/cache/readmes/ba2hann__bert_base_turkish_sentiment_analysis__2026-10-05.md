---
language: tr
tags:
  - text-classification
  - sentiment-analysis
license: mit
datasets:
  - custom-dataset
metrics:
  - accuracy
  - precision
  - recall
  - f1
model-index:
  - name: ba2hann/bert-base-turkish-sentiment-analize
    results:
      - task:
          type: text-classification
          name: Sentiment Analysis
        dataset:
          name: Custom Dataset
          type: custom
        metrics:
          - type: accuracy
            value: 0.937
          - type: precision
            value: 0.944
          - type: recall
            value: 0.919
          - type: f1
            value: 0.927
---

# Türkçe Duygu Analizi Modeli (ba2hann/bert-base-turkish-sentiment-analize)

Bu model, Türkçe metinler için duygu analizi yapmayı amaçlamaktadır. Model, dört farklı duygu kategorisini sınıflandırmak üzere eğitilmiştir:

*   Irkçılık
*   Kızdırma (Hakaret/Küfür)
*   Nötr
*   Cinsiyetçilik

## Model Detayları

Bu model, `bert-base-turkish-cased` modeli temel alınarak özel bir veri seti üzerinde eğitilmiştir. Hedef, sosyal medyada ve diğer metin tabanlı platformlarda sıklıkla karşılaşılan olumsuz ve ayrımcı söylemleri tespit etmektir.

## Performans Metrikleri

Modelin genel performansı aşağıdaki gibidir:

*   **Doğruluk (Accuracy):** %93.7

Kategori bazlı performans metrikleri ise şöyledir:

| Kategori     | Precision | Recall | F1 Score |
|--------------|-----------|--------|----------|
| Irkçılık     | 0.881     | 0.919  | 0.899    |
| Kızdırma     | 0.944     | 0.912  | 0.927    |
| Nötr         | 0.960     | 0.965  | 0.963    |
| Cinsiyetçilik | 0.857     | 0.904  | 0.880    |

## Nasıl Kullanılır?

Aşağıdaki Python kodu, `transformers` kütüphanesi ile bu modelin nasıl kullanılacağını göstermektedir:

```python
import torch
from transformers import pipeline

model_name = "ba2hann/bert-base-turkish-sentiment-analize"

sentiment_pipeline = pipeline(
    task="text-classification",
    model=model_name,
    tokenizer=model_name,
    device=0 if torch.cuda.is_available() else -1  # GPU varsa kullan, yoksa CPU
)

category_map = {
    0: "Irkçılık",
    1: "Kızdırma",
    2: "Nötr",
    3: "Cinsiyetçilik"
}

def analyze_sentiment(text):
    sonuc = sentiment_pipeline(text)[0]
    label_index = int(sonuc['label'].split('_')[-1])
    kategori = category_map.get(label_index, "Bilinmeyen")
    return {
        "text": text,
        "category": kategori,
        "score": sonuc['score']
    }

if __name__ == "__main__":
    ornek_cumleler = [
        "Bu çok güzel bir gün.", #Nötr
        "Sen ne kadar aptalsın!", #Kızdırma
        "Bu ırkçı bir söylem.", #Irkçılık
        "Kadınlar araba kullanamaz.", #Cinsiyetçilik
        "Bu konu hakkında hiçbir fikrim yok." #Nötr
    ]
    for ornek_cumle in ornek_cumleler:
      sonuc = analyze_sentiment(ornek_cumle)
      print("\nAnaliz Sonuçları:")
      print(f"Analiz Edilen Cümle: {sonuc['text']}")
      print(f"Tahmin: {sonuc['category']}")
      print(f"Tahmin Güveni: {sonuc['score']:.2%}")