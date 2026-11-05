---
language: en
license: mit
tags:
  - text-classification
  - emotion-detection
  - goemotions
  - roberta
  - multi-label-classification
datasets:
  - go_emotions
metrics:
  - f1
---

# RoBERTa-base Fine-tuned on GoEmotions (28 classes)

This model is a `roberta-base` encoder fine-tuned on the [GoEmotions](https://huggingface.co/datasets/go_emotions) dataset for 28-class multi-label emotion classification.

Produced as the final classifier (Ablation 6) for a bachelor's thesis: **LLM-Based Emotion-Aware Adaptive Learning Assistant**. Serves as the emotion detection component of a CVT-grounded tutoring pipeline.

## Training Details

| Parameter | Value |
|---|---|
| Base model | `roberta-base` |
| Dataset | GoEmotions — standard train/val/test split |
| Loss | Clipped Asymmetric Loss (γ_pos=1, γ_neg=3, clip=0.04) |
| Optimizer | AdamW + Layer-wise LR Decay (decay=0.9, top_lr=2e-5) |
| Scheduler | Cosine annealing with 10% warmup |
| Batch size | 32 |
| Best epoch | 5 of 10 (early stopping patience=3) |
| Threshold | 0.5 (per-label sigmoid) |

## Test Set Results

| Metric | Score |
|---|---|
| **Macro-F1** | **0.5472** |
| Micro-F1 | 0.6119 |
| Precision (macro) | 0.5293 |
| Recall (macro) | 0.5930 |
| Zero-F1 classes | 0 |

Generalisation ratio (test / val macro-F1): 1.010

## Labels (index 0-27)

admiration, amusement, anger, annoyance, approval, caring, confusion, curiosity, desire, disappointment, disapproval, disgust, embarrassment, excitement, fear, gratitude, grief, joy, love, nervousness, optimism, pride, realization, relief, remorse, sadness, surprise, neutral

## Inference

```python
from transformers import RobertaTokenizerFast, RobertaForSequenceClassification
import torch

tokenizer = RobertaTokenizerFast.from_pretrained("hoorSobh/roberta_ablation6")
model     = RobertaForSequenceClassification.from_pretrained("hoorSobh/roberta_ablation6")
model.eval()

text   = "I do not understand this at all"
inputs = tokenizer(text, return_tensors='pt', truncation=True, max_length=128)

with torch.no_grad():
    probs = torch.sigmoid(model(**inputs).logits).squeeze()

threshold = 0.5
detected  = [model.config.id2label[i] for i, p in enumerate(probs.tolist()) if p >= threshold]
top1      = model.config.id2label[probs.argmax().item()]
print("Top-1 emotion:", top1)
print("All detected: ", detected)
```

## Citation

```
Demszky et al. (2020). GoEmotions: A Dataset of Fine-Grained Emotions. ACL 2020.
```
