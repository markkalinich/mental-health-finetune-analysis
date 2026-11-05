---
license: llama3.1
base_model: meta-llama/Llama-3.1-8B-Instruct
base_model_relation: merge
library_name: transformers
pipeline_tag: text-generation
tags:
- safety
- alignment
---

# HARC — Llama-3.1-8B-Instruct

HARC safety-alignment LoRA merged into `meta-llama/Llama-3.1-8B-Instruct` (full standalone model).
Part of the [HARC](https://github.com/microsoft/HARC) release; see paper arXiv:2607.00572.

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
model = AutoModelForCausalLM.from_pretrained("microsoft/HARC-Llama-3.1-8B-Instruct", torch_dtype="bfloat16", device_map="auto")
tok = AutoTokenizer.from_pretrained("microsoft/HARC-Llama-3.1-8B-Instruct")
```
