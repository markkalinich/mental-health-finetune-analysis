---
language: en
license: mit
tags:
  - medical
  - radiology
  - t5
  - text2text-generation
  - information-extraction
  - huggingface
datasets:
  - aiims-radiology-internal
pipeline_tag: text2text-generation
---

# T5-Small for Medical Report Labeling (Radiology NLP)

A fine-tuned `t5-small` model that extracts **structured clinical labels** from **free-form radiologist diagnoses**. This model transforms raw diagnostic text into 5 key medical labels, supporting downstream machine learning and analysis in medical imaging.

>  Trained on real-world anonymized radiology data in collaboration with AIIMS, New Delhi.

---

## Problem Statement

Medical reports — especially radiologist diagnoses — are often unstructured, verbose, and inconsistent. This project addresses that problem by creating a model that can extract:

-  **Abnormal/Normal**
-  **Pathologies Extracted**
-  **Midline Shift**
-  **Location & Brain Organ**
-  **Bleed Subcategory**

---

##  Use Case

The output of this model can be paired with MRI scans to train supervised models for diagnosis, segmentation, or triaging. This can also help hospitals build structured EMRs from legacy reports.

---

##  Model Details

- **Base Model**: `t5-small`
- **Architecture**: Seq2Seq
- **Trained On**: Internal AIIMS-labeled Excel dataset
- **Framework**: Hugging Face Transformers

---

## Evaluation

The test loss on an average is 0.03

---

## Example Input/Output

### Input (Prompt)
```text
Extract info: Acute intracerebral hemorrhage with 4 mm midline shift and parietal lobe involvement.
```
## How to use

``` python

from transformers import pipeline

pipe = pipeline("text2text-generation", model="gursmeep/t5-radiology-final")

prompt = "Extract info: Acute SDH with frontal lobe involvement and mild midline shift."
result = pipe(prompt, max_length=256, do_sample=False)

print(result[0]['generated_text'])

```

## Dataset Background
- Source: Excel sheet of annotated radiologist reports

- Annotated via: GPT-4-assisted labeling

- Origin: Data shared by company during internship project in collaboration with AIIMS

## Training Setup
- Trained on Colab GPU

- Used Hugging Face Trainer and DataCollatorForSeq2Seq

- 4 Epochs, Batch Size: 8

- Input Format: "Extract info: {diagnosis text}"

## Model Card Author

Developed by Gursmeep Kaur during a medical NLP internship project


