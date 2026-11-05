---
language: en
tags:
- text-classification
- prompt-injection
- security
- deberta-v3
license: mit
---

# Prompt Injection Guard — Classifier v1

## Model Description

DeBERTa-v3-base fine-tuned for binary prompt injection detection.
Classifies user inputs to LLM applications as benign or injection attempt.

Built as part of a 35-day portfolio project targeting the Anthropic Safeguards ML/Research Engineer role.

## Training Data

Four public datasets unified into a single DuckDB schema after MinHash deduplication: 11,690 examples total.
Train/val/test split: 70/15/15, stratified by attack category.

## Training Details

- Base model: microsoft/deberta-v3-base
- Epochs: 3, Learning rate: 2e-5, Batch size: 16
- Training time: ~28 minutes on Colab T4

## Evaluation Results (Held-Out Test Set, n=1,754)

| Metric | Value |
|--------|-------|
| Macro F1 | 0.9957 |
| 95% Bootstrap CI | (0.9924, 0.9982) |
| Accuracy | 1.00 |
| Injection Recall | 1.00 |
| Injection Precision | 0.99 |

### Per-Category F1

| Category | F1 | n |
|----------|-----|---|
| direct | 1.0000 | 92 |
| jailbreak | 1.0000 | 26 |
| system_prompt_leak | 1.0000 | 12 |
| unknown | 0.9962 | 1566 |
| role_play | 0.9644 | 57 |

## Repository

https://github.com/Shihabuddin-Alvi/prompt-injection-guard
