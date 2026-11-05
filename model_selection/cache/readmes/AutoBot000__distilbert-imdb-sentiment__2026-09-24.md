---
language: en
license: mit
library_name: transformers
tags:
- text-classification
- sentiment-analysis
- fine-tuned
datasets:
- imdb
base_model: distilbert-base-uncased
---

# DistilBERT IMDb Sentiment Analysis

DistilBERT를 IMDb 영화 리뷰 감정분석 데이터셋으로 fine-tuning한 모델입니다.

## 학습 상세

- **베이스 모델:** distilbert-base-uncased
- **데이터셋:** IMDb (train 2,000 / test 500 샘플)
- **태스크:** 이진 감정분류 (긍정/부정)
- **Epoch:** 2
- **Learning Rate:** 2e-5
- **Batch Size:** 16
- **Max Length:** 256

## 사용법
```python
from transformers import pipeline

classifier = pipeline("text-classification", model="AutoBot000/distilbert-imdb-sentiment")
result = classifier("This movie was absolutely fantastic!")
print(result)
```

## 한계

- 학습 데이터를 2,000개로 축소하여 실습 목적으로 학습함
- 전체 데이터(25K)로 학습 시 성능 향상 기대
- 영어 리뷰 전용