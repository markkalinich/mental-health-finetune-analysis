---
language:
- id
- jv
license: apache-2.0
base_model: indolem/indobertweet-base-uncased
tags:
- text-classification
- emotion-detection
- javanese
- indonesian
- cross-lingual-transfer
datasets:
- PRDECT-ID
metrics:
- accuracy
- f1
model-index:
- name: IndoBERTweet-Emotion-Transfer-Javanese
  results:
  - task:
      type: text-classification
      name: Emotion Classification
    dataset:
      type: PRDECT-ID
      name: PRDECT-ID with Javanese Ngoko Translation
    metrics:
    - type: f1
      value: 0.0  # Ganti dengan hasil f1-score macro dari classification_report Anda
      name: Macro F1
---

# IndoBERTweet for Cross-Lingual Emotion Classification (ID to JV)

Model ini merupakan hasil *fine-tuning* dari [IndoBERTweet](https://huggingface.co/indolem/indobertweet-base-uncased) untuk klasifikasi emosi. Proyek ini berfokus pada **Cross-Lingual Transfer Learning**, di mana model dilatih menggunakan data Bahasa Indonesia dan dievaluasi menggunakan data Bahasa Jawa (Ngoko).

## Deskripsi Model
Model ini dirancang untuk mendeteksi berbagai emosi dalam teks. Pendekatan yang digunakan adalah melatih model pada bahasa sumber (*source language*) yang kaya sumber daya (Bahasa Indonesia) dan mengujinya pada bahasa target (*target language*) yang lebih spesifik (Bahasa Jawa Ngoko) untuk melihat sejauh mana model memahami konteks emosi lintas bahasa.

- **Base Model:** `indolem/indobertweet-base-uncased`
- **Dataset:** PRDECT-ID (dengan tambahan kolom terjemahan Bahasa Jawa Ngoko)
- **Tugas:** Multi-class Emotion Classification

## Parameter Pelatihan
Konfigurasi berikut digunakan selama proses *fine-tuning*:
* **Epochs:** 10
* **Batch Size:** 16 (Train & Eval)
* **Learning Rate:** 2e-5
* **Weight Decay:** 0.01
* **Max Length:** 128 tokens
* **Optimizer:** AdamW

## Metodologi
Eksperimen dilakukan dalam dua tahap utama:
1. **Tahap 1 (Source Training):** Melakukan fine-tuning penuh pada kolom `Customer Review` (Bahasa Indonesia).
2. **Tahap 2 (Zero-Shot Cross-Lingual Evaluation):** Mengevaluasi performa model yang telah dilatih tersebut langsung pada kolom `review_jawa_ngoko` (Bahasa Jawa) tanpa pelatihan tambahan pada bahasa target.

## Hasil (Evaluation)
Berdasarkan eksperimen pada *validation set*:
* **Dataset:** Javanese Ngoko (Target)
* **Metrik Utama:** Macro F1-Score dan Accuracy (Lihat bagian bawah Model Card untuk detail per kelas).

> **Catatan:** Laporan evaluasi lengkap tersedia di file `error_analysis.csv` untuk analisis linguistik lebih lanjut mengenai pergeseran makna atau kesalahan klasifikasi pada dialek Ngoko.

## Cara Penggunaan
Anda dapat menggunakan model ini dengan library `transformers`:

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

model_name = "path/to/your-model" # Ganti dengan repo ID Anda
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

text = "Aku seneng banget karo barange, apik tenan!"
inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=128)

with torch.no_grad():
    outputs = model(**inputs)
    predictions = torch.nn.functional.softmax(outputs.logits, dim=-1)
    print(predictions)