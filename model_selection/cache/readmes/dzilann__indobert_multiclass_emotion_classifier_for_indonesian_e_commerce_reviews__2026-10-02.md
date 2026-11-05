---
language: id
pipeline_tag: text-classification
framework: pytorch
base_model: indobenchmark/indobert-base-p1
tags:
- indobert
- indonesian
- emotion-classification
- text-classification
- pytorch
- e-commerce
license: apache-2.0
datasets:
- ZakyF/PRDECT-ID
---
# Klasifikasi Emosi Ulasan E-Commerce Indonesia (IndoBERT - Fine-Tuned)

Model ini merupakan hasil *fine-tuning* dari [IndoBERT](https://huggingface.co/indobenchmark/indobert-base-p1) untuk klasifikasi emosi multikelas pada teks ulasan produk e-commerce berbahasa Indonesia. 

Model ini dikembangkan sebagai bagian dari penelitian skripsi yang membandingkan performa model Generative AI (Zero-Shot & Few-Shot) dengan model Fine-tuning berbasis BERT. Berdasarkan hasil pengujian, model IndoBERT ini mencapai performa terbaik dengan **F1-Score dan Akurasi sebesar 84%**.

## 📝 Deskripsi Model
Selama proses *fine-tuning*, seluruh parameter model dilatih ulang secara menyeluruh, mencakup:
* **Lapisan Embedding:** Penyesuaian representasi vektor kata terhadap kosakata e-commerce.
* **Lapisan Encoder:** Optimasi 12 lapisan transformer untuk menangkap konteks emosi dalam bahasa Indonesia.
* **Classification Head:** Lapisan linear di atas model dasar untuk memetakan representasi teks ke dalam 5 kategori emosi.

Model ini dirancang untuk diintegrasikan ke dalam sistem analisis emosi untuk membantu pelaku industri memahami emosi pelanggan secara otomatis.

## 📊 Dataset
Model ini dilatih menggunakan dataset **PRDECT-ID**, sebuah dataset ulasan produk Tokopedia yang mencakup 29 kategori produk.

* **Label:** `Anger` (Marah), `Fear` (Takut), `Happy` (Senang), `Love` (Suka), dan `Sadness` (Sedih).
* **Publikasi:** *PRDECT-ID: Indonesian product reviews dataset for emotion classification tasks*
* **DOI:** [10.1016/j.dib.2022.108554](https://doi.org/10.1016/j.dib.2022.108554)

## 📈 Hasil Evaluasi (Evaluation Results)
Evaluasi dilakukan untuk mengukur efektivitas model pada data uji:

* **Akurasi:** 84%
* **F1-Score (Macro):** 84%
* **Precision (Macro):** 85%
* **Recall (Macro):** 84%

## ⚙️ Prosedur Pelatihan (Training Procedure)
* **Model Dasar:** `indobenchmark/indobert-base-p1`
* **Framework:** PyTorch & Hugging Face Transformers
* **Hardware:** NVIDIA Tesla T4 (Google Colab)
* **Metode:** Full Fine-tuning (Semua parameter dilatih ulang)
* **Optimizer:** AdamW
* **Learning Rate:** 20e-6
* **Epochs:** 20 (Maximum)

## ⏱️ Kinerja Inferensi (Inference Performance)
Berdasarkan pengujian pada dataset PRDECT-ID, model menunjukkan efisiensi sebagai berikut:

* **Rata-rata Latency:** 0,063 detik/sampel
* **Throughput:** 647 sampel/menit

## ⚠️ Batasan Penggunaan (Limitations)
1. **Konteks Data:** Model ini paling optimal digunakan untuk ulasan produk e-commerce. Penggunaan pada teks formal atau domain lain (seperti politik atau medis) mungkin menurunkan akurasi.
2. **Bahasa:** Khusus Bahasa Indonesia (termasuk bahasa tidak baku/slang yang umum di platform e-commerce).
3. **Kategori Emosi:** Terbatas pada lima kategori (Anger, Fear, Happy, Love, Sadness).

---
## ✅ Cara Penggunaan (Usage)

Anda dapat menggunakan model ini menggunakan library `transformers` berbasis PyTorch:
```python
import torch
import torch.nn.functional as F
from transformers import AutoTokenizer, AutoModelForSequenceClassification

# 1. Inisialisasi
model_path = "Rasyy/indobert_multiclass_emotion_classifier_for_indonesian_e_commerce_reviews"
label_map = {0: 'Anger', 1: 'Fear', 2: 'Happy', 3: 'Love', 4: 'Sad'}

def load_model_and_tokenizer(path):
    try:
        print("Memuat tokenizer & model...")
        tokenizer = AutoTokenizer.from_pretrained(path)
        model = AutoModelForSequenceClassification.from_pretrained(path)
        print("Model siap digunakan!")
        return tokenizer, model
    except Exception as e:
        print(f"Error: {e}")
        return None, None

tokenizer, model = load_model_and_tokenizer(model_path)

# 2. Prediksi
text = "Barangnya bagus banget, pengiriman cepat dan kurir ramah. Suka!"
inputs = tokenizer(
    text,
    max_length=128, # Sesuaikan dengan max_length saat training
    truncation=True,
    padding='max_length',
    return_tensors='pt'
)

with torch.no_grad():
    outputs = model(**inputs)
    logits = outputs.logits
    
# 3. Hitung Probabilitas
probabilities = F.softmax(logits, dim=-1).squeeze().cpu().numpy()
predicted_class_id = torch.argmax(logits, dim=1).item()
predicted_label = label_map.get(predicted_class_id, "Unknown")

# Output hasil
print(f"Teks: {text}")
print(f"Prediksi: {predicted_label}")
print(f"Skor Probabilitas: {probabilities[predicted_class_id]:.4f}")