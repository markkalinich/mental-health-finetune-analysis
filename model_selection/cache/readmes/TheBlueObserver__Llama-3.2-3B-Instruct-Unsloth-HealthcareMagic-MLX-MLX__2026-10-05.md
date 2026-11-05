---
base_model: TheBlueObserver/Llama-3.2-3B-Instruct-Unsloth-HealthcareMagic-MLX
library_name: transformers
tags:
- mlx
---

# TheBlueObserver/Llama-3.2-3B-Instruct-Unsloth-HealthcareMagic-MLX-MLX

The Model [TheBlueObserver/Llama-3.2-3B-Instruct-Unsloth-HealthcareMagic-MLX-MLX](https://huggingface.co/TheBlueObserver/Llama-3.2-3B-Instruct-Unsloth-HealthcareMagic-MLX-MLX) was
converted to MLX format from [TheBlueObserver/Llama-3.2-3B-Instruct-Unsloth-HealthcareMagic-MLX](https://huggingface.co/TheBlueObserver/Llama-3.2-3B-Instruct-Unsloth-HealthcareMagic-MLX)
using mlx-lm version **0.20.2**.

## Use with mlx

```bash
pip install mlx-lm
```

```python
from mlx_lm import load, generate

model, tokenizer = load("TheBlueObserver/Llama-3.2-3B-Instruct-Unsloth-HealthcareMagic-MLX-MLX")

prompt="hello"

if hasattr(tokenizer, "apply_chat_template") and tokenizer.chat_template is not None:
    messages = [{"role": "user", "content": prompt}]
    prompt = tokenizer.apply_chat_template(
        messages, tokenize=False, add_generation_prompt=True
    )

response = generate(model, tokenizer, prompt=prompt, verbose=True)
```
