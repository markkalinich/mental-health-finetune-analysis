---
license: mit
tags:
- mental-health
- nlp
- text-classification
- domain-adversarial
- dann
- mentalbert
- gradient-reversal
language: en
---

# MentalBERT V5 — Domain-Adversarial (DANN) 8-Class Flat Classifier

Domain-Adversarial Neural Network (DANN) built on `mental/mental-bert-base-uncased`,
classifying social media text into 8 mental-health categories with source-invariant
representations enforced via a Gradient Reversal Layer (GRL).

**Reference:** Ganin & Lempitsky (2015) — *Unsupervised Domain Adaptation by Backpropagation*, ICML.

## Classes
Anxiety, Bipolar, Depression, Directed Aggression, Normal, Personality Disorder, Stress, Suicidal

## Architecture
```
[CLS] pooler output (768-d)
  ├── Head A — Classification : Dropout(0.1) → Linear(768, 8)  [deployed]
  └── GRL(λ) → Head B — Source: Dropout(0.1) → Linear(768, 6)  [training only]
```

## Results
| Metric | Value |
|---|---|
| Test Accuracy | 81.50% |
| F1 Macro | 0.8245 |
| F1 Weighted | 0.8155 |
| Dep→Sui bleed | 808 |
| Sui→Dep bleed | 565 |
| Total bleed | 1373 |
| Source-head F1 (GRL diagnostic) | 0.0992 (chance ≈ 0.167) |

## Load Pattern (Inference)
```python
import torch, torch.nn as nn, json, joblib
from transformers import BertModel, BertTokenizerFast
from huggingface_hub import hf_hub_download

repo = 'itsLu/mentalbert-v5-dann'

# Load encoder + tokenizer
base = BertModel.from_pretrained(repo)
tok  = BertTokenizerFast.from_pretrained(repo)

# Download cls_head weights and config
cls_path    = hf_hub_download(repo, 'cls_head.pt')
cfg_path    = hf_hub_download(repo, 'inference_config.json')
le_path     = hf_hub_download(repo, 'label_encoder.joblib')

cfg = json.load(open(cfg_path))
le  = joblib.load(le_path)

cls_head = nn.Linear(768, cfg['n_classes'])
checkpoint = torch.load(cls_path, map_location='cpu')
cls_head.load_state_dict(checkpoint['linear'])

# Inference
base.eval(); cls_head.eval()
with torch.no_grad():
    enc    = tok(text, return_tensors='pt', truncation=True, max_length=128, padding='max_length')
    pooled = base(**enc).pooler_output
    logits = cls_head(pooled)
    pred   = le.inverse_transform([logits.argmax(-1).item()])[0]
```

## GRL λ Schedule
λ(p) = 2 / (1 + exp(−10.0·p)) − 1,  p = step / total\_steps

Ramps from 0 (no adversarial pressure) to ~1.0 (full adversarial pressure) over training.

## Training Config
- Base model: `mental/mental-bert-base-uncased`
- MAX\_LEN=128, BATCH=32, EPOCHS=4, LR=2e-5
- WeightedRandomSampler + class-weighted CE + per-sample source reliability
- FP16 mixed precision, gradient clip 1.0, linear warmup 10%
- Best checkpoint by val F1 macro (classification head only)
