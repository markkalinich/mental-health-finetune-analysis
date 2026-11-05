---
language: ko
license: other
license_name: aihub-terms-of-use
license_link: https://www.aihub.or.kr/intrcn/guid/usagepolicy.do
base_model: beomi/KcELECTRA-base-v2022
pipeline_tag: text-classification
tags:
- korean
- emotion
- sentiment-analysis
- electra
- kcelectra
metrics:
- f1
- accuracy
---

# KcELECTRA Korean Emotion Classification (6 classes)
**KcELECTRA 한국어 감정 분류 (대분류 6종)**

A Korean emotion classifier fine-tuned from
[beomi/KcELECTRA-base-v2022](https://huggingface.co/beomi/KcELECTRA-base-v2022)
on the **AI-Hub Emotional Dialogue Corpus**. Given a single utterance, it predicts
one of **6 emotion classes**.

[beomi/KcELECTRA-base-v2022](https://huggingface.co/beomi/KcELECTRA-base-v2022)를
**AI허브 감성대화말뭉치**로 파인튜닝한 한국어 감정 분류 모델입니다. 입력 **발화 한 건**을
받아 **대분류 6개 감정** 중 하나로 분류합니다.

- **Input / 입력**: utterance text / 발화 텍스트
- **Output / 출력**: 6 emotions / 6개 감정 — `분노`, `기쁨`, `불안`, `당황`, `슬픔`, `상처`
- **Architecture / 구조**: standard `ElectraForSequenceClassification`

## Usage / 사용법

```python
from transformers import pipeline

clf = pipeline("text-classification", model="GGARA02/kcelectra-korean-emotion")
print(clf("요즘 너무 외롭고 아무도 내 맘을 몰라주는 것 같아"))
# → [{'label': ..., 'score': ...}]
```

For the full probability distribution over all emotions / 전체 감정별 확률이 필요하면:

```python
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

name = "GGARA02/kcelectra-korean-emotion"
tok = AutoTokenizer.from_pretrained(name)
model = AutoModelForSequenceClassification.from_pretrained(name).eval()

enc = tok("요즘 너무 외롭고 아무도 내 맘을 몰라주는 것 같아", return_tensors="pt")
with torch.no_grad():
    probs = model(**enc).logits.softmax(-1)[0]

for i, p in enumerate(probs):
    print(model.config.id2label[i], round(float(p), 4))
```

## Labels / 레이블

| id | 한국어 | English |
|----|--------|---------|
| 0 | 분노 | Anger |
| 1 | 기쁨 | Joy |
| 2 | 불안 | Anxiety |
| 3 | 당황 | Embarrassment |
| 4 | 슬픔 | Sadness |
| 5 | 상처 | Hurt |

## Performance / 성능

### AI-Hub test split (5,135 samples, utterance-only) / AI허브 감성대화말뭉치 테스트셋

Evaluated on the test split of the AI-Hub Emotional Dialogue Corpus, under the **same
conditions** (utterance-only input, 6 classes) as NIA's reference ALBERT model that was
evaluated on the same data.

AI허브 감성대화말뭉치의 테스트 분할에서, 동일 데이터로 평가된 NIA 참조 ALBERT 모델과
**동일 조건**(사용자 발화만 입력, 대분류 6개)으로 비교했습니다.

| Metric / 지표 | This model / 본 모델 | NIA reference ALBERT / NIA 참조 ALBERT |
|------|--------|---------------------------|
| Accuracy (Top-1 / EM) | **86.95%** | 67.2% |
| Macro F1 | **0.8672** | 0.809 |
| Binary F1 (confidence ≥ 0.5) | 0.9300 | — |
| Top-2 Accuracy | 93.96% | — |
| Top-3 Accuracy | 97.31% | — |

#### Per-class performance / 클래스별 성능

| Emotion / 감정 | Precision | Recall | F1 | Support |
|------|-----------|--------|-----|---------|
| 분노 (Anger) | 0.8380 | 0.8474 | 0.8427 | 806 |
| 기쁨 (Joy) | 0.9827 | 0.9795 | 0.9811 | 928 |
| 불안 (Anxiety) | 0.8531 | 0.8603 | 0.8567 | 945 |
| 당황 (Embarrassment) | 0.8733 | 0.8402 | 0.8564 | 820 |
| 슬픔 (Sadness) | 0.8234 | 0.8602 | 0.8414 | 851 |
| 상처 (Hurt) | 0.8364 | 0.8140 | 0.8250 | 785 |

## Training / 학습 정보

**Data / 데이터**
- AI-Hub [Emotional Dialogue Corpus / 감성대화말뭉치](https://www.aihub.or.kr/aihubdata/data/view.do?dataSetSn=86) (built by NIA)
- Input is the concatenation of one speaker's utterances (사람문장1~3), **utterance text only** (no metadata).
- Train 51,630 / Validation 6,641

**Hyperparameters / 하이퍼파라미터**

| | |
|---|---|
| Base model | `beomi/KcELECTRA-base-v2022` (MIT) |
| Epochs | 5 |
| Max sequence length | 128 |
| Batch size | 32 (train) / 64 (eval) |
| Optimizer | AdamW (weight decay 0.01) |
| Learning rate | 2e-5 (encoder) / 1e-4 (classifier head, 5×) |
| LR schedule | linear warmup 10% + linear decay |
| Gradient clipping | 1.0 |
| Seed | 42 |

**Architecture / 모델 구조**

| | |
|---|---|
| Type | ELECTRA (discriminator) |
| Hidden size | 768 |
| Hidden layers | 12 |
| Attention heads | 12 |
| Intermediate size | 3072 |
| Vocab size | 54,343 |
| Parameters | ~113M |

## License & Attribution / 라이선스 및 출처

- The base model KcELECTRA is under the **MIT license**.
  베이스 모델 KcELECTRA는 **MIT 라이선스**입니다.
- Training data is the **AI-Hub Emotional Dialogue Corpus**
  ([dataset page](https://www.aihub.or.kr/aihubdata/data/view.do?dataSetSn=86)),
  a work product of the National Information Society Agency (NIA).
  학습 데이터는 **AI허브 감성대화말뭉치**이며, 한국지능정보사회진흥원(NIA)의 사업 결과물입니다.
- Use of this model is subject to the
  [AI-Hub usage policy](https://www.aihub.or.kr/intrcn/guid/usagepolicy.do).
  Please review and comply with it, and credit the use of AI-Hub data when using this model.
  이 모델의 이용은 [AI허브 이용정책](https://www.aihub.or.kr/intrcn/guid/usagepolicy.do)을
  따릅니다. 정책을 확인하고 준수해 주세요. 또한 이 모델을 사용할 경우 AI허브 데이터를
  사용하였음을 출처로 명시해 주세요.

## Limitations / 한계

- Emotion is subjective and cannot be reduced to a single label; use as an auxiliary
  signal only.
  감정은 주관적이며 단일 레이블로 환원되지 않습니다. 보조 지표로만 사용하세요.
