---
language:
- ru
- en
license: cc-by-nc-4.0
library_name: sentence-transformers
pipeline_tag: sentence-similarity
base_model: deepvk/USER2-small
tags:
- sentence-transformers
- feature-extraction
- sentence-similarity
- retrieval
- kompas-3d
- cad
- api-search
- russian
---

<div align="center">

<img src="banner.png" alt="KOMPAS-3D GUARD" width="100%">

# KOMPAS-3D GUARD-34M

**Семантический поиск по API КОМПАС-3D**

[34M](https://huggingface.co/dwnmf/KOMPAS-3D-GUARD-34M) ·
[150M](https://huggingface.co/dwnmf/KOMPAS-3D-GUARD-150M) ·
[600M](https://huggingface.co/dwnmf/KOMPAS-3D-GUARD-600M)

</div>

---

## Что это

Модель-эмбеддер, которая превращает запрос инженера на живом языке в вектор и
находит нужный элемент API КОМПАС-3D. Спрашиваете «как получить радиус окружности» —
получаете `ICircle.Radius`. Спрашиваете «плоскость XOY» — получаете `o3d_planeXOY`.

Универсальные модели поиска на этой задаче работают плохо. API КОМПАС-3D — это
десятки тысяч близких по смыслу методов, свойств и перечислений с русскими
описаниями и английскими именами. `IView.Scale` и `IView.ScaleValue`,
`IPart7.Name` и `IPart7.FileName` — для общей модели это почти одно и то же,
а для инженера разница принципиальная.

Эта модель обучена именно на такой разметке и различает такие пары.

**KOMPAS-3D GUARD-34M** — самая быстрая в линейке. Запускается на CPU, подходит для локальной работы и больших объёмов.

## Результаты

<img src="benchmarks.png" alt="Бенчмарки KOMPAS-3D GUARD" width="100%">

Поиск по корпусу из **38 249 документов** API КОМПАС-3D на двух наборах
по 1 000 запросов каждый:

- **Semantic Route** — обычные инженерные запросы на русском и английском.
- **Hard Disambiguation** — запросы про похожие сущности, которые легко спутать.

### Метрики этой модели

| Метрика | Semantic Route | Hard Disambiguation |
|---|---:|---:|
| Recall@1 | 24,5% | 22,8% |
| Recall@3 | 53,9% | 53,1% |
| Recall@5 | 70,2% | 67,5% |
| MRR@10 | 42,9% | 40,9% |
| nDCG@10 | 52,2% | 49,9% |

`Recall@5` означает: нужный элемент API попал в первые пять результатов.

### Вся линейка

| Модель | Параметры | dim | Semantic Route<br>Recall@5 | Hard Disambiguation<br>Recall@5 |
|---|---:|---:|---:|---:|
| KOMPAS-3D GUARD V1 *(предыдущее поколение)* | 34M | 384 | 59,2% | 58,1% |
| **KOMPAS-3D GUARD-34M — эта модель** | 34,4M | 384 | **70,2%** | **67,5%** |
| [KOMPAS-3D GUARD-150M](https://huggingface.co/dwnmf/KOMPAS-3D-GUARD-150M) | 149,0M | 768 | **82,5%** | **79,5%** |
| [KOMPAS-3D GUARD-600M](https://huggingface.co/dwnmf/KOMPAS-3D-GUARD-600M) | 595,8M | 1024 | **89,1%** | **88,8%** |

Относительно предыдущего поколения **KOMPAS-3D GUARD-34M** даёт
**+11,0 п.п.** на Semantic Route и **+9,4 п.п.** на Hard Disambiguation
по Recall@5.

<img src="benchmarks_detail.png" alt="Полные метрики" width="100%">

Сырые числа — в [`benchmarks/metrics.json`](benchmarks/metrics.json).

## Быстрый старт

```bash
pip install sentence-transformers
```

```python
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("dwnmf/KOMPAS-3D-GUARD-34M")

# Запросы и документы кодируются с РАЗНЫМИ префиксами — это обязательно.
queries = model.encode(
    ["как получить радиус окружности", "сохранить деталь в файл"],
    prompt_name="search_query",
    normalize_embeddings=True,
)
documents = model.encode(
    ["ICircle.Radius — радиус окружности", "IKompasDocument.Save — сохранить документ"],
    prompt_name="search_document",
    normalize_embeddings=True,
)

scores = queries @ documents.T
print(scores)
```

Префиксы `search_query: ` и `search_document: ` применялись при обучении.
Без них качество заметно падает — это самая частая ошибка при интеграции.

> **Важно.** Корпус и запросы должны кодироваться одной и той же моделью и в одной
> точности. Если проиндексировать документы одной моделью или в другой разрядности,
> а запросы гонять через другую, векторные пространства не совпадут и качество упадёт
> сильнее, чем от любого выбора модели по отдельности.

## Какую модель выбрать

| Задача | Модель |
|---|---|
| Локальный запуск, CPU, десятки тысяч запросов | [34M](https://huggingface.co/dwnmf/KOMPAS-3D-GUARD-34M) |
| Универсальный выбор для продакшена | [150M](https://huggingface.co/dwnmf/KOMPAS-3D-GUARD-150M) |
| Максимальная точность, есть GPU | [600M](https://huggingface.co/dwnmf/KOMPAS-3D-GUARD-600M) |

## Характеристики

| | |
|---|---|
| Параметры | 34,4 млн |
| Размерность вектора | 384 |
| Максимальный контекст | 8192 токенов |
| Слоёв | 12 |
| Архитектура | ModernBERT |
| Пулинг | mean |
| Метрика близости | косинусная |
| Базовая модель | [deepvk/USER2-small](https://huggingface.co/deepvk/USER2-small) |
| Вес | 69 МБ (bfloat16) |
| Языки | русский, английский |

## Границы применимости

Модель делает одну вещь и делает её хорошо — **ищет элементы API КОМПАС-3D**.
Что важно понимать:

- это **эмбеддер, а не генератор**: он не пишет код и не отвечает текстом;
- вне домена КОМПАС-3D качество не гарантируется — для общего поиска берите
  базовые модели [deepvk/USER2](https://huggingface.co/deepvk/USER2-base) или
  [Qwen3-Embedding](https://huggingface.co/Qwen/Qwen3-Embedding-0.6B);
- модель отражает состав API на момент сборки корпуса и не знает о более
  новых методах;
- поиск возвращает кандидатов, а не гарантию: в продакшене результат стоит
  проверять компилятором и графом вызовов.

## Лицензия

**CC BY-NC 4.0 — только некоммерческое использование.**

Коммерческое использование весов, индексов и производных артефактов требует
отдельного письменного разрешения. Напишите на **hello@kompasmcp.ru** —
коммерческие лицензии выдаются.

Базовая модель [deepvk/USER2-small](https://huggingface.co/deepvk/USER2-small)
распространяется под Apache-2.0; условия апстрима сохраняются для его
компонентов. Ограничение CC BY-NC 4.0 распространяется на КОМПАС-специфичный
файнтюн и упакованные артефакты этого репозитория. Подробнее —
[`LICENSE.md`](LICENSE.md) и [`NOTICE.md`](NOTICE.md).

## Контакты

- **Почта** — hello@kompasmcp.ru
- **Telegram** — [t.me/lya_ocean](https://t.me/lya_ocean)
- **SDK** — [github.com/dwnmf/kompas-3d-guard-bin](https://github.com/dwnmf/kompas-3d-guard-bin)

<div align="center">

**Три модели. Один SDK.**

</div>
