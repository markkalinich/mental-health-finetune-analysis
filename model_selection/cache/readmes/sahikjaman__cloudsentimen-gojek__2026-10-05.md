---
language: id
license: mit
base_model: indobenchmark/indobert-base-p1
tags:
  - text-classification
  - sentiment-analysis
  - indonesian
  - indobert
pipeline_tag: text-classification
---

# sahikjaman/cloudsentimen-gojek

Model klasifikasi sentimen (positif/netral/negatif) ulasan **Gojek** di Google Play Store,
hasil fine-tuning `indobenchmark/indobert-base-p1`. Bagian dari proyek mata kuliah Komputasi Awan,
FTMM Universitas Airlangga (NIM 163221024).

## Cara pakai
```python
from transformers import pipeline
clf = pipeline("text-classification", model="sahikjaman/cloudsentimen-gojek")
clf("aplikasi sering error saldo hilang")
```

## Data & label
- Sumber: ulasan publik Google Play (`google-play-scraper`).
- Label *weak-supervised* dari rating: 4–5 → positif, 3 → netral, 1–2 → negatif.
- **Keterbatasan:** label berasal dari rating, bukan anotasi manual; kelas netral minoritas.

## Preprocessing (WAJIB saat inference)
Teks dibersihkan identik dengan training (lowercase, hapus URL/emoji/tanda baca,
normalisasi slang, stopword Sastrawi). Lihat `cloudsentimen.preprocess.clean_for_inference`.
