---
language: id
tags:
- text-classification
- sentiment-analysis
- tiktok
- indobert
pipeline_tag: text-classification
library_name: transformers
widget:
- text: Wapres kita kosong banget anjay
  example_title: Contoh Negatif (Slang)
- text: Semangat terus pak gibran, sehat selalu
  example_title: Contoh Positif
- text: Banjir dimana-mana pemerintah diem aja
  example_title: Contoh Keluhan
license: mit
base_model:
- indobenchmark/indobert-base-p1
---

# TikTok Sentiment Analysis

Model ini adalah hasil fine-tuning dari **IndoBERT (indobenchmark/indobert-base-p1)** yang dilatih khusus menggunakan dataset komentar **TikTok**.

Model ini dirancang untuk memahami gaya bahasa media sosial Indonesia yang informal, mengandung banyak singkatan, *slang*, dan sarkasme (khususnya dalam konteks isu sosial/politik).

## 🎯 Intended Use
Model ini dibuat untuk keperluan **Tugas Project** (Metode Numerik).
Cocok digunakan untuk:
- Analisis sentimen komentar media sosial (TikTok).
- Mendeteksi polaritas opini publik (Positif, Netral, Negatif).
- Menangani teks dengan *noise* tinggi (typo/bahasa gaul).

## ⚠️ Limitations (Disclaimer)
- **Experimental Version:** Model ini merupakan versi awal (v1) dan dilatih dengan epoch terbatas.
- **No Rigorous Validation:** Belum dilakukan pengujian validasi mendalam (cross-validation) atau benchmark akurasi formal.
- **Bias:** Model dilatih pada dataset spesifik komentar bertema polititik dan bencana alam, sehingga mungkin memiliki bias terhadap topik atau tokoh tertentu.

## 💻 How to Use (Python)

```python
from transformers import pipeline

model_id = "zekiell/indobert-tiktok-political-sentiment"

nlp = pipeline("text-classification", model=model_id)

result = nlp("Kerjanya bagus dan hasilnya memuaskan")
print(result)