---
language: en
license: mit
tags:
  - text-classification
  - sentiment-analysis
  - distilbert
  - glassdoor
  - company-culture
datasets:
  - Gopinath-AI/glassdoor_reviews
metrics:
  - accuracy
  - f1
---

# WorkPulse — Company Culture Sentiment Analyzer

Fine-tuned DistilBERT for 3-class sentiment classification of company culture based on employee reviews.

## Demo
🌐 **Live App:** https://workpulse-frontend-pied.vercel.app

## Model Description

This model classifies employee reviews into 3 categories:
- **Negative (0)** — Toxic, dysfunctional, or exploitative workplace
- **Neutral (1)** — Mixed or mediocre experience
- **Positive (2)** — Genuinely good workplace culture

## Training Data

- **Dataset:** Gopinath-AI/glassdoor_reviews (838,566 real Glassdoor reviews)
- **Training samples:** 50,000 (balanced — 16,666 per class)
- **Key insight:** 46.2% of negative reviews had positive language in their `pros` field. Solution: used `cons` text for Negative/Neutral labels and `pros` text for Positive labels to eliminate label-text mismatch.

## Training Results

| Metric | Score |
|---|---|
| Overall Accuracy | 78.9% |
| F1 — Negative | 0.689 |
| F1 — Neutral | 0.712 |
| F1 — Positive | 0.966 |
| F1 — Macro | 0.789 |

## Usage

```python
from transformers import pipeline

classifier = pipeline(
    "text-classification",
    model="Madhuri1003/workpulse-distilbert"
)

result = classifier("Great culture, supportive management, excellent work life balance")
print(result)
# [{'label': 'Positive', 'score': 0.999}]
```

## Limitations

- Neutral class F1 of 0.71 — ambiguous reviews occasionally misclassified
- Trained on English reviews only
- Mixed sentiment not explicitly detected (use the full API for mixed detection)

## Links

- **GitHub:** https://github.com/imperfectly-perfect1003/internship-2026/tree/main/Week5-NLP-WorkPulse
- **API:** https://madhuri1003-workpulse-api.hf.space/docs
- **Training Notebook:** Available in GitHub repo