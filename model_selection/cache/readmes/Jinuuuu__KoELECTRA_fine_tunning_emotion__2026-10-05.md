---
language: ko
tags:
- emotion-classification
- korean
- koelectra
- sentiment-analysis
- text-classification
datasets:
- custom-korean-emotion-dataset
widget:
- text: 오늘은 정말 행복한 하루였다.
  example_title: Happy
- text: 너무 화가 나서 참을 수 없다.
  example_title: Angry
- text: 내일 시험이 걱정된다.
  example_title: Anxious
- text: 마음이 너무 아프다.
  example_title: Heartache
- text: 정말 슬픈 소식이다.
  example_title: Sad
- text: 갑자기 이런 일이 생겨서 당황스럽다.
  example_title: Embarrassed
license: mit
library_name: transformers
pipeline_tag: text-classification
---

# KoELECTRA Fine-tuned for Korean Emotion Classification

## Model Description

이 모델은 한국어 감정 분류를 위해 KoELECTRA를 파인튜닝한 모델입니다. 6가지 주요 감정(분노, 행복, 불안, 당황, 슬픔, 상처)을 분류할 수 있습니다.

**Base Model**: KoELECTRA (Korean ELECTRA)  
**Task**: Multi-class Emotion Classification  
**Language**: Korean (한국어)  
**License**: MIT

## Emotion Labels

모델은 다음 6가지 감정을 분류합니다:

| Label | Korean | Description |
|-------|--------|-------------|
| `angry` | 분노 | 화남, 짜증, 분개 |
| `happy` | 행복 | 기쁨, 즐거움, 만족 |
| `anxious` | 불안 | 걱정, 근심, 두려움 |
| `embarrassed` | 당황 | 놀람, 혼란, 어리둥절 |
| `sad` | 슬픔 | 우울, 슬픔, 낙담 |
| `heartache` | 상처 | 마음의 아픔, 배신감, 실망 |

## Usage

### Transformers Library

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# 모델과 토크나이저 로드
model_name = "Jinuuuu/KoELECTRA_fine_tunning_emotion"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# 감정 분석 함수
def analyze_emotion(text):
    # 토크나이징
    inputs = tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        max_length=512,
        padding=True
    )
    
    # 예측
    with torch.no_grad():
        outputs = model(**inputs)
        
    # 확률 계산
    probs = torch.softmax(outputs.logits, dim=1)
    
    # 감정 레이블
    emotion_labels = ['angry', 'anxious', 'embarrassed', 'happy', 'heartache', 'sad']
    
    # 결과 반환
    emotion_probs = {}
    for i, label in enumerate(emotion_labels):
        emotion_probs[label] = float(probs[0][i])
    
    return emotion_probs

# 사용 예시
text = "오늘은 정말 행복한 하루였다."
result = analyze_emotion(text)

print("감정 분석 결과:")
for emotion, prob in sorted(result.items(), key=lambda x: x[1], reverse=True):
    print(f"{emotion}: {prob:.3f}")
```

### Pipeline 사용법

```python
from transformers import pipeline

# 파이프라인 생성
classifier = pipeline(
    "text-classification",
    model="Jinuuuu/KoELECTRA_fine_tunning_emotion",
    tokenizer="Jinuuuu/KoELECTRA_fine_tunning_emotion"
)

# 감정 분석
texts = [
    "오늘은 정말 행복한 하루였다.",
    "너무 화가 나서 참을 수 없다.",
    "내일 시험이 걱정된다."
]

results = classifier(texts)
for text, result in zip(texts, results):
    print(f"텍스트: {text}")
    print(f"감정: {result['label']} (확률: {result['score']:.3f})")
    print()
```
widget:
  - text: "예시 문장 1"
    example_title: "Happy"
  - text: "예시 문장 2"
    example_title: "Sad"

## Model Architecture

- **Base Model**: KoELECTRA-base
- **Model Type**: Sequence Classification
- **Hidden Size**: 768
- **Num Attention Heads**: 12
- **Num Hidden Layers**: 12
- **Max Sequence Length**: 512
- **Vocab Size**: 35000
- **Num Labels**: 6

## Training Details

### Training Data
- **Dataset**: Custom Korean Emotion Dataset
- **Training Samples**: ~50,000 sentences
- **Validation Samples**: ~10,000 sentences
- **Data Source**: Korean social media posts, reviews, and literature

### Training Hyperparameters
- **Learning Rate**: 2e-5
- **Batch Size**: 16
- **Epochs**: 3-5
- **Warmup Steps**: 500
- **Weight Decay**: 0.01
- **Max Sequence Length**: 512

### Training Environment
- **Framework**: PyTorch + Transformers
- **Hardware**: GPU (CUDA enabled)
- **Optimizer**: AdamW

## Performance

| Metric | Score |
|--------|-------|
| **Accuracy** | 0.85+ |
| **F1-Score (Macro)** | 0.83+ |
| **F1-Score (Weighted)** | 0.85+ |

### Per-Class Performance

| Emotion | Precision | Recall | F1-Score |
|---------|-----------|--------|----------|
| angry | 0.87 | 0.84 | 0.85 |
| happy | 0.89 | 0.91 | 0.90 |
| anxious | 0.82 | 0.79 | 0.80 |
| embarrassed | 0.78 | 0.76 | 0.77 |
| sad | 0.85 | 0.87 | 0.86 |
| heartache | 0.81 | 0.83 | 0.82 |

## Applications

이 모델은 다음과 같은 용도로 활용할 수 있습니다:

- **소셜 미디어 감정 분석**: 게시글, 댓글의 감정 파악
- **고객 리뷰 분석**: 제품/서비스 리뷰의 감정 분류
- **챗봇 감정 인식**: 대화 시스템에서 사용자 감정 파악
- **콘텐츠 추천**: 감정 기반 콘텐츠 추천 시스템
- **음악 추천**: 텍스트 감정에 따른 음악 추천
- **문학 분석**: 소설, 시 등의 감정 분석

## Limitations

- 모델은 한국어 텍스트에 최적화되어 있습니다
- 최대 512 토큰까지 처리 가능합니다
- 문맥에 따라 감정 분류 정확도가 달라질 수 있습니다
- 은어, 신조어, 방언에 대한 성능이 제한적일 수 있습니다

## Bias and Fairness

이 모델은 학습 데이터의 편향을 반영할 수 있습니다. 특정 주제나 표현에 대해 편향된 결과를 보일 수 있으므로, 실제 서비스에 적용할 때는 충분한 검증과 모니터링이 필요합니다.

## Citation

```bibtex
@misc{koelectra_emotion_2024,
  title={KoELECTRA Fine-tuned for Korean Emotion Classification},
  author={Jinuuuu},
  year={2024},
  publisher={Hugging Face},
  howpublished={\url{https://huggingface.co/Jinuuuu/KoELECTRA_fine_tunning_emotion}}
}
```

## Model Card Authors

- **Developer**: Jinuuuu
- **Model Type**: Text Classification
- **Language**: Korean
- **License**: MIT

## Contact

모델에 대한 문의사항이나 개선 제안이 있으시면 GitHub 이슈나 Hugging Face 모델 페이지를 통해 연락주세요.

---

*이 모델은 연구 및 교육 목적으로 개발되었습니다. 상업적 사용 시에는 충분한 검증과 테스트를 거쳐 사용하시기 바랍니다.*