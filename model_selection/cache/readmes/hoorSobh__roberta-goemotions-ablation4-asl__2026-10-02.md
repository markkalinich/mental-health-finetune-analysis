---
language: en
license: mit
tags:
  - text-classification
  - emotion-detection
  - multi-label-classification
  - goemotions
  - roberta
datasets:
  - go_emotions
metrics:
  - f1
---

# RoBERTa-base Fine-tuned on GoEmotions — Ablation 4 (Clipped ASL)

This model is part of an undergraduate thesis:
**"LLM-Based Emotion-Aware Adaptive Learning Assistant"**

## Model Description

RoBERTa-base fine-tuned on the GoEmotions dataset (Demszky et al., ACL 2020)
for 28-class multi-label emotion classification, using Clipped Asymmetric Loss.

This is Ablation 4 in a six-ablation study. The final classifier (Ablation 6,
with LLRD + cosine annealing) is hosted separately.

## Training Details

| Parameter | Value |
|---|---|
| Base model | roberta-base |
| Dataset | GoEmotions (43,410 train / 5,426 val / 5,427 test) |
| Loss function | Clipped Asymmetric Loss (γ_pos=1, γ_neg=3, clip=0.04) |
| Learning rate | 2e-5 |
| Batch size | 32 |
| Best epoch | 3 |
| Threshold | 0.5 |

## Test Set Results (GoEmotions, threshold=0.5)

| Metric | Value |
|---|---|
| Macro-F1 | 0.5335 |
| Micro-F1 | 0.5912 |
| Precision | 0.5101 |
| Recall | 0.5752 |
| Zero-F1 classes | 0 |
| Grief F1 | 0.5333 |

## Usage

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

LABELS = [
    "admiration", "amusement", "anger", "annoyance", "approval",
    "caring", "confusion", "curiosity", "desire", "disappointment",
    "disapproval", "disgust", "embarrassment", "excitement", "fear",
    "gratitude", "grief", "joy", "love", "nervousness",
    "optimism", "pride", "realization", "relief", "remorse",
    "sadness", "surprise", "neutral"
]

tokenizer = AutoTokenizer.from_pretrained("hoorSobh/roberta-goemotions-ablation4-asl")
model = AutoModelForSequenceClassification.from_pretrained(
    "hoorSobh/roberta-goemotions-ablation4-asl",
    num_labels=28,
    problem_type="multi_label_classification"
)
model.eval()

text = "I finally understood how recursion works — this is so satisfying!"
inputs = tokenizer(text, return_tensors="pt", max_length=128, truncation=True)
with torch.no_grad():
    logits = model(**inputs).logits
probs = torch.sigmoid(logits).squeeze()
top1 = LABELS[probs.argmax().item()]
print(f"Dominant emotion: {top1}")
```

## Citation

If you use this model, please cite:

- Demszky et al. (2020). GoEmotions. ACL 2020.
- Ramakrishnan & Dhinesh Babu (2025). IEEE Access. DOI: 10.1109/ACCESS.2025.3557091