---
language: ru
license: mit
tags:
- summarization
- pegasus
- russian
- sentiment-analysis
pipeline_tag: summarization
---

# ruPEGASUS for Kinopoisk Review Summarization

## Описание
Модель для генеративной суммаризации отзывов на русском языке. Обучалась на датасете Kinopoisk с использованием дистилляции знаний от LLM (Qwen/Qwen2.5-1.5B-Instruct).

## Задача
Создание кратких, информативных резюме отзывов с выделением ключевых плюсов и минусов.

## Метрики на тестовой выборке

| Модель | ROUGE-1 | ROUGE-2 | ROUGE-L | BERTScore | SBERT Sim |
|--------|---------|---------|---------|-----------|-----------|
| Baseline (TF-IDF) | 0.0331 | 0.0029 | 0.0291 | 0.6233 | 0.5612 |
| **ruPEGASUS** | **0.1323** | **0.0483** | **0.1323** | **0.5890** | **0.2032** |

## Улучшение относительно Baseline

| Метрика | Улучшение |
|--------|-----------|
| ROUGE-1 | +9.9% |
| ROUGE-2 | +4.5% |
| ROUGE-L | +10.3% |
| BERTScore | +-3.4% |
| SBERT Sim | +-35.8% |

## Использование

```python
from transformers import PegasusForConditionalGeneration, PegasusTokenizer

model = PegasusForConditionalGeneration.from_pretrained("Auttar/kinopoisk-pegasus")
tokenizer = PegasusTokenizer.from_pretrained("Auttar/kinopoisk-pegasus")

def summarize(review):
    # PEGASUS не требует специального префикса
    inputs = tokenizer(review, return_tensors="pt", max_length=512, truncation=True)
    outputs = model.generate(inputs.input_ids, max_length=128, num_beams=4)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

# Пример
review = "Фильм просто бомба! Актеры играют отлично, сюжет держит в напряжении."
print(summarize(review))
`````

# Обучение
Базовая модель: google/pegasus-x-base

Датасет: Auttar/KinopoiskReviewsSummarization (18,405 пар)

Эпохи: 3

Learning rate: 3e-5

Batch size: 2 (с gradient accumulation 4 → эффективный batch 8)

Оптимизатор: AdamW

FP16: Да
# Ссылки
Датасет: https://huggingface.co/datasets/Auttar/KinopoiskReviewsSummarization

Модель: https://huggingface.co/Auttar/kinopoisk-pegasus
