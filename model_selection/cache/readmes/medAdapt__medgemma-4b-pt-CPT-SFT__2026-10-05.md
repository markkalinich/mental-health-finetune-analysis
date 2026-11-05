---
language:
- fr
- en
license: apache-2.0
tags:
- medical
- continual-pretraining
- instruction-tuning
- cpt+sft
- causal-lm
- question-answering
base_model: medgemma-4b-pt
model_type: causal-lm
---

# medgemma-4b-pt-CPT-SFT (CPT+SFT)

## Model description
This checkpoint applies **two-stage domain adaptation**:
1) **CPT** on unlabeled medical text to adapt representations on Dr-BERT/NACHOS corpus , then  
2) **SFT** on labeled medical QA to optimize task performance (MedInjection-FR/ALL) .
