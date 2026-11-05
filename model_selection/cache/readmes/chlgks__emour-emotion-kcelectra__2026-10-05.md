---
language:
  - ko
license: mit
base_model: beomi/KcELECTRA-base
pipeline_tag: text-classification
library_name: transformers
tags:
  - korean
  - emotion-classification
  - kcelectra
metrics:
  - f1
widget:
  - text: "오늘 진짜 고마웠어"
    example_title: "고마움"
  - text: "미안해 내가 잘못했어"
    example_title: "미안함"
  - text: "너 왜 자꾸 그래 진짜 짜증나"
    example_title: "화남"
  - text: "하 오늘 너무 피곤하다"
    example_title: "힘듦"
  - text: "내일 뭐 할 거야?"
    example_title: "궁금"
---

# emour-emotion-kcelectra

**한국어 대화 감정 분류 (15종) — 문장 단위 모델.**
커플 메신저 서비스 **Emour** 의 **1차 모델**이며, 아래 두 맥락 모델의 **warm-start 시작점**입니다.

> 🔎 **새로 쓰신다면 [`emour-emotion-kcelectra-context-v2`](https://huggingface.co/chlgks/emour-emotion-kcelectra-context-v2) 를 쓰십시오.**
> 이 모델은 문장 하나만 보기 때문에 `"됐어"` `"괜찮아"` 처럼 **맥락에 따라 의미가 달라지는 말을 구분하지 못합니다.**
> 이 저장소는 **비교 기준(baseline)으로서의 가치** 때문에 남겨둡니다 — 뒤의 맥락 모델을 평가할 때
> **우리가 만든 데이터를 전혀 학습하지 않은 모델**이 필요했고, 그 역할을 이 모델이 했습니다.

## 사용법

문장 하나만 넣습니다.

```python
from transformers import pipeline

clf = pipeline("text-classification", model="chlgks/emour-emotion-kcelectra")
print(clf("오늘 진짜 고마웠어"))   # [{'label': '고마움', ...}]
```

## 라벨 (15종)

| 분류 | 라벨 |
|---|---|
| 긍정 | 기쁨 · 설렘 · 편안 |
| 중립 | 걱정 · 놀람 · 평범 · 부끄러움 · 궁금 |
| 부정 | 슬픔 · 화남 · 당황 · 힘듦 |
| 관계 신호 | 고마움 · 미안함 · 서운함 |

일반적인 감정 분류에 **'관계 신호' 축을 추가로 설계**했습니다. 커플 대화에서는 감정의 긍부정보다 *상대에게 무엇을 전하려는 발화인지*가 더 중요한 경우가 많기 때문입니다.

## 학습

| 항목 | 값 |
|---|---|
| Base | [`beomi/KcELECTRA-base`](https://huggingface.co/beomi/KcELECTRA-base) |
| 데이터 | AI Hub 감성대화 말뭉치를 15라벨로 변환 + 합성 데이터 보강 |
| 손실 | 클래스 불균형 가중 손실 |
| 모델 선택 | valid macro-F1 기준 best epoch |

## 성능 — 그리고 이 모델이 남긴 교훈

| 평가 조건 | macro-F1 |
|---|---|
| 커플 문장 gold셋 153문장 | **0.73** |
| **실제 대화 흐름에 적용** | **0.175** |

**0.73을 보고 배포했는데 실사용에서 0.175로 무너졌습니다.**

여기서 두 가지를 동시에 확인했습니다.

1. 문장 단위 모델이라 맥락을 읽지 못합니다.
2. **0.73이라는 숫자 자체가 실제 사용 환경을 전혀 반영하지 못한 지표였습니다.**

두 번째가 더 중요했습니다. **모델을 고치기 전에 평가 방식을 고쳐야 했습니다.** 이 판단에서 맥락 모델이 나왔습니다.

## 계보

| 모델 | 단계 |
|---|---|
| **`emour-emotion-kcelectra`** ← 이 모델 | 문장 단위 |
| [`-context`](https://huggingface.co/chlgks/emour-emotion-kcelectra-context) | 맥락 인식 (문장쌍) |
| [`-context-v2`](https://huggingface.co/chlgks/emour-emotion-kcelectra-context-v2) | 맥락 + **실사용자 대화 재학습 — 최종** |

🔗 [GitHub — chlgks2/Emour](https://github.com/chlgks2/Emour)

## 라이선스

MIT. base 모델 [`beomi/KcELECTRA-base`](https://huggingface.co/beomi/KcELECTRA-base)(MIT)를 따릅니다.
