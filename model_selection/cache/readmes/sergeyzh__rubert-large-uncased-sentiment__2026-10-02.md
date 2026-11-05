---
language:
- ru

pipeline_tag: text-classification

tags:
- russian
- sentiment-analysis
- multi-class-classification
- rubert
- transformers

license: mit

base_model: sergeyzh/rubert-large-uncased-sts

library_name: transformers

---

Модель BERT-large для классификации сентимента русских отзывов: 3 класса — Negative (0), Neutral (1), Positive (2).

Получена на базе модели [sergeyzh/rubert-large-uncased-sts](https://huggingface.co/sergeyzh/rubert-large-uncased-sts) путём дистилляции мягких меток (soft labels), сгенерированных teacher-моделью FRIDA (архитектура T5-encoder, 823M параметров), предварительно дообученной на данных сентимент-анализа.

Модель содержит 12 слоёв — вдвое меньше стандартных 24 для архитектуры BERT-large (по скорости инференса сопоставима с классическими BERT-base моделями).

Основные характеристики модели:
 - размер hidden — 1024,
 - длина контекста — 512,
 - слоёв — 12,
 - параметров — ~209M (вес ~798 МБ).

Классы: `0` — Negative, `1` — Neutral, `2` — Positive.


## Использование

Самый простой способ — `pipeline`:

```Python
from transformers import pipeline

model = pipeline("text-classification", model="sergeyzh/rubert-large-uncased-sentiment")
model("Просто шедевр. Каждая минута на вес золота, ни секунды скуки. Музыка, игра актёров, режиссура — всё на высочайшем уровне.", truncation=True, max_length=512)
# [{'label': 'Positive', 'score': 0.7779}]
```

Если нужны вероятности всех классов, используйте `transformers` напрямую:

```Python
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

checkpoint = "sergeyzh/rubert-large-uncased-sentiment"
tokenizer = AutoTokenizer.from_pretrained(checkpoint)
model = AutoModelForSequenceClassification.from_pretrained(checkpoint)

text = "Просто шедевр. Каждая минута на вес золота, ни секунды скуки. Музыка, игра актёров, режиссура — всё на высочайшем уровне."
inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=512)
with torch.no_grad():
    logits = model(**inputs).logits
proba = torch.softmax(logits, dim=1)
label = model.config.id2label[proba.argmax().item()]
print(label, proba.tolist())
# Positive [[0.0126, 0.2095, 0.7779]]
```


## Обучение

- Базовая модель: [sergeyzh/rubert-large-uncased-sts](https://huggingface.co/sergeyzh/rubert-large-uncased-sts)
- Метод: дистилляция мягких меток (soft-label distillation) от teacher-модели FRIDA (архитектура T5-encoder, 24 слоя, 1536d, 823M параметров), предварительно дообученной на данных сентимент-анализа
- Смешанный loss: 0.75 × CE(hard) + 0.25 × CE(soft), где soft-метки — softmax-вероятности teacher по 3 классам (max_length = 512)
- Данные: 105500 train + 21500 validation русских отзывов — датасеты Kinopoisk, RuReviews, Georeview
- 3 эпохи, effective batch_size = 32 (batch_size = 8, grad_accum = 4), lr = 2e-5, warmup = 0.1, weight_decay = 0.01, max_length = 256
- Отбор по валидационной F1 (лучшая эпоха 3, val F1 = 0.7725)


## Метрики

Тестовые наборы: Kinopoisk (1500), RuReviews (15000), Georeview (5000, 5-звёздный рейтинг сведён к 3 классам: 1–2 звезды — Negative, 3 — Neutral, 4–5 — Positive). Оценка: argmax по логитам, max_length = 512.

| Модель | Kinopoisk Acc/F1 | RuReviews Acc/F1 | Georeview Acc/F1 | Avg F1 |
| :--- | :---: | :---: | :---: | :---: |
| **sergeyzh/rubert-large-uncased-sentiment** | **0.7013** / **0.6929** | 0.7851 / 0.7866 | **0.7858** / **0.7361** | **0.7385** |
| [sergeyzh/rubert-tiny-sentiment](https://huggingface.co/sergeyzh/rubert-tiny-sentiment) | 0.6593 / 0.6519 | 0.7672 / 0.7690 | 0.7680 / 0.7130 | 0.7113 |
| [seara/rubert-base-cased-russian-sentiment](https://huggingface.co/seara/rubert-base-cased-russian-sentiment) | 0.5653 / 0.5679 | **0.8163** / **0.8183** | 0.6566 / 0.6434 | 0.6765 |
| [seara/rubert-tiny2-russian-sentiment](https://huggingface.co/seara/rubert-tiny2-russian-sentiment) | 0.4980 / 0.5032 | 0.7877 / 0.7899 | 0.6218 / 0.6122 | 0.6351 |
| [blanchefort/rubert-base-cased-sentiment](https://huggingface.co/blanchefort/rubert-base-cased-sentiment) | 0.5253 / 0.5209 | 0.7615 / 0.7549 | 0.6716 / 0.6047 | 0.6268 |
| [blanchefort/rubert-base-cased-sentiment-rusentiment](https://huggingface.co/blanchefort/rubert-base-cased-sentiment-rusentiment) | 0.5413 / 0.5470 | 0.6230 / 0.6327 | 0.6022 / 0.5760 | 0.5852 |
| [cointegrated/rubert-tiny-sentiment-balanced](https://huggingface.co/cointegrated/rubert-tiny-sentiment-balanced) | 0.4293 / 0.3977 | 0.7330 / 0.7344 | 0.6158 / 0.5857 | 0.5726 |
