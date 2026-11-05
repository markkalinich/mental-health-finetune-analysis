---
language: ko
license: mit
tags:
  - korean
  - psychology
  - emotion-classification
  - counseling
  - kcelectra
metrics:
  - f1
---

# PGOS Emotion Agent — Stage 1 (대분류)

**Psychological Growth OS(PGOS)** 프로젝트의 감정 분류 모델입니다.
계층적 2단계 분류기의 **1단계 대분류** 모델입니다.

## 모델 개요

입력 텍스트를 6개 감정 대분류로 분류합니다.

| 클래스 | 포함 감정 |
|---|---|
| 분노계 | 분노, 좌절, 짜증 |
| 슬픔계 | 슬픔, 우울, 후회 |
| 불안계 | 불안, 걱정 |
| 상처계 | 상처, 억울, 질투 |
| 당황계 | 수치심, 죄책감, 당황 |
| 기쁨계 | 기쁨, 안도 |

## 성능

| 지표 | 값 |
|---|---|
| Macro F1 | **0.692** |
| Accuracy | **0.684** |

## 학습 데이터

- **원천**: AI Hub 018 감성대화 말뭉치
- **데이터**: 클래스당 균등 샘플링 + GPT-4o-mini 증강
- **총 학습 데이터**: 64,000개

## 베이스 모델

[beomi/KcELECTRA-base-v2022](https://huggingface.co/beomi/KcELECTRA-base-v2022)

## 사용 방법

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

tokenizer = AutoTokenizer.from_pretrained("nuguri01/pgos-emotion-stage1-major")
model = AutoModelForSequenceClassification.from_pretrained("nuguri01/pgos-emotion-stage1-major")

text = "오늘 너무 화가 나고 짜증이 밀려와요"
inputs = tokenizer(text, return_tensors="pt", max_length=128, truncation=True)
with torch.no_grad():
    logits = model(**inputs).logits
pred = torch.argmax(logits, dim=-1).item()
labels = ["분노계", "슬픔계", "불안계", "상처계", "당황계", "기쁨계"]
print(f"대분류: {labels[pred]}")
```

## PGOS 파이프라인
입력 텍스트
↓
Stage 1 (이 모델) → 대분류 예측
↓
Stage 2 (소분류 모델) → 세부 감정 예측
↓
Top-3 감정 반환 (Hit Rate 0.877)

## 관련 모델

- Stage 2: [pgos-emotion-stage2-anger](https://huggingface.co/nuguri01/pgos-emotion-stage2-anger)
- Stage 2: [pgos-emotion-stage2-sadness](https://huggingface.co/nuguri01/pgos-emotion-stage2-sadness)
- Stage 2: [pgos-emotion-stage2-anxiety](https://huggingface.co/nuguri01/pgos-emotion-stage2-anxiety)
- Stage 2: [pgos-emotion-stage2-hurt](https://huggingface.co/nuguri01/pgos-emotion-stage2-hurt)
- Stage 2: [pgos-emotion-stage2-embarrass](https://huggingface.co/nuguri01/pgos-emotion-stage2-embarrass)
- Stage 2: [pgos-emotion-stage2-joy](https://huggingface.co/nuguri01/pgos-emotion-stage2-joy)

## 프로젝트

- **서비스**: Psychological Growth OS (PGOS)
- **철학**: Carl Rogers 인간중심치료 + ACT Hexaflex
- **Behavior Agent**: [nuguri01/pgos-behavior-agent](https://huggingface.co/nuguri01/pgos-behavior-agent)
