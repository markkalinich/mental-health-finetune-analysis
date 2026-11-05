---
base_model: unsloth/Llama-3.2-3B
tags:
- text-generation-inference
- transformers
- llama
- medical
- autocomplete
license: apache-2.0
language:
- en
pipeline_tag: text-generation
library_name: transformers
---

# Medical Autocomplete - Llama 3.2 3B (Merged)

Fine-tuned Llama 3.2 3B model for medical text autocomplete.

- **Base model:** unsloth/Llama-3.2-3B
- **Fine-tuning method:** QLoRA (merged into full model)
- **Training data:** Medical articles (peS2o)
- **Developed by:** bargar92
