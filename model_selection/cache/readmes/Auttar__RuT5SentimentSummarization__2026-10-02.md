---
language: ru
license: mit
tags:
- summarization
- t5
- russian
- sentiment-analysis
pipeline_tag: summarization
---

# RuT5-Base for Sentiment Summarization

## Описание
Модель для генеративной суммаризации отзывов на русском языке. Обучалась на датасете Kinopoisk с использованием дистилляции знаний от LLM (Qwen/Qwen2.5-1.5B-Instruct).

## Задача
Создание кратких, информативных резюме отзывов с выделением ключевых плюсов и минусов.

## Метрики на тестовой выборке

| Модель | ROUGE-1 | ROUGE-2 | ROUGE-L | BERTScore | SBERT Sim |
|--------|---------|---------|---------|-----------|-----------|
| Baseline (TF-IDF) | 0.0331 | 0.0029 | 0.0291 | 0.6233 | 0.5612 |
| **ruT5-base** | **0.1497** | **0.0600** | **0.1497** | **0.7227** | **0.6786** |

## Улучшение относительно Baseline

| Метрика | Улучшение |
|--------|-----------|
| ROUGE-1 | +11.7% |
| ROUGE-2 | +5.7% |
| ROUGE-L | +12.1% |
| BERTScore | +9.9% |
| SBERT Sim | +11.7% |


## Использование

```python
from transformers import T5ForConditionalGeneration, T5Tokenizer

model = T5ForConditionalGeneration.from_pretrained("Auttar/RuT5SentimentSummarization")
tokenizer = T5Tokenizer.from_pretrained("Auttar/RuT5SentimentSummarization")

def summarize(review):
    input_text = f"summarize: {review}"
    inputs = tokenizer(input_text, return_tensors="pt", max_length=512, truncation=True)
    outputs = model.generate(inputs.input_ids, max_length=128, num_beams=4)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)


# Пример
review = "Фильм отличный! Актеры играют великолепно, сюжет захватывает."
print(summarize(review))

`````
# Обучение
Базовая модель: sberbank-ai/ruT5-base

Датасет: Kinopoisk с сгенерированными резюме

Эпохи: 3

Learning rate: 5e-5

Batch size: 4

# Ссылки
Модель: https://huggingface.co/Auttar/RuT5SentimentSummarization
