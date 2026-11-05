---
language:
- ru
license: mit
library_name: transformers
pipeline_tag: text-classification
tags:
- sentiment-analysis
- russian
- rubert
- low-latency
- weighted-cross-entropy
datasets:
- MonoHime/ru_sentiment_dataset
base_model:
- cointegrated/rubert-tiny2
metrics:
- accuracy
- f1
---

# Russian Sentiment Classifier

Классификатор тональности русскоязычных пользовательских текстов.

## Classes

- `0`: Neutral
- `1`: Positive
- `2`: Negative

## Base model

`cointegrated/rubert-tiny2`

Модель была полностью дообучена для классификации текста на три класса.

## Dataset

`MonoHime/ru_sentiment_dataset`

После очистки и удаления дубликатов:

- Train: 180,853
- Validation: 9,642
- Test: 9,642

## Training

- Epochs: 3
- Maximum sequence length: 128
- Learning rate: 2e-5
- Train batch size: 64
- Weighted Cross Entropy: enabled
- Best model metric: Negative F1
- GPU: Tesla T4

Class weights:

- Neutral: 1.3124
- Positive: 0.7020
- Negative: 1.2292

## Test metrics

| Metric | Value |
|---|---:|
| Accuracy | 0.7811 |
| Macro Precision | 0.7713 |
| Macro Recall | 0.7918 |
| Macro F1 | 0.7768 |
| Neutral F1 | 0.6960 |
| Positive F1 | 0.7989 |
| Negative F1 | 0.8354 |
| Negative Recall | 0.8787 |

## Latency

End-to-end latency includes preprocessing, tokenization and inference.
Batch size is 1.

| Device | Mean | Median | P95 | Requests/sec |
|---|---:|---:|---:|---:|
| Tesla T4 GPU | 7.33 ms | 6.57 ms | 12.92 ms | 136.41 |
| Colab CPU | 13.84 ms | 13.69 ms | 16.77 ms | 72.26 |

## Usage

```python
import torch

from transformers import (
  AutoModelForSequenceClassification,
  AutoTokenizer,
)

MODEL_NAME = "Bektur756/rubert-tiny2-russian-sentiment"

tokenizer = AutoTokenizer.from_pretrained(
  MODEL_NAME
)

model = (
  AutoModelForSequenceClassification
  .from_pretrained(MODEL_NAME)
)

text = "Отличный сервис, всё понравилось."

inputs = tokenizer(
  text,
  return_tensors="pt",
  truncation=True,
  max_length=128,
)

with torch.inference_mode():
  logits = model(**inputs).logits

probabilities = torch.softmax(
  logits,
  dim=-1,
)[0]

predicted_id = int(
  probabilities.argmax()
)

print(model.config.id2label[predicted_id])
print(probabilities.tolist())
## Limitations

В исходном датасете присутствуют шумные и неоднозначные метки.
Слабее всего модель распознаёт нейтральный класс.
