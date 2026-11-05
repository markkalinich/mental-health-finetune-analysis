
---
language: id
license: mit
tags:
  - sentiment-analysis
  - aspect-based-sentiment-analysis
  - indonesian
  - indobert
  - multi-label-classification
metrics:
  - f1
pipeline_tag: text-classification
---

# IndoBERT for Aspect-Based Sentiment Analysis (ABSA)

Model untuk menganalisis sentimen berbasis aspek pada ulasan Fakultas MIPA Universitas Hasanuddin.

## Model Description

- **Base Model**: [IndoBERT-base-p2](https://huggingface.co/indobenchmark/indobert-base-p2)
- **Task**: Multi-label Aspect-Based Sentiment Analysis
- **Language**: Indonesian
- **Training**: Synthetic-to-Real dengan Persona-Based Prompting

## Aspects & Sentiments

| Aspek | Deskripsi |
|-------|----------|
| Layanan Akademik | Dosen, PA, kurikulum, nilai |
| Layanan Penunjang | Staf TU, satpam, OB |
| Fasilitas Inti | Lab, ruang kelas, perpustakaan |
| Sarana Penunjang | WiFi, AC, toilet, parkir |

**Sentimen**: Positif, Netral, Negatif

## Performance

| Metric | Synthetic Test | Real Test |
|--------|---------------|----------|
| F1-Macro | 0.8868 | 0.7549 |

## Author

- **Minhajul Yusri Khairi** - Universitas Hasanuddin
- Pembimbing: Octavian, S.Si., M.Kom.
