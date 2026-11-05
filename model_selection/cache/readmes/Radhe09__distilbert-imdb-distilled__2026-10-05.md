---
language: en
license: apache-2.0
tags:
- text-classification
- sentiment-analysis
- distilbert
- knowledge-distillation
- imdb
datasets:
- imdb
metrics:
- accuracy
---

# DistilBERT — IMDB Sentiment (Knowledge Distillation)

## Model Description
This is a **DistilBERT** model fine-tuned on IMDB sentiment analysis
using **Knowledge Distillation** from a BERT teacher model.

## Teacher Model
👉 [Sachin-Rathore-1234/bert-imdb-sentiment](https://huggingface.co/Sachin-Rathore-1234/bert-imdb-sentiment)

## Distillation Details
| Setting      | Value        |
|--------------|--------------|
| Teacher      | BERT-base    |
| Student      | DistilBERT   |
| Temperature  | 4.0          |
| Alpha        | 0.7          |
| Epochs       | 3            |
| Dataset      | IMDB (3000)  |

## Results vs Teacher
| Metric            | Teacher (BERT) | Student (DistilBERT) |
|-------------------|----------------|----------------------|
| Accuracy          | ~91%           | ~89%                 |
| Parameters        | 110M           | 66M                  |
| Size Reduction    | -              | 40% smaller          |
| Speed Improvement | -              | 1.6x faster          |

## Usage
```python
from transformers import pipeline

classifier = pipeline(
    'sentiment-analysis',
    model='Sachin-Rathore-1234/distilbert-imdb-distilled'
)

result = classifier("This movie was absolutely amazing!")
print(result)
# [{'label': 'POSITIVE', 'score': 0.98}]
```

## Labels
- LABEL_0 → Negative
- LABEL_1 → Positive
