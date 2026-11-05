---
license: other
license_name: health-ai-developer-foundations
license_link: https://developers.google.com/health-ai-developer-foundations/terms
library_name: mlx
pipeline_tag: text-generation
extra_gated_heading: Access MedGemma on Hugging Face
extra_gated_prompt: To access MedGemma on Hugging Face, you're required to review
  and agree to [Health AI Developer Foundation's terms of use](https://developers.google.com/health-ai-developer-foundations/terms).
  To do this, please ensure you're logged in to Hugging Face and click below. Requests
  are processed immediately.
extra_gated_button_content: Acknowledge license
base_model: google/medgemma-27b-text-it
tags:
- medical
- clinical-reasoning
- thinking
- mlx
---

# mlx-community/medgemma-27b-text-it-bf16

This model [mlx-community/medgemma-27b-text-it-bf16](https://huggingface.co/mlx-community/medgemma-27b-text-it-bf16) was
converted to MLX format from [google/medgemma-27b-text-it](https://huggingface.co/google/medgemma-27b-text-it)
using mlx-lm version **0.25.1**.

## Use with mlx

```bash
pip install mlx-lm
```

```python
from mlx_lm import load, generate

model, tokenizer = load("mlx-community/medgemma-27b-text-it-bf16")

prompt = "hello"

if tokenizer.chat_template is not None:
    messages = [{"role": "user", "content": prompt}]
    prompt = tokenizer.apply_chat_template(
        messages, add_generation_prompt=True
    )

response = generate(model, tokenizer, prompt=prompt, verbose=True)
```
