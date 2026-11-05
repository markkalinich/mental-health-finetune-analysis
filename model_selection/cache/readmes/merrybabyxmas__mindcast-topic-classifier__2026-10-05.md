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

# Mindcast Topic Classifier

## Model Description

한국어 텍스트의 주제를 분류하는 모델입니다.

이 모델은 LoRA (Low-Rank Adaptation)를 사용하여 효율적으로 파인튜닝되었으며, 최종적으로 base model과 merge되어 배포되었습니다.

**Training Date**: 2025-12-12

## Performance

### Test Set Results

| Metric | Score |
|---|---|
| **Accuracy** | **0.5583** |
| **F1 Score (Macro)** | **0.1024** |
| **F1 Score (Weighted)** | **0.4001** |

### Confusion Matrix

```
[[67  0  0  0  0  0  0]
 [24  0  0  0  0  0  0]
 [ 6  0  0  0  0  0  0]
 [15  0  0  0  0  0  0]
 [ 6  0  0  0  0  0  0]
 [ 1  0  0  0  0  0  0]
 [ 1  0  0  0  0  0  0]]
```

### Detailed Classification Report

```
              precision    recall  f1-score   support

          사회     0.5583    1.0000    0.7166        67
          정치     0.0000    0.0000    0.0000        24
        생활문화     0.0000    0.0000    0.0000         6
          세계     0.0000    0.0000    0.0000        15
          경제     0.0000    0.0000    0.0000         6
        IT과학     0.0000    0.0000    0.0000         1
         스포츠     0.0000    0.0000    0.0000         1

   micro avg     0.5583    0.5583    0.5583       120
   macro avg     0.0798    0.1429    0.1024       120
weighted avg     0.3117    0.5583    0.4001       120

```

## Training Details

### Hyperparameters


| Hyperparameter | Value |
|---|---|
| Base Model | `klue/roberta-base` |
| Batch Size | 64 |
| Epochs | 1 |
| Learning Rate | 0.0001 |
| Warmup Ratio | 0.1 |
| Weight Decay | 0.01 |
| LoRA r | 8 |
| LoRA alpha | 16 |
| LoRA dropout | 0.05 |


### Training Data

- **Train samples**: 970
- **Valid samples**: 108
- **Test samples**: 120
- **Number of labels**: 7
- **Labels**: 사회, 정치, 생활문화, 세계, 경제, IT과학, 스포츠


## Usage

### Installation

```bash
pip install transformers torch
```

### Quick Start

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline

# Load model
model_name = "merrybabyxmas/mindcast-topic-classifier"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# Create pipeline
classifier = pipeline("text-classification", model=model, tokenizer=tokenizer)

# Predict
text = "오늘 날씨가 정말 좋네요"
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
  title = {Mindcast Topic Classifier},
  year = {2025},
  publisher = {HuggingFace},
  howpublished = {\url{https://huggingface.co/merrybabyxmas/mindcast-emotion-sc-only}},
}
```

## Contact

For questions or feedback, please open an issue on the model repository.

---

*This model card was automatically generated.*
