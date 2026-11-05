---
language:
- id
library_name: transformers
tags:
- text-classification
- sentiment-analysis
- distilbert
- imdb
datasets:
- imdb
metrics:
- accuracy
- f1
---

# DistilBERT Base Uncased - Fine-tuned on IMDB

Ini adalah model **DistilBERT Base Uncased** yang telah di-*fine-tune* pada dataset **IMDB** untuk tugas klasifikasi sentimen. Model ini dapat mengklasifikasikan sebuah teks ulasan film ke dalam label **`POSITIVE`** atau **`NEGATIVE`**.

Model ini dibuat sebagai bagian dari proyek pembelajaran pribadi. Kode untuk proses training dapat ditemukan di [repositori GitHub ini](https://github.com/DavaIlham261/NLP-Practice-IMDB-Sentiment).

## 🚀 How to Use

Anda dapat menggunakan model ini secara langsung dengan `pipeline` dari library Transformers:

```python
from transformers import pipeline

# Ganti dengan nama repo model Anda di Hugging Face
model_path = "DavaIlham/distilbert-finetuned-sentiment-imdb" 

# Muat pipeline
sentiment_analyzer = pipeline("sentiment-analysis", model=model_path)

# Lakukan prediksi
reviews = [
    "This is one of the best movies I have ever seen, a true masterpiece!",
    "The acting was wooden and the plot was completely nonsensical."
]

results = sentiment_analyzer(reviews)
print(results)
# Output yang diharapkan:
# [{'label': 'POSITIVE', 'score': 0.99...}, {'label': 'NEGATIVE', 'score': 0.99...}]
```

## 📈 Training & Evaluation

### Training Procedure
Model ini dilatih menggunakan `Trainer` API dari library Hugging Face Transformers. Berikut adalah beberapa detail hyperparameters:
* **Dataset:** `imdb`
* **Epochs:** 3
* **Optimizer:** AdamW
* **Learning Rate:** 5e-5 (default dari Trainer)
* **Batch Size:** 16 (default dari Trainer)

### Evaluation Results
Model ini dievaluasi pada split `test` dari dataset IMDB dan mencapai hasil sebagai berikut:

* **Loss:** `0.45617571473121643`
* **Accuracy:** `0.91188`
* **F1-Score:** `0.9118722130287433`

## 👤 Author
* **Dava Ilham Muhammad**
* GitHub: [@DavaIlham261](https://github.com/DavaIlham261)

---

**Tip:** Di Hugging Face, Anda bisa langsung mengedit file `README.md` ini dari halaman repositori model Anda dengan mengklik "Edit model card".