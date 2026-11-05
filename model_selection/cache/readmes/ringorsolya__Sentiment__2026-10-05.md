---
language:
  - hu
license: cc-by-nc-4.0
tags:
  - sentiment-analysis
  - xlm-roberta
  - hungarian
  - text-classification
datasets:
  - custom
metrics:
  - accuracy
  - f1
pipeline_tag: text-classification
---

# Sentiment

Fine-tuned [xlm-roberta-base](https://huggingface.co/xlm-roberta-base) for **Hungarian sentiment classification**.

## Model Details

- **Base model**: `xlm-roberta-base`
- **Task**: 3-class sentiment classification (negative / neutral / positive)
- **Language**: Hungarian
- **Training data**: ~37K sentences (stratified split from ~46K total)
- **Class weighting**: Balanced weights applied during training to handle class imbalance

## Labels

| Label ID | Label | Description |
|----------|-------|-------------|
| 0 | negative | Negative sentiment |
| 1 | neutral | Neutral sentiment |
| 2 | positive | Positive sentiment |

## Overall Results

| Metric | Value |
|--------|-------|
| Accuracy | 0.8442320225939605 |
| F1 (macro) | 0.8387464047460437 |
| F1 (weighted) | 0.8435908941071462 |

## Per-Language Results

| Language | Samples | Accuracy | F1 (macro) | F1 (weighted) |
|----------|---------|----------|------------|---------------|
| hun | 4603 | 0.8442 | 0.8387 | 0.8436 |


## Usage

```python
from transformers import pipeline

classifier = pipeline("text-classification", model="ringorsolya/Sentiment")

classifier("Ez egy fantasztikus nap!")
# [{'label': 'positive', 'score': 0.95}]

classifier("Szörnyű volt a kiszolgálás.")
# [{'label': 'negative', 'score': 0.92}]
```

## Training Details

- **Epochs**: 5
- **Batch size**: 32
- **Learning rate**: 2e-05
- **Weight decay**: 0.01
- **Warmup ratio**: 0.1
- **Max sequence length**: 128
- **FP16**: True
- **Class weights**: [0.8114, 1.1219, 1.1413]
