---
library_name: transformers
tags:
- jailbreak-detection
- safety
- security
language:
- en
metrics:
- accuracy
- roc_auc
base_model:
- prajjwal1/bert-tiny
- google-bert/bert-base-uncased
pipeline_tag: text-classification
---

# Model Card for Model ID

A small model to detect saturation jailbreak attacks.  Not intended for standalone use against other kinds of jailbreaks.

## Model Details

### Model Description

- **Developed by:** Guardrails AI, Joseph Catrambone
- **Funded by [optional]:** Guardrails AI
- **Model type:** Transformer, BERT
- **Language(s) (NLP):** English
- **License:** Restrictive
- **Finetuned from model [optional]:** bert-tiny

### Model Sources [optional]

- **Repository:** https://www.github.com/guardrails-ai/detect-jailbreak

## Uses

Designed as a small prefilter for a subset of saturation attacks.

### Out-of-Scope Use

Not designed to catch other types of jailbreaks.  Saturation protection is one part of a more complite suite of defenses against improper use of ML systems.
