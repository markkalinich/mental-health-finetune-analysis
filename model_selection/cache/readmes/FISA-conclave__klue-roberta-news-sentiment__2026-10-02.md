
---
language:
- ko
license: apache-2.0
tags:
- text-classification
- sentiment-analysis
- korean
- news
- finance
datasets:
- custom
metrics:
- accuracy
- f1
authors:
- tobykim
model-index:
- name: KLUE-RoBERTa News Sentiment
  results:
  - task:
      type: text-classification
      name: Sentiment Analysis
    metrics:
    - type: accuracy
      value: 0.8426
      name: Accuracy
    - type: f1
      value: 0.8468
      name: F1-Macro
---

# KLUE-RoBERTa 뉴스 기사 기업 감정분석 모델

## 모델 설명

이 모델은 **뉴스 기사 속 특정 기업에 대한 감정(호재/악재/중립)을 분석**하기 위해 fine-tuning된 KLUE-RoBERTa 모델입니다.

### 사용 목적
- 뉴스 기사에서 특정 기업에 대한 긍정/부정/중립 감정 자동 분류
- 금융 뉴스 감정 분석
- 기업 평판 모니터링

### 레이블
- `0`: negative (악재/부정) - 해당 기업에 대한 부정적 내용
- `1`: neutral (중립) - 해당 기업에 대한 중립적 내용
- `2`: positive (호재/긍정) - 해당 기업에 대한 긍정적 내용

## 성능

| Metric | Score |
|--------|-------|
| Accuracy | 0.8426 |
| F1-Macro | 0.8468 |
| F1-Weighted | 0.8422 |

## 하이퍼파라미터 (Optuna로 최적화)

```json
{
  "learning_rate": 9.78310992630157e-06,
  "num_train_epochs": 8,
  "weight_decay": 0.06436845335086991,
  "warmup_ratio": 0.10859899755289561,
  "per_device_train_batch_size": 32
}
```

## 사용 방법

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# 모델 로드
model_name = "FISA-conclave/klue-roberta-news-sentiment"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# 예측
text = "삼성전자의 3분기 실적이 시장 예상을 크게 상회했다."
inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=128)

with torch.no_grad():
    outputs = model(**inputs)
    probs = torch.softmax(outputs.logits, dim=1)[0]
    pred = torch.argmax(probs).item()

labels = {0: "negative", 1: "neutral", 2: "positive"}
print(f"예측: {labels[pred]} ({probs[pred]:.2%})")
```

## 학습 데이터

- **총 샘플 수**: 9,992개
- **출처**:
  - finance_sentiment_corpus
  - korfin-asc
  - twice_kr_fin

## 베이스 모델

- [klue/roberta-base](https://huggingface.co/klue/roberta-base)

## 인용

```bibtex
@misc{klue-roberta-news-sentiment,
  author = {Tobykim},
  title = {KLUE-RoBERTa News Sentiment Analysis},
  year = {2024},
  publisher = {HuggingFace},
  howpublished = {\url{https://huggingface.co/FISA-conclave/klue-roberta-news-sentiment}}
}
```

## 라이센스

Apache 2.0
