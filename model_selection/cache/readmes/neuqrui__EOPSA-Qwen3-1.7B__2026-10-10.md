---
license: apache-2.0
base_model: Qwen/Qwen3-1.7B
tags:
- qwen3
- eopsa
- safety
- alignment
pipeline_tag: text-generation
---

# EOPSA-Qwen3-1.7B

EOPSA (Efficient On-Policy Self-Distilled Safety Alignment) checkpoint of [Qwen3-1.7B](https://huggingface.co/Qwen/Qwen3-1.7B).

- Training code: [https://github.com/neuqrui/EOPSA](https://github.com/neuqrui/EOPSA)
- Model collection: [https://huggingface.co/collections/neuqrui/eopsa](https://huggingface.co/collections/neuqrui/eopsa)
- Safety evaluation: [https://github.com/neuqrui/LLM-Safety-Eval](https://github.com/neuqrui/LLM-Safety-Eval)

## Load

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "neuqrui/EOPSA-Qwen3-1.7B"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype="auto",
    device_map="auto",
)
```
