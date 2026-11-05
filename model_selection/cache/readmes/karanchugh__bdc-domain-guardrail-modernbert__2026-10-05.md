---
license: apache-2.0
language:
- en
tags:
- text-classification
- modernbert
- automotive
- guardrail
- domain-classification
pipeline_tag: text-classification
widget:
- text: "Can I schedule an oil change for tomorrow?"
  example_title: "Service Request (ALLOW)"
- text: "What's your favorite movie?"
  example_title: "Off-topic (BLOCK)"
- text: "Hello, I need help with my car"
  example_title: "Greeting + Service (ALLOW)"
---

# BDC Domain Guardrail - ModernBERT

Binary classifier for automotive service domain relevance. Determines if user messages are relevant to BDC (Business Development Center) conversations.

## Labels
- **BLOCK (0)**: Message is off-topic, not related to automotive service
- **ALLOW (1)**: Message is relevant to automotive service, scheduling, or conversational

## Training Details
- **Base Model**: answerdotai/ModernBERT-base
- **Method**: LoRA fine-tuning (r=32, alpha=64) with guardrail-optimized loss
- **Training Data**: ~14,600 samples with confidence-weighted soft labels
- **Optimization**: Asymmetric penalty for false blocks (1.5x weight)
- **Class Weights**: None (natural distribution)

## Performance (Threshold: 0.35)
| Metric | Value |
|--------|-------|
| Accuracy | 91.9% |
| Macro F1 | 0.907 |
| ALLOW Precision | 89.1% |
| ALLOW Recall | 98.6% |
| **False Blocks** | **1.4%** (20/1397) |
| BLOCK Precision | 0.839 |
| BLOCK Recall | 0.910 |

**Recommended threshold: 0.35** (optimized for minimal false blocks while maintaining high ALLOW recall)

## Usage

### ONNX (Recommended for Production)
```python
import onnxruntime as ort
import numpy as np
from transformers import AutoTokenizer
from huggingface_hub import hf_hub_download

# Download unquantized ONNX model
onnx_path = hf_hub_download("karanchugh/bdc-domain-guardrail-modernbert", "onnx/model.onnx")
tokenizer = AutoTokenizer.from_pretrained("karanchugh/bdc-domain-guardrail-modernbert")

# Create session
session = ort.InferenceSession(onnx_path, providers=['CPUExecutionProvider'])

# Inference with optimal threshold
text = "Can I schedule an oil change?"
inputs = tokenizer(text, return_tensors="np", truncation=True, max_length=256, padding="max_length")
outputs = session.run(None, {
    "input_ids": inputs["input_ids"].astype(np.int64),
    "attention_mask": inputs["attention_mask"].astype(np.int64),
})

logits = outputs[0][0]
probs = np.exp(logits) / np.exp(logits).sum()
allow_prob = probs[1]

# Use threshold=0.35 for optimal guardrail performance
prediction = "ALLOW" if allow_prob > 0.35 else "BLOCK"
print(f"{prediction}: {allow_prob:.3f}")
```

### PyTorch
```python
from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch

model = AutoModelForSequenceClassification.from_pretrained("karanchugh/bdc-domain-guardrail-modernbert")
tokenizer = AutoTokenizer.from_pretrained("karanchugh/bdc-domain-guardrail-modernbert")

text = "Can I schedule an oil change?"
inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=256)

with torch.no_grad():
    outputs = model(**inputs)
    probs = torch.softmax(outputs.logits, dim=-1)
    allow_prob = probs[0][1].item()
    
# Use threshold=0.35 for optimal guardrail performance
prediction = "ALLOW" if allow_prob > 0.35 else "BLOCK"
print(f"{prediction}: {allow_prob:.3f}")
```

## Files
- `model.safetensors`: Full merged PyTorch model
- `onnx/model.onnx`: **Unquantized ONNX model (571 MB) - recommended for production**
- `tokenizer.json`: Fast tokenizer

## Important: Decision Threshold

**Do NOT use default threshold of 0.5!**

The model is optimized for **threshold=0.35** which provides:
- 98.6% ALLOW recall (catches 98.6% of valid customer messages)
- Only 1.4% false blocks (minimal impact on customer experience)
- 89.1% ALLOW precision (acceptable false allow rate)

Using threshold=0.5 will result in 7.7% false blocks (108 blocked valid messages).

## Deployment Configuration

```bash
GUARDRAIL_USE_DOMAIN_MODEL=true
GUARDRAIL_RELEVANCE_THRESHOLD=0.35  # Critical: use 0.35, not 0.5!
```

## Model Size & Latency
- **Model size**: 571 MB (unquantized for best accuracy)
- **CPU inference**: ~100-130ms per sample
- **Recommended**: Use batching for better throughput

**Note**: Quantized version (254 MB) showed 6% accuracy degradation and is not recommended.

## Training Improvements
This model was trained with:
- ✅ No inverse frequency weighting (prevents over-blocking)
- ✅ Asymmetric loss penalty (1.5x weight on false blocks)
- ✅ Threshold optimization (0.35 vs default 0.5)

Result: **81% reduction in false blocks** compared to baseline (from 7.7% to 1.4%).
