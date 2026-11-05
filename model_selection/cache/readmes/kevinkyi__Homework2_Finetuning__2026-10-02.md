---
library_name: transformers
pipeline_tag: text-classification
license: mit
tags:
  - distilbert
  - sentiment
  - football
  - fine-tuning
model_name: DistilBERT Football Sentiment (Positive vs Negative)
language:
  - en
---

# DistilBERT Football Sentiment — Positive vs Negative

## Purpose
Fine-tune a compact transformer (DistilBERT) to classify short football-related comments as **positive (1)** or **negative (0)**. This supports a course assignment on text modeling and evaluation.

## Dataset
- **Source:** `james-kramer/football_news` on Hugging Face.
- **Schema:** `text` (string), `label` (0/1).
- **Task:** Binary sentiment classification (`0=negative`, `1=positive`).
- **Splits:** Stratified **80/10/10** (train/val/test) created in this notebook.
- **Cleaning:** Strip text, drop empty/NA rows.

## Preprocessing
- **Tokenizer:** `distilbert-base-uncased` (uncased), `max_length=256`, truncation.
- **Label mapping:** `{0: "negative", 1: "positive"}`.

## Training Setup
- **Base model:** `distilbert-base-uncased`
- **Epochs:** 5
- **Batch size:** 16
- **Learning rate:** 3e-05
- **Weight decay:** 0.01
- **Warmup ratio:** 0.1
- **Early stopping:** patience = 2 (monitor F1 on validation)
- **Seed:** 42
- **Hardware:** Google Colab (GPU)

## Metrics (Held-out Test)
```json
{
  "eval_loss": 0.0029852271545678377,
  "eval_accuracy": 1.0,
  "eval_precision": 1.0,
  "eval_recall": 1.0,
  "eval_f1": 1.0,
  "eval_runtime": 0.3123,
  "eval_samples_per_second": 352.273,
  "eval_steps_per_second": 22.417,
  "epoch": 4.0
}
```

## Confusion Matrix & Errors
The Colab notebook includes a confusion matrix for validation and test, plus a short error analysis with example misclassifications and hypotheses (e.g., injury news phrased neutrally but labeled negative).
|           | Pred 0 | Pred 1 |
|-----------|-------:|-------:|
| **True 0**|   55   |   0    |
| **True 1**|   0    |   55   |

## Brief Error Analysis (Concrete Examples & Hypotheses)
No misclassifications were observed in the held-out test split (confusion matrix = perfect).  
However, given the very small dataset size (~30 examples), this likely reflects **overfitting** rather than true robustness. 

## Limitations & Ethics
- Dataset size and labeling style can lead to unstable metrics; neutral/ambiguous tone is hard.
- Sports injury and team-management news may bias wording and labels.
- For coursework only; not for production or sensitive decisions.

## Reproducibility
- Python: 3.12
- Transformers: >=4.41
- Datasets: >=2.19
- Seed: 42

## License
- Code & weights: MIT (adjust per course guidelines)
- Dataset: see the original dataset's license/terms

## AI Assistance Disclosure
- GenAI tools assisted with notebook structure and documentation; modeling choices and evaluation were implemented and verified by the author.
