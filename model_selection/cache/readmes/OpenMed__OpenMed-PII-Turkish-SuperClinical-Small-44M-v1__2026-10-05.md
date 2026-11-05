---
license: apache-2.0
language:
- tr
base_model: microsoft/deberta-v3-small
library_name: transformers
pipeline_tag: token-classification
tags:
- token-classification
- ner
- pii
- pii-detection
- de-identification
- privacy
- healthcare
- medical
- clinical
- phi
- pytorch
- transformers
- openmed
- turkish
widget:
- text: Örnek hasta Ayşe Yılmaz'ın e-posta adresi ayse.yilmaz@example.com ve telefon numarası
    +90 555 000 00 00.
  example_title: Synthetic clinical text with PII (Turkish)
---

# OpenMed-PII-Turkish-SuperClinical-Small-44M-v1

This is an OpenMed token-classification checkpoint intended for Turkish
(`tr`) personally identifiable information (PII) and protected health
information (PHI) span detection.

## Model details

- Language scope: Turkish (`tr`)
- Task: token classification / named entity recognition
- Base model: [`microsoft/deberta-v3-small`](https://huggingface.co/microsoft/deberta-v3-small)
- Library: Transformers

## Usage

```python
from transformers import pipeline

model_id = "OpenMed/OpenMed-PII-Turkish-SuperClinical-Small-44M-v1"
detector = pipeline(
    "token-classification",
    model=model_id,
    aggregation_strategy="simple",
)

text = "Örnek hasta Ayşe Yılmaz'ın e-posta adresi ayse.yilmaz@example.com ve telefon numarası +90 555 000 00 00."
print(detector(text))
```

The checkpoint's configured `id2label` mapping is authoritative for the
available entity labels. Preserve returned character offsets when applying
redaction or replacement.

## Evaluation status

No verified Turkish evaluation artifact was available during this metadata
repair, so this card intentionally reports no language-specific scores.
Evaluate direct-identifier recall, false negatives, span boundaries, and
domain shift on representative data before deployment.

## Limitations and safety

This model can miss identifiers or over-redact clinically useful context. It
is not an anonymization guarantee, a compliance determination, or a medical
device. Use defense in depth and human review for high-sensitivity workflows.
Do not include real patient information in public examples, logs, or issue
reports.
