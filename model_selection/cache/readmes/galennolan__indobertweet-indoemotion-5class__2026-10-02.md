---
license: apache-2.0 
language:
- id
library_name: transformers
tags:
- text-classification
- sentiment-analysis
- emotion-classification
- indonesian
- indobertweet
datasets:
- PRDECT-ID
metrics:
- accuracy
- f1
- precision
- recall
base_model:
- Aardiiiiy/indobertweet-base-Indonesian-sentiment-analysis
---
# IndoBERTweet untuk Klasifikasi Emosi Bahasa Indonesia (5 Label)

Model ini merupakan hasil *fine-tune lanjutan* dari [`Aardiiiiy/indobertweet-base-Indonesian-sentiment-analysis`](https://huggingface.co/Aardiiiiy/indobertweet-base-Indonesian-sentiment-analysis).  
Awalnya model tersebut hanya mengenali 3 sentimen: **positive**, **negative** dan **neutral**.  
Sekarang model ini dikembangkan lebih lanjut untuk mengenali **lima jenis emosi** dalam teks Bahasa Indonesia:

- `anger  `
- `fear   `
- `happy  `
- `love   `
- `sadness`

## 🎯 Tujuan
Model ini cocok digunakan untuk analisis emosi pada:
- Ulasan produk
- Komentar sosial media
- Respon pengguna aplikasi
- Teks pendek lain yang ditulis dalam Bahasa Indonesia

## Tentang Dataset

Fine-tuning menggunakan dataset PRDECT-ID (Produk Review Dataset for Emotion Classification Task - Indonesia). Dataset ini berisi ulasan produk berbahasa Indonesia dengan label emosi yang dideskripsikan sebagai berikut:

| Emosi  | Deskripsi                                                                                         | Contoh                                                                                                   |
|--------|-------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|
| anger  | Mengandung kata-kata marah, komplain, kata kasar, tanda baca kapital                             | *"Barang jelek!!! tiga hari sudah pada lepas pinggirnya, barang mahal tapi kualitasnya jelek banget"*  |
| fear   | Mengandung kalimat peringatan, keraguan, pertanyaan terhadap produk/penjual/pengiriman           | *"Saya sarankan buat video unboxing, hidupkan langsung dan instal CPU Z."*                               |
| happy  | Pujian, ekspresi puas, bangga terhadap produk/penjual                                           | *"Mantap adminnya selalu merhatiin pembeli. Respect, proses super cepat, sampai juga cepat, barang sesuai."* |
| love   | Ekspresi cinta atau suka berlebihan, pujian kuat pada produk/penjual                            | *"Produknya bagus dan sukaaakkk banget!!!"*                                                            |
| sadness| Mengekspresikan kekecewaan, penyesalan terhadap produk                                         | *"Sangat kecewa, phone holder tidak lengkap, packing cuma pakai keresek hitam."*                        |

Tabel berikut menunjukkan performa model pada set validasi per epoch:

| Epoch | Training Loss | Validation Loss | Accuracy | F1 (Macro) | Precision (Macro) | Recall (Macro) |
|-------|---------------|-----------------|----------|------------|-------------------|----------------|
| 1     | 0.850000      | 0.628058        | 0.7167   | 0.7115     | 0.7177            | 0.7167         |
| 2     | 0.649600      | 0.674608        | 0.7259   | 0.7253     | 0.7466            | 0.7259         |
| 3     | 0.558100      | 0.655473        | 0.7444   | 0.7449     | 0.7599            | 0.7444         |
| 4     | 0.476800      | 0.712344        | 0.7444   | 0.7425     | 0.7526            | 0.7444         |
| 5     | 0.414400      | 0.805933        | 0.7370   | 0.7384     | 0.7466            | 0.7370         |
| 6     | 0.345500      | 0.907782        | 0.7444   | 0.7452     | 0.7471            | 0.7444         |
| 7     | 0.311500      | 0.991595        | 0.7278   | 0.7257     | 0.7263            | 0.7278         |
| 8     | 0.257800      | 1.177693        | 0.7222   | 0.7197     | 0.7219            | 0.7222         |
| 9     | 0.232200      | 1.227367        | 0.7407   | 0.7400     | 0.7403            | 0.7407         |
| 10    | 0.219800      | 1.273331        | 0.7444   | 0.7443     | 0.7459            | 0.7444         |

**Catatan tentang Performa:**
Berdasarkan hasil di atas, *validation loss* mulai meningkat setelah epoch ke-3, yang mengindikasikan potensi *overfitting*. Kinerja terbaik (berdasarkan F1-Score tertinggi pada set validasi sebelum *validation loss* meningkat signifikan) diamati pada **Epoch 3** (F1: 0.7449, Accuracy: 0.7444, Validation Loss: 0.655473) atau **Epoch 6** (F1: 0.7452, Accuracy: 0.7444, Validation Loss: 0.907782) jika F1-Score yang menjadi fokus utama meskipun *validation loss* sudah lebih tinggi. Pengguna disarankan untuk mengevaluasi *checkpoint* dari epoch-epoch tersebut atau melakukan *fine-tuning* lebih lanjut dengan strategi mitigasi *overfitting* (seperti yang didiskusikan dalam penelitian terkait model ini).



## 🔍 Contoh Penggunaan
Contoh penggunaan model untuk klasifikasi emosi menggunakan Hugging Face `pipeline`:

```python
from transformers import pipeline

classifier = pipeline("text-classification", model="galennolan/indobertweet-indoemotion-5class")

text = "Produknya bagus tapi pengiriman lama."
hasil = classifier(text)
print(hasil)
# [{'label': 'anger', 'score': ...}]
# Decode label index
label_id = int(hasil[0]['label'].split('_')[-1])
print("Emotion:", le.inverse_transform([label_id])[0])