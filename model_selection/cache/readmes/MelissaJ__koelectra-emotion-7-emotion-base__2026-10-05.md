---
language: ko
license: apache-2.0
base_model: monologg/koelectra-base-v3-discriminator
pipeline_tag: text-classification
tags:
- korean
- emotion
- emotion-classification
- koelectra
metrics:
- accuracy
- f1
widget:
- text: 오늘 드디어 합격 소식을 들었어!
  example_title: 기쁨
- text: 밤마다 미래가 걱정돼서 잠이 안 와.
  example_title: 불안
- text: 오늘 회의는 3시에 시작합니다.
  example_title: 중립
---

# koelectra-emotion-7-emotion-base

한국어 문장의 감정을 분류하는 KoELECTRA-base-v3 파인튜닝 모델입니다.
문장 1개를 입력하면 **7개 클래스** — 감정 6종(기쁨, 분노, 상처, 불안, 당황, 슬픔) + **중립**(감정 없음) — 의 확률을 출력합니다.

- Base model: [monologg/koelectra-base-v3-discriminator](https://huggingface.co/monologg/koelectra-base-v3-discriminator)
- 입력: 한국어 단문(발화 1개), max_length 128 토큰
- 라벨 매핑은 `config.json`의 `id2label`에 포함되어 있어 별도 파일이 필요 없습니다

## 사용법

```python
import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer

repo = "MelissaJ/koelectra-emotion-7-emotion-base"
tokenizer = AutoTokenizer.from_pretrained(repo)
model = AutoModelForSequenceClassification.from_pretrained(repo)
model.eval()

@torch.no_grad()
def classify_emotion(text: str) -> dict[str, float]:
    enc = tokenizer(text, truncation=True, max_length=128, return_tensors="pt")
    probs = torch.softmax(model(**enc).logits[0], dim=-1)
    result = {model.config.id2label[i]: p.item() for i, p in enumerate(probs)}
    return dict(sorted(result.items(), key=lambda x: -x[1]))

print(classify_emotion("오늘 드디어 합격 소식을 들었어!"))
# {'기쁨': 0.998, ...}
```

`pipeline`으로도 사용할 수 있습니다:

```python
from transformers import pipeline
clf = pipeline("text-classification", model=repo, top_k=None)
clf("점심 뭐 먹을까?")
```

## 학습 데이터

| 클래스 | 소스 | train / val |
|---|---|---|
| 감정 6종 | AI Hub 감성대화말뭉치 (사람문장1~3을 독립 샘플로 전개) | 144,696 / 17,910 |
| 중립 | KLUE-YNAT 뉴스 제목 | 12,000 / 1,500 |
| 중립 | 송영숙 챗봇 데이터 일상(label 0) 질문 | 4,734 / 525 |
| 중립 | KorNLI 전제문 (train: MultiNLI, val: XNLI dev+test) | 8,000 / 1,000 |

총 train 169,430 / val 20,935 문장. 클래스 불균형(기쁨이 적음)은 weighted cross-entropy로 보정했습니다.

**대화 스타일 증강 (v2, 2026-08)**: train/val 각 50%에 호명("○○님!", "○○아,"),
구어 감탄("아이고, 진짜!", "어휴," 등), 말줄임("...")을 **라벨 불변으로 전 클래스에
균일 주입**했습니다. v1은 중립 소스가 전부 뉴스·챗봇체라 "호명·구어 감탄 = 중립"이라는
도메인 지름길을 학습했고, 캐릭터 대화체 감정 발화("멜리사님! 정말 화가 난다!")가
중립 확률 ~1.0으로 포화되는 문제가 실측됐습니다. 균일 주입으로 스타일을 무정보
특징으로 만들어 이 지름길을 차단했습니다.

## 학습 설정

- 8 epochs, batch 32, lr 3e-5, max_length 128, fp16, seed 42
- warmup 10%, weight decay 0.01, f1_macro 기준 best model 선택 (early stopping patience 2)

## 성능 (val 20,935문장, 스타일 증강 적용 분포)

v2의 val은 스타일 증강이 적용된 분포라 v1 수치(acc 0.6790 / f1_macro 0.6744)와
직접 비교할 수 없습니다 — 사실상 새(더 어려운) 벤치마크입니다.

| 지표 | 값 |
|---|---|
| accuracy | 0.6745 |
| f1_macro | 0.6699 |
| f1_weighted | 0.6757 |

| 클래스 | precision | recall | f1 |
|---|---|---|---|
| 기쁨 | 0.8975 | 0.8610 | 0.8789 |
| 분노 | 0.6380 | 0.6045 | 0.6208 |
| 상처 | 0.5208 | 0.4969 | 0.5086 |
| 불안 | 0.5749 | 0.5952 | 0.5849 |
| 당황 | 0.5271 | 0.5979 | 0.5603 |
| 슬픔 | 0.5484 | 0.5433 | 0.5458 |
| 중립 | 0.9930 | 0.9864 | 0.9897 |

호명·감탄이 섞인 회귀 프로브(v1에서 전부 중립 ~1.0으로 포화되던 문장들)가
v2에서 올바른 감정으로 복귀함을 확인했습니다 — 예: "멜리사님! 정말 화가 난다!"
→ 분노 0.79, "...아이고, 진짜! ○○님는 나한테 맨날 일만 시키지!" → 분노 0.98.
호명이 섞인 중립("○○님, 오늘 회의는 3시에 시작합니다")은 중립으로 유지됩니다.

## 한계

- **상처/슬픔/불안 경계가 흐립니다.** 감성대화말뭉치 특성상 라벨러 간에도 갈리는 부류라 f1이 0.5 안팎입니다. 확신 임계값(최상위 확률 0.5 미만이면 판단 보류) 병행을 권장합니다.
- **반말 구어 평서문 중립**("부산까지 세 시간 걸려")은 감정(주로 기쁨)으로 오분류될 수 있습니다. 감정 학습 데이터가 대부분 반말 구어체 발화라서 생긴 편향입니다. 뉴스형 문장, 일상 질문, 경어체/문어체 평서문 중립은 잘 잡힙니다.
- 단문(발화 1개) 기준으로 학습되어, 긴 문단보다 문장 단위 입력이 학습 분포와 맞습니다.

## 감정 판단 예시

```
"오늘 드디어 합격 소식을 들었어!"      → 기쁨 0.998
"밤마다 미래가 걱정돼서 잠이 안 와."   → 불안 0.489 (2위 상처 0.300)
"오늘 회의는 3시에 시작합니다."        → 중립 1.000
"점심 뭐 먹을까?"                      → 중립 1.000
```
