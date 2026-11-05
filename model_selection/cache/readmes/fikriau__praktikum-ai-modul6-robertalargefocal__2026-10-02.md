---
library_name: transformers
tags:
- text-classification
- multi-label-classification
- emotion-classification
- roberta
- indonesian
language: en
datasets:
- emotion
---

# Model Klasifikasi Emosi Multi-Label (Praktikum Modul 6)

Model ini adalah `roberta-large` yang telah di-fine-tune untuk tugas klasifikasi emosi multi-label pada dataset teks Bahasa Inggris. Model ini mampu mendeteksi satu atau lebih dari 14 emosi yang berbeda dari sebuah teks, dan dikembangkan sebagai bagian dari pengerjaan Praktikum Modul 6 - Mata Kuliah Kecerdasan Buatan dan Pembelajaran Mesin.

## Detail Model

### Deskripsi Model

Tujuan utama proyek ini adalah untuk membangun sebuah model yang akurat dalam mengklasifikasikan emosi secara multi-label, di mana sebuah teks bisa memiliki beberapa emosi sekaligus (contoh: 'joy' dan 'excitement'). Model ini dilatih dan dievaluasi berdasarkan kompetisi Kaggle dengan metrik evaluasi utama **Macro F1-Score**.

Untuk mencapai performa terbaik dengan keterbatasan hardware (GPU 16 GB), berbagai teknik optimasi canggih diterapkan selama proses training.

- **Developed by:** [fikriau](https://huggingface.co/fikriau)
- **Model type:** `roberta`
- **Language(s) (NLP):** English (`en`)
- **License:** `apache-2.0`
- **Finetuned from model:** `roberta-large`

### Model Sources

- **Repository:** [https://huggingface.co/fikriau/praktikum-ai-modul6-robertalargefocal](https://huggingface.co/fikriau/praktikum-ai-modul6-robertalargefocal)

## Uses

### Direct Use

Model ini dapat digunakan secara langsung untuk prediksi emosi menggunakan `pipeline` dari 🤗 Transformers.

```python
from transformers import pipeline

pipe = pipeline("text-classification", model="fikriau/praktikum-ai-modul6-robertalargefocal", top_k=None)

text = "I can't believe I won the lottery, I'm so happy and excited!"

# Hasil prediksi akan memberikan skor untuk semua 14 label
results = pipe(text)
print(results)
# Contoh Output:
# [[{'label': 'excitement', 'score': 0.98}, {'label': 'joy', 'score': 0.97}, ...]]
```

## Bias, Risks, and Limitations
Model ini dilatih pada dataset yang disediakan untuk praktikum. Bias yang ada di dalam data tersebut kemungkinan besar juga akan tercermin pada prediksi model. Performa model mungkin akan berbeda pada jenis teks yang sangat berbeda dari data latihnya (misalnya, teks formal, teks teknis, atau dialek yang unik). Pengguna disarankan untuk menyadari potensi bias ini saat menggunakan model.

## How to Get Started with the Model
```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

model_name = "fikriau/praktikum-ai-modul6-robertolargefocal"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

text = "This is the best day of my life, I feel so much gratitude!"
inputs = tokenizer(text, return_tensors="pt")

with torch.no_grad():
    logits = model(**inputs).logits

# Dapatkan probabilitas dengan sigmoid dan tentukan label dengan threshold 0.5
probabilities = torch.sigmoid(logits)
predictions = (probabilities > 0.5).int()

# Tampilkan hasil prediksi untuk setiap emosi
for i, label in enumerate(model.config.id2label.items()):
    if predictions[0][i].item() == 1:
        print(f"Detected Emotion: {label[1]} (Score: {probabilities[0][i]:.4f})")
```
## Training Details

### Training Data

Model ini di-fine-tune pada dataset **Emotion Classification** yang disediakan untuk kompetisi Kaggle pada Praktikum Modul 6. Dataset ini terdiri dari 46,455 sampel teks berbahasa Inggris, masing-masing dapat memiliki satu atau lebih dari 14 label emosi.

Analisis data awal (EDA) menunjukkan adanya **ketidakseimbangan kelas (class imbalance)** yang signifikan, di mana beberapa emosi seperti `annoyance` jauh lebih sering muncul daripada emosi lain seperti `embarrassment` dan `fear`. Temuan ini menjadi justifikasi utama untuk menggunakan `FocalLoss` sebagai fungsi kerugian (loss function) saat training.

Data dibagi menjadi 90% untuk set training dan 10% untuk set validasi.

### Training Procedure

Proses training dirancang untuk memaksimalkan performa dengan mengatasi tantangan ketidakseimbangan kelas dan keterbatasan memori GPU (VRAM 16 GB).

#### Preprocessing

1.  **Text Cleaning:** Teks input dibersihkan terlebih dahulu untuk menghapus artefak digital seperti URL dan `@username`. Emoji juga diubah menjadi representasi teksnya (misalnya, `😂` -> `:face_with_tears_of_joy:`) untuk mempertahankan sinyal emosionalnya.
2.  **Tokenization:** Teks yang sudah bersih di-tokenisasi menggunakan `RobertaTokenizer` yang sesuai dengan model `roberta-large`.
3.  **Padding & Truncation:** Semua sekuens teks dipotong atau diberi padding hingga panjang seragam `MAX_LENGTH = 128`. Panjang ini dipilih sebagai kompromi terbaik antara menangkap konteks teks dan memastikan model `roberta-large` muat di dalam memori GPU.

#### Training Hyperparameters

Konfigurasi training menggunakan serangkaian teknik canggih untuk mencapai performa optimal:

- **Loss Function:** `FocalLoss` (dengan parameter default `alpha=0.25`, `gamma=2.0`) digunakan untuk memaksa model lebih fokus pada pembelajaran sampel dari kelas emosi yang jarang muncul.
- **Training Regime:** `fp16` (mixed precision) diaktifkan untuk mengurangi penggunaan memori dan mempercepat komputasi di GPU.
- **Optimizer:** `adamw_8bit` dari library `bitsandbytes` digunakan untuk mengurangi jejak memori dari state optimizer secara signifikan.
- **Batching Strategy:** `per_device_train_batch_size` diatur ke **4**, dan `gradient_accumulation_steps` diatur ke **8**. Ini menghasilkan **batch size efektif sebesar 32** (4 x 8), yang memungkinkan training stabil dengan penggunaan memori yang rendah.
- **Learning Rate:** `2e-5` digunakan sebagai titik awal yang solid untuk fine-tuning model besar.
- **LR Scheduler:** `cosine`, untuk membantu model mencapai konvergensi yang lebih halus.
- **Epochs:** Model dilatih selama **3 epoch**. Evaluasi dilakukan di setiap akhir epoch untuk memonitor performa dan memilih checkpoint terbaik.