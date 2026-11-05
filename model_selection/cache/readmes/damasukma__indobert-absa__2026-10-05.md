---
language: id
datasets:
- custom
tags:
- indobert
- sentiment-analysis
- absa
- aspect-based-sentiment-analysis
- bahasa-indonesia
---

# IndoBERT for Aspect-Based Sentiment Analysis (ABSA)

Model ini adalah hasil fine-tuning dari [`indobenchmark/indobert-base-p1`](https://huggingface.co/indobenchmark/indobert-base-p1) untuk tugas **Aspect-Based Sentiment Analysis (ABSA)** dalam Bahasa Indonesia.

## 📝 Deskripsi

ABSA adalah tugas NLP untuk mengklasifikasi sentimen terhadap aspek-aspek spesifik dalam suatu kalimat. Contoh aspek: `rasa`, `harga`, `kualitas`, `pengiriman`.

Model ini dilatih menggunakan dataset review makanan berbahasa Indonesia, dengan format label per aspek.

Contoh input kalimat:

> "Rasa: enak bgt, harga: agak mahal, pengiriman: cepat"

Model akan memprediksi sentimen dari aspek-aspek tersebut secara terpisah (`positive`, `neutral`, `negative`).

---

## 📦 Penggunaan
```python
from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification
# Load model ABSA
model_name = "damasukma/indobert-absa"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

absa_pipe = pipeline("text-classification", model=model, tokenizer=tokenizer)

# Contoh kalimat & aspek
kalimat = "rasa kayanya enak kualitas kurang baik"
aspek = "kualitas"

# Format input untuk ABSA: [sentence] [SEP] [aspect]
text_input = f"{kalimat} [SEP] {aspek}"

# Prediksi sentimen
pred = absa_pipe(text_input)
print(pred)
```