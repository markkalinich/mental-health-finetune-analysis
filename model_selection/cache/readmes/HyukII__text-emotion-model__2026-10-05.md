---
language: ko
license: mit
tags:
  - text-classification
  - emotion
pipeline_tag: text-classification
library_name: transformers
---

# Korean Emotion Classifier

- 6개 감정: 기쁨/당황/분노/불안/상처/슬픔  
- 기반 모델: klue/bert-base

## Usage
```python
from transformers import AutoModelForSequenceClassification, AutoTokenizer
tok = AutoTokenizer.from_pretrained("HyukII/my-emotion-text")
model = AutoModelForSequenceClassification.from_pretrained("HyukII/my-emotion-text").eval()
