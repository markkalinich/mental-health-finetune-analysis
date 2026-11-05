---
language: ko
license: apache-2.0
tags:
  - text-classification
  - emotion-classification
  - korean
  - bert
metrics:
  - accuracy
  - f1
pipeline_tag: text-classification
---

# KoBERT Emotion Classification - Korean Emotion Classification

한국어 감정 분류 모델 (6가지 감정)

## Model Description

이 모델은 AI Hub의 공감형 대화 데이터셋을 사용하여 파인튜닝된 한국어 감정 분류 모델입니다.

- **Base Model**: monologg/kobert
- **Task**: 6-class emotion classification
- **Language**: Korean
- **Dataset**: AI Hub 공감형 대화 (Empathetic Dialogue)

## Labels

| Label | Emotion | English |
|-------|---------|----------|
| 0 | 기쁨 | Joy |
| 1 | 슬픔 | Sadness |
| 2 | 분노 | Anger |
| 3 | 불안 | Anxiety |
| 4 | 당황 | Embarrassment |
| 5 | 상처 | Hurt |

## Training Data

- **Dataset**: AI Hub 공감형 대화 (Empathetic Dialogue)
- **Train samples**: 22,758
- **Validation samples**: 1,591
- **Test samples**: 1,591

## Performance

| Metric | Score |
|--------|-------|
| Accuracy | 98.49% |
| F1 Score (weighted) | 98.49% |

## Usage

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

model_name = "jeongyoonhuh/kobert-emotion-6class"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

text = "오늘 정말 기분이 좋아요!"
inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=256)

with torch.no_grad():
    outputs = model(**inputs)
    prediction = torch.argmax(outputs.logits, dim=1).item()

emotions = ['기쁨', '슬픔', '분노', '불안', '당황', '상처']
print(f"Predicted emotion: {emotions[prediction]}")
```

## Training Hyperparameters

- Learning rate: 2e-5
- Batch size: 16
- Epochs: 5
- Weight decay: 0.01
- Warmup steps: 500
- Max sequence length: 256
