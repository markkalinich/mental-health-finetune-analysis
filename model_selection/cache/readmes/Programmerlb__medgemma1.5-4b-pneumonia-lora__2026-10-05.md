---
language: en
license: apache-2.0
library_name: transformers
pipeline_tag: text-generation
tags:
- medgemma
- gemma
- medical
- healthcare
- pneumonia
base_model: google/medgemma-1.5-4b-it
widget:
- text: "I have fever and cough for 3 days. What should I do?"
- text: "65-year-old with shortness of breath and chest pain. Is this urgent?"
- text: "What are red flags that should make me seek emergency care?"
---

# MedGemma 1.5 4B – Pneumonia (Merged)

This repository contains a **merged fine-tuned MedGemma model** focused on pneumonia-related clinical guidance.

> ⚠️ **Disclaimer**  
> Educational and research use only. Not for real medical diagnosis or treatment.

## Base model
- google/medgemma-1.5-4b-it

## Quickstart (Transformers)

```python
!pip install -U transformers accelerate sentencepiece safetensors

import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

repo_id = "Programmerlb/medgemma1.5-4b-pneumonia-lora"

tokenizer = AutoTokenizer.from_pretrained(repo_id, use_fast=True)
model = AutoModelForCausalLM.from_pretrained(
    repo_id,
    device_map="auto",
    dtype=torch.float16,
)

prompt = "I have fever and productive cough for 5 days with shortness of breath. What should I do?"
inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
output = model.generate(**inputs, max_new_tokens=200)
print(tokenizer.decode(output[0], skip_special_tokens=True))
