---
language:
  - tr
license: mit
tags:
  - bert
  - text-classification
  - sentiment-analysis
  - turkish
  - pytorch
  - transformers
datasets:
  - turkish_product_reviews
base_model: dbmdz/bert-base-turkish-cased
model-index:
  - name: DexopT/BERTURK
    results:
      - task:
          type: text-classification
          name: Sentiment Analysis
        dataset:
          name: Turkish Product Reviews
          type: turkish_product_reviews
        metrics:
          - type: accuracy
            value: 0.9612
            name: Accuracy
          - type: f1
            value: 0.9598
            name: F1 (weighted)
---

# BERTurk — Türkçe Duygu Analizi

`dbmdz/bert-base-turkish-cased` modeli üzerine Türkçe ürün yorumları ile fine-tune edilmiş bir duygu analizi (sentiment analysis) modelidir.

## Model Detayları

| Özellik | Değer |
|---|---|
| Temel model | `dbmdz/bert-base-turkish-cased` |
| Görev | İkili sınıflandırma (Pozitif / Negatif) |
| Dil | Türkçe |
| Doğruluk | **%96.12** |
| F1 Skoru | **0.9598** |
| Parametre | ~110M |
| Max token | 128 |

## Kullanım

### Transformers Pipeline

```python
from transformers import pipeline

sentiment = pipeline(
    "text-classification",
    model="DexopT/BERTURK"
)

sonuc = sentiment("Ürün gerçekten harika, çok memnun kaldım!")
print(sonuc)
# [{'label': 'positive', 'score': 0.9934}]
```

### Manuel Kullanım

```python
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

model_name = "DexopT/BERTURK"
tokenizer  = AutoTokenizer.from_pretrained(model_name)
model      = AutoModelForSequenceClassification.from_pretrained(model_name)
model.eval()

metin = "Berbat bir ürün, para israfı."

inputs = tokenizer(metin, return_tensors="pt", truncation=True, max_length=128)

with torch.no_grad():
    logits = model(**inputs).logits

probs    = torch.softmax(logits, dim=-1)[0]
label_id = probs.argmax().item()
label    = model.config.id2label[label_id]
guven    = probs[label_id].item()

print(f"Sonuç    : {label}")
print(f"Güven    : {guven:.4f}")
print(f"Pozitif  : {probs[1].item():.4f}")
print(f"Negatif  : {probs[0].item():.4f}")
```

### Toplu Tahmin

```python
yorumlar = [
    "Harika ürün, kesinlikle tavsiye ederim!",
    "Çok kötü, hiç memnun kalmadım.",
    "Fiyatına göre gayet iyi.",
    "Kargo geç geldi ama ürün kaliteliydi.",
]

for yorum in yorumlar:
    r = sentiment(yorum, truncation=True, max_length=128)[0]
    print(f"[{r['label'].upper():8}] {r['score']:.2%}  →  {yorum[:50]}")
```

## Eğitim

### Veri Seti

[Turkish Product Reviews](https://huggingface.co/datasets/turkish_product_reviews) veri seti kullanılmıştır.

- Toplam: ~235.000 Türkçe e-ticaret yorumu
- Eğitim: 18.000 örnek
- Test: 2.000 örnek
- Etiketler: `positive` (1), `negative` (0)

### Hiperparametreler

```python
TrainingArguments(
    num_train_epochs       = 3,
    per_device_train_batch_size = 32,
    per_device_eval_batch_size  = 64,
    learning_rate          = 2e-5,
    warmup_steps           = 200,
    weight_decay           = 0.01,
    fp16                   = True,       # T4 GPU
    evaluation_strategy    = "epoch",
    load_best_model_at_end = True,
    metric_for_best_model  = "f1",
)
```

### Eğitim Sonuçları

| Epoch | Train Loss | Val Loss | Doğruluk | F1 |
|---|---|---|---|---|
| 1 | 0.1303 | 0.1664 | 95.40% | 94.56% |
| 2 | 0.1001 | 0.1555 | 95.80% | 95.63% |
| 3 | **0.0812** | **0.1489** | **96.12%** | **95.98%** |

### Eğitim Ortamı

- GPU: NVIDIA T4 (Google Colab)
- Süre: ~20 dakika
- Framework: PyTorch + Hugging Face Transformers

## Etiketler

| ID | Label | Açıklama |
|---|---|---|
| 0 | `negative` | Negatif yorum |
| 1 | `positive` | Pozitif yorum |

## Sınırlılıklar

- Maksimum token uzunluğu 128 olarak ayarlanmıştır, uzun metinler kırpılır.
- Model yalnızca Türkçe üzerinde eğitilmiştir; diğer dillerde güvenilir sonuç vermez.
- Nötr veya karma duygular içeren yorumlarda doğruluk düşebilir.
- Ürün yorumları dışındaki metin türleri (haber, akademik metin vb.) için optimize edilmemiştir.

## Lisans

MIT License

## Atıf

```bibtex
@misc{berturk2025,
  author    = {Yılmaz KARAAĞAÇ (DexopT)},
  title     = {BERTurk: Turkish Sentiment Analysis},
  year      = {2026},
  publisher = {Hugging Face},
  url       = {https://huggingface.co/DexopT/BERTURK}
}
```

---

**Yılmaz KARAAĞAÇ** · [GitHub](https://github.com/DexopT)
