---
license: llama3.2
language: en
base_model: distil-labs/Distil-PII-Llama-3.2-3B-Instruct
pipeline_tag: text-generation
tags:
- pii-redaction
- privacy
- slm
- distil-labs
- mlx
library_name: mlx
---

# Otilde/Distil-PII-Llama-3.2-3B-Instruct-mxfp4-MLX

This model [Otilde/Distil-PII-Llama-3.2-3B-Instruct-mxfp4-MLX](https://huggingface.co/Otilde/Distil-PII-Llama-3.2-3B-Instruct-mxfp4-MLX) was
converted to MLX format from [distil-labs/Distil-PII-Llama-3.2-3B-Instruct](https://huggingface.co/distil-labs/Distil-PII-Llama-3.2-3B-Instruct)
using mlx-lm version **0.28.2**.

## Use with mlx

```bash
pip install mlx-lm
```

```python
from mlx_lm import load, generate

model, tokenizer = load("Otilde/Distil-PII-Llama-3.2-3B-Instruct-mxfp4-MLX")

prompt = "hello"

if tokenizer.chat_template is not None:
    messages = [{"role": "user", "content": prompt}]
    prompt = tokenizer.apply_chat_template(
        messages, add_generation_prompt=True
    )

response = generate(model, tokenizer, prompt=prompt, verbose=True)
```
