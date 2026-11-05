---
tags: [medgemma, epicast, medical, surveillance, west-africa, merged]
base_model: google/medgemma-4b-it
license: apache-2.0
language: [en, pcm, ha, yo, fr, tw]
---

# EpiCast MedGemma 4B Merged (v2)

MedGemma 4B-IT with EpiCast multilingual LoRA merged into base weights for standalone deployment.

## Base Model
[google/medgemma-4b-it](https://huggingface.co/google/medgemma-4b-it) (Google Health AI Developer Foundations)

## Details
- Base: google/medgemma-4b-it
- LoRA: Janeodum/epicast-multilang-lora (merged)
- Fine-tuned on 3,400+ multilingual clinical examples across 6 languages
- 11 WHO IDSR syndrome categories
- Optimized for on-device syndromic extraction in West Africa
