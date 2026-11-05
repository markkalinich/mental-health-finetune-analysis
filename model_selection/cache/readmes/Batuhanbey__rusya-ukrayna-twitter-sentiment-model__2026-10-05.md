---
language:
- tr
tags:
- sentiment-analysis
- text-classification
- twitter
- xlm-roberta
pipeline_tag: text-classification
---

# Rusya-Ukrayna Savaşı Twitter Duygu Analizi Modeli

Bu model, Rusya-Ukrayna savaşıyla ilgili Twitter/X paylaşımlarını beş duygu sınıfına ayırmak için fine-tune edilmiştir.

## Etiketler

- `mutlu`
- `uzgun`
- `kizgin`
- `saskin`
- `notr`

## Kullanım

```python
from transformers import pipeline

classifier = pipeline("text-classification", model="Batuhanbey/rusya-ukrayna-twitter-sentiment-model")
result = classifier("Bugün savaşla ilgili çok üzücü haberler var.")
print(result)
```

## Temel Model

Model, `xlm-roberta-base` mimarisi üzerine duygu analizi görevi için eğitilmiştir.

## Not

Bu model akademik/TÜBİTAK proje çalışması kapsamında hazırlanmıştır. Sonuçlar otomatik sınıflandırmadır; siyasi, hukuki veya resmi değerlendirme amacıyla kullanılmamalıdır.
