---
{}
---
# Telehealth PII Redactor

A custom fine-tuned BERT model for automatic PII detection 
and redaction in telehealth audio transcripts. Built to 
demonstrate privacy-first design in patient-facing voice AI.

## Model Description
This model is fine-tuned from `dslim/bert-base-NER` on a 
synthetic telehealth dataset to detect and redact 
HIPAA-sensitive information from medical transcripts.

## Labels
| Label      | Description           |
|------------|-----------------------|
| B/I-PATIENT | Patient name         |
| B/I-DOCTOR  | Provider/doctor name |
| B/I-MRN     | Medical record number|
| B/I-PHONE   | Phone number         |
| B/I-DATE    | Dates                |

## Performance
| Metric    | Score |
|-----------|-------|
| F1        | 1.00  |
| Precision | 1.00  |
| Recall    | 1.00  |

## Training Data
Custom synthetic telehealth dataset with 1600 labeled 
sentences across 8 real-world clinical scenarios.
Dataset: YOUR_USERNAME/telehealth-pii-dataset

## How to Use
```python
from transformers import pipeline

pii_detector = pipeline(
    "ner",
    model="PandhereAnu/telehealth-pii-redactor",
    aggregation_strategy="simple"
)

text = "Patient Sarah Mitchell called Dr. Patel at 415-882-3901"
results = pii_detector(text)
print(results)
```

## Redaction Example
Input:
```
Patient Sarah Mitchell called Dr. Patel at 415-882-3901
```
Output:
```
Patient [PATIENT] called [DOCTOR] at [PHONE]
```

## Intended Use
- Telehealth transcript de-identification
- HIPAA compliance automation
- Privacy-first voice AI pipelines

## Limitations
- Trained on synthetic data
- Real world performance may vary
- English language only
