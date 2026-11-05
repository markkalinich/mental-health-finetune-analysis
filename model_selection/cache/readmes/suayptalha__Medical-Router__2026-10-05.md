---
license: apache-2.0
datasets:
- suayptalha/Treatment-Instructions
- suayptalha/Psychological-Support
- suayptalha/Diagnose-Instructions
language:
- en
base_model:
- answerdotai/ModernBERT-base
pipeline_tag: text-classification
library_name: transformers
tags:
- moe
---

# MoE Router Model

Classify clinical text into:

* **0:** Diagnosis
* **1:** Treatment
* **2:** Psychological Support

## Training

* **Base model:** ModernBERT-base
* **Epochs:** 3
* **Learning rate:** 3e-5
* **Batch size:** 16