---
library_name: mlx
tags:
- mlx
base_model: Intelligent-Internet/II-Medical-8B
pipeline_tag: text-generation
---

# mlx-community/II-Medical-8B-bf16

This model [mlx-community/II-Medical-8B-bf16](https://huggingface.co/mlx-community/II-Medical-8B-bf16) was
converted to MLX format from [Intelligent-Internet/II-Medical-8B](https://huggingface.co/Intelligent-Internet/II-Medical-8B)
using mlx-lm version **0.25.0**.

## Use with mlx

```bash
pip install mlx-lm
```

```python
from mlx_lm import load, generate

model, tokenizer = load("mlx-community/II-Medical-8B-bf16")

prompt = "hello"

if tokenizer.chat_template is not None:
    messages = [{"role": "user", "content": prompt}]
    prompt = tokenizer.apply_chat_template(
        messages, add_generation_prompt=True
    )

response = generate(model, tokenizer, prompt=prompt, verbose=True)
```
