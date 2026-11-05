---
license: llama3.1
datasets:
- nvidia/Aegis-AI-Content-Safety-Dataset-2.0
language:
- en
base_model:
- meta-llama/Llama-3.1-8B-Instruct
- nvidia/llama-3.1-nemoguard-8b-content-safety
---

# Llama-3.1-NemoGuard-8B Content Safety Merged

This model is a merged version of:
- Base: [meta-llama/Llama-3.1-8B-Instruct](https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct)
- Adapter: [nvidia/llama-3.1-nemoguard-8b-content-safety](https://huggingface.co/nvidia/llama-3.1-nemoguard-8b-content-safety)

## Usage
```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained("oneonlee/llama-3.1-nemoguard-8b-content-safety-merged")
tokenizer = AutoTokenizer.from_pretrained("oneonlee/llama-3.1-nemoguard-8b-content-safety-merged")
```