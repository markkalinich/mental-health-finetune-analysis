---
license: apache-2.0
language: tr
tags:
  - sentiment-analysis
  - text-classification
  - bert
base_model: dbmdz/bert-base-turkish-uncased
pipeline_tag: sentiment-analysis
datasets:
  - Goktug06/restoran-sentiment-dataset
metrics:
  - accuracy
  - f1
---

# Turkish Sentiment Classifier v1

Bu model, Türkçe metinler üzerinde **duygu analizi (sentiment analysis)** yapmak için fine-tune edilmiştir. Özellikle restoran yorumlarında **pozitif, nötr ve negatif** duygu sınıflandırması için tasarlanmıştır.

- **Model Mimarisi:** BERT (dbmdz/bert-base-turkish-uncased tabanlı)
- **Girdi:** Türkçe serbest metin
- **Çıktı:** Üç sınıf — `0: Negatif`, `1: Nötr`, `2: Pozitif`

## Kullanım Örneği (Transformers.js ile Tarayıcıda)

```js
import { pipeline } from "@xenova/transformers";
const sentiment = await pipeline(
  "sentiment-analysis",
  "Goktug06/sentiment-turkish-v1"
);
const result = await sentiment("Restoran çok güzeldi, servisten memnun kaldım.");
console.log(result);
