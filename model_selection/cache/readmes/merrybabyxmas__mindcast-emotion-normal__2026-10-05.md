---
language: ko
license: apache-2.0
tags:
- text-classification
- korean
- emotion-classification
- sentiment-analysis
datasets:
- custom
metrics:
- accuracy
- f1
widget:
- text: "오늘 정말 기분이 좋아!"
---

# Mindcast Emotion Classifier (Normal)

## Model Description

한국어 일반 댓글에서 6가지 감정을 분류하는 모델입니다.

이 모델은 LoRA (Low-Rank Adaptation)를 사용하여 효율적으로 파인튜닝되었으며, 최종적으로 base model과 merge되어 배포되었습니다.

**Training Date**: 2025-12-15

## Performance

### Test Set Results

| Metric | Score |
|---|---|
| **Accuracy** | **0.2383** |
| **F1 Score (Macro)** | **0.1915** |
| **F1 Score (Weighted)** | **0.2708** |

### Confusion Matrix

```
[[33 34 24 30 34 21]
 [ 2  5  1  3 10  2]
 [ 1  3  2  3  3  1]
 [ 1  0  0  1  1  0]
 [ 7  8  3  2 17 12]
 [ 3  6  3  2  7 13]]
```

### Detailed Classification Report

```
              precision    recall  f1-score   support

          분노     0.7021    0.1875    0.2960       176
          슬픔     0.0893    0.2174    0.1266        23
          불안     0.0606    0.1538    0.0870        13
          상처     0.0244    0.3333    0.0455         3
          당황     0.2361    0.3469    0.2810        49
          기쁨     0.2653    0.3824    0.3133        34

   micro avg     0.2383    0.2383    0.2383       298
   macro avg     0.2296    0.2702    0.1915       298
weighted avg     0.4936    0.2383    0.2708       298

```

## Training Details

### Hyperparameters


| Hyperparameter | Value |
|---|---|
| Base Model | `klue/roberta-base` |
| Batch Size | 64 |
| Epochs | 60 |
| Learning Rate | 0.0001 |
| Warmup Ratio | 0.1 |
| Weight Decay | 0.01 |
| LoRA r | 8 |
| LoRA alpha | 16 |
| LoRA dropout | 0.05 |


### Training Data

- **Train samples**: 973 (from 1 files)
- **Valid samples**: 109
- **Test samples**: 298 (from 1 files)
- **Number of labels**: 6
- **Labels**: 분노, 슬픔, 불안, 상처, 당황, 기쁨


## Usage

### Installation

```bash
pip install transformers torch
```

### Quick Start

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline

# Load model
model_name = "merrybabyxmas/mindcast-emotion-normal"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# Create pipeline
classifier = pipeline("text-classification", model=model, tokenizer=tokenizer)

# Predict
text = "오늘 정말 행복한 하루였어요"
result = classifier(text)
print(result)

```

## Model Architecture

- **Base Model**: klue/roberta-base
- **Task**: Sequence Classification
- **Number of Labels**: N/A

## Citation

If you use this model, please cite:

```bibtex
@misc{mindcast-model,
  author = {Mindcast Team},
  title = {Mindcast Emotion Classifier (Normal)},
  year = {2025},
  publisher = {HuggingFace},
  howpublished = {\url{https://huggingface.co/merrybabyxmas/mindcast-emotion-sc-only}},
}
```

## Contact

For questions or feedback, please open an issue on the model repository.

---

*This model card was automatically generated.*
