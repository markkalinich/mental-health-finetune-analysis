---
license: mit
base_model: distilbert-base-uncased
pipeline_tag: text-classification
---

# Medical Intent Classifier

DistilBERT fine-tuned to classify patient queries into 9 clinical intent categories for NHS triage routing. Part of a project demonstrating how a model that scored 100% on a standard train/test split turned out to be only 18% reliable on independent, realistic patient phrasing — and what it took (LIME diagnosis + targeted LLM-generated augmentation across 12 iterations) to reach 92.3% on a leakage-checked stress test.

**Full project, methodology, and demo:** https://github.com/umarkhan0206/medical-intent-classifier

## Categories
causes · exams and tests · information · inheritance · precautions · side effects · symptoms · treatment and outlook · when to contact a medical professional

## Usage

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification

tokenizer = AutoTokenizer.from_pretrained("umarkhan0206/medical-intent-classifier")
model = AutoModelForSequenceClassification.from_pretrained("umarkhan0206/medical-intent-classifier")
```

This is a routing aid, **not a diagnostic tool**, and should not be used for clinical decision-making.