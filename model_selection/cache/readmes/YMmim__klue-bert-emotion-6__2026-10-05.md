---
language: ko
license: cc-by-nc-4.0
base_model: klue/bert-base
tags:
  - text-classification
  - emotion
  - korean
pipeline_tag: text-classification
---

# KLUE-BERT 한국어 감정 분류 (6-class)

`klue/bert-base`를 AI Hub「공감형 대화」데이터로 미세조정한 한국어 감정 분류 모델입니다.

## 라벨
| id | 감정 |
|----|------|
| 0 | 기쁨 |
| 1 | 슬픔 |
| 2 | 분노 |
| 3 | 불안 |
| 4 | 당황 |
| 5 | 상처 |

## 성능 (검증 세트)
- Accuracy: **0.7375**
- F1 (macro): **0.7291**

## 학습 정보
- Base: `klue/bert-base`
- 데이터: AI Hub 공감형 대화 (화자 발화 24,250문장, 8:2 분할)
- 3 epochs, batch 8 (grad accum 2), lr 2e-5, max_length 128, fp16, RTX 3060

## 사용법
```python
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

REPO = "YMmim/klue-bert-emotion-6"
labels = ["기쁨", "슬픔", "분노", "불안", "당황", "상처"]
tok = AutoTokenizer.from_pretrained(REPO)
model = AutoModelForSequenceClassification.from_pretrained(REPO)
model.eval()

x = tok("시험 결과가 걱정돼서 잠이 안 와.", return_tensors="pt", truncation=True, max_length=128)
with torch.no_grad():
    print(labels[int(model(**x).logits.argmax())])
```

## 한계
감정 라벨이 발화 단위가 아니라 대화 단위로 부여된 데이터 특성상,
한 대화 내 모든 화자 발화에 동일 감정이 적용되어 성능 상한에 제약이 있습니다.

## 출처
AI Hub 「공감형 대화」 데이터셋 기반. 비상업적 용도로 사용하세요.
