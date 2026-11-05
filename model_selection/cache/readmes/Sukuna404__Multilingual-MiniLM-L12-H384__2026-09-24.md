---
language: en
license: apache-2.0
base_model: distilbert-base-uncased
tags:
  - text-classification
  - emotion-detection
  - distilbert
  - pytorch
  - safetensors
datasets:
  - dair-ai/emotion
metrics:
  - accuracy
  - f1
---

# DistilBERT Emotion Detection — FP32

Fine-tuned version of DistilBERT for 6-class emotion classification using the [dair-ai/emotion](https://huggingface.co/datasets/dair-ai/emotion) dataset.

## Model Performance
| Format   | Accuracy | F1 Macro |
|----------|----------|----------|
| FP32     | 92.50%   | 0.8799   |
| INT8*    | 91.95%   | 0.8659   |

*INT8 is applied at runtime via `quantize_dynamic` — see usage below.

## Labels
| ID | Emotion  |
|----|----------|
| 0  | sadness  |
| 1  | joy      |
| 2  | love     |
| 3  | anger    |
| 4  | fear     |
| 5  | surprise |

## Usage (CPU — recommended)
```python
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

repo_id = "Sukuna404/distilbert-emotion-fp32"

tokenizer = AutoTokenizer.from_pretrained(repo_id)
model = AutoModelForSequenceClassification.from_pretrained(repo_id)

# Optional: apply INT8 quantization at runtime for faster CPU inference
model = torch.quantization.quantize_dynamic(
    model,
    {torch.nn.Linear},
    dtype=torch.qint8
)

model.eval()
model.cpu()

def predict(text: str) -> str:
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding="longest")
    with torch.no_grad():
        outputs = model(**inputs)
    pred_id = outputs.logits.argmax().item()
    return model.config.id2label[pred_id]

print(predict("I am so happy today!"))   # joy
print(predict("I am really angry!"))     # anger
```

## Limitations
- English only
- 6 emotion classes only
