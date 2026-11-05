---
language: vi
license: mit
tags:
  - sentiment-analysis
  - vietnamese
  - phobert
  - text-classification
  - transformers
datasets:
  - custom-vietnamese-reviews
metrics:
  - accuracy
  - f1
model-index:
  - name: vietnamese-sentiment-phobert
    results:
      - task:
          type: text-classification
          name: Sentiment Analysis
        metrics:
          - type: accuracy
            value: 0.85
          - type: f1
            value: 0.84
---

# Vietnamese Sentiment Analysis with PhoBERT

Fine-tuned **VinAI/PhoBERT-base** for 3-class sentiment classification on Vietnamese product reviews.

## Model Description

This model classifies Vietnamese text into three sentiment categories:
- **Positive** (tích cực)
- **Neutral** (trung lập)
- **Negative** (tiêu cực)

## Training Data

- **10,000+** Vietnamese product reviews
- Balanced across 3 sentiment classes
- Preprocessed with Vietnamese word segmentation

## Performance

| Metric | Score |
|--------|-------|
| Accuracy | 85% |
| F1-Score (weighted) | 0.84 |

## Usage

```python
from transformers import pipeline

classifier = pipeline("text-classification", model="sanvo/vietnamese-sentiment-phobert")
result = classifier("Sản phẩm rất tốt, tôi rất hài lòng")
print(result)
```

## Training Details

- **Base model:** vinai/phobert-base
- **Epochs:** 5
- **Batch size:** 16
- **Learning rate:** 2e-5
- **Max length:** 256 tokens
- **Optimizer:** AdamW with linear warmup
