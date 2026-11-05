---
language: en
tags:
  - obliteratus
  - abliteration
  - uncensored
  - obliterate
base_model: Qwen/Qwen3.5-9B
---

# Qwen3.5-9B-OBLITERATED

This model was abliterated using the **`gabliteration`** method via
[OBLITERATUS](https://github.com/elder-plinius/OBLITERATUS).

| Detail | Value |
|--------|-------|
| Base model | `Qwen/Qwen3.5-9B` |
| Method | `gabliteration` |
| Source | obliterate |

## How to Use

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained("Qwen3.5-9B-OBLITERATED")
tokenizer = AutoTokenizer.from_pretrained("Qwen3.5-9B-OBLITERATED")

prompt = "Hello, how are you?"
inputs = tokenizer(prompt, return_tensors="pt")
outputs = model.generate(**inputs, max_new_tokens=256)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```

## About OBLITERATUS

OBLITERATUS is an open-source tool for removing refusal behavior from language
models via activation engineering (abliteration). Learn more at
[github.com/elder-plinius/OBLITERATUS](https://github.com/elder-plinius/OBLITERATUS).
