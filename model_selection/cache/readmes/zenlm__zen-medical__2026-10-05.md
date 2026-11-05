---
license: apache-2.0
language:
- en
tags:
- zen
- zenlm
- hanzo-ai
- medical
- clinical
- healthcare
pipeline_tag: text-generation
library_name: transformers
base_model: Qwen/Qwen3-8B
---

# Zen Medical

> **Parameters**: 8B | **Architecture**: Qwen3 | **Context**: 32K | **License**: Apache 2.0

Medical AI for clinical research, literature synthesis, pharmacology, and diagnostic support workflows.

Designed for medical researchers and healthcare AI developers. Not for clinical diagnosis.

Fine-tuned from [Qwen/Qwen3-8B](https://huggingface.co/Qwen/Qwen3-8B) (Apache-2.0) with Hanzo identity + agentic-data training + abliteration.

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
model = AutoModelForCausalLM.from_pretrained("zenlm/zen-medical", torch_dtype="auto")
tokenizer = AutoTokenizer.from_pretrained("zenlm/zen-medical")
messages = [{"role": "user", "content": "Your domain-specific prompt here"}]
text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
inputs = tokenizer(text, return_tensors="pt").to(model.device)
output = model.generate(**inputs, max_new_tokens=1024)
print(tokenizer.decode(output[0][inputs.input_ids.shape[-1]:], skip_special_tokens=True))
```

## Credits

Built on [Qwen/Qwen3-8B](https://huggingface.co/Qwen/Qwen3-8B) by the Alibaba Qwen team, licensed under Apache-2.0. Hanzo adds identity training, agentic-data fine-tuning, and abliteration.

---
## The Zen LM Family

Joint research between **Hanzo AI** (Techstars '17), **Zoo Labs Foundation** (501c3), and **Lux Partners Limited**.

All weights Apache 2.0. Download, run locally, fine-tune, deploy commercially.

[HuggingFace](https://huggingface.co/zenlm) · [Chat](https://hanzo.chat) · [API](https://api.hanzo.ai) · [Docs](https://zenlm.org)
