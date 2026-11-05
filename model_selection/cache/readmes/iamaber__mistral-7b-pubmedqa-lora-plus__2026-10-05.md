---
license: apache-2.0
library_name: transformers
base_model: mistralai/Mistral-7B-Instruct-v0.3
pipeline_tag: text-generation
datasets:
  - qiaojin/PubMedQA
tags:
  - peft
  - lora
  - loraplus
  - pubmedqa
  - medical
---

# pubmedqa-loraplus Model

## Overview

This merged artifact fine-tunes `mistralai/Mistral-7B-Instruct-v0.3` on `qiaojin/PubMedQA` / `pqa_labeled` using LoRA+.

## Training Setup

| Field | Value |
| --- | --- |
| Train examples | 900 |
| Eval examples | 100 |
| Epochs | 3 |
| Train batch size | 4 |
| Eval batch size | 4 |
| Gradient accumulation | 4 |
| Learning rate | 5e-05 |
| Best eval loss | 0.5188 |
| Latest eval loss | 0.5188 |
| Latest train loss | 0.4810 |
| Train runtime (s) | 566.5676 |
| Global step | 171 |

## Evaluation Summary

| Metric | Value |
| --- | --- |
| PubMedQA accuracy | 0.4500 |
| PubMedQA macro F1 | 0.2069 |
| PubMedQA weighted F1 | 0.2793 |
| PubMedQA samples | 100 |
| Medical MMLU accuracy | 0.1600 |
| Medical MMLU samples | 50 |

## Medical MMLU Subject Breakdown

| Subject | Accuracy | Correct | Total |
| --- | --- | --- | --- |
| anatomy | 0.1600 | 8 | 50 |
| clinical_knowledge | 0.0000 | 0 | 0 |
| college_medicine | 0.0000 | 0 | 0 |
| medical_genetics | 0.0000 | 0 | 0 |
| professional_medicine | 0.0000 | 0 | 0 |
| virology | 0.0000 | 0 | 0 |

## PubMedQA Confusion Matrix

| Actual \ Predicted | yes | no | maybe |
| --- | --- | --- | --- |
| yes | 45 | 0 | 0 |
| no | 40 | 0 | 0 |
| maybe | 15 | 0 | 0 |
