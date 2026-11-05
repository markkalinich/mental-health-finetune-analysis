---
license: apache-2.0
language:
- en
tags:
- medical
- icd10
- medical coding
- clinical
- healthcare
- icd10dx
- CAC
widget:
- text: >-
    Chief Complaint: John has been experiencing shortness of breath and mild
    chest pain for the past two days.

    Medical History: He has a history of hypertension, which is currently under
    control with medication. Additionally, he was diagnosed with Type 2 Diabetes
    five years ago and had an episode of bronchitis last year.

    Examination Findings: During the examination, it was noted that Johns heart
    rate was elevated, and his blood pressure was slightly high at 150/95 mmHg.
    His respiratory rate was above normal limits, and his oxygen saturation was
    94% on room air.

    Investigations: An ECG was performed, which thankfully did not show any
    significant ST changes, typically indicative of acute coronary syndrome. A
    chest X-ray was also done, revealing no acute cardiopulmonary processes.

    Assessment and Plan: Given the elevated heart rate and hypertension, coupled
    with his shortness of breath, there is a concern for the early signs of
    congestive heart failure. However, the absence of acute changes in the ECG
    and the normal chest X-ray findings are reassuring. It is important to
    consider his history of hypertension and diabetes in the overall assessment,
    as these factors elevate his risk for cardiovascular complications.

    A conservative approach is recommended at this stage. We will start diuretic
    therapy to manage potential fluid overload and schedule an echocardiogram to
    further assess his cardiac function. In the meantime, his blood pressure and
    blood glucose levels will be closely monitored. A follow-up appointment is
    scheduled for next week, with instructions to return earlier if his symptoms
    worsen.
  example_title: Example 1
- text: 'Impression: fever, chills, cough, chest pain, shortness of breath, N/V.'
  example_title: Example 2
---
# ICD-10 DX Code Identification Model

## Overview
This model is designed for the identification of tokens related to ICD-10 DX codes in clinical documents. We focus on a subset of approximately 4,000+ codes, 
which are the most frequently used in clinical documentation. Please refer config.json file for target codes we used to train this model.

## Model Details
- **Type**: Named Entity Recognition (NER)
- **Target**: ICD-10 DX Codes
- **Code Subset**: 4,000+ most common codes

## Dataset
The dataset comprises clinical documents annotated for ICD-10 DX codes. We ensure a balanced representation of the selected codes to prevent model bias. 
the dataset is private one, used internally to trian the model.

## Training
Due to GPU memory constraints, training is conducted in epochs with periodic evaluations to monitor performance and mitigate overfitting.

# Use a pipeline as a high-level helper

from transformers import pipeline

pipe = pipeline("token-classification", model="imperiumhf/imp_clinical_dxcode_ner_v2")

## Evaluation
Need to update metrics

## Limitations and Considerations
- Overfitting risk due to repeated training on the same dataset.
- The balance between model complexity and the large number of classes.
- Regular model evaluation for performance monitoring.

## Contact
krishnareddyn@kpmd.biz

## Acknowledgements
All the rights over this model is reserved for Imperium software solutions pvt ltd.