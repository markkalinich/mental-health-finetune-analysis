---
language:
  - ko
license: mit
base_model: chlgks/emour-emotion-kcelectra
pipeline_tag: text-classification
library_name: transformers
tags:
  - korean
  - emotion-classification
  - conversation
  - context-aware
  - kcelectra
metrics:
  - f1
  - accuracy
inference: false
model-index:
  - name: emour-emotion-kcelectra-context
    results:
      - task:
          type: text-classification
          name: Emotion Classification (15 labels, context-aware)
        dataset:
          type: custom
          name: Emour couple-chat emotion test set (111 samples, private)
        metrics:
          - type: f1
            name: macro-F1
            value: 0.387
          - type: accuracy
            name: Accuracy
            value: 0.423
---

# emour-emotion-kcelectra-context

**한국어 커플 대화 감정 분류 (15종) — 맥락 인식 모델의 1차 버전.**

문장 하나가 아니라 **직전 대화와 대상 문장을 문장쌍으로 함께 인코딩**해, `"됐어"` `"괜찮아"` 처럼 흐름에 따라 의미가 달라지는 말을 구분합니다.

> 🔎 **새로 쓰신다면 [`emour-emotion-kcelectra-context-v2`](https://huggingface.co/chlgks/emour-emotion-kcelectra-context-v2) 를 쓰십시오.**
> v2는 이 모델을 배포한 뒤 얻은 **실사용자 대화 2,193건으로 재학습**한 최종 버전입니다.
> 이 저장소는 **그 이전 단계의 기록**으로 남겨둡니다.

## ⚠️ 사용법 — 문장쌍으로 넣어야 합니다

`tokenizer(context, target)` 형태의 **문장쌍(text pair)으로 학습**됐습니다.
`"맥락 [SEP] 대상"` 처럼 한 개의 문자열로 넣으면 `token_type_ids`가 달라져 결과가 부정확합니다.

```python
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

MODEL = "chlgks/emour-emotion-kcelectra-context"
tok = AutoTokenizer.from_pretrained(MODEL)
model = AutoModelForSequenceClassification.from_pretrained(MODEL).eval()

context = "A: 오늘 약속 취소됐어\nB: 왜? 무슨 일 있어?"   # "화자: 발화" 를 \n 으로 연결
target  = "됐어"

enc = tok(context, target, truncation="longest_first", max_length=128, return_tensors="pt")
with torch.no_grad():
    pred = model(**enc).logits.argmax(-1).item()
print(model.config.id2label[pred])
```

> 🔕 **추론 위젯을 꺼 두었습니다.** HuggingFace의 text-classification 위젯은 입력창이 하나뿐이라 문장쌍을 넣을 수 없어, 이 모델을 잘못 쓴 결과가 대표 예시처럼 보이게 됩니다.

## 라벨 (15종)

| 분류 | 라벨 |
|---|---|
| 긍정 | 기쁨 · 설렘 · 편안 |
| 중립 | 걱정 · 놀람 · 평범 · 부끄러움 · 궁금 |
| 부정 | 슬픔 · 화남 · 당황 · 힘듦 |
| 관계 신호 | 고마움 · 미안함 · 서운함 |

## 학습

| 항목 | 값 |
|---|---|
| Base | [`beomi/KcELECTRA-base`](https://huggingface.co/beomi/KcELECTRA-base) |
| 초기화 | **warm-start** — [`chlgks/emour-emotion-kcelectra`](https://huggingface.co/chlgks/emour-emotion-kcelectra) 에서 이어 학습 |
| 데이터 | 팀이 직접 구축한 롤플레이 대화 · 합성 · **대조쌍 150건** |
| 라벨링 단위 | **직전 10개 발화 + 마지막 1줄** |
| Max length | 128 (`truncation="longest_first"`) |

**대조쌍**은 같은 문장이 맥락에 따라 다른 감정을 갖는 쌍입니다. 문장만으로는 두 샘플을 구분할 수 없으므로 **맥락을 봐야만 손실이 줄어듭니다** — 모델이 감정 키워드만 외우는 지름길 학습을 막기 위한 장치입니다.

## 성능

실데이터 test **111건** 기준 **macro-F1 0.387**, accuracy 0.423.

누수 없는 비교 기준(우리 데이터를 전혀 학습하지 않은 단문 배포 모델) 위에서 측정한 개선폭은 **macro-F1 0.175 → 0.39 (2.2배)** 이고, 기존에 아예 못 잡던 감정(당황 0.00→0.50, 슬픔 0.00→0.40, 놀람 0.00→0.22)이 복구됐습니다.

> test/valid는 실데이터만 쓰고 합성·대조쌍은 학습 전용으로 격리해 **데이터 누수를 0으로** 만들었습니다.

## 계보

| 모델 | 단계 | test macro-F1 |
|---|---|---|
| [`emour-emotion-kcelectra`](https://huggingface.co/chlgks/emour-emotion-kcelectra) | 문장 단위 | — |
| **`-context`** ← 이 모델 | 맥락 인식 | 0.387 (n=111) |
| [`-context-v2`](https://huggingface.co/chlgks/emour-emotion-kcelectra-context-v2) | 맥락 + 실사용 재학습 · **최종** | 0.5065 (n=660) |

> ⚠️ 두 맥락 모델의 점수는 **서로 다른 test 분할**에서 측정한 것이라 직접 비교할 수 없습니다.

🔗 [GitHub — chlgks2/Emour](https://github.com/chlgks2/Emour)

## 라이선스

MIT. base 모델 [`beomi/KcELECTRA-base`](https://huggingface.co/beomi/KcELECTRA-base)(MIT)를 따릅니다.
