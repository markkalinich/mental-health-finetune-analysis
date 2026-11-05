---
license: mit
language:
- en
metrics:
- f1
- accuracy
---
# Postoperative Patient Sentiment

## Model Details
- **Base model:** `cjen1008/distilroberta-healthcare-sentiment`
- **Task:** 3-class sentiment classification
- **Labels:** `negative`, `mixed/neutral`, `positive`, assigned by two physicians training as orthopedic surgeons

## Intended Use
Sentiment classification of postoperative patient comments from spine and arthroplasty cohorts for research and quality-improvement workflows.

## Training
- **Fine-tuning set:** 400 comments total (200 spine, 200 arthroplasty)
- **Hyperparameters:** 4 epochs, learning rate `2e-5`, batch size `8` (train) / `16` (eval), max length `256`

## Evaluation (Holdout)
| Cohort | n | Macro F1 | Weighted F1 | Accuracy |
|---|---:|---:|---:|---:|
| Spine | 205 | 0.687353 | 0.747496 | 0.746341 |
| Arthroplasty | 191 | 0.744606 | 0.788168 | 0.801047 |

## Limitations
- Developed in a specific institutional context; external generalization is not guaranteed.
- Labels are based on human rater judgments and may reflect rater variability.
- Not intended as a standalone clinical decision tool.