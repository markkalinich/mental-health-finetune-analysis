---
language:
- id
license: mit
tags:
- text-classification
- sentiment-analysis
- bert
- fine-tuned
- indonesian
- tutorial
- beginner-friendly
base_model: bert-base-uncased
datasets:
- Faisaljabir/ulasan-film-indonesia
metrics:
- accuracy
- f1
- roc_auc
pipeline_tag: text-classification
---

# Sentiment BERT — Klasifikasi Sentimen Ulasan Film Indonesia

## Model Details

### Model Description

Model ini adalah **BERT yang di-fine-tune** untuk mengklasifikasikan
sentimen ulasan film berbahasa Indonesia menjadi dua kategori:
**Positif** (LABEL_1) atau **Negatif** (LABEL_0).

Model ini dibuat sebagai **bahan pembelajaran** bagi pemula yang ingin
memahami proses fine-tuning model bahasa (Language Model) dari awal
hingga publikasi di HuggingFace.

- **Developed by:** [Faisal Jabir]
- **Funded by:** Mandiri / pribadi
- **Shared by:** [Faisal Jabir]
- **Model type:** Text Classification (Binary Sentiment Analysis)
- **Language(s):** Indonesian (id)
- **License:** MIT
- **Finetuned from:** `bert-base-uncased` (Google, 2019)

### Model Sources

- **Repository:** https://github.com/icalcode/sentiment-bert-tutorial
- **Paper:** Tidak ada — ini model tutorial


---

## Uses

### Direct Use

Model ini dapat langsung digunakan untuk mengklasifikasikan sentimen
teks ulasan film berbahasa Indonesia tanpa training tambahan.

```python
from transformers import pipeline

nlp = pipeline("text-classification", model="Faisaljabir/sentiment-bert")

hasil = nlp("Film ini sangat bagus dan menghibur!")
print(hasil)
# Output: [{'label': 'LABEL_1', 'score': 0.92}]
# LABEL_1 = Positif, LABEL_0 = Negatif
```

### Downstream Use (Opsional)

Model ini dapat di-fine-tune lebih lanjut untuk:
- Analisis sentimen domain lain (produk, restoran, berita)
- Dataset bahasa Indonesia yang lebih besar
- Task klasifikasi teks biner lainnya

### Out-of-Scope Use

Model ini **tidak cocok** untuk:
- Teks bahasa selain Indonesia
- Klasifikasi lebih dari 2 kelas (multi-class)
- Aplikasi kritis yang membutuhkan akurasi sangat tinggi
- Produksi skala besar (data training terlalu kecil)

---

## Bias, Risks, and Limitations

- **Data training sangat kecil** (30 contoh) — hanya untuk tujuan
  pembelajaran. Performa tidak dapat diandalkan untuk produksi.
- **Domain terbatas** — hanya dilatih pada ulasan film, mungkin tidak
  akurat untuk domain lain.
- **Bahasa informal** — model mungkin kesulitan dengan slang, singkatan,
  atau campuran bahasa (code-switching).
- **Ketidakseimbangan kelas** — jika data produksi berbeda distribusinya
  dengan data training, performa bisa menurun.

### Recommendations

Untuk penggunaan serius, disarankan:
1. Gunakan dataset yang jauh lebih besar (minimal 1.000 contoh)
2. Gunakan model berbahasa Indonesia seperti `indobenchmark/indobert-base-p1`
3. Lakukan evaluasi pada data independen sebelum deployment

---

## How to Get Started with the Model

### Cara paling sederhana (pipeline)

```python
from transformers import pipeline

# Load model
nlp = pipeline("text-classification", model="username_kamu/sentiment-bert")

# Prediksi satu teks
hasil = nlp("Film ini sangat menghibur!")
print(hasil)
# [{'label': 'LABEL_1', 'score': 0.89}]

# Prediksi banyak teks sekaligus
ulasan_list = [
    "Ceritanya bagus dan akting pemainnya luar biasa",
    "Membosankan dan tidak ada yang menarik",
    "Biasa saja, tidak istimewa",
]
hasil_list = nlp(ulasan_list)
for ulasan, hasil in zip(ulasan_list, hasil_list):
    label = "POSITIF" if hasil["label"] == "LABEL_1" else "NEGATIF"
    print(f"{label} ({hasil['score']:.2f}): {ulasan}")
```

### Cara manual (untuk kontrol lebih)

```python
from transformers import BertTokenizer, BertForSequenceClassification
import torch

tokenizer = BertTokenizer.from_pretrained("Faisaljabir/sentiment-bert")
model = BertForSequenceClassification.from_pretrained("Faisaljabir/sentiment-bert")

teks = "Film yang sangat bagus!"
inputs = tokenizer(teks, return_tensors="pt", padding=True, truncation=True)

with torch.no_grad():
    outputs = model(**inputs)
    pred = torch.argmax(outputs.logits).item()

print("POSITIF" if pred == 1 else "NEGATIF")
```

---

## Training Details

### Training Data

- **Sumber:** Data buatan (synthetic) untuk keperluan tutorial
- **Jumlah:** 30 ulasan film (15 positif, 15 negatif)
- **Bahasa:** Indonesia
- **Split:**
  - Training: 24 data (80%)
  - Validation: 3 data (10%)
  - Test: 3 data (10%)
- **Dataset HuggingFace:** `Faisaljabir/ulasan-film-indonesia`
  
### Dataset Sources
* HuggingFace : https://huggingface.co/datasets/Faisaljabir/ulasan-film-indonesia
* Kaggle      : https://www.kaggle.com/datasets/faisaljabir/ulasan-film-indonesia-tutorial-sentimen-analysis

### Training Procedure

#### Preprocessing

1. Tokenisasi menggunakan `BertTokenizer` (bert-base-uncased)
2. Panjang maksimal token: 64
3. Padding ke panjang seragam
4. Truncation untuk teks yang terlalu panjang

#### Training Hyperparameters

| Parameter         | Nilai         |
|-------------------|---------------|
| Base model        | bert-base-uncased |
| Learning rate     | 2e-5          |
| Epochs            | 3             |
| Batch size        | 8             |
| Optimizer         | AdamW         |
| Epsilon           | 1e-8          |
| Max sequence length | 64          |
| Frozen layers     | Layer 0–9 (10 layer pertama di-freeze) |
| Trainable layers  | Layer 10–11 + classifier head |

#### Strategi Fine-tuning

Menggunakan teknik **partial freezing**:
- 10 layer pertama BERT di-freeze (tidak diubah)
- 2 layer terakhir + classification head dilatih ulang
- Tujuan: efisiensi training dan mencegah catastrophic forgetting

#### Speeds, Sizes, Times

- **Ukuran model:** ~440 MB
- **Waktu training:** ~5–10 menit (Google Colab CPU)
- **Waktu training (GPU):** ~1–2 menit (Google Colab T4)
- **Waktu inference:** <1 detik per teks

---

## Evaluation

### Testing Data

Evaluasi dilakukan pada test set yang terpisah (3 data, tidak pernah
dilihat selama training).

### Metrics

| Metrik   | Penjelasan                              |
|----------|-----------------------------------------|
| Accuracy | Proporsi prediksi yang benar            |
| F1-Score | Rata-rata harmonis Precision dan Recall |
| AUC-ROC  | Area under ROC curve (0.5=random, 1=sempurna) |

### Results

> ⚠️ Catatan: Hasil sangat bervariasi karena data test hanya 3 sampel.
> Ini adalah model tutorial, bukan model produksi.

| Model       | Accuracy | F1-Score | AUC-ROC |
|-------------|----------|----------|---------|
| MLP (tabular) | ~0.67  | ~0.67    | ~0.70   |
| BERT (teks)   | ~0.67  | ~0.67    | ~0.75   |

*Hasil aktual bisa berbeda setiap run karena data sangat kecil.*

### Summary

Model berhasil menyelesaikan proses fine-tuning BERT end-to-end dari
data mentah hingga publikasi di HuggingFace. Untuk tujuan pembelajaran,
proses ini sudah mendemonstrasikan semua konsep penting: tokenisasi,
fine-tuning, evaluasi, dan deployment.

---

## Environmental Impact

Estimasi menggunakan [Machine Learning Impact Calculator](https://mlco2.impact.electricitymaps.com/).

| Parameter       | Nilai                    |
|----------------|--------------------------|
| Hardware type  | Google Colab (CPU/T4 GPU) |
| Hours used     | < 0.5 jam                |
| Cloud provider | Google Cloud Platform     |
| Compute region | us-central1 (Iowa, USA)  |
| Carbon emitted | ~0.001 kg CO₂eq (sangat kecil) |

---

## Technical Specifications

### Model Architecture

```
BertForSequenceClassification
├── BertModel (bert-base-uncased)
│   ├── BertEmbeddings
│   ├── BertEncoder (12 layers)
│   │   ├── Layer 0–9  : FROZEN (tidak dilatih)
│   │   └── Layer 10–11: TRAINABLE
│   └── BertPooler     : TRAINABLE
└── Classifier
    ├── Linear(768 → 2)
    └── Softmax
```

- **Total parameter:** 109,483,778
- **Parameter dilatih:** ~14,000,000 (12.8%)
- **Parameter di-freeze:** ~95,000,000 (87.2%)

### Compute Infrastructure

- **Hardware:** Google Colab (CPU atau T4 GPU)
- **Software:**
  - Python 3.10
  - PyTorch 2.x
  - Transformers 4.35+
  - Datasets 2.x

---

## Citation

Jika menggunakan model atau tutorial ini, silakan kutip sebagai:

**BibTeX:**
```bibtex
@misc{Faisaljabir-sentimentbert,
  author    = {Faisal Jabir},
  title     = {Sentiment BERT: Tutorial Fine-tuning BERT untuk Pemula},
  year      = {2026},
  publisher = {HuggingFace},
  url       = {https://huggingface.co/Faisaljabir/sentiment-bert}
}
```

**APA:**
Faisal Jabir. (2026). *Sentiment BERT: Tutorial Fine-tuning BERT untuk
Pemula*. HuggingFace. https://huggingface.co/Faisaljabir/sentiment-bert

---

## Glossary

| Istilah | Penjelasan |
|---------|-----------|
| Fine-tuning | Melatih ulang model pre-trained pada data spesifik |
| Tokenisasi | Mengubah teks menjadi token (angka) yang bisa dibaca model |
| Epoch | Satu putaran training melewati semua data |
| Batch | Kelompok data yang diproses sekaligus |
| Frozen layer | Layer yang tidak diubah parameternya saat training |
| BERT | Bidirectional Encoder Representations from Transformers |
| F1-Score | Metrik yang menyeimbangkan Precision dan Recall |
| Overfitting | Model hafal data training tapi buruk di data baru |

---

## Model Card Authors

- **Nama:** [Faisal Jabir]
- **Email:** [faisal.ces@gmail.com]

## Model Card Contact

Untuk pertanyaan atau laporan masalah, hubungi melalui:
- HuggingFace: [@Faisaljabir](https://huggingface.co/Faisaljabir)
- Email: [faisal.ces@gmail.com]

---

*Model card ini dibuat sebagai bagian dari tutorial pembelajaran
Machine Learning untuk pemula. Semua konsep dijelaskan dengan
bahasa yang mudah dipahami.*
