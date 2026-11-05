---
language: id
license: apache-2.0
tags:
- indobert
- sentiment-analysis
- indonesian
pipeline_tag: text-classification
---

# IndoBERT Sentimen Analysis Text Labeling

Model ini adalah versi *fine-tuned* dari IndoBERT yang dioptimalkan untuk klasifikasi sentimen teks Bahasa Indonesia.

## Model Performance
* **Classification**: Mendukung tiga kelas sentimen: Positif, Negatif dan Netral.

## Acknowledgments
Proses pelatihan model ini menggunakan skrip yang didasarkan pada proyek milik **crypter70** (GitHub: [crypter70](https://github.com/crypter70)). Pengembangan dilakukan lebih lanjut untuk menyesuaikan dengan alur kerja analisis data berita dan deployment otomatis.

## Intended Use
Model ini dirancang untuk:
1. Melabeli data teks (Review, Komen, Artikel)
2. Mendukung analisis tren sentimen dalam kegiatan Exploratory Data Analysis (EDA).