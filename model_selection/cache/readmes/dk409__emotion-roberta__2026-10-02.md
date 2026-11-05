---
language: en
license: mit
library_name: transformers
tags:
  - emotion
  - text-classification
  - roberta
datasets:
  - dair-ai/emotion
metrics:
  - accuracy
  - f1
pipeline_tag: text-classification
---

# Emotion Text Classifier (RoBERTa)

A fine-tuned `roberta-base` model for classifying text into 6 emotions:
**sadness, joy, love, anger, fear, surprise**.

## Training Details

- **Base model:** `roberta-base`
- **Dataset:** [dair-ai/emotion](https://huggingface.co/datasets/dair-ai/emotion) (20k train / 2k val / 2k test)
- **Epochs:** 5
- **Learning rate:** 2e-5
- **Batch size:** 16
- **Weight decay:** 0.01
- **Best model selection:** accuracy on validation set
- **Mixed precision:** fp16 (trained on T4 GPU)

## Results

Update these with your actual results after training:

| Metric | Score |
|--------|-------|
| Test Accuracy | ~93% |
| Weighted F1 | ~93% |

## Usage

```python
from transformers import pipeline

classifier = pipeline("text-classification", model="dk409/emotion-roberta", top_k=None)

result = classifier("I'm so happy today!")
print(result)
# [[{{'label': 'joy', 'score': 0.98}}, {{'label': 'love', 'score': 0.01}}, ...]]
```

## Labels

| ID | Label |
|----|-------|
| 0 | sadness |
| 1 | joy |
| 2 | love |
| 3 | anger |
| 4 | fear |
| 5 | surprise |
