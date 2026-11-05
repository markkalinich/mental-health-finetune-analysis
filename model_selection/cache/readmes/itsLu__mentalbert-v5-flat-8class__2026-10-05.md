---
language: en
license: apache-2.0
tags:
- mental-health
- text-classification
- mentalbert
pipeline_tag: text-classification
widget:
- text: "I have been feeling hopeless for months and I just want it to end."
  example_title: Suicidal
- text: "My heart races constantly and I can't stop worrying."
  example_title: Anxiety
- text: "I will kill every single one of you, you will regret it."
  example_title: Directed Aggression
---

# MentalBERT V5 — Flat 8-Class Mental Health Classifier

Single-pass MentalBERT fine-tuned on the V5 mental-health dataset. Predicts one of 8 classes:

`Anxiety`, `Bipolar`, `Depression`, `Directed Aggression`, `Normal`, `Personality Disorder`, `Stress`, `Suicidal`.

## Test Set Results (V5 stratified 70/10/20, random_state=42)

| Metric | Value |
|---|---|
| Accuracy | 82.84% |
| F1 macro | 0.8350 |
| F1 weighted | 0.8280 |
| Sui→Dep (missed crises) | 516 |
| Total Dep↔Sui bleed | 1249 |
| ROC AUC (macro) | 0.9638 |

## Quick Start (Python)

```python
from transformers import pipeline

clf = pipeline("text-classification", model="<YOUR_USERNAME>/mentalbert-v5-flat-8class")
result = clf("I haven't slept in days, I feel like everything is falling apart.")
print(result)  # [{'label': 'Stress', 'score': 0.87}]
```

## API Call (HF Inference Endpoint)

```python
import requests
HF_TOKEN = "hf_..."
URL = "https://api-inference.huggingface.co/models/<YOUR_USERNAME>/mentalbert-v5-flat-8class"
headers = {"Authorization": f"Bearer {HF_TOKEN}"}
r = requests.post(URL, headers=headers, json={"inputs": "I want to end it all."})
print(r.json())  # [{'label': 'Suicidal', 'score': 0.91}, ...]
```

For top-k probabilities over all classes, pass `{"inputs": text, "parameters": {"top_k": 8}}`.

## Limitations

- This is a screening signal, not a clinical diagnosis. Use only as one input among many.
- Sui→Dep (516) errors are missed crisis cases. Pair with a safety threshold or with the
  hierarchical companion model (`mentalbert-v5-hierarchical-longformer`) for safety-critical applications.
- Trained on Reddit-style English text; out-of-distribution domains (clinical notes, formal prose) may degrade.

## Training Details

- Backbone: `mental/mental-bert-base-uncased`
- MAX_LEN: 128, batch=32, LR=2e-05, epochs=4, label_smoothing=0.05
- Imbalance: `WeightedRandomSampler` + class-weighted CrossEntropy (cap=3.0)
- Hardware: NVIDIA T4 (Kaggle)
