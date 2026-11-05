---
language:
  - ko
license: cc-by-sa-4.0
library_name: transformers
pipeline_tag: token-classification
tags:
  - korean
  - pii
  - ner
  - token-classification
  - privacy
  - de-identification
base_model: klue/roberta-base
datasets:
  - seongyeon1/ko-pii-ner-100k
metrics:
  - f1
  - precision
  - recall
widget:
  - text: "홍길동 고객님, 주민등록번호 900101-1234567 확인되었습니다. 환불 계좌 110-123-456789로 입금됩니다."
  - text: "접수번호 20260831-001234 건은 담당 부서로 이관되었습니다. 문의는 1588-1588입니다."
---

# ko-pii-ner-roberta-base

한국어 개인정보(PII) 탐지용 토큰 분류 모델입니다.
한국 고유 식별자(주민등록번호·외국인등록번호·여권번호·운전면허번호)와
**조사 결합 경계**를 정면으로 다루도록 학습했습니다.

- 베이스: [`klue/roberta-base`](https://huggingface.co/klue/roberta-base)
- 데이터: [`seongyeon1/ko-pii-ner-100k`](https://huggingface.co/datasets/seongyeon1/ko-pii-ner-100k)
- 라벨: 20종 3티어 / BIO 41 클래스

## 성능

**인용해야 할 숫자는 F5 0.9344입니다.** KDPII가 공식 지정한 test split
2,006건으로, 학습·검증 어디에도 들어가지 않은 실제 한국어 발화입니다.

| 홀드아웃 (`test_kdpii`, 미학습) | n | P | R | F1 | F5 |
|---|---:|---:|---:|---:|---:|
| **전체** | 2,006 | 0.9119 | 0.9354 | 0.9235 | **0.9344** |
| KDPII 대화 | 458 | 0.9055 | 0.9340 | 0.9195 | 0.9328 |
| KDPII 단문 | 1,548 | 0.9183 | 0.9368 | 0.9275 | 0.9360 |

F5는 recall에 25배 가중한 F-beta입니다. PII 탐지에서는 미탐이 오탐보다
훨씬 치명적이라 이 지표를 주 지표로 씁니다.

### 내부 test 전체 수치를 인용하지 마세요

| 내부 test (`test.jsonl`) | n | F1 | F5 |
|---|---:|---:|---:|
| 합성 (조합형 + 템플릿형) | 5,378 | **0.9994** | 0.9994 |
| ai4privacy 현지화 | 2,100 | 0.9961 | 0.9976 |
| KDPII 단문 (실제 발화) | 1,417 | 0.9264 | 0.9352 |
| KDPII 대화 (실제 발화) | 413 | 0.9032 | 0.9268 |
| 전체 | 9,888 | 0.9921 | 0.9937 |

전체 F5 0.9937은 test의 54%를 차지하는 합성 구간(F1 0.9994)이 만든 값입니다.
**합성 구간과 실제 발화 사이에 0.07의 격차**가 있고, 이는 베이스 모델을
KoELECTRA로 바꿔도 동일하게(오히려 0.098로 더 크게) 재현됩니다.
합성 데이터로 학습한 PII 모델을 자기 분포에서 평가하면 안 된다는 근거입니다.

### 베이스 모델 비교

동일 데이터·동일 하이퍼파라미터(lr 2e-5, 1 epoch, batch 32)로 학습한 결과입니다.

| | klue/roberta-base (이 모델) | koelectra-base-v3 |
|---|---:|---:|
| 라이선스 | CC-BY-SA-4.0 | Apache-2.0 |
| **홀드아웃 F5** | **0.9344** | 0.9038 |
| 내부 test F5 | 0.9937 | 0.9893 |
| 합성 구간 F5 | 0.9994 | 0.9987 |
| 최종 train loss | 0.0568 | 0.1011 |

합성 구간에서는 차이가 거의 없고 **실제 발화에서만 3포인트 벌어집니다.**
다만 ELECTRA 계열은 통상 더 높은 학습률(3e-5~5e-5)을 선호하므로,
이 격차가 KoELECTRA의 최선이라고 단정할 수는 없습니다.

### Hard negative

무-PII 문서 580건에서 **오탐 0건 / 오탐 토큰 0개**.
recall을 25배 가중하면 모델이 "숫자 뭉치는 일단 PII"로 붕괴하기 쉬운데,
학습 데이터에 hard negative(주문번호 `20260831-001234`, 대표번호 `1588-1588`,
버전 `10.0.1.5` 등)를 심어 이를 막았습니다.
KoELECTRA도 동일하게 오탐 0건입니다.

### 엔티티별 내부 test 성능

| 라벨 | 티어 | P | R | F1 | support |
|---|---:|---:|---:|---:|---:|
| `DRIVER_LICENSE_NUM` | 1 | 1.0000 | 1.0000 | 1.0000 | 342 |
| `FOREIGNER_REG_NUM` | 1 | 0.9965 | 1.0000 | 0.9982 | 282 |
| `PASSPORT_NUM` | 1 | 0.9968 | 1.0000 | 0.9984 | 310 |
| `RRN` | 1 | 1.0000 | 0.9978 | 0.9989 | 453 |
| `ACCOUNT_NUM` | 2 | 1.0000 | 0.9975 | 0.9988 | 407 |
| `ADDRESS` | 2 | 0.9912 | 0.9987 | 0.9950 | 794 |
| `BIZ_REG_NUM` | 2 | 0.9961 | 1.0000 | 0.9981 | 258 |
| `CARD_NUM` | 2 | 0.9948 | 1.0000 | 0.9974 | 385 |
| `EMAIL` | 2 | 1.0000 | 1.0000 | 1.0000 | 687 |
| `IP_ADDRESS` | 2 | 1.0000 | 1.0000 | 1.0000 | 276 |
| `PERSON_NAME` | 2 | 0.9905 | 0.9943 | 0.9924 | 1,572 |
| `PHONE_NUM` | 2 | 0.9987 | 1.0000 | 0.9993 | 741 |
| `PLATE_NUM` | 2 | 0.9966 | 0.9966 | 0.9966 | 290 |
| `URL_PERSONAL` | 2 | 1.0000 | 1.0000 | 1.0000 | 351 |
| `USER_ID` | 2 | 0.9688 | 0.9502 | 0.9594 | 261 |
| `AFFILIATION` | 3 | 0.9620 | 0.9883 | 0.9750 | 512 |
| `AGE` | 3 | 0.9942 | 0.9971 | 0.9956 | 341 |
| `DOB` | 3 | 0.9931 | 0.9931 | 0.9931 | 289 |
| `POSITION` | 3 | 0.9820 | 0.9849 | 0.9835 | 332 |
| `SENSITIVE_ATTR` | 3 | 0.9823 | 1.0000 | 0.9911 | 278 |

Tier 1 네 종은 포맷이 정형이라 F1 0.998 이상입니다.
가장 약한 라벨은 표층 패턴 없이 문맥으로만 갈리는 `USER_ID`와 `AFFILIATION`입니다.

## 라벨 체계 (20종 3티어)

**Tier 1 — 고유식별정보** (개인정보보호법 시행령 §19)
`RRN` · `FOREIGNER_REG_NUM` · `PASSPORT_NUM` · `DRIVER_LICENSE_NUM`

**Tier 2 — 직접식별자**
`PERSON_NAME` · `PHONE_NUM` · `EMAIL` · `ADDRESS` · `ACCOUNT_NUM` · `CARD_NUM` ·
`BIZ_REG_NUM` · `USER_ID` · `URL_PERSONAL` · `PLATE_NUM` · `IP_ADDRESS`

**Tier 3 — 준식별자·민감정보**
`DOB` · `AGE` · `AFFILIATION` · `POSITION` · `SENSITIVE_ATTR`

## 사용법

```python
from transformers import pipeline

ner = pipeline(
    "token-classification",
    model="seongyeon1/ko-pii-ner-roberta-base",
    aggregation_strategy="simple",
)

text = "홍길동 고객님, 주민등록번호 900101-1234567 확인되었습니다."
for ent in ner(text):
    print(ent["entity_group"], ent["word"], round(ent["score"], 3))
```

마스킹:

```python
def mask(text: str) -> str:
    spans = sorted(ner(text), key=lambda e: e["start"], reverse=True)
    for e in spans:
        text = text[: e["start"]] + f"[{e['entity_group']}]" + text[e["end"] :]
    return text

mask("김철수씨 연락처는 010-9876-5432이고 이메일은 chulsoo@naver.com입니다.")
# '[PERSON_NAME]씨 연락처는 [PHONE_NUM]이고 이메일은 [EMAIL]입니다.'
```

조사 앞에서 span이 정확히 끊기고, 주문번호·대표번호 같은 PII 유사 문자열은
탐지하지 않습니다.

## 학습 설정

| 항목 | 값 |
|---|---|
| 베이스 모델 | `klue/roberta-base` |
| 손실 | Focal loss (α=1.0, γ=2.0, O 태그 가중 0.1) |
| epochs | 1 |
| batch size | 32 |
| learning rate | 2e-5 (warmup 500 steps) |
| max_length | 256 (동적 패딩) |
| 학습 데이터 | 78,963건 (KDPII test split 제외) |
| 하드웨어 | Apple Silicon MPS |
| 학습 시간 | 42분 (31.1 samples/s) |
| 최종 train loss | 0.0568 |

## 한계

- **1 epoch·base 모델 결과입니다.** `klue/roberta-large`와 다중 epoch은 미실시입니다.
- **베이스라인 비교가 없습니다.** 규칙 기반 탐지기나 다국어 PII 모델과의 비교는
  아직 하지 않았습니다.
- **평가는 KDPII 대화체 하나뿐입니다.** 사람이 주석한 실제 업무 문서 평가셋이 없어
  법률 문서·SNS·음성 전사 등 다른 도메인 성능은 알 수 없습니다.
- 학습 데이터의 도메인은 고객상담·사내메일·의료·금융·공공민원·채용 6종입니다.
- Tier 3(준식별자)은 문맥 의존적이라 라벨 경계가 Tier 1·2보다 모호합니다.

**실무 투입 전에 대상 도메인의 실제 텍스트로 반드시 재평가하세요.**

## 라이선스와 귀속

이 모델은 **CC-BY-SA-4.0**입니다. 베이스 모델 KLUE가 CC-BY-SA-4.0이고
ShareAlike 조항이 파생물에 전파되기 때문입니다.
이 모델을 추가 학습해 배포하는 경우에도 CC-BY-SA-4.0을 유지해야 합니다.

원저작자 귀속:

- **KLUE** — *KLUE: Korean Language Understanding Evaluation*,
  [arXiv:2105.09680](https://arxiv.org/abs/2105.09680),
  [KLUE-benchmark/KLUE](https://github.com/KLUE-benchmark/KLUE). CC-BY-SA-4.0
- **KDPII** — *KDPII: A New Korean Dialogic Dataset for the Deidentification of
  Personally Identifiable Information*, IEEE Access, 2024.
  [DOI 10.5281/zenodo.10968609](https://doi.org/10.5281/zenodo.10968609). CC-BY-4.0
- **ai4privacy** — [`pii-masking-openpii-1.5m`](https://huggingface.co/datasets/ai4privacy/pii-masking-openpii-1.5m),
  Copyright (c) 2026 Ai Suisse SA. CC-BY-4.0
