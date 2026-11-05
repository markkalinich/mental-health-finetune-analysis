---
base_model: Qwen/Qwen3.5-9B
library_name: transformers
pipeline_tag: text-generation
language:
- pl
tags:
- polish
- medical
- domain-adaptation
---

# Qwen3.5-9B-medadapt

Polish medical domain adaptation of `Qwen/Qwen3.5-9B`.

This revision contains the variant trained via continued pretraining on polish medical text pretraining followed by SFT on Polish and English medical instructions .

This is the corrected Polish + English SFT run initialized from this repository's `cpt` branch. Answer-only targets use the non-thinking chat format with completion-only loss and native assistant turn endings. The exported chat template supports both reasoning and non-reasoning inference.


Branches:

- `main`: CPT + SFT model
- `cpt`: continued pretraining model
- `sft_pl`: Polish SFT model
- `sft_pl_eng`: Polish + English SFT model

Current branch: `main`
