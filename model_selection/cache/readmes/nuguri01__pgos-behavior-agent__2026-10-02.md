---
language: ko
license: mit
tags:
  - korean
  - psychology
  - behavior-classification
  - counseling
  - kcelectra
metrics:
  - f1
---

# PGOS Behavior Agent

**Psychological Growth OS(PGOS)** 프로젝트의 행동 패턴 분류 모델입니다.

## 모델 개요

심리상담 대화에서 내담자의 행동 패턴을 5가지로 분류합니다.

| 클래스 | 설명 | 예시 |
|---|---|---|
| 접근 (Approach) | 문제/감정을 능동적으로 탐색 | "한번 말해봤어요", "직접 물어봤어요" |
| 회피 (Avoidance) | 불편한 상황/감정을 피함 | "그냥 신경 안 써요", "어차피" |
| 위축 (Withdrawal) | 관계/활동에서 사회적 철수 | "요즘 아무도 안 만나요", "혼자 있고 싶어요" |
| 지속 (Persistence) | 비효과적 패턴을 알면서 반복 | "또 이러고 있어요", "매번 이렇게 돼요" |
| 중립 (Neutral) | 위 패턴이 뚜렷하지 않은 일반 대화 | 일상 서술, 정보 전달 |

## 성능

| 지표 | 값 |
|---|---|
| Top-1 Macro F1 | **0.754** |
| Top-2 Hit Rate | **0.899** |
| Top-3 Hit Rate | **0.985** |

### 클래스별 F1

| 클래스 | F1 |
|---|---|
| 위축 | 0.976 |
| 지속 | 0.956 |
| 중립 | 0.657 |
| 회피 | 0.617 |
| 접근 | 0.567 |

## 학습 데이터

- **원천 데이터**: AI Hub 심리상담 데이터 (우울증/불안장애/중독/일반군, 75개 회기)
- **입력 단위**: 연속 3턴 슬라이딩 윈도우
- **GPT 증강**: 위축/지속 클래스 부족분 GPT-4o-mini로 보강
- **최종 학습 데이터**: 클래스당 750개 균등 (총 3,750개)

## 베이스 모델

[beomi/KcELECTRA-base-v2022](https://huggingface.co/beomi/KcELECTRA-base-v2022)

## 학습 설정

```python
TrainingArguments(
    num_train_epochs=6,
    per_device_train_batch_size=32,
    learning_rate=2e-5,
    weight_decay=0.03,
    loss="CrossEntropy"  # 하드 라벨
)
```

## 사용 방법

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

model_name = "nuguri01/pgos-behavior-agent"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# 입력: 3턴 대화 (슬라이딩 윈도우)
text = "[내담자] 요즘 친구들 연락이 와도 답장을 안 하게 돼요. | [상담사] 어떤 마음인 것 같아요? | [내담자] 그냥 혼자 있고 싶어요."

inputs = tokenizer(text, return_tensors="pt", max_length=256, truncation=True)
with torch.no_grad():
    logits = model(**inputs).logits

probs = torch.softmax(logits, dim=-1)
labels = ["접근", "회피", "위축", "지속", "중립"]
top1_idx = probs.argmax().item()
top2_idx = probs.topk(2).indices[0][1].item()

print(f"주패턴: {labels[top1_idx]} ({probs[0][top1_idx]:.3f})")
print(f"보조패턴: {labels[top2_idx]} ({probs[0][top2_idx]:.3f})")

# 복합 패턴 플래그 (보조패턴 25% 이상)
if probs[0][top2_idx] >= 0.25:
    print(f"복합 패턴: {labels[top1_idx]}+{labels[top2_idx]}")
```

## PGOS 아키텍처에서의 역할

  사용자 발화 → Behavior Agent (이 모델)

{
"primary_behavior": "위축",
"primary_score": 0.87,
"secondary_behavior": "회피",
"secondary_score": 0.09,
"is_complex": false
}

→ Coordinator → 대화 전략 결정

## 프로젝트

- **서비스**: Psychological Growth OS (PGOS)
- **철학**: Carl Rogers 인간중심치료 + ACT Hexaflex
- **Emotion Agent**: [nuguri01/pgos-emotion-stage1-major](https://huggingface.co/nuguri01/pgos-emotion-stage1-major)
