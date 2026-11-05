---
language:
- ru
license: apache-2.0
library_name: transformers
pipeline_tag: text-classification
base_model: cointegrated/rubert-tiny2
datasets:
- billerjully/ru-absa-restaurant-reviews
tags:
- sentiment-analysis
- restaurant-reviews
- russian
- absa
widget:
- text: "Вчера были с женой в этом ресторане, всё очень понравилось! Кухня на высоте, официанты вежливые и внимательные."
  example_title: "Позитивный отзыв"
- text: "Ужасное место. Ждали заказ полтора часа, еда пришла холодной, официант хамил, а цены завышены."
  example_title: "Негативный отзыв"
- text: "Обычное кафе рядом с офисом. Заходили на бизнес-ланч, всё стандартно, ничего особенного."
  example_title: "Нейтральный отзыв"
---

# BERT-absa-rest-reviews-asc

Document-level sentiment classifier for **Russian restaurant reviews**. Given the full text of
a review, it predicts the overall sentiment: **Positive**, **Negative**, or **Neutral**.

This is a fine-tune of [cointegrated/rubert-tiny2](https://huggingface.co/cointegrated/rubert-tiny2)
(a compact Russian BERT, 29M parameters) for sequence classification. It complements the aspect
extraction model [billerjully/BERT-absa-rest-reviews-ate](https://huggingface.co/billerjully/BERT-absa-rest-reviews-ate):
together they answer "what is the review about" and "how does the reviewer feel overall".

## Usage

```python
from transformers import pipeline

asc = pipeline(
    "text-classification",
    model="billerjully/BERT-absa-rest-reviews-asc",
    top_k=None,  # return probabilities for all three classes
)

text = "Ужасное место. Еда пришла холодной, официант хамил, цены завышены."
print(asc(text)[0])
```

```
[{'label': 'Positive', 'score': 0.71},
 {'label': 'Negative', 'score': 0.15},
 {'label': 'Neutral', 'score': 0.14}]
```

## Training data

Trained on [billerjully/ru-absa-restaurant-reviews](https://huggingface.co/datasets/billerjully/ru-absa-restaurant-reviews) —
7,253 Russian restaurant reviews:

| Label | Count | Share |
|---|---|---|
| Positive | 6,163 | 85.0% |
| Negative | 591 | 8.1% |
| Neutral | 499 | 6.9% |

<!-- TODO: add evaluation metrics (macro-F1 on a held-out balanced test split) -->

## Limitations

- Document-level only; no aspect-level sentiment.
- Domain-specific (restaurant reviews) and Russian language only.

## Related

- Aspect extraction model: [billerjully/BERT-absa-rest-reviews-ate](https://huggingface.co/billerjully/BERT-absa-rest-reviews-ate)
- Dataset: [billerjully/ru-absa-restaurant-reviews](https://huggingface.co/datasets/billerjully/ru-absa-restaurant-reviews)
- Base model: [cointegrated/rubert-tiny2](https://huggingface.co/cointegrated/rubert-tiny2)
