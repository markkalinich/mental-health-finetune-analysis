---
language: en
tags:
- medical
- triage
- bert
- emergency-medicine
- classification
license: mit
datasets:
- KTAS-ED
metrics:
- accuracy
---

# EdgeMed Clinical BERT

Fine-tuned BERT model for emergency triage ESI level classification,
part of the EdgeMed edge intelligence healthcare routing framework.

## Model Details
- Base model: BERT (clinical fine-tuned)
- Task: ESI triage classification (ESI-1 to ESI-5)
- Training data: 1,267 KTAS-ED emergency department patients
- Accuracy: 71.7%

## ESI Levels
| Level | Severity | SLA |
|------|---------|------|
| ESI-1 | Resuscitation | < 2 min |
| ESI-2 | Emergent | < 10 min |
| ESI-3 | Urgent | < 30 min |
| ESI-4 | Less Urgent | < 60 min |
| ESI-5 | Non-Urgent | < 120 min |

## Usage
from transformers import AutoTokenizer, AutoModelForSequenceClassification

tokenizer = AutoTokenizer.from_pretrained("Mahdiya/edgemed-clinical-bert")
model = AutoModelForSequenceClassification.from_pretrained("Mahdiya/edgemed-clinical-bert")

## Citation
EdgeMed: A Lightweight Edge Intelligence Framework for
Preference-Aware Emergency Healthcare Routing
