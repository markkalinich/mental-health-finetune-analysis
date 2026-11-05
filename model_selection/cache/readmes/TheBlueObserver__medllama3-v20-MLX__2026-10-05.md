---
base_model: ProbeMedicalYonseiMAILab/medllama3-v20
license: llama3
tags:
- mlx
---

# TheBlueObserver/medllama3-v20-MLX

The Model [TheBlueObserver/medllama3-v20-MLX](https://huggingface.co/TheBlueObserver/medllama3-v20-MLX) was
converted to MLX format from [ProbeMedicalYonseiMAILab/medllama3-v20](https://huggingface.co/ProbeMedicalYonseiMAILab/medllama3-v20)
using mlx-lm version **0.20.2**.

## Use with mlx

```bash
pip install mlx-lm
```

```python
from mlx_lm import load, generate

model, tokenizer = load("TheBlueObserver/medllama3-v20-MLX")

prompt="hello"

if hasattr(tokenizer, "apply_chat_template") and tokenizer.chat_template is not None:
    messages = [{"role": "user", "content": prompt}]
    prompt = tokenizer.apply_chat_template(
        messages, tokenize=False, add_generation_prompt=True
    )

response = generate(model, tokenizer, prompt=prompt, verbose=True)
```
