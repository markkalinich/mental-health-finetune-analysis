---
library_name: transformers
language:
- ko
license: mit
base_model: beomi/KcELECTRA-base
tags:
- absa
- sentiment-analysis
- aspect-based-sentiment-analysis
- generated_from_trainer
metrics:
- accuracy
- f1
model-index:
- name: kcELECTRA-absa-none
  results: []
---


# kcELECTRA-absa-none

kcELECTRA-absa-none은  
[beomi/KcELECTRA-base](https://huggingface.co/beomi/KcELECTRA-base)를 기반으로  
[AI Hub 속성기반 감정분석 데이터](https://aihub.or.kr/aihubdata/data/view.do?dataSetSn=71603)을 활용해 학습된  
Aspect-Based Sentiment Analysis (ABSA) 모델입니다.

이 모델은 전자기기 리뷰 문장에서 특정 aspect(속성)에 대한 감정(긍정, 부정, 중립/미언급)을 분석하도록 학습되었습니다.

---

## 🧩 Model description

### 🧠 학습 목적

소비자 리뷰에는 다양한 제품 속성(aspect)이 등장하며, 문장 전체의 긍부정만으로는 충분히 세밀한 분석이 어렵습니다.  
예를 들어 다음과 같은 문장을 봅시다.

> “화면은 정말 선명하고 배터리는 오래가지만, 발열이 조금 있어요.”

- 화면: 긍정  
- 배터리: 긍정  
- 발열: 부정

이 모델은 이런 세부 감정을 구분하기 위해 설계된 Aspect 기반 감성분석(ABSA) 모델입니다.  
각 리뷰를 대상으로 사전에 정의된 전자기기 관련 aspect 목록을 기준으로 감정을 분류합니다.

---

## ⚙️ Intended uses & limitations

### ✅ Intended uses
- 전자기기 관련 리뷰의 aspect-level 감성분석  
- 제품 속성별 만족도 분석 및 인사이트 추출  
- 리뷰 요약, 브랜드 모니터링, AI 고객 응대 시스템 등과의 결합

### ⚠️ Limitations
- AI Hub 전자기기 분야 데이터에 맞춰 학습되었기 때문에,  
  다른 도메인(예: 음식, 여행 등)에서는 성능이 저하될 수 있습니다.  

---

## 🧾 Training and evaluation data

### 📊 데이터 출처
AI Hub: “속성기반 감정분석 데이터”  
(https://aihub.or.kr/aihubdata/data/view.do?dataSetSn=71603)

### 📁 학습 도메인
전자기기 분야 세부 카테고리:
- 계절가전
- 컴퓨터주변기기
- 휴대폰주변기기
- 자동차기기
- 가전
- IT기기
- 영상음향가전
- 생활미용욕실가전
- 주방가전
- 카메라·게임기·태블릿

### 🧩 사용된 주요 Aspect 목록
제품 전반: 품질, 디자인, 가격, 성능  
사용성: 조작성, 휴대성, 무게, 소음  
기능: 화면, 배터리, 발열, 충전, 연결성  
기타: 내구성, 구성품, 배송, 포장 등

---

## 🧮 Training procedure

### 🔧 Hyperparameters

learning_rate: 3e-5  
train_batch_size: 16  
eval_batch_size: 16  
seed: 42  
optimizer: AdamW (betas=(0.9, 0.999), eps=1e-8)  
lr_scheduler_type: linear  
num_epochs: 3  

---

### 🧠 Training results

|Training Loss | Epoch | Step | Validation Loss | Accuracy | F1  |
|------|-----|------|-------|---------|-------|
|0.2011 | 1.0 | 5008 | 0.2402 | 0.5967 | 0.3407 | 
|0.1394 | 2.0 | 10016 | 0.1429 | 0.7954 | 0.4230 | 
|0.1408 | 3.0 | 15024 | 0.1459 | 0.8261 | 0.4985  |

---

## 🧰 Framework versions

Transformers 4.57.1  
PyTorch 2.8.0+cu126  
Datasets 4.0.0  
Tokenizers 0.22.1  

---

## 💡 Example usage

### 1. pipeline 사용 버전

```python
from transformers import pipeline

# 1. 모델 불러오기
checkpoint = "jxchlee/kcELECTRA-absa-none"
absa_pipeline = pipeline(
    task="text-classification",
    model=checkpoint,
    tokenizer=checkpoint,
    return_all_scores=True
)


# 2. 분석 대상 리뷰
review = "화면은 선명하고 배터리도 오래가지만 발열이 조금 있어요."
aspect_list = ['가격', '기능', '내구성', '디자인', '무게', '배터리',
               '사이즈', '색상', '소비전력', '소음', '소재',
               '시간/속도', '용량', '음량/음질', '제조일/제조사',
               '제품구성', '조작성', '편의성', '품질', '화질']

# 3. 예측 수행
results = {}
for aspect in aspect_list:
    input_text = f"{aspect}: {review}"
    preds = absa_pipeline(input_text)
    label = max(preds[0], key=lambda x: x["score"])
    results[aspect] = {"label": label["label"], "score": round(label["score"], 4)}

  # 4. 결과 출력
label_map = {"LABEL_0": "부정", "LABEL_1": "중립", "LABEL_2": "긍정", "LABEL_3": "언급없음"}
print(review)
label3 = {}
for k, v in results.items():
    if v['label'] == 'LABEL_3':
      label3[k] = v
    else:
      print(f"{k:10s} → {label_map[v['label']]} ({v['score']})")
for k, v in label3.items():
  print(f"{k:10s} → {label_map[v['label']]} ({v['score']})")

```


### 2. model 사용 버전


```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# 1️⃣ 모델 로드
model_name = "jxchlee/kcELECTRA-absa-none"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# 2️⃣ 입력 리뷰 & Aspect
review = "화면은 선명하고 배터리도 오래가지만 발열이 조금 있어요."
aspect_list = ["화면", "배터리", "발열"]

# 3️⃣ 예측
for aspect in aspect_list:
    text = f"{aspect}: {review}"
    inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=400)
    with torch.no_grad():
        outputs = model(**inputs)
        probs = torch.nn.functional.softmax(outputs.logits, dim=-1)
        pred = torch.argmax(probs, dim=-1).item()

    label_map = {0: "부정", 1: "중립", 2: "긍정", 3: "언급없음"}
    print(f"[{aspect}] → {label_map[pred]} (확률={probs[0][pred]:.2f})")
```

---

## 🧩 예시 출력

```
# 1. pipeline
화면은 선명하고 배터리도 오래가지만 발열이 조금 있어요.
내구성        → 부정 (0.9229)
배터리        → 긍정 (0.9567)
화질         → 긍정 (0.5763)
가격         → 언급없음 (0.9993)
기능         → 언급없음 (0.9946)
디자인        → 언급없음 (0.998)
무게         → 언급없음 (0.9994)
사이즈        → 언급없음 (0.9991)
...

2. model
[화면] → 긍정 (확률=0.92)
[배터리] → 긍정 (확률=0.88)
[발열] → 부정 (확률=0.79)
```

---
