---
language:
- fr
- en
license: apache-2.0
tags:
- medical
- domain-adaptation
- continual-pretraining
- causal-lm
- question-answering
- evaluation
datasets:
- Dr-BERT/NACHOS
base_model: MedLLaMA-13B
model_type: causal-lm
---

# MedLLaMA-13B-CPT (CPT)

## Model description
This checkpoint is a **continual-pretrained (CPT)** version of **MedLLaMA-13B**, adapted on unlabeled french medical text to strengthen domain-specific representations for medical question answering. CPT is performed via **full-parameter training** on medical corpora (Dr-BERT/NACHOS).
