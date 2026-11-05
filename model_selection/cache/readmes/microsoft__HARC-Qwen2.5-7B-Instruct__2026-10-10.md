---
license: apache-2.0
base_model: Qwen/Qwen2.5-7B-Instruct
base_model_relation: merge
library_name: transformers
pipeline_tag: text-generation
tags:
- safety
- alignment
---

# HARC — Qwen2.5-7B-Instruct

HARC safety-alignment LoRA merged into `Qwen/Qwen2.5-7B-Instruct` (full standalone model).
Part of the [HARC](https://github.com/microsoft/HARC) release; see paper arXiv:2607.00572.

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
model = AutoModelForCausalLM.from_pretrained("microsoft/HARC-Qwen2.5-7B-Instruct", torch_dtype="bfloat16", device_map="auto")
tok = AutoTokenizer.from_pretrained("microsoft/HARC-Qwen2.5-7B-Instruct")
```
