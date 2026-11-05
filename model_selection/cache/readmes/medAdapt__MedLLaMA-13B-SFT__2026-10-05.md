---
language:
- fr
- en
license: apache-2.0
tags:
- medical
- instruction-tuning
- sft
- lora
- causal-lm
- question-answering
datasets:
- MedInjection-FR/ALL
base_model: MedLLaMA-13B
model_type: causal-lm
---

# MedLLaMA-13B-SFT (SFT)

## Model description
This checkpoint is a **supervised fine-tuned (SFT)** version of **MedLLaMA-13B**, trained on **labeled medical QA** (MedInjection-FR/ALL) data to improve task performance—especially for **medical MCQA**. SFT is implemented using DoRA.
