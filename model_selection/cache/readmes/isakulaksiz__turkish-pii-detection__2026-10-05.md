---
license: mit
datasets:
- unimelb-nlp/wikiann
language:
- tr
metrics:
- accuracy
base_model:
- dbmdz/bert-base-turkish-uncased
pipeline_tag: token-classification
---
# 🔒 BerTurk Kişisel Veri Maskeleme Modeli (Turkish PII Detection)

Bu model, Türkçe metinlerde kişisel verileri (isim, lokasyon, kurum vb.) tespit edip maskelemek için BerTurk (BERT-based) üzerine fine-tune edilmiştir. Modelin çıktısı, tespit edilen kişisel verileri ilgili maske etiketleriyle değiştirir ve isteğe bağlı olarak maske-sözlük eşleşmesini de sağlar.

## 📌 Kullanım Alanları
- Kişisel veri maskeleme (KVKK/GDPR uyumluluğu)
- Metin anonimleştirme
- Veri temizleme ve ön işleme

---

## 🧠 Model Bilgileri

- **Base Model:** `dbmdz/bert-base-turkish-uncased`
- **Model Tipi:** Token Classification (NER)
- **Dil:** Türkçe

---


## 🏋️‍♂️ Eğitim Parametreleri

```python
from transformers import TrainingArguments

training_args = TrainingArguments(
    output_dir="pii_detection_model",
    learning_rate=2e-5,
    per_device_train_batch_size=16,
    per_device_eval_batch_size=16,
    num_train_epochs=3,
    weight_decay=0.01,
)

```

## 🚀 Kullanım Örneği (Inference)

```python
from transformers import pipeline, AutoTokenizer, AutoModelForTokenClassification

model = AutoModelForTokenClassification.from_pretrained("isakulaksiz/turkish-pii-detection")
tokenizer = AutoTokenizer.from_pretrained("isakulaksiz/turkish-pii-detection")

ner_pipeline = pipeline("ner", model=model, tokenizer=tokenizer, aggregation_strategy="simple")

text = "isa kulaksız erzurum ilinde atatürk üniversitesinde eğitim görmektedir."

results = ner_pipeline(text)