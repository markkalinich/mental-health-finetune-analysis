---
license: mit
base_model: deepseek-ai/DeepSeek-R1-Distill-Llama-8B
datasets:
- FreedomIntelligence/medical-o1-reasoning-SFT
pipeline_tag: text-generation
language:
- en
library_name: transformers
---

# DeepSeek-R1-Medical-O1-QA

This is a fine-tuned version of the **deepseek-ai/DeepSeek-R1-Distill-Llama-8B** base model.

## Model Job
This model is specialized in text-based medical Question Answering (QA). It uses step-by-step reasoning to break down clinical scenarios, patient symptoms, and medical captions to provide clear answers.

## Dataset
Trained on the **FreedomIntelligence/medical-o1-reasoning-SFT** dataset to learn clinical chain-of-thought reasoning.

## Limitations
⚠️ This model is for research and educational purposes only. It cannot be used as a medical or diagnostic tool without a medical expert or doctor's supervision.