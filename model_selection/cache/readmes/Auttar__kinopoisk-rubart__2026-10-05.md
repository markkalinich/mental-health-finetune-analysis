---
language: ru
license: mit
tags:
- summarization
- bart
- russian
- sentiment-analysis
pipeline_tag: summarization
---

# ruBART for Kinopoisk Review Summarization

## Описание
Модель для генеративной суммаризации отзывов на русском языке. Обучалась на датасете Kinopoisk с использованием дистилляции знаний от LLM (Qwen/Qwen2.5-1.5B-Instruct).

## Задача
Создание кратких, информативных резюме отзывов с выделением ключевых плюсов и минусов.

## Метрики на тестовой выборке

| Модель | ROUGE-1 | ROUGE-2 | ROUGE-L | BERTScore | SBERT Sim |
|--------|---------|---------|---------|-----------|-----------|
| Baseline (TF-IDF) | 0.0331 | 0.0029 | 0.0291 | 0.6233 | 0.5612 |
| **ruBART** | **0.0580** | **0.0267** | **0.0580** | **0.7442** | **0.7540** |

## Улучшение относительно Baseline

| Метрика | Улучшение |
|--------|-----------|
| ROUGE-1 | +2.5% |
| ROUGE-2 | +2.4% |
| ROUGE-L | +2.9% |
| BERTScore | +12.1% |
| SBERT Sim | +19.3% |

## Использование

```python
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

model = AutoModelForSeq2SeqLM.from_pretrained("Auttar/kinopoisk-rubart")
tokenizer = AutoTokenizer.from_pretrained("Auttar/kinopoisk-rubart")

def summarize(review):
    input_text = f"summarize: {review}"
    inputs = tokenizer(input_text, return_tensors="pt", max_length=512, truncation=True)
    outputs = model.generate(inputs.input_ids, max_length=128, num_beams=4)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

# Пример
review = "Фильм просто бомба! Актеры играют отлично, сюжет держит в напряжении."
print(summarize(review))

`````

# Обучение
Базовая модель: sn4kebyt3/ru-bart-large

Датасет: Auttar/KinopoiskReviewsSummarization (18,405 пар)

Эпохи: 3

Learning rate: 3e-5

Batch size: 4

Оптимизатор: AdamW

# Ссылки
Датасет: https://huggingface.co/datasets/Auttar/KinopoiskReviewsSummarization

Модель: https://huggingface.co/Auttar/kinopoisk-rubart
