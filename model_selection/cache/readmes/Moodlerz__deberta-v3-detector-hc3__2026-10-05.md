---
language: en
tags:
  - text-classification
  - ai-text-detection
  - pytorch
license: mit
---

# Moodlerz/deberta-v3-detector-hc3

## What is this?
This model was fine-tuned as part of a research project comparing transformer-based 
AI-text detectors across two benchmark datasets: **HC3** and **ELI5**.

The task is binary classification:
- **Label 0** → Human-written text  
- **Label 1** → LLM-generated text  

## Model details
DeBERTa-v3-base (microsoft/deberta-v3-base) fine-tuned on HC3 for AI-text detection. Binary classifier: human (0) vs LLM-generated (1). Trained in full fp32 (bf16/fp16 disabled due to disentangled attention gradient issues). No intermediate checkpointing — final in-memory weights used directly.

## Training setup
| Setting | Value |
|---|---|
| Epochs | 1 |
| Batch size (train) | 16 |
| Learning rate | 2e-5 |
| Warmup steps | 500 |
| Weight decay | 0.01 |
| Dropout | 0.2 |
| Max seq length | 512 |
| Validation split | 10% |
| Best model metric | ROC-AUC |

## Datasets
- **HC3** — Human ChatGPT Comparison Corpus  
- **ELI5** — Explain Like I'm 5 (Reddit QA dataset)  
Cross-dataset evaluation (e.g. trained on HC3, tested on ELI5) was used to 
measure generalisability of each detector.

## How to load
```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

model = AutoModelForSequenceClassification.from_pretrained("Moodlerz/deberta-v3-detector-hc3")
tokenizer = AutoTokenizer.from_pretrained("Moodlerz/deberta-v3-detector-hc3")

text = "Your input text here"
inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=512)
with torch.no_grad():
    logits = model(**inputs).logits
prob_llm = torch.softmax(logits, dim=-1)[0][1].item()
print(f"P(LLM-generated): {prob_llm:.4f}")
```

## Notes
- Local training dir: `./models/DeBERTa_hc3`  
- All models in this series are private repos under `Moodlerz`.  
- Part of a larger study — do not use for production content moderation without further evaluation.
