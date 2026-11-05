---
language: en
license: apache-2.0
tags:
  - text-classification
  - sentiment-analysis
  - qwen2
  - lora
  - fine-tuned
datasets:
  - google-research-datasets/go_emotions
metrics:
  - accuracy
  - f1
  - precision
  - recall
pipeline_tag: text-classification
---

# Qwen2.5-1.5B Comment Classifier

Fine-tuned **Qwen/Qwen2.5-1.5B** for 4-class comment sentiment classification.

## Classes
| Label | Description |
|-------|-------------|
| positive | Admiration, joy, love, gratitude, etc. |
| negative | Anger, disgust, sadness, fear, etc. |
| neutral | Neutral statements |
| ambiguous | Surprise, confusion, curiosity, realization |

## Training Details
- **Base model:** Qwen/Qwen2.5-1.5B
- **Method:** LoRA (r=16, alpha=32)
- **Dataset:** GoEmotions (58k+ comments)
- **Epochs:** 3

## Usage
```python
from transformers import pipeline

classifier = pipeline("text-classification", model="jovincia/qwen25-comment-classifier")
result = classifier("This product is amazing!")
print(result)
```

## Performance Metrics
See the `results/` folder for detailed evaluation and monitoring reports.
