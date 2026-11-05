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

# Mindcast Sarcasm Detector

## Model Description

한국어 텍스트가 비꼬는 표현(sarcasm)인지 아닌지를 판별하는 이진 분류 모델입니다.

이 모델은 LoRA (Low-Rank Adaptation)를 사용하여 효율적으로 파인튜닝되었으며, 최종적으로 base model과 merge되어 배포되었습니다.

**Training Date**: 2025-12-15

## Performance

### Test Set Results

| Metric | Score |
|---|---|
| **Accuracy** | **0.6519** |
| **F1 Score (Macro)** | **0.6499** |
| **F1 Score (Weighted)** | **0.6526** |

### Confusion Matrix

```
[[196 102]
 [ 86 156]]
```

### Detailed Classification Report

```
               precision    recall  f1-score   support

Non-sarcastic     0.6950    0.6577    0.6759       298
    Sarcastic     0.6047    0.6446    0.6240       242

    micro avg     0.6519    0.6519    0.6519       540
    macro avg     0.6498    0.6512    0.6499       540
 weighted avg     0.6545    0.6519    0.6526       540

```

## Training Details

### Hyperparameters


| Hyperparameter | Value |
|---|---|
| Base Model | `klue/roberta-base` |
| Batch Size | 64 |
| Epochs | 30 |
| Learning Rate | 0.0001 |
| Warmup Ratio | 0.1 |
| Weight Decay | 0.01 |
| LoRA r | 8 |
| LoRA alpha | 16 |
| LoRA dropout | 0.05 |


### Training Data

- **Train samples**: 1428
- **Valid samples**: 159
- **Test samples**: 540
- **Number of labels**: 2
- **Labels**: Non-sarcastic, Sarcastic


## Usage

### Installation

```bash
pip install transformers torch
```

### Quick Start

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline

# Load model
model_name = "merrybabyxmas/mindcast-sarcasm-detector"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# Create pipeline
classifier = pipeline("text-classification", model=model, tokenizer=tokenizer)

# Predict
text = "아 진짜 좋네요~ 완전 최고에요~"
result = classifier(text)
print(result)
# Output: [{'label': 'Sarcastic', 'score': 0.92}]

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
  title = {Mindcast Sarcasm Detector},
  year = {2025},
  publisher = {HuggingFace},
  howpublished = {\url{https://huggingface.co/merrybabyxmas/mindcast-emotion-sc-only}},
}
```

## Contact

For questions or feedback, please open an issue on the model repository.

---

*This model card was automatically generated.*
