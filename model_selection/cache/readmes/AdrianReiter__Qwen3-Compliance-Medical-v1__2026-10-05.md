---
library_name: mlx
tags:
- mlx
- medical
- compliance
- regulatory
base_model: Qwen/Qwen3-0.6B
---

# Qwen3 Compliance Medical Agent (v1)

This model is a fine-tuned version of **Qwen3-0.6B** specialized in Medical Device Regulation (ISO 13485, IEC 62304, ISO 14971).

## 💻 How to use

### With MLX (Apple Silicon)
```bash
pip install mlx-lm

from mlx_lm import load, generate

model, tokenizer = load("AdrianReiter/Qwen3-Compliance-Medical-v1")

prompt = """<|im_start|>system
You are a Regulatory Consultant. Always analyze dependencies and risk before answering.<|im_end|>
<|im_start|>user
We want to use an open-source library in our device. What are the risks?<|im_end|>
<|im_start|>assistant
"""

response = generate(model, tokenizer, prompt=prompt, verbose=True)

from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "AdrianReiter/Qwen3-Compliance-Medical-v1"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id)

# ... use standard pipeline ...