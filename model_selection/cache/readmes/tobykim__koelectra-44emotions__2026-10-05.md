---
datasets:
- searle-j/kote
language:
- ko
metrics:
- f1
base_model:
- monologg/koelectra-base-v3-discriminator
pipeline_tag: text-classification
library_name: transformers
tags:
- multi-Label-Classification
- multi-label-dataset
- sentiment-analysis
- sentiment
- multi-label-emotion-classification
- emotion-classification
- custom
- chat-app
- messenger
providers:
- hf-inference
---
# Korean Emotion Classification (44 labels, KoELECTRA)

## 📌 개요
이 모델은 한국어 텍스트에서 **44가지 감정(emotion)** 을 분류하기 위해 학습되었습니다.  
베이스 모델은 [`monologg/koelectra-base-v3-discriminator`](https://huggingface.co/monologg/koelectra-base-v3-discriminator) 이며,  
[KOTE](https://huggingface.co/datasets/searle-j/kote) 데이터셋 + 추가 수집 데이터로 파인튜닝하였습니다.

---

## 🧾 모델 정보
- **Base Model**: KoELECTRA-base-v3-discriminator
- **Task**: Multi-label emotion classification
- **Labels**: 44개 감정
- **Loss Function**: Asymmetric Loss (γ⁻=3)
- **Threshold**: 0.6

---

## 🎯 감정 라벨 (총 44개)
불평/불만, 환영/호의, 감동/감탄, 지긋지긋, 고마움, 슬픔, 화남/분노,
존경, 기대감, 우쭐댐/무시함, 안타까움/실망, 비장함, 의심/불신, 뿌듯함,
편안/쾌적, 신기함/관심, 아껴주는, 부끄러움, 공포/무서움, 절망,
한심함, 역겨움/징그러움, 짜증, 어이없음, 없음, 패배/자기혐오,
귀찮음, 힘듦/지침, 즐거움/신남, 깨달음, 죄책감, 증오/혐오,
흐뭇함(귀여움/예쁨), 당황/난처, 경악, 부담/안_내킴,
서러움, 재미없음, 불쌍함/연민, 놀람, 행복, 불안/걱정, 기쁨, 안심/신뢰

---

## 📊 성능 (Validation 기준)
- **Micro F1**: ~0.62
- **Micro Precision**: ~0.70
- **Micro Recall**: ~0.55
- **Macro F1**: ~0.47
- **Hamming Loss**: ~0.12

---

## 🚀 사용 방법
```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import numpy as np

# 모델 로드
model_name = "tobykim/koelectra-44emotions"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# 입력 문장
text = "오늘 너무 기분 좋아!"
inputs = tokenizer(text, return_tensors="pt")

# 추론
with torch.no_grad():
    logits = model(**inputs).logits
    probs = torch.sigmoid(logits).numpy()[0]

# 감정 라벨 매핑
LABELS = [
    '불평/불만','환영/호의','감동/감탄','지긋지긋',
    '고마움','슬픔','화남/분노','존경','기대감',
    '우쭐댐/무시함','안타까움/실망','비장함',
    '의심/불신','뿌듯함','편안/쾌적','신기함/관심',
    '아껴주는','부끄러움','공포/무서움','절망',
    '한심함','역겨움/징그러움','짜증','어이없음',
    '없음','패배/자기혐오','귀찮음','힘듦/지침',
    '즐거움/신남','깨달음','죄책감','증오/혐오',
    '흐뭇함(귀여움/예쁨)','당황/난처','경악',
    '부담/안_내킴','서러움','재미없음','불쌍함/연민',
    '놀람','행복','불안/걱정','기쁨','안심/신뢰'
]
threshold = 0.5
results = [(label, float(p)) for label, p in zip(LABELS, probs) if p > threshold]
print(sorted(results, key=lambda x: x[1], reverse=True))

--

# 🏷️ 라이선스

Base model: KoELECTRA (MIT License)

Dataset: KOTE + 추가 수집 데이터 (공개 데이터 기반)

Model: 자유롭게 연구/학습 목적 사용 가능