---
language: en
license: mit
tags:
- medical
- healthcare
- text-generation
- gpt2
library_name: transformers
pipeline_tag: text-generation
---

# Medical LLM 1GB - Simple Version

A medical-focused language model based on DistilGPT-2, optimized for healthcare applications.

## Model Details

- **Base Model**: DistilGPT-2
- **Parameters**: ~82M
- **Size**: ~350MB
- **Domain**: Medical/Healthcare
- **License**: MIT

## Usage

```python
from transformers import AutoTokenizer, AutoModelForCausalLM

model = AutoModelForCausalLM.from_pretrained("dkumarcvp/medical-llm-1gb")
tokenizer = AutoTokenizer.from_pretrained("dkumarcvp/medical-llm-1gb")

# Generate medical text
prompt = "Question: What are the symptoms of diabetes?\nAnswer:"
inputs = tokenizer(prompt, return_tensors="pt")
outputs = model.generate(**inputs, max_length=150, temperature=0.7)
response = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(response)
```

## Disclaimer

⚠️ **For educational and research purposes only. Not for medical diagnosis or treatment.**

## Hardware Requirements

- **RAM**: 2GB minimum
- **Storage**: 1GB
- **Device**: CPU compatible
