---
tags:
- autotrain
- text-generation-inference
- text-generation
- peft
- mlx
- mlx-my-repo
library_name: transformers
base_model: devparagiri/icd10-llama3-3b-sft
widget:
- messages:
  - role: user
    content: What is your favorite condiment?
license: other
datasets:
- FiscaAI/icd10cm-prompt
---

# jc2375/icd10-llama3-3b-sft-mlx-fp16

The Model [jc2375/icd10-llama3-3b-sft-mlx-fp16](https://huggingface.co/jc2375/icd10-llama3-3b-sft-mlx-fp16) was converted to MLX format from [devparagiri/icd10-llama3-3b-sft](https://huggingface.co/devparagiri/icd10-llama3-3b-sft) using mlx-lm version **0.26.4**.

## Use with mlx

```bash
pip install mlx-lm
```

```python
from mlx_lm import load, generate

model, tokenizer = load("jc2375/icd10-llama3-3b-sft-mlx-fp16")

prompt="hello"

if hasattr(tokenizer, "apply_chat_template") and tokenizer.chat_template is not None:
    messages = [{"role": "user", "content": prompt}]
    prompt = tokenizer.apply_chat_template(
        messages, tokenize=False, add_generation_prompt=True
    )

response = generate(model, tokenizer, prompt=prompt, verbose=True)
```
