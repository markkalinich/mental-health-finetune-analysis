---
language:
- multilingual
tags:
- xlm-roberta
- sentiment-analysis
- text-classification
metrics:
- f1
pipeline_tag: text-classification
---

# CMPE 346 - Assignment 02: Multilingual Sentiment Classification

## Model Details
- **Base Model:** xlm-roberta-large
- **Task:** Binary sentiment classification 

## Training
- **Epochs:** 3
- **Learning Rate:** 1e-5
- **Batch Size:** 16
- **Max Length:** 512
- **Weight Decay:** 0.01
- **FP16:** True
- **GPU:** A100

## Results

| Epoch | Training Loss | Validation Loss | F1     |
|-------|--------------|-----------------|--------|
| 1     | 0.4330       | 0.2066          | 0.9244 |
| 2     | 0.3413       | 0.2147          | 0.9283 |
| 3     | 0.2684       | 0.2398          | 0.9279 |

**Final Validation F1 Score: 0.9282**
