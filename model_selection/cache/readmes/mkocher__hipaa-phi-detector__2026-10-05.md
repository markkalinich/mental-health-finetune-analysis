---
language: en
license: apache-2.0
tags:
  - token-classification
  - ner
  - hipaa
  - phi
  - healthcare
  - privacy
  - distilbert
datasets:
  - custom
pipeline_tag: token-classification
---

# HIPAA PHI Detector (DistilBERT)

A fine-tuned DistilBERT model for detecting Protected Health Information (PHI) in text, covering all 18 HIPAA Safe Harbor categories.

## Model Details

- **Architecture**: DistilBERT (66M params) with token classification head
- **Training**: Fine-tuned on 5,000+ synthetic HIPAA examples
- **Labels**: 37 BIO labels (18 entity types x 2 + O)
- **Framework**: PyTorch / HuggingFace Transformers

## Supported Entity Types

| Label | HIPAA Category |
|-------|---------------|
| NAME | Names |
| LOCATION | Geographic subdivisions |
| DATE | Dates |
| PHONE | Phone numbers |
| FAX | Fax numbers |
| EMAIL | Email addresses |
| SSN | Social Security numbers |
| MRN | Medical record numbers |
| HEALTH_PLAN | Health plan beneficiary numbers |
| ACCOUNT | Account numbers |
| LICENSE | Certificate/license numbers |
| VEHICLE | Vehicle identifiers |
| DEVICE | Device identifiers |
| URL | Web URLs |
| IP | IP addresses |
| BIOMETRIC | Biometric identifiers |
| PHOTO | Photographic images |
| OTHER | Any other unique identifying number |

## Usage

```python
from transformers import pipeline

pipe = pipeline("token-classification", model="mkocher/hipaa-phi-detector", aggregation_strategy="simple")
results = pipe("Patient John Smith, SSN 123-45-6789")
```

Or with the `aare-core` package:

```python
from aare import HIPAAGuardrail

guardrail = HIPAAGuardrail()
result = guardrail.check("Patient John Smith, SSN 123-45-6789")
if result.blocked:
    print(f"PHI detected: {result.violations}")
```

## License

Apache 2.0
