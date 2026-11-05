---
license: mit
language:
- en
base_model:
- AIMH/mental-longformer-base-4096
pipeline_tag: text-classification
tags:
- depression-detection
- mental-health
- longformer
- text-classification
- personality-traits
metrics:
- accuracy
- precision
- recall
- f1
- roc_auc
library_name: transformers
---


# Mental-Longformer for Depression Detection (Text + Traits)

**Base:** `AIMH/mental-longformer-base-4096`  
**Task:** Binary text classification (control vs. depressed) at **user level**.  
**Input mode:** *text + traits* — three personality traits neuroticism, conscientiousness, agreeableness  (N, C, A) are prefixed into the text.  
**Data:** eRisk 2025 (user-level). Class imbalance addressed via **synthetic augmentation** (Gemini 2.0 Flash Lite) on the depressed class; final train/val/test ≈ (1117/239/240) users, near-balanced.

**Result:** F1: 0.9620, Accuracy: 0.9625, Precision: 0.9661, Recall: 0.9580, ROC-AUC: 0.9942

## Input Format (text + traits)
The training concatenates the normalized traits to the front of the user's concatenated posts:
```
[TRAITS] N=0.742233 C=0.318224 A=0.411334 [/TRAITS]

<user_text ...>
```
Traits used: **neuroticism, conscientiousness, agreeableness** (normalized to [0,1]).

## Usage
```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

repo_id = "ppp57420/mental-longformer-text-ocean-personality"
tok = AutoTokenizer.from_pretrained(repo_id)
model = AutoModelForSequenceClassification.from_pretrained(repo_id).eval()

# Build the text+traits string
N, C, A = 0.74, 0.32, 0.41 # example normalized traits
user_text = "I have been feeling overwhelmed and tired lately... (concat user posts)"
inp_text = f"[TRAITS] N={N:.3f} C={C:.3f} A={A:.3f} [/TRAITS]\\n\\n" + user_text


# Longformer tip: set CLS token to global attention
enc = tok(inp_text, return_tensors="pt", truncation=True, padding="max_length", max_length=4096)
attn = enc["attention_mask"]
global_attn = attn.clone()
if global_attn.size(1) > 0:
global_attn[:, 0] = 1 # CLS


with torch.no_grad():
out = model(**enc, global_attention_mask=global_attn).logits # [1,2]
probs = out.softmax(dim=-1).squeeze(0).tolist()
print({"control": probs[0], "depressed": probs[1]})
```

## Notes
- This repository contains the best checkpoint selected by validation F1 with early stopping and hyperparameter search (Optuna).
- Model may reflect dataset biases; not a diagnostic tool.
- If you want **text-only** inference, omit the `[TRAITS]...[/TRAITS]` block.