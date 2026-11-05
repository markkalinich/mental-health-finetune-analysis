---
language: ko
license: mit
tags:
- roberta
- emotion-classification
- korean
- sentiment-analysis
- klue
datasets:
- ai-hub
metrics:
- accuracy
model-index:
- name: moodtown-emotion-model
  results:
  - task:
      type: text-classification
      name: Emotion Classification
    dataset:
      name: AI Hub 감성 대화 말뭉치
      type: ai-hub
      split: validation
    metrics:
    - type: accuracy
      value: 0.639
      name: Validation Accuracy
base_model:
- klue/roberta-base
---

# moodtown-emotion-model

한국어 감정 분류를 위한 KLUE-RoBERTa-base 기반 모델입니다.

## 모델 설명

이 모델은 **KLUE-RoBERTa-base**를 기반으로 하여 한국어 텍스트의 감정을 5가지 카테고리로 분류합니다.  
[moodtown](https://github.com/bearivh/moodtown) 프로젝트의 일부로 개발되었으며, AI Hub 감성 대화 말뭉치를 사용하여 학습되었습니다.

### 감정 라벨

모델은 다음 5가지 감정을 분류합니다.

- **기쁨** (joy)
- **당황** (embarrassment/surprise)
- **분노** (anger)
- **불안** (anxiety/fear)
- **슬픔** (sadness)

## 모델 세부사항

- **기반 모델**: `klue/roberta-base`
- **모델 타입**: `RobertaForSequenceClassification`
- **입력 길이**: 최대 128 토큰
- **학습 데이터**: AI Hub 감성 대화 말뭉치 (HS01 발화만 사용, 51,628개 샘플)
- **학습 방식**: Fine-tuning

### 데이터셋 라벨 매핑

AI Hub 원본 라벨을 5개 감정으로 매핑.

- E10~E19 → 분노
- E20~E29 → 슬픔
- E30~E39 → 불안
- E40~E59 → 당황 (상처+당황 통합)
- E60~E69 → 기쁨

## 사용 방법

### Transformers 라이브러리 사용

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# 모델 및 토크나이저 로드
model_name = "sihyeonmoon/moodtown-emotion-model"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# 텍스트 분류
text = "오늘 정말 기분이 좋아요"
inputs = tokenizer(
    text,
    return_tensors="pt",
    max_length=128,
    truncation=True,
    padding=True,
)

with torch.no_grad():
    outputs = model(**inputs)
    predictions = torch.nn.functional.softmax(outputs.logits, dim=-1)

labels = ["기쁨", "당황", "분노", "불안", "슬픔"]

predicted_label = labels[predictions.argmax().item()]
confidence = predictions.max().item()

print(f"예측 감정: {predicted_label} (신뢰도: {confidence:.2%})")

### Pipeline 사용

```python
from transformers import pipeline

classifier = pipeline(
    "text-classification",
    model="your-username/moodtown-emotion-classifier",
    tokenizer="your-username/moodtown-emotion-classifier",
    return_all_scores=True,
)

result = classifier("오늘 하루가 힘들었어요.")
print(result)
```

## 학습 정보

### 하이퍼파라미터

- **Train/Validation Split**: 90% / 10%
- **Batch Size**: 32 (gradient accumulation=2 → effective batch size=64)
- **Learning Rate**: 2e-5
- **Optimizer**: AdamW
- **Scheduler**: Cosine Annealing + Warmup
- **Epochs**: 2
- **Label Smoothing**: 0.1
- **Mixed Precision**: FP16

### 학습 환경

- **Framework**: PyTorch
- **Device**: GPU (CUDA)

---

## 평가 결과

### Validation 성능

- **Accuracy**: 63.90%
- **Loss**: 1.0781

### 한계점

- '당황' 감정이 다른 감정(불안·슬픔 등)과 혼동되는 경우가 많음  
- 데이터셋 라벨 구조상 '당황'과 '상처'의 경계가 모호함  
- 감정 표현 간의 의미적 중첩으로 인해 구조적 분류 한계 존재

---

## 제한사항

- 이 모델은 **참고용 감정 분류 모델**입니다  
- 실제 서비스나 프로덕션 환경에서는 더 높은 성능의 모델이 필요할 수 있습니다  
- AI Hub 데이터는 구어체 기반이므로, 문어체 입력에 대한 일반화 성능이 다를 수 있습니다

---

## 참고 자료

- **원본 프로젝트**: https://github.com/bearivh/moodtown  
- **기반 모델**: https://huggingface.co/klue/roberta-base  
- **데이터셋**: https://aihub.or.kr/aihubdata/data/view.do?dataSetSn=86  

---

## 라이선스

MIT License

---

## 인용

```bibtex
@misc{moodtown-emotion-model,
  title={moodtown-emotion-model: Korean Emotion Classification Model},
  author={Moon sihyeon},
  year={2025},
  publisher={Hugging Face},
  howpublished={\url{https://huggingface.co/sihyeonmoon/moodtown-emotion-model}}
}