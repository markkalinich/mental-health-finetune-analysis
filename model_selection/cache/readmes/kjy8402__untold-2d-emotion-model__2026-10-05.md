---
license: mit
base_model: intfloat/multilingual-e5-large-instruct
tags:
- emotion-analysis
- korean
- sentiment-analysis
- russell-model
- valence-arousal
language:
- ko
pipeline_tag: text-classification
---

# UnTold 2D Emotion Analysis Model

이 모델은 Russell의 감정 모델을 기반으로 한 2차원 감정 분석 모델입니다.

## 모델 설명
- **Base Model**: intfloat/multilingual-e5-large-instruct
- **Task**: 2차원 감정 회귀 (Valence-Arousal)
- **Dataset**: KOTE (Korean Online That Emotion)
- **Languages**: 한국어

## 사용법

```python
from transformers import AutoTokenizer, AutoModel
import torch

# 모델과 토크나이저 로드
tokenizer = AutoTokenizer.from_pretrained("kjy8402/untold-2d-emotion-model")
base_model = AutoModel.from_pretrained("intfloat/multilingual-e5-large-instruct")

# EmotionRegressor 클래스 정의 필요 (GitHub 참조)
# model = EmotionRegressor(base_model)
# model.load_state_dict(torch.load("model.safetensors"))

# 감정 분석
text = "오늘 정말 기분이 좋아요!"
# result = analyze_sentiment(text)
# {"valence": 0.25, "arousal": 0.34, "emotion_label": "excited"}
```

## 감정 레이블
- excited (흥분), pleasant (즐거움), calm (평온)
- angry (분노), unpleasant (불쾌), sad (슬픔)  
- tense (긴장), relaxed (이완), neutral (중립)

## 출력 형식
```json
{
  "valence": float,      // -1(부정) ~ 1(긍정)
  "arousal": float,      // -1(낮은 각성) ~ 1(높은 각성)
  "emotion_label": str,  // Russell 모델 기반 감정 레이블
  "confidence": float    // 예측 신뢰도
}
```

## GitHub Repository
전체 코드: [UnTold Repository](https://github.com/0nsetofspring/UnTold)
