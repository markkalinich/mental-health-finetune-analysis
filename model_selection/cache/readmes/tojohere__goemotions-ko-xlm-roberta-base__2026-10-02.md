---
language: ko
license: mit
tags:
  - emotion-detection
  - korean
  - xlm-roberta
  - go-emotions
  - onnx
  - sentilog
datasets:
  - google-research-datasets/go_emotions
  - searle-j/kote
metrics:
  - f1
---

# GoEmotions Korean — xlm-roberta-base (v2)

Fine-tuned [xlm-roberta-base](https://huggingface.co/FacebookAI/xlm-roberta-base) for 28-emotion classification on Korean text. Used in [SentiLog](https://play.google.com/store/apps/details?id=com.sentilog.app) for on-device journaling sentiment analysis.

## Model Details

- **Base model:** FacebookAI/xlm-roberta-base (270M params)
- **Training data:** GoEmotions (EN+KO bilingual) + KOTE (50K native Korean emotions)
- **Translation:** NLLB-200-distilled-600M for EN→KO
- **Training:** 8 epochs with early stopping (patience=2, best at epoch 6)
- **Quantization:** INT8 dynamic quantization for ONNX (266MB)

## Performance (v2)

| Metric | v1 | v2 |
|--------|-----|-----|
| F1 Macro (training) | 0.379 | **0.568** |
| 28×3 Top-1 | 67% | **68%** |
| 28×3 Top-3 | 83% | 81% |
| Sanity Checks | 8/8 | 8/8 |
| Missed Emotions | 2/28 | 2/28 |

## Labels (28 GoEmotions)

admiration, amusement, anger, annoyance, approval, caring, confusion, curiosity, desire, disappointment, disapproval, disgust, embarrassment, excitement, fear, gratitude, grief, joy, love, nervousness, optimism, pride, realization, relief, remorse, sadness, surprise, neutral

## Files

- **model.safetensors** — PyTorch checkpoint (for fine-tuning)
- **goemotions.onnx** — INT8 quantized ONNX (for inference, 266MB)
- **tokenizer.json** — Unigram tokenizer

## Usage (ONNX)

```python
import onnxruntime as ort
from tokenizers import Tokenizer

session = ort.InferenceSession("goemotions.onnx")
tokenizer = Tokenizer.from_file("tokenizer.json")

encoding = tokenizer.encode("오늘 정말 행복해요")
import numpy as np
input_ids = np.array([encoding.ids], dtype=np.int64)
attention_mask = np.array([encoding.attention_mask], dtype=np.int64)

outputs = session.run(None, {"input_ids": input_ids, "attention_mask": attention_mask})
```
