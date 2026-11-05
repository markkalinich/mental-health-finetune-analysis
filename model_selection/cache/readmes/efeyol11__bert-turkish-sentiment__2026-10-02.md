---
library_name: transformers
language:
- tr
license: apache-2.0
base_model: savasy/bert-base-turkish-sentiment-cased
tags:
- sentiment-analysis
- text-classification
- turkish
- bert
- news
datasets:
- winvoker/turkish-sentiment-analysis-dataset
metrics:
- accuracy
- f1
pipeline_tag: text-classification
model-index:
- name: bert-turkish-sentiment
  results:
  - task:
      type: text-classification
      name: Turkish Sentiment Classification
    dataset:
      name: winvoker/turkish-sentiment-analysis-dataset
      type: winvoker/turkish-sentiment-analysis-dataset
      split: test
    metrics:
    - type: accuracy
      value: 0.9728
    - type: f1
      value: 0.9535
      name: F1 (macro)
    - type: f1
      value: 0.9726
      name: F1 (weighted)
---

# bert-turkish-sentiment

Türkçe metinler için 3-sınıflı duygu analizi modeli (`negative` / `neutral` / `positive`). Haber başlık + özet metinleri üzerinde duygu sınıflandırması yapmak üzere fine-tune edilmiştir.

## Model Details

### Model Description

Bu model, Türkçe haber metinlerinin duygu durumunu otomatik olarak sınıflandıran bir BERT tabanlı sequence classification modelidir. Bir B-projesi kapsamında haber takip sistemi için geliştirilmiş olup, GitHub Actions üzerinde haftalık otomatik retrain pipeline'ı ile sürekli güncellenmektedir.

- **Developed by:** efeyol11
- **Model type:** BertForSequenceClassification
- **Language(s) (NLP):** Türkçe (tr)
- **License:** Apache 2.0
- **Finetuned from model:** [savasy/bert-base-turkish-sentiment-cased](https://huggingface.co/savasy/bert-base-turkish-sentiment-cased)

### Model Sources

- **Repository:** [efeyol11/bert-turkish-sentiment](https://huggingface.co/efeyol11/bert-turkish-sentiment)

### Label Mapping

```python
LABEL2ID = {"negative": 0, "neutral": 1, "positive": 2}
ID2LABEL = {0: "negative", 1: "neutral", 2: "positive"}
```

Eğitim verisindeki Türkçe ham etiketler (`negatif`, `notr`, `nötr`, `pozitif`) bu üç sınıfa map edilmektedir.

## Uses

### Direct Use

Model, kısa-orta uzunluktaki Türkçe metinlerin (özellikle haber başlık + kısa özet kombinasyonları) genel duygu polaritesini sınıflandırmak için doğrudan kullanılabilir.

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

tokenizer = AutoTokenizer.from_pretrained("efeyol11/bert-turkish-sentiment")
model = AutoModelForSequenceClassification.from_pretrained("efeyol11/bert-turkish-sentiment")

text = "Türkiye ekonomisi son çeyrekte beklentilerin üzerinde büyüme kaydetti."
inputs = tokenizer(text, return_tensors="pt", truncation=True, padding="max_length", max_length=128)

with torch.no_grad():
    outputs = model(**inputs)

probs = torch.softmax(outputs.logits, dim=-1)
pred_id = probs.argmax(dim=-1).item()
print(model.config.id2label[pred_id], probs[0, pred_id].item())
```

### Downstream Use

- Türkçe haber agregasyon platformlarında otomatik etiketleme
- Sosyal medya / yorum metinlerinin duygu izlenmesi
- Domain-specific bir göreve aktarım için ek fine-tuning (transfer learning) için başlangıç noktası

### Out-of-Scope Use

- Aspect-based sentiment analysis (model genel duygu polaritesi tahmin eder, belirli bir konuya/yönüne ayrıştırma yapmaz)
- 128 token'dan çok daha uzun metinlerin tek seferde sınıflandırılması — uzun metinler kesilecek ve bilgi kaybı oluşacaktır
- Türkçe dışındaki diller
- Sarkazm, ironi veya açıkça ifade edilmemiş duygu içeren metinler — bu durumlarda model güvenilirliği düşer

## Bias, Risks, and Limitations

- **Domain mismatch:** Eğitim verisi tek bir genel-amaçlı Türkçe duygu corpus'u (`winvoker/turkish-sentiment-analysis-dataset`); haber domain'ine spesifik augmentation yalnızca güveni ≥0.85 olan ~74 pseudo-label örnekle yapılmıştır. Çok niş haber konularında performans düşebilir.
- **Class imbalance / pseudo-labeling bias:** Haftalık retrain'de model kendi yüksek-güvenli tahminleriyle augment edildiği için zaman içinde mevcut bias'lar pekişebilir (confirmation bias riski).
- **Sequence length:** `max_length=128` ile eğitildiği için uzun haber özetleri kesilir.
- **Subsampling:** Retrain script'inde kullanılan `--max-orig-samples 8000` parametresi class-stratified değildir; minority sınıf örnekleri yetersiz kalabilir.
- **Sosyal bias:** Türkçe duygu corpus'u demografik ya da konu temelli bias barındırabilir; bu bias modele aktarılmış olabilir (formal bir bias audit yapılmamıştır).

### Recommendations

Üretim ortamında bu modeli kullanırken:
- Özellikle hassas / yüksek riskli kararlar için tek başına model çıktısına dayanılmamalıdır.
- Domain'e özgü değerlendirme seti üzerinde periyodik performans kontrolü önerilir.
- Pseudo-label augmentation döngüsünün uzun vadeli etkisi izlenmelidir (drift monitoring).

## How to Get Started with the Model

```python
from transformers import pipeline

clf = pipeline(
    "text-classification",
    model="efeyol11/bert-turkish-sentiment",
    tokenizer="efeyol11/bert-turkish-sentiment",
)

clf("Borsa İstanbul yeni rekor kırdı, yatırımcılar memnun.")
# [{'label': 'positive', 'score': 0.99...}]
```

## Training Details

### Training Data

- **Dataset:** [winvoker/turkish-sentiment-analysis-dataset](https://huggingface.co/datasets/winvoker/turkish-sentiment-analysis-dataset)
- **Language:** Türkçe
- **Splits:**
  - Train: 440,679 örnek
  - Test/Validation: 48,965 örnek
- **Augmentation (weekly retrain):** PostgreSQL'den çekilen, model güveni ≥ 0.85 olan haber pseudo-label'leri (max 50,000; en son run'da 74 örnek dahil edilmiştir).

### Preprocessing

- Tokenizer: `BertTokenizer`, `do_lower_case=True`
- `truncation=True`, `padding="max_length"`, `max_length=128`
- Haber örneklerinde input formatı: `f"{cleaned_title}. {cleaned_summary}"`
- 20 karakterden kısa metinler filtrelenir
- Train set'i deterministik shuffle (`seed=42`)

### Training Hyperparameters

Aşağıdaki konfigürasyon, Hub'a push edilen modeli üreten weekly retrain pipeline'ına aittir:

| Parametre | Değer |
|-----------|-------|
| Epochs | 2 |
| Per-device train batch size | 32 |
| Per-device eval batch size | 32 |
| Learning rate | 1e-5 |
| Weight decay | 0.01 |
| LR scheduler | Linear with warmup (HF default) |
| Optimizer | AdamW (HF default) |
| Warmup steps | 0 |
| Precision | fp32 |
| Eval strategy | epoch |
| Save strategy | epoch |
| Best metric | f1_macro (`load_best_model_at_end=True`) |
| Seed | 42 (dataset shuffle) |

İlk full fine-tune (Apple MPS üzerinde): `epochs=3`, `batch_size=16`, `lr=2e-5` (resume'da 5e-6'ya düşürüldü), `weight_decay=0.01`, `max_length=128`, fp32. Yaklaşık 1 epoch = 87 dakika.

#### Speeds, Sizes, Times

- **Hardware:** GitHub Actions `ubuntu-latest` (CPU-only, no GPU/accelerator)
- **Training time (last successful run):** ~4 saat (8K original sample subset üzerinde)

## Evaluation

### Testing Data, Factors & Metrics

- **Testing Data:** `winvoker/turkish-sentiment-analysis-dataset` test split (48,965 örnek)
- **Metrics:** `accuracy`, `f1_macro`, `f1_weighted` — sklearn `f1_score` ile hesaplanır.

### Results

#### Fine-tuned model

| Metric | Değer |
|--------|-------|
| eval_loss | 0.0959 |
| eval_accuracy | **0.9728** |
| eval_f1_macro | **0.9535** |
| eval_f1_weighted | **0.9726** |

#### Baseline (savasy/bert-base-turkish-sentiment-cased, no fine-tuning on this label space)

| Metric | Değer |
|--------|-------|
| accuracy | 0.2383 |
| f1_macro | 0.2018 |
| f1_weighted | 0.2339 |

#### Before / After

| Metric | Baseline | Fine-tuned | Δ |
|--------|----------|------------|---|
| accuracy | 0.2383 | 0.9728 | **+0.7345** |
| f1_macro | 0.2018 | 0.9535 | **+0.7517** |
| f1_weighted | 0.2339 | 0.9726 | **+0.7387** |

> Not: Baseline model farklı bir label space ve farklı bir veri dağılımı üzerinde eğitildiği için doğrudan karşılaştırma değildir; bu tablo bu görev/etiket şeması için fine-tuning'in net katkısını göstermek amaçlıdır.

#### Quality Gate

Retrain pipeline'ı yalnızca `f1_macro ≥ 0.80` olan modelleri Hub'a push eder.

## Technical Specifications

### Model Architecture and Objective

- **Architecture:** `BertForSequenceClassification`
- **Hidden layers:** 12
- **Attention heads:** 12
- **Hidden size:** 768
- **Intermediate size:** 3072
- **Max position embeddings:** 512
- **Vocab size:** 32,000
- **Problem type:** `single_label_classification`
- **Dtype:** float32

### Compute Infrastructure

#### Hardware

GitHub Actions `ubuntu-latest` runner (CPU-only).

#### Software

- `transformers >= 4.40.0`
- `torch >= 2.2.0`
- `accelerate >= 1.1.0`
- `datasets >= 2.19.0`
- `scikit-learn >= 1.4.0`
- `mlflow >= 2.12.0`
- `sentence-transformers >= 3.0.0`
- `sentencepiece >= 0.2.0`
- Python `>= 3.10` (CI: 3.12)

## Model Card Authors

efeyol11

## Model Card Contact

HuggingFace üzerinden: [efeyol11](https://huggingface.co/efeyol11)