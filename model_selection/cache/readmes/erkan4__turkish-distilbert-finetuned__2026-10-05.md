---
library_name: transformers
language:
- tr
base_model:
- distilbert/distilbert-base-uncased-finetuned-sst-2-english
pipeline_tag: text-classification
tags:
- turkish
- sentiment-analysis
- movie-reviews
- 5-class
---

# Turkish Movie Sentiment (5-sınıf) — DistilBERT

Bu depo, Türkçe film yorumları üzerinde 5 sınıflı (1–5 yıldız) duygu analizi için ince ayar (fine-tune) edilmiş bir DistilBERT modelini içerir. Model; `TFLai/turkish_movie_sentiment` veri kümesi üzerinde eğitilmiş, sınıf etiketleri 0–4 aralığında olacak şekilde (rating_1 … rating_5) yeniden haritalandırılmıştır.

## Model Details

### Model Description
- **Geliştiren:** [Bilgi ekleyin]
- **Paylaşan:** [Bilgi ekleyin]
- **Model türü:** DistilBERT tabanlı metin sınıflandırma (sequence classification)
- **Dil(ler):** Türkçe
- **Lisans:** [Lisansınızı belirtin]
- **İnce ayar başlangıç noktası:** `distilbert/distilbert-base-uncased-finetuned-sst-2-english` (son sınıf katmanı 5 etiket için yeniden başlatıldı)

### Model Sources
- **Veri kümesi:** `TFLai/turkish_movie_sentiment`
- **Kod/Çalışma:** Eğitim Hugging Face `transformers` `Trainer` API’siyle yapılmıştır.
- **Demo [opsiyonel]:** [Bağlantı ekleyin]
- **Repo [opsiyonel]:** [Bağlantı ekleyin]

## Uses

### Direct Use
- Türkçe film yorumları için 5-seviyeli duygu/puan sınıflandırması (rating_1 … rating_5).

### Downstream Use
- Benzer Türkçe inceleme/veri alanlarında (ör. ürün yorumları) 5 sınıf duygu analizi için yeniden kullanım ve/veya yeniden ince ayar.

### Out-of-Scope Use
- 5 sınıfın dışındaki duygu kategorileri.
- Uzun belge sınıflandırması (128 token üzeri agresif kesilmeler anlam kaybına yol açabilir).
- Alan dışı (domain shift) metinlerde güvenilirlik beklenmemelidir.

## Bias, Risks, and Limitations
- Veri, film yorumları alanına özgüdür; diğer alanlara genellenebilirlik sınırlı olabilir.
- Sınıf dağılımı dengesizlikleri yanlılığa neden olabilir.
- İncelikli duygu/ironi/sarkazm tespiti zayıf kalabilir.

### Recommendations
- Üretim kullanımında alanınıza ait bir validasyon setiyle performansı teyit edin.
- Girdi uzunluklarını 128 token sınırına göre kontrol edin; gerekiyorsa `max_length` ayarını ve kesme stratejilerini gözden geçirin.

## How to Get Started with the Model

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline

repo_id = "KULLANICI_ADI/MODEL_ADI"  # bu depoyu yazın
tokenizer = AutoTokenizer.from_pretrained(repo_id)
model = AutoModelForSequenceClassification.from_pretrained(repo_id)

clf = pipeline("text-classification", model=model, tokenizer=tokenizer)
print(clf("Harika bir film, kesinlikle tavsiye ederim."))
```

## Training Details

### Training Data
- `datasets.load_dataset("TFLai/turkish_movie_sentiment")`
- Eğitim/Değerlendirme bölünmesi: train %80 / test %20 (seed=42)

### Preprocessing
- Etiket dönüşümü: `point` alanı virgül → nokta düzeltmesi sonrası `int(float(...)) - 1` ile 1–5 → 0–4 dönüşümü.
- Tokenizasyon: `truncation=True, padding="max_length", max_length=128`.

### Training Hyperparameters
- Epochs: 3
- Batch size: 16 (train/eval)
- Learning rate: 2e-5
- Weight decay: 0.01
- Değerlendirme: `evaluation_strategy="epoch"`
- Kayıt: `save_strategy="epoch"`, `load_best_model_at_end=True`
- Optimizasyon/karma hassasiyet: Varsayılan `Trainer` ayarları (fp32)

### Speeds, Sizes, Times
- Model boyutu: DistilBERT sınıflandırma başlığı ile (yaklaşık ~260MB, dosya biçimine göre değişir).
- Eğitim süresi/donanım: [Bilgi ekleyin]

## Evaluation

### Testing Data, Factors & Metrics
- Test bölümü: %20 ayrım
- Metrik: Accuracy (Hugging Face `evaluate` → `accuracy`)

### Results
- Accuracy: [Sonucu ekleyin]
- Not: Değerlendirme, 128 token sınırı ve alan dağılımı ile sınırlıdır.

## Model Examination
- Çıktı etiketleri: `id2label = {0:"rating_1", 1:"rating_2", 2:"rating_3", 3:"rating_4", 4:"rating_5"}`
- Sınıf sırası eğitimde kullanılan map ile uyumludur.

## Environmental Impact
- Donanım: [CPU/GPU bilgisi]
- Süre: [Eğitim saatleri]
- CO₂ tahmini: [Bilgi ekleyin]

## Technical Specifications

### Model Architecture and Objective
- DistilBERT gövdesi + 5 sınıflı sınıflandırma başlığı (cross-entropy).

### Compute Infrastructure
- Donanım: [Bilgi ekleyin]
- Yazılım: `transformers 4.56.2`, `datasets`, `accelerate`, `evaluate`, `torch`

## Citation

**BibTeX:**