---
license: mit
language:
- tr
metrics:
- accuracy
pipeline_tag: text-classification
tags:
- sentiment-analysis
- emotion-classification
- turkish
- distilbert
- stress-detection
- motivation
---

# distilbert-base-turkish-emotion-analysis

This model is a fine-tuned version of **DistilBERT** optimized to analyze emotional states in Turkish text. Unlike standard positive/negative sentiment models, this model is specifically trained to detect whether a user's statement indicates **Stress (Stresli)**, **Motivation (Motive)**, or a **Neutral (Nötr)** state.

Bu model, Türkçe metinler üzerinde duygu ve durum analizi yapmak için ince ayar (fine-tune) yapılmış bir **DistilBERT** modelidir. Standart pozitif/negatif duygu analizlerinden farklı olarak; kullanıcının cümlelerinden **Stresli**, **Motive** veya **Nötr** olduğunu tespit etmek üzere özel bir veri setiyle eğitilmiştir.

## Model Details / Model Detayları

- **Developed by:** omercakar123
- **Model type:** Transformer-based Text Classification (DistilBERT)
- **Language(s) (NLP):** Turkish (tr)
- **License:** MIT
- **Finetuned from model:** dbmdz/distilbert-base-turkish-cased

---

## Intended Uses / Kullanım Amaçları

### Direct Use / Doğrudan Kullanım
This model is perfect for personal assistant ecosystems, mental well-being applications, AI mentors, and chatbot platforms that need to dynamically adapt their tone based on the user's emotional and psychological state (stressed or motivated).

Bu model; akıllı asistan ekosistemleri, zihinsel iyi oluş (wellness) uygulamaları, yapay zeka mentörleri ve kullanıcının psikolojik durumuna (stresli veya motive) göre dinamik cevap üretmek isteyen chatbot platformları için idealdir.

---

## How to Get Started with the Model / Nasıl Kullanılır?

Anyone can easily download and run this model using Hugging Face's `pipeline` API with the following Python code:

Aşağıdaki hazır Python kodunu kullanarak modeli doğrudan projenize dahil edebilir ve kullanıcıların duygusal durumlarını analiz edebilirsiniz:

```python
from transformers import pipeline

# Load the emotion classification pipeline
# Duygu ve durum analizi pipeline'ını yükle
classifier = pipeline(
    "text-classification", 
    model="omercakar123/distilbert-base-turkish-emotion-analysis"
)

# Test sentences representing different emotional states
# Farklı duygu durumlarını temsil eden örnek cümleler
texts = [
    "Bugün ödevleri yetiştiremeyeceğim diye çok korkuyorum, üzerimde acayip bir baskı var.", # Stresli
    "Harika bir gün! Bu projeyi tamamlamak için inanılmaz bir enerji hissediyorum içimde.", # Motive
    "Yarınki toplantı saat ikiye ertelenmiş, bilginiz olsun.", # Nötr
]

# Run prediction / Tahminleri çalıştır
results = classifier(texts)

for text, result in zip(texts, results):
    print(f"Metin: {text}")
    print(f"Durum (Label): {result['label']} | Güven Skoru: {result['score']:.4f}\n")

Training Details / Eğitim Detayları
Training Data / Eğitim Verisi
The model was fine-tuned on a custom, curated Turkish dataset specifically labeled for stress levels, motivational status, and neutral daily assistant dialogues.

Model; stres seviyeleri, motivasyon durumları ve günlük nötr asistan diyaloglarını içeren, özel olarak etiketlenmiş yerel bir Türkçe veri seti üzerinde eğitilmiştir.

Model Architecture / Mimari
Built on DistilBERT, offering a lightweight, fast, and production-ready alternative to standard BERT models while retaining high classification accuracy.

DistilBERT mimarisi sayesinde, standart BERT modellerine göre çok daha hafif, hızlı ve üretim (production) ortamlarına uygun bir yapı sunarken yüksek başarım oranını korur.

Model Card Contact / İletişim
Developed as a specialized NLP module for personalized assistant ecosystems. For questions and contributions, feel free to reach out via Hugging Face.