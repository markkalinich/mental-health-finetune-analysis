---
library_name: transformers
pipeline_tag: token-classification
tags:
- token-classification
- ner
- pii
- deberta
- nlp
- privacy
- named-entity-recognition
language:
- en
---

# DeBERTa-v3-base Nemotron PII

Fine-tuned `microsoft/deberta-v3-base` model for PII detection using the NVIDIA Nemotron-PII dataset.

## Model

- Base model: `microsoft/deberta-v3-base`
- Dataset: `nvidia/Nemotron-PII`
- Training examples: 1,000
- Validation examples: 200
- Task: PII token classification
- Labeling scheme: BIO

## PII labels

The model was trained for these 10 categories:

- employee_id
- employment_status
- biometric_identifier
- device_identifier
- health_plan_beneficiary_number
- license_plate
- medical_record_number
- vehicle_identifier
- education_level
- blood_type

## Validation results

Evaluated on 200 validation examples:

| Metric | Score |
|---|---:|
| Precision | 0.91 |
| Recall | 0.92 |
| Micro F1 | 0.91 |
| Macro F1 | 0.85 |
| Weighted F1 | 0.92 |
| Validation Loss | 0.01345 |

## Per-label F1

| Label | F1 |
|---|---:|
| biometric_identifier | 0.97 |
| blood_type | 1.00 |
| device_identifier | 0.00 |
| education_level | 0.93 |
| employee_id | 0.85 |
| employment_status | 0.81 |
| health_plan_beneficiary_number | 0.99 |
| license_plate | 0.97 |
| medical_record_number | 0.97 |
| vehicle_identifier | 0.98 |

## Intended use

This model is intended for experimentation and learning around PII detection and NLP token classification.

## Limitations

The model was trained on a relatively small 1,000-example subset, so further training and evaluation on larger and more diverse datasets is recommended.

The `device_identifier` category showed weak validation performance and requires further improvement.

## Training

The model was fine-tuned using Hugging Face Transformers with BIO-formatted token classification labels.

## License

The underlying NVIDIA Nemotron-PII dataset is licensed under CC BY 4.0. Please review the dataset and base-model licenses before redistribution or commercial use.
