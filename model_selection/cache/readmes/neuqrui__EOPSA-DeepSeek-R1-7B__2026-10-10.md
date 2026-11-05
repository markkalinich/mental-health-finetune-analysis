---
license: apache-2.0
base_model: deepseek-ai/DeepSeek-R1-Distill-Qwen-7B
tags:
- deepseek
- qwen
- eopsa
- safety
- alignment
pipeline_tag: text-generation
---

# EOPSA-DeepSeek-R1-7B

EOPSA (Efficient On-Policy Self-Distilled Safety Alignment) checkpoint of [DeepSeek-R1-Distill-Qwen-7B](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-7B).

- Training code: [https://github.com/neuqrui/EOPSA](https://github.com/neuqrui/EOPSA)
- Model collection: [https://huggingface.co/collections/neuqrui/eopsa](https://huggingface.co/collections/neuqrui/eopsa)
- Safety evaluation: [https://github.com/neuqrui/LLM-Safety-Eval](https://github.com/neuqrui/LLM-Safety-Eval)

## Load

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "neuqrui/EOPSA-DeepSeek-R1-7B"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype="auto",
    device_map="auto",
)
```
