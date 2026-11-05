---
license: mit
tags:
- emotion-classification
- distilroberta
- fine-tuned
- mental-health
datasets:
- dair-ai/emotion
metrics:
- f1
- accuracy
base_model: j-hartmann/emotion-english-distilroberta-base
language:
- en
---

# DistilRoBERTa Fine-Tuned for Emotion Classification

Fine-tuned from `j-hartmann/emotion-english-distilroberta-base` on the `dair-ai/emotion` dataset.

Part of the [Mental Health Agentic AI Platform](https://github.com/JIYA-YDV/Mental-Health-Agentic-AI-Platform).

## Performance

| Metric | Baseline | Fine-Tuned |
|--------|----------|------------|
| Macro F1 | 0.869 | **0.892** |
| Accuracy | 0.914 | **0.930** |

## Labels

- 0: sadness
- 1: joy
- 2: love
- 3: anger
- 4: fear
- 5: surprise

## Usage

```python
from transformers import pipeline
classifier = pipeline("text-classification", model="YDVJIYA/distilroberta-base-finetuned-emotion")
result = classifier("I feel hopeless and tired today")
print(result)

Training Configuration
Epochs: 3
Batch size: 32
Learning rate: 2e-5
Warmup ratio: 0.1
Weight decay: 0.01
Mixed precision (fp16)
Seed: 42

Author
Trained by Jiya Yadav as part of an end-to-end agentic AI platform.
