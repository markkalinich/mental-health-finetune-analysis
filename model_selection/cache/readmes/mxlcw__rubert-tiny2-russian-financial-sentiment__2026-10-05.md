---
license: mit
language:
- ru
pipeline_tag: text-classification
tags:
- sentiment-analysis
- multi-class-classification
- financial
- telegram
- rubert
- sentiment
- bert
- tiny
- russian
- multiclass
- classification
- Text Classification

widget:
  - text: >-
      Сбер зафиксировал рост прибыли на 40% в декабре. Если банк сохранит эту
      динамику, то бумаги могут легко превзойти текущий таргет — 12%.
      Это довольно консервативный таргет, который бумаги могут легко превзойти,
      если Сбер покажет прибыль выше уровня 2021 года. В этом году Сбер может
      возобновить дивиденды, что может дать дополнительный импульс бумагам банка.
    example_title: Positive
  - text: >-
      Сегодня в еженедельной рубрике «Газпромбанк.Мнение» рассказываем о
      ситуации в алмазодобывающий отрасли и об акциях Алросы.
      Как инвесторам реагировать на мощное восстановление спроса на рынке алмазов
      за последний год и остался ли потенциал для роста акций
      у российской ювелирной компании?
    example_title: Neutral
  - text: >-
      На фоне санкций и дефицита госбюджета РФ компания Северсталь может 
      потерять доступ к европейским рынкам. Причина — избыток сырья,
      из-за чего цены реализации могли снизиться, а также риск повышения
      налоговой нагрузки на фоне дефицита госбюджета РФ — все это создает
      неопределенность относительно результатов в 2023 году.
    example_title: Negative
---

This is [seara/rubert-tiny2-russian-sentiment](https://huggingface.co/seara/rubert-tiny2-russian-sentiment) model fine-tuned for __sentiment classification__ of short __Russian__ financial posts from Telegram channels.

---

The task is a __multi-class classification__ with the following labels:

```yaml
0: neutral
1: positive
2: negative
```
## Usage

```python
from transformers import pipeline
model = pipeline(model="mxlcw/rubert-tiny2-russian-economic-sentiment")
model("""На фоне санкций и дефицита госбюджета РФ компания Северсталь может 
      потерять доступ к европейским рынкам. Причина — избыток сырья,
      из-за чего цены реализации могли снизиться, а также риск повышения
      налоговой нагрузки на фоне дефицита госбюджета РФ — все это создает
      неопределенность относительно результатов в 2023 году.""")
#[{'label': 'negative', 'score': 0.9207897186279297}]
```

## Dataset

This model was trained on the following dataset:
- Telegram Financial Sentiment (ru)

An overview of the training data can be found [here](https://www.kaggle.com/datasets/mikezz11/telegram-financial-sentiment-ru).