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

# Mindcast Emotion Classifier (Sarcastic)

## Model Description

한국어 비꼬는 댓글(sarcasm)에서 6가지 감정을 분류하는 모델입니다.

이 모델은 LoRA (Low-Rank Adaptation)를 사용하여 효율적으로 파인튜닝되었으며, 최종적으로 base model과 merge되어 배포되었습니다.

**Training Date**: 2025-12-15

## Performance

### Test Set Results

| Metric | Score |
|---|---|
| **Accuracy** | **0.3140** |
| **F1 Score (Macro)** | **0.2097** |
| **F1 Score (Weighted)** | **0.3518** |

### Confusion Matrix

```
[[41 21 15  3 26 33]
 [ 5  4  1  0  6  3]
 [ 4  1  2  0  1  0]
 [ 0  0  0  0  0  0]
 [ 6  7  3  0 20 16]
 [ 3  4  2  0  6  9]]
```

### Detailed Classification Report

```
              precision    recall  f1-score   support

          분노     0.6949    0.2950    0.4141       139
          슬픔     0.1081    0.2105    0.1429        19
          불안     0.0870    0.2500    0.1290         8
          상처     0.0000    0.0000    0.0000         0
          당황     0.3390    0.3846    0.3604        52
          기쁨     0.1475    0.3750    0.2118        24

   micro avg     0.3140    0.3140    0.3140       242
   macro avg     0.2294    0.2525    0.2097       242
weighted avg     0.4980    0.3140    0.3518       242

```

## Training Details

### Hyperparameters


| Hyperparameter | Value |
|---|---|
| Base Model | `klue/roberta-base` |
| Batch Size | 64 |
| Epochs | 150 |
| Learning Rate | 0.0001 |
| Warmup Ratio | 0.1 |
| Weight Decay | 0.01 |
| LoRA r | 8 |
| LoRA alpha | 16 |
| LoRA dropout | 0.05 |


### Training Data

- **Train samples**: 446 (from 1 files)
- **Valid samples**: 50
- **Test samples**: 242 (from 1 files)
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
model_name = "merrybabyxmas/mindcast-emotion-sarcastic"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# Create pipeline
classifier = pipeline("text-classification", model=model, tokenizer=tokenizer)

# Predict (sarcastic text)
text = "아 진짜 최고다~ 오늘도 망했네"
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
  title = {Mindcast Emotion Classifier (Sarcastic)},
  year = {2025},
  publisher = {HuggingFace},
  howpublished = {\url{https://huggingface.co/merrybabyxmas/mindcast-emotion-sc-only}},
}
```

## Contact

For questions or feedback, please open an issue on the model repository.

---

*This model card was automatically generated.*
