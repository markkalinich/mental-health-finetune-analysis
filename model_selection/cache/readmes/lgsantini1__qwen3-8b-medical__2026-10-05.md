---
base_model: unsloth/Qwen3-8B-unsloth-bnb-4bit
tags:
- text-generation
- conversational
- medical
- qa
- transformers
- unsloth
- qwen3
license: apache-2.0
language:
- en
- pt
---

# Qwen3-8B Medical (Fine-tuned)

- **Developed by:** lgsantini1  
- **License:** apache-2.0  
- **Finetuned from:** unsloth/Qwen3-8B-unsloth-bnb-4bit  

## Overview
This is a Qwen3-8B model fine-tuned for medical-style question answering based on publicly available QA datasets.

## Training data
This model was fine-tuned using data sourced from:

- **PubMedQA** — A dataset of question answering pairs grounded in biomedical research abstracts.  
  Repo: https://github.com/pubmedqa/pubmedqa  
  (Used only the content available in the repository; no additional web crawling.)

> If you also used other datasets (e.g., MedQuAD), add them here with links and licenses.

## Intended use
- Educational / informational assistance for medical QA style prompts.
- Useful for summarization, explanation of concepts, and drafting answers that should be **verified**.

## Limitations & safety
- This model can **hallucinate** or provide incomplete/incorrect medical guidance.
- **Not a medical device**. Do not use for diagnosis, treatment decisions, or emergency situations.
- Always verify answers with reliable sources and qualified professionals.

## How to use

### Transformers (Python)
```python
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

repo_id = "lgsantini1/qwen3-8b-medical"

tok = AutoTokenizer.from_pretrained(repo_id)
model = AutoModelForCausalLM.from_pretrained(repo_id, torch_dtype="auto", device_map="auto")

prompt = "Explain hypertension in simple terms."
inputs = tok(prompt, return_tensors="pt").to(model.device)
out = model.generate(**inputs, max_new_tokens=200)
print(tok.decode(out[0], skip_special_tokens=True))
