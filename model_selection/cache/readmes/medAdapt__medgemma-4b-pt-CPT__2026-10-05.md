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
base_model: medgemma-4b-pt
model_type: causal-lm
---

# medgemma-4b-pt-CPT (CPT)

## Model description
This checkpoint is a **continual-pretrained (CPT)** version of **medgemma-4b-pt**, adapted on unlabeled french medical text to strengthen domain-specific representations for medical question answering. CPT is performed via **full-parameter training** on medical corpora (Dr-BERT/NACHOS).
