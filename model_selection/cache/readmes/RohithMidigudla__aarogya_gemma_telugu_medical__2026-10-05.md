---
library_name: transformers
base_model: google/gemma-4-E4B-it
tags:
  - gemma
  - telugu
  - medical
  - grpo
  - merged
  - healthcare
language:
  - te
license: gemma
---

# Aarogya Gemma Telugu Medical

Aarogya Gemma Telugu Medical is a Telugu medical question-answering model built on `google/gemma-4-E4B-it`. 

The model is designed to answer medical multiple-choice questions and provide short Telugu explanations.

## Model Details

- **Base model:** `google/gemma-4-E4B-it`
- **Model type:** Full merged Transformers checkpoint
- **Precision:** `bfloat16`
- **Language:** Telugu (`te`)
- **Task:** Medical QA and concise Telugu medical explanations

## Training

This model combines Telugu and medical adaptation with GRPO alignment on Telugu MedMCQA-style data.
