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
  - conversation
  - context-aware
  - kcelectra
metrics:
  - f1
  - accuracy
inference: false
model-index:
  - name: emour-emotion-kcelectra-context-v2
    results:
      - task:
          type: text-classification
          name: Emotion Classification (15 labels, context-aware)
        dataset:
          type: custom
          name: Emour couple-chat emotion test set (660 samples, private)
        metrics:
          - type: f1
            name: macro-F1
            value: 0.5065
          - type: accuracy
            name: Accuracy
            value: 0.539
---

# emour-emotion-kcelectra-context-v2

**한국어 커플 대화 감정 분류 모델 (15종) — 문장 하나가 아니라 직전 대화 맥락과 함께 판단합니다.**

`"됐어"` `"괜찮아"` 같은 말은 앞선 흐름에 따라 감정이 완전히 달라집니다. 이 모델은 **직전 대화(최대 10발화)와 대상 문장을 문장쌍으로 함께 인코딩**해 그 차이를 구분합니다.

커플 메신저 서비스 **Emour**(2026.07~08)에서 실제로 서빙한 모델이고, **베타 테스트 사용자 291명의 실제 대화 로그로 재학습**한 최종 버전입니다.

---

## ⚠️ 사용법 — 문장쌍으로 넣어야 합니다

이 모델은 `tokenizer(context, target)` 형태의 **문장쌍(text pair)으로 학습**됐습니다.
`"맥락 [SEP] 대상"` 처럼 **한 개의 문자열로 넣으면 `token_type_ids`가 달라져 결과가 부정확**합니다.

```python
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

MODEL = "chlgks/emour-emotion-kcelectra-context-v2"
tok = AutoTokenizer.from_pretrained(MODEL)
model = AutoModelForSequenceClassification.from_pretrained(MODEL).eval()

# 맥락은 "화자: 발화" 를 줄바꿈으로 이어 붙입니다 (학습 때와 동일한 형식)
context = "A: 오늘 약속 취소됐어\nB: 왜? 무슨 일 있어?\nA: 그냥 좀 그렇게 됐어"
target  = "됐어"

enc = tok(context, target, truncation="longest_first", max_length=128, return_tensors="pt")
with torch.no_grad():
    pred = model(**enc).logits.argmax(-1).item()

print(model.config.id2label[pred])   # 예: 서운함
```

`pipeline` 을 쓴다면 딕셔너리로 문장쌍을 넘깁니다.

```python
from transformers import pipeline

clf = pipeline("text-classification", model=MODEL)
clf({"text": context, "text_pair": target})
```

맥락 없이 대상 문장만 넣어도 동작하지만, **이 모델의 이점이 사라집니다.** 그럴 때는 단문 모델([`chlgks/emour-emotion-kcelectra`](https://huggingface.co/chlgks/emour-emotion-kcelectra))을 쓰는 편이 맞습니다.

> 🔕 **추론 위젯을 꺼 두었습니다.** HuggingFace의 text-classification 위젯은 입력창이 하나뿐이라 **문장쌍을 넣을 수 없습니다.**
> 위젯을 켜두면 맥락 없이 한 문장만 들어가, 이 모델을 **잘못된 방식으로 써 본 결과**가 대표 예시처럼 보이게 됩니다.
> 위 코드로 직접 실행해 보시는 편이 정확합니다.

### 입력 규칙 요약

| 항목 | 값 |
|---|---|
| 입력 형태 | `tokenizer(context, target)` → `[CLS] 맥락 [SEP] 대상 [SEP]` |
| 맥락 형식 | `"{화자}: {발화}"` 를 `\n` 으로 연결 (화자는 `A` / `B`) |
| 맥락 길이 | 최대 10발화 |
| `max_length` | 128 |
| `truncation` | `longest_first` — 길면 맥락부터 잘립니다 |
| 전처리 | 추론 전에 **띄어쓰기 교정**(kiwipiepy)을 적용했습니다. 아래 「띄어쓰기」 항목 참고 |

---

## 라벨 체계 (15종)

일반적인 감정 분류에 **'관계 신호' 축을 추가로 설계**했습니다. 커플 대화에서는 감정의 긍부정보다 *상대에게 무엇을 전하려는 발화인지*가 더 중요한 경우가 많기 때문입니다.

| id | 라벨 | 분류 | 정의 |
|---:|---|---|---|
| 0 | 기쁨 | 긍정 | 좋은 일에 대한 즐거움·기분 좋음 |
| 1 | 설렘 | 긍정 | 애정·기대·두근거림 |
| 2 | 편안 | 긍정 | 긴장이 풀린 안정감·안심 |
| 3 | 걱정 | 중립 | 아직 안 일어난 일에 대한 불안·염려 |
| 4 | 놀람 | 중립 | 예상 밖 사건에 대한 즉각 반응 |
| 5 | 평범 | 중립 | 감정 신호 없음 (호응·단순 정보) |
| 6 | 부끄러움 | 중립 | 창피함·수줍음·민망함 |
| 7 | 궁금 | 중립 | 알고 싶음·질문·확인 |
| 8 | 슬픔 | 부정 | 상실·우울·정서적 아픔 |
| 9 | 화남 | 부정 | 분노·짜증·불만 |
| 10 | 당황 | 부정 | 어이없음·기막힘 |
| 11 | 힘듦 | 부정 | 지침·피곤·소진 |
| 12 | 고마움 | **관계 신호** | 감사 표현 |
| 13 | 미안함 | **관계 신호** | 사과 표현 |
| 14 | 서운함 | **관계 신호** | 섭섭함·소외감 |

---

## 학습 데이터

**공개 말뭉치로는 커플 채팅 도메인 성능이 나오지 않아 직접 구축했습니다.** 총 **3,648건**입니다.

| 종류 | 개수 | 설명 |
|---|---:|---|
| 실데이터 | 2,640 | 사람이 직접 라벨링한 실제 대화 |
| ㄴ 실유저 (배포 DB) | 2,193 | 베타 테스트 사용자 291명의 실제 대화 → **3인 교차 라벨링** |
| ㄴ 롤플레이 | 447 | 팀 롤플레이 (1주일차·2년차·싸움·놀람당황) |
| 합성 | 858 | 생성 후 사람이 검수 |
| 대조쌍 | 150 | 맥락 학습용 — 같은 문장, 다른 맥락 |
| **합계** | **3,648** | |

### 라벨링 단위가 이 모델의 핵심입니다

처음에는 대화를 **한 줄씩** 보고 라벨링했습니다. 그런데 실제 대화에서 감정은 앞선 흐름이 결정합니다.
**직전 10개 발화를 함께 보고 마지막 한 줄의 감정을 판단**하는 방식으로 바꾼 것이 전환점이었습니다 — 모델 구조가 아니라 **라벨 단계에서부터** 맥락을 반영한 것입니다.

### 대조쌍 — 키워드 암기를 막습니다

감정 단어가 문장에 직접 있으면(예: `"짜증나"`) 모델이 맥락을 보지 않고 그 키워드만으로 판단하는 **지름길 학습(shortcut)** 이 생깁니다. 맥락을 넣어도 모델이 무시하면 구조 변경이 무의미합니다.

그래서 **같은 문장이 앞선 맥락에 따라 다른 감정을 갖는 쌍 150건**을 만들었습니다. 문장만으로는 두 샘플을 구분할 수 없으므로 **맥락을 봐야만 손실이 줄어듭니다.** 대조쌍은 학습 전용이고 평가에는 넣지 않았습니다.

---

## 학습 설정

| 항목 | 값 |
|---|---|
| Base | [`beomi/KcELECTRA-base`](https://huggingface.co/beomi/KcELECTRA-base) |
| 초기화 | **warm-start** — 단문 모델 [`chlgks/emour-emotion-kcelectra`](https://huggingface.co/chlgks/emour-emotion-kcelectra) 에서 이어 학습 |
| Epochs / LR / Batch | 8 / 2e-5 / 16 |
| Weight decay / Warmup | 0.0 / 0.0 — 희소 감정 보존에 유리했습니다 |
| Max length | 128 |
| 손실 | 클래스 불균형 가중 손실 |
| 모델 선택 | valid macro-F1 기준 best epoch |
| 대조쌍 가중 | ×2 복제 |

> **띄어쓰기 증강은 끄고 정규화로 해결했습니다.** `기분나빠`(붙여 쓴 표기)가 오분류되는 원인은 subword 토크나이저였습니다. 증강을 시도했지만 **학습에 없는 다른 붙임 표기는 여전히 못 잡았습니다** — 증강은 본 것만 커버합니다. 그래서 **추론 전 띄어쓰기 교정(kiwipiepy)** 으로 입력을 정규화하는 쪽을 택했고, 재학습 없이 서버 코드 변경만으로 해결됐습니다.

---

## 성능

실데이터 test **660건** 기준입니다.

| 지표 | 값 |
|---|---|
| **macro-F1** | **0.5065** |
| accuracy | 0.539 |
| weighted F1 | 0.548 |

### 라벨별

| 라벨 | precision | recall | f1 | support |
|---|---:|---:|---:|---:|
| 평범 | 0.763 | 0.628 | 0.689 | 261 |
| 화남 | 0.514 | 0.545 | 0.529 | 66 |
| 궁금 | 0.588 | 0.517 | 0.550 | 58 |
| 당황 | 0.340 | 0.383 | 0.360 | 47 |
| 편안 | 0.294 | 0.263 | 0.278 | 38 |
| 기쁨 | 0.317 | 0.541 | 0.400 | 37 |
| 놀람 | 0.361 | 0.542 | 0.433 | 24 |
| 설렘 | 0.360 | 0.375 | 0.367 | 24 |
| 서운함 | 0.304 | 0.304 | 0.304 | 23 |
| 슬픔 | 0.526 | 0.455 | 0.488 | 22 |
| 힘듦 | 0.448 | 0.650 | 0.531 | 20 |
| 걱정 | 0.500 | 0.500 | 0.500 | 16 |
| 미안함 | 0.733 | 0.733 | 0.733 | 15 |
| 부끄러움 | 0.500 | 0.600 | 0.545 | 5 |
| 고마움 | 0.800 | 1.000 | 0.889 | 4 |

> 15종 다중분류에서 랜덤 추측의 macro-F1은 약 0.067입니다.

### 평가 데이터 누수를 0으로 만들었습니다

모델을 비교하는 과정에서 **평가셋 오염으로 점수가 뒤집히는 현상**을 발견했습니다. 우리가 만든 데이터가 test에 섞이면 새 모델이 자동으로 유리해집니다.

- test/valid는 **실데이터만** 사용하고, 합성·대조쌍은 **학습 전용으로 격리**했습니다.
- 비교 기준을 **우리 데이터를 전혀 학습하지 않은 단문 배포 모델**로 고정했습니다.

그 누수 없는 기준 위에서 측정한 **맥락 모델의 개선폭은 macro-F1 0.175 → 0.39 (2.2배)** 였고, 기존에 아예 못 잡던 감정(당황 0.00→0.50, 슬픔 0.00→0.40, 놀람 0.00→0.22)이 복구됐습니다.

---

## 모델 계보

| 모델 | 단계 | 학습 데이터 | test macro-F1 |
|---|---|---|---|
| [`emour-emotion-kcelectra`](https://huggingface.co/chlgks/emour-emotion-kcelectra) | 단문 | AI Hub 감성대화 말뭉치 → 15라벨 변환 + 합성 | — |
| [`emour-emotion-kcelectra-context`](https://huggingface.co/chlgks/emour-emotion-kcelectra-context) | 맥락 | + 팀 롤플레이 · 대조쌍 | 0.387 (n=111) |
| **`emour-emotion-kcelectra-context-v2`** ← 이 모델 | 맥락 + 실사용 | **+ 실사용자 대화 2,193건** | **0.5065 (n=660)** |

> ⚠️ **두 맥락 모델의 점수는 서로 다른 test 분할에서 측정한 것이라 직접 비교할 수 없습니다.**
> v2의 test는 실사용자 데이터가 들어와 **6배 커졌고(111 → 660)** 분포도 달라졌습니다.
> 「0.387 → 0.5065 로 올랐다」는 주장은 이 수치만으로는 성립하지 않습니다.

**공개 데이터 → 직접 만든 데이터 → 실사용 데이터** 순으로 옮겨간 것이 이 모델의 흐름입니다. 각 단계에서 성능이 올라갔고, 그 이유는 매번 **학습 데이터의 분포가 실제 사용 환경에 가까워졌기** 때문입니다.

---

## 한계와 주의사항

- **도메인이 좁습니다.** 커플 간 1:1 채팅체를 전제로 학습했습니다. 뉴스·리뷰·업무 대화 등 다른 도메인에서는 성능을 보장할 수 없습니다.
- **`편안`·`서운함`·`당황`의 F1이 낮습니다**(0.28~0.36). 사람도 라벨이 갈리는 구간이고, 교차 라벨링에서도 이견이 많았던 감정들입니다.
- **`평범`의 support가 전체의 40%**(261/660)입니다. 실제 대화 분포를 그대로 반영한 것이지만, macro-F1이 소수 라벨에 민감하다는 점을 감안해 읽어야 합니다.
- **문장쌍으로 넣지 않으면 정확도가 떨어집니다.** 위 「사용법」 참고.
- **감정 판단을 자동화하는 도구로만 쓰십시오.** 사람의 심리 상태를 진단하거나 관계를 평가하는 용도로 쓰기에 적합하지 않습니다.
- **학습 데이터에는 동의를 받은 베타 테스터의 대화가 포함**됩니다. 원본 대화 데이터는 공개하지 않으며, 이 저장소에는 학습된 가중치만 있습니다.

---

## 서비스에서의 사용

Emour 백엔드(Spring Boot)는 미분석 메시지를 직전 맥락과 함께 AI 서버(FastAPI)로 보내고, 결과를 저장한 뒤 WebSocket으로 푸시했습니다.

```jsonc
// POST /analyze
{
  "context": [{"speaker": "A", "text": "오늘 약속 취소됐어"}],   // 최대 10개
  "target":  [{"message_id": 101, "speaker": "B", "text": "됐어"}]
}
// → 응답 개수는 항상 target 개수와 일치
{"101": {"emotion": "서운함"}}
```

**스키마와 15라벨을 계약으로 고정**해, 모델 교체를 환경변수 수정 + 재시작만으로 처리했습니다. 덕분에 베타 테스트 중에도 무중단 롤백이 가능했습니다.

🔗 [GitHub — chlgks2/Emour](https://github.com/chlgks2/Emour)

## 라이선스

MIT. base 모델 [`beomi/KcELECTRA-base`](https://huggingface.co/beomi/KcELECTRA-base)(MIT)를 따릅니다.
