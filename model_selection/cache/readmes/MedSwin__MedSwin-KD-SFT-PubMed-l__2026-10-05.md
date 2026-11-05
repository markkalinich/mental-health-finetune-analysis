---
license: apache-2.0
datasets:
- MedSwin/PubMedQA-l
language:
- en
base_model:
- MedSwin/MedSwin-7B-KD
pipeline_tag: question-answering
metrics:
- bertscore: 0.8341
tags:
- medical
---

- **Developed by:** Medical Swinburne University of Technology AI Team
- **Funded by:** [Swinburne University of Technology](https://www.swinburne.edu.au)
- **Language(s):** English
- **License:** Apache 2.0
  
## Model Details
This is a Supervised Finetuning (SFT) model on top of a Knowledge Distillation model (KD), on labelled dataset from PubMedQA.

> Review all model metrics benchmark via [Benchmark Document Preview](https://hackmd.io/@ngFNmXW1RVOfNb7b3NYBJg/model_review).