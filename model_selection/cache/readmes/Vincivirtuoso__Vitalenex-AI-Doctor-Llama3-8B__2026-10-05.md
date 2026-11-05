---
license: apache-2.0
language:
- en
- pcm
tags:
- llama3
- medical
- pidgin
- vitalenex
- chat
pipeline_tag: text-generation
---

# Vitalenex-AI-Doctor-Llama3-8B

This is a fine-tuned version of `aaditya/Llama3-OpenBioLLM-8B` specialized for medical conversations with a focus on Nigerian & Pidgin English context.

## Model Description

This model was fine-tuned on a combination of general medical conversations and a synthetically generated dataset of Pidgin English health queries. It is intended to be used as a helpful AI assistant for preliminary health information.

## Intended Uses & Limitations

This model is an MVP for the Vitalenex AI project.

## How to Use (with Transformers)

```python
from transformers import AutoTokenizer, AutoModelForCausalLM

model_id = "Vincivirtuoso/Vitalenex-AI-Doctor-Llama3-8B"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id)
# ...