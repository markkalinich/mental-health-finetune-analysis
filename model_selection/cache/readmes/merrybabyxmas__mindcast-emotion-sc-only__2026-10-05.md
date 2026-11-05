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

# Mindcast Emotion Classifier

## Model Description

한국어 텍스트에서 6가지 감정(분노, 슬픔, 불안, 상처, 당황, 기쁨)을 분류하는 모델입니다. 일반 댓글과 비꼬는 댓글(sarcasm) 모두를 학습하여 다양한 문맥에서 감정을 정확하게 인식합니다.

이 모델은 LoRA (Low-Rank Adaptation)를 사용하여 효율적으로 파인튜닝되었으며, 최종적으로 base model과 merge되어 배포되었습니다.

**Training Date**: 2025-12-15

## Performance

### Test Set Results

| Metric | Score |
|---|---|
| **Accuracy** | **0.2111** |
| **F1 Score (Macro)** | **0.1663** |
| **F1 Score (Weighted)** | **0.2473** |

### Confusion Matrix

```
[[56 68 31 66 36 58]
 [ 6 10  6 10  6  4]
 [ 2  8  2  5  4  0]
 [ 1  0  0  1  1  0]
 [13 25  5 13 16 29]
 [ 3 10  4  7  5 29]]
```

### Detailed Classification Report

```
              precision    recall  f1-score   support

          분노     0.6914    0.1778    0.2828       315
          슬픔     0.0826    0.2381    0.1227        42
          불안     0.0417    0.0952    0.0580        21
          상처     0.0098    0.3333    0.0190         3
          당황     0.2353    0.1584    0.1893       101
          기쁨     0.2417    0.5000    0.3258        58

   micro avg     0.2111    0.2111    0.2111       540
   macro avg     0.2171    0.2505    0.1663       540
weighted avg     0.4814    0.2111    0.2473       540

```

## Training Details

### Hyperparameters


| Hyperparameter | Value |
|---|---|
| Base Model | `klue/roberta-base` |
| Batch Size | 64 |
| Epochs | 50 |
| Learning Rate | 0.0001 |
| Warmup Ratio | 0.1 |
| Weight Decay | 0.01 |
| LoRA r | 8 |
| LoRA alpha | 16 |
| LoRA dropout | 0.05 |


### Training Data

- **Train samples**: 1420 (from 2 files)
- **Valid samples**: 158
- **Test samples**: 540 (from 2 files)
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
model_name = "merrybabyxmas/mindcast-emotion-sc-only"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# Create pipeline
classifier = pipeline("text-classification", model=model, tokenizer=tokenizer)

# Predict
text = "오늘 정말 기분이 좋아!"
result = classifier(text)
print(result)
# Output: [{'label': '기쁨', 'score': 0.95}]

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
  title = {Mindcast Emotion Classifier},
  year = {2025},
  publisher = {HuggingFace},
  howpublished = {\url{https://huggingface.co/merrybabyxmas/mindcast-emotion-sc-only}},
}
```

## Contact

For questions or feedback, please open an issue on the model repository.

---

*This model card was automatically generated.*
