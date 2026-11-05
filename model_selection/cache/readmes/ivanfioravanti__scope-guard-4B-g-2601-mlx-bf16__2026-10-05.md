---
base_model: principled-intelligence/scope-guard-4B-g-2601
tags:
- text-generation-inference
- transformers
- safety
- guardrails
- guardrailing
- scope
- mlx
license: gemma
language:
- en
- it
- fr
- es
- de
pipeline_tag: text-generation
library_name: mlx
---

# ivanfioravanti/scope-guard-4B-g-2601-mlx-bf16

This model [ivanfioravanti/scope-guard-4B-g-2601-mlx-bf16](https://huggingface.co/ivanfioravanti/scope-guard-4B-g-2601-mlx-bf16) was
converted to MLX format from [principled-intelligence/scope-guard-4B-g-2601](https://huggingface.co/principled-intelligence/scope-guard-4B-g-2601)
using mlx-lm version **0.31.3**.

## Use with mlx

```bash
pip install mlx-lm
```

```python
from mlx_lm import load, generate

model, tokenizer = load("ivanfioravanti/scope-guard-4B-g-2601-mlx-bf16")

prompt = "hello"

if tokenizer.chat_template is not None:
    messages = [{"role": "user", "content": prompt}]
    prompt = tokenizer.apply_chat_template(
        messages, add_generation_prompt=True, return_dict=False,
    )

response = generate(model, tokenizer, prompt=prompt, verbose=True)
```
