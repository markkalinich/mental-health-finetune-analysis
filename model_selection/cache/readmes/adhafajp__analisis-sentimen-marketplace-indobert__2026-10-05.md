---
license: mit
language:
- id
base_model:
- indobenchmark/indobert-large-p2
pipeline_tag: text-classification
tags:
- sentiment-analysis
- indonesian
- app-reviews
---

# IndoBERT Fine-Tuned for Indonesian App Reviews Sentiment

Model ini adalah hasil *fine-tuning* dari `indobenchmark/indobert-large-p2` untuk tugas klasifikasi sentimen teks dalam Bahasa Indonesia. Proyek ini dikembangkan sebagai bagian dari submission "Belajar Fundamental Deep Learning" di **Dicoding Indonesia** dan program **IDCamp 2025**, yang berhasil meraih rating **Bintang 5**.

## Model Details

### Model Description

Model ini dilatih untuk mengenali sentimen pengguna pada ulasan aplikasi di Google Play Store (aplikasi *Merchant*/*Marketplace*). Model mengklasifikasikan teks ke dalam tiga kategori: **Positif, Netral, dan Negatif**.

- **Developed by:** Adhafa Joan Putranto
- **Model type:** Transformer-based Text Classification
- **Language(s) (NLP):** Indonesian
- **License:** MIT
- **Finetuned from model:** indobenchmark/indobert-large-p2

## Uses

### Direct Use

Model ini dapat langsung digunakan untuk menganalisis sentimen ulasan produk, aplikasi, atau komentar dalam Bahasa Indonesia.

### Out-of-Scope Use

Model mungkin tidak bekerja maksimal pada teks yang menggunakan bahasa daerah yang sangat kental atau teks dengan singkatan yang tidak umum di luar domain ulasan aplikasi.

## How to Get Started with the Model

Gunakan kode di bawah ini untuk mencoba model menggunakan library `transformers`:

```python
from transformers import pipeline

pretrained_name = "adhafajp/analisis-sentimen-marketplace-indobert"
nlp = pipeline("sentiment-analysis", model=pretrained_name)

text = "Aplikasi ini sangat membantu pekerjaan saya sehari-hari, tapi kadang agak berat."
result = nlp(text)
print(result)
```

## Training Details

### Training Data

Model dilatih menggunakan dataset mandiri hasil scraping sebanyak 10.000+ ulasan Google Play Store. Dataset mencakup berbagai ulasan aplikasi populer di Indonesia dengan distribusi tiga kelas sentimen.

### Preprocessing

Tahapan preprocessing meliputi:

1. Pembersihan karakter khusus dan emoji.

2. Pemetaan kata slang atau bahasa gaul Indonesia ke bahasa baku (Normalisasi).

3. Tokenisasi menggunakan IndoBertTokenizer.

## Evaluation

### Testing Data & Metrics

Evaluasi dilakukan menggunakan testing set yang dipisahkan dari dataset original dengan metrik utama Accuracy.

### Results

Model menunjukkan performa generalisasi yang sangat baik pada data ulasan yang belum pernah dilihat sebelumnya, selaras dengan atau bahkan melebihi hasil performa model ML klasik pada proyek yang sama yang mencapai akurasi **>92%**.

## Environmental Impact

- Hardware Type: GPU (RTX 2050 Laptop)