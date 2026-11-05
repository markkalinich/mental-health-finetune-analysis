---
language: ru
license: mit
base_model: DeepPavlov/rubert-base-cased
tags:
  - text-classification
  - sentiment-analysis
  - russian
  - bert
datasets:
  - blinoff/kinopoisk
metrics:
  - f1
---

# RuBERT Kinopoisk Sentiment

Модель для бинарной классификации тональности русскоязычных отзывов (Bad / Good),
дообученная на датасете Кинопоиска.

## Метрики на тестовой выборке

| Class | Precision | Recall | F1 |
|-------|-----------|--------|----|
| bad   | 0.87      | 0.91   | 0.89 |
| good  | 0.99      | 0.98   | 0.98 |
| **macro avg** | **0.93** | **0.94** | **0.94** |

## Использование

```python
from transformers import pipeline

pipe = pipeline(
    "text-classification",
    model="toma4ik/rubert-kinopoisk-sentiment"
)

pipe("Отличный фильм, смотрел на одном дыхании!")
```

## Обучение

- **Base model:** DeepPavlov/rubert-base-cased  
- **Dataset:** blinoff/kinopoisk (binary: bad/good, neutral excluded)  
- **Oversampling:** random oversampling для балансировки классов  
- **Epochs:** 3, best checkpoint — epoch 2  
- **Learning rate:** 2e-5

## Ссылки

- 📦 [GitHub](https://github.com/timuraminov77/rubert-kinopoisk-sentiment.git)