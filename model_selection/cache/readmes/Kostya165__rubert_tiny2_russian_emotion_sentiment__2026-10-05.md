---
license: cc-by-sa-4.0
datasets:
- Kostya165/ru_emotion_dvach
language:
- ru
metrics:
- accuracy
base_model:
- cointegrated/rubert-tiny2
pipeline_tag: text-classification
tags:
- russian
- emotion
- sentiment
- sentiment-analisys
- emotion-analisys
- emotion-classification
- emotion-detection
- rubert
- rubert-tiny
---
# rubert_tiny2_russian_emotion_sentiment

## Описание 

Модель `rubert_tiny2_russian_emotion_sentiment` — это дообученная версия легковесной модели [`cointegrated/rubert-tiny2`](https://huggingface.co/cointegrated/rubert-tiny2) для классификации пяти эмоций в русскоязычных сообщениях:

- **0**: aggression (агрессия)  
- **1**: anxiety (тревожность)  
- **2**: neutral (нейтральное состояние)  
- **3**: positive (позитив)  
- **4**: sarcasm (сарказм)  


### Результаты на валидации

| Метрика    | Значение |
|------------|----------|
| Accuracy   | 0.8911   |
| F1 macro   | 0.8910   |
| F1 micro   | 0.8911   |

**Точность по классам**:

- агрессия    (0): 0.9120  
- тревожность (1): 0.9462  
- нейтральное (2): 0.8663  
- позитив     (3): 0.8884  
- сарказм     (4): 0.8426  

### Использование

```bash
pip install transformers torch
```

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Загружаем модель и токенизатор
MODEL_ID = "Kostya165/rubert_tiny2_russian_emotion_sentiment"
tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)
model     = AutoModelForSequenceClassification.from_pretrained(MODEL_ID)
model.eval()

texts = [
    "Сегодня отличный день!",
    "Меня это всё бесит и раздражает."
]

# Токенизация
enc = tokenizer(texts, padding=True, truncation=True, max_length=128, return_tensors="pt")
with torch.no_grad():
    logits = model(**enc).logits
    preds = logits.argmax(dim=-1).tolist()

# Преобразуем ID обратно в метки
id2label = model.config.id2label
labels = [id2label[p] for p in preds]
print(labels)  # например: ['positive', 'aggression']
```

### Как было обучено

- **База**: `cointegrated/rubert-tiny2`  
- **Датасет**: `Kostya165/ru_emotion_dvach`
- **Эпохи**: 2  
- **Batch size**: 32  
- **LR**: 1e-5  
- **Mixed precision**: FP16  
- **Регуляризация**: Dropout 0.1, weight_decay 0.01, warmup_ratio 0.1    

### Зависимости

- `transformers>=4.30.0`  
- `torch>=1.10.0`  
- `datasets`  
- `evaluate`  

### Лицензия

CC-BY-SA 4.0.  

### Цитирование

```bibtex
@article{rubert_tiny2_russian_emotion_sentiment,
  title   = {Russian Emotion Sentiment Classification with RuBERT-tiny2},
  author  = {Kostya165},
  year    = {2024},
  howpublished = {\url{https://huggingface.co/Kostya165/rubert_tiny2_russian_emotion_sentiment}}
}
```

---

## English

# rubert_tiny2_russian_emotion_sentiment

**Description**

The `rubert_tiny2_russian_emotion_sentiment` model is a fine‑tuned version of the lightweight [`cointegrated/rubert-tiny2`](https://huggingface.co/cointegrated/rubert-tiny2) for classifying five emotions in Russian text:

- **0**: aggression  
- **1**: anxiety  
- **2**: neutral  
- **3**: positive  
- **4**: sarcasm  


**Validation Results**

| Metric     | Value  |
|------------|--------|
| Accuracy   | 0.8911 |
| F1 macro   | 0.8910 |
| F1 micro   | 0.8911 |

**Per‑class accuracy**:

- aggression: 0.9120  
- anxiety:    0.9462  
- neutral:    0.8663  
- positive:   0.8884  
- sarcasm:    0.8426  

**Usage**

```bash
pip install transformers torch
```

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

MODEL_ID = "Kostya165/rubert_tiny2_russian_emotion_sentiment"
tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)
model     = AutoModelForSequenceClassification.from_pretrained(MODEL_ID)
model.eval()

texts = ["Сегодня отличный день!", "Меня это всё бесит и раздражает."]
enc = tokenizer(texts, padding=True, truncation=True, max_length=128, return_tensors="pt")
with torch.no_grad():
    logits = model(**enc).logits
    preds = logits.argmax(dim=-1).tolist()

labels = [model.config.id2label[p] for p in preds]
print(labels)  # e.g. ['positive', 'aggression']
```

**Training Details**

- Base: `cointegrated/rubert-tiny2`  
- Dataset: `Kostya165/ru_emotion_dvach` (train/validation)  
- Epochs: 2  
- Batch size: 32  
- Learning rate: 1e‑5  
- Mixed precision: FP16  
- Regularization: Dropout 0.1, weight_decay 0.01, warmup_ratio 0.1  

**Requirements**

- `transformers>=4.30.0`  
- `torch>=1.10.0`  
- `datasets`  
- `evaluate`  

**License**

CC-BY-SA 4.0.  

**Citation**

```bibtex
@article{rubert_tiny2_russian_emotion_sentiment,
  title   = {Russian Emotion Sentiment Classification with RuBERT-tiny2},
  author  = {Kostya165},
  year    = {2024},
  howpublished = {\url{https://huggingface.co/Kostya165/rubert_tiny2_russian_emotion_sentiment}}
}
```
