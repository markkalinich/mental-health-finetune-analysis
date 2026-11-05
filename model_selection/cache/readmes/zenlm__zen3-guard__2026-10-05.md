---
language: en
license: apache-2.0
base_model: ibm-granite/granite-guardian-3.2-5b
tags:
  - text-classification
  - zen
  - zenlm
  - hanzo
  - zen3
  - safety
  - moderation
  - content-classification
pipeline_tag: text-generation
library_name: transformers
---

# zen3-guard

Safety moderation model for content classification and filtering.

Repackaged from [ibm-granite/granite-guardian-3.2-5b](https://huggingface.co/ibm-granite/granite-guardian-3.2-5b) (apache-2.0, IBM Granite). **Not trained from scratch** — a permissively-licensed redistribution for the OSS-clean Zen model line.

## Overview

Zen Guard provides content-risk classification for prompts and responses across the Granite Guardian risk taxonomy (harm, social bias, jailbreak, violence, profanity, sexual content, unethical behavior, and RAG groundedness/relevance checks).

Developed by [Hanzo AI](https://hanzo.ai) and the [Zoo Labs Foundation](https://zoo.ngo).

## Quick Start

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "zenlm/zen3-guard"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id, torch_dtype="auto", device_map="auto")

messages = [{"role": "user", "content": "How do I learn programming?"}]
guardian_config = {"risk_name": "harm"}
text = tokenizer.apply_chat_template(messages, guardian_config=guardian_config, tokenize=False, add_generation_prompt=True)
inputs = tokenizer(text, return_tensors="pt").to(model.device)
outputs = model.generate(**inputs, max_new_tokens=20)
print(tokenizer.decode(outputs[0][inputs.input_ids.shape[1]:], skip_special_tokens=True))  # -> "Yes" / "No"
```

## Model Details

| Attribute | Value |
|-----------|-------|
| Parameters | 5B |
| Architecture | Granite (`GraniteForCausalLM`) |
| Context | 128K tokens |
| License | Apache 2.0 |

## License

`apache-2.0`. Upstream: **ibm-granite/granite-guardian-3.2-5b** by IBM Granite. Upstream LICENSE/NOTICE retained in-repo.
