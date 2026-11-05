---
language: ko
license: mit
library_name: transformers
tags:
- text-classification
- korean
- mental-health
- depression-detection
- bert
pipeline_tag: text-classification
---

# Korean Depression/Anxiety Detection Model

한국어 텍스트 기반 우울/불안 감지 모델입니다.

## Model Description

- **Model Type:** BERT for Sequence Classification
- **Language:** Korean (ko)
- **Task:** Binary Classification (정상 vs 우울/불안)
- **Base Model:** BERT (Korean)

## Labels

| Label | Description |
|-------|-------------|
| 0 | 정상 (Normal) |
| 1 | 우울/불안 (Depression/Anxiety) |

## Usage

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# 모델 로드
tokenizer = AutoTokenizer.from_pretrained("YOUR_USERNAME/final_depression_model")
model = AutoModelForSequenceClassification.from_pretrained("YOUR_USERNAME/final_depression_model")
model.eval()

# 예측
def predict(text):
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
    with torch.no_grad():
        outputs = model(**inputs)
        probs = torch.softmax(outputs.logits, dim=-1)
        prediction = torch.argmax(probs, dim=-1).item()
    return {
        "label": prediction,  # 0=정상, 1=우울/불안
        "confidence": probs[0][prediction].item()
    }

# 사용 예시
result = predict("요즘 너무 힘들고 아무것도 하기 싫어요")
print(result)
```

## Model Details

- **Architecture:** BertForSequenceClassification
- **Hidden Size:** 768
- **Attention Heads:** 12
- **Hidden Layers:** 12
- **Vocab Size:** 30,000
- **Max Position Embeddings:** 300

## Intended Use

이 모델은 정신건강 관련 연구 및 챗봇 서비스에서 사용자의 감정 상태를 파악하기 위한 목적으로 개발되었습니다.

## Limitations

- 이 모델은 전문적인 의료 진단 도구가 아닙니다.
- 실제 우울증/불안장애 진단은 반드시 전문 의료진과 상담하세요.
- 모델의 예측 결과는 참고용으로만 사용해야 합니다.

## License

MIT License
