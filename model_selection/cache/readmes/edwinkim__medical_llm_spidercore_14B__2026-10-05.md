---
base_model: Qwen/Qwen3-14B
tags:
- medical
- korean
- healthcare
- llm
- qwen
language:
- ko
- en
pipeline_tag: text-generation
---

# Medical LLM SpiderCore 14B

## Model Description

Medical LLM SpiderCore 14B is a large language model specialized for Korean medical domain. Based on the Qwen3 architecture, it is optimized for medical question-answering and clinical reasoning tasks.

## Model Details

- **Model Architecture**: Qwen3ForCausalLM
- **Parameters**: 14B
- **Languages**: Korean, English
- **Specialization**: Medical, Healthcare

## Usage

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "edwinkim/medical_llm_spidercore_14B"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Example usage
prompt = "The patient presents with the following symptoms: headache, fever, cough. What are the possible diagnoses?"
inputs = tokenizer(prompt, return_tensors="pt")
outputs = model.generate(**inputs, max_length=512)
response = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(response)
```

## Limitations and Warnings

⚠️ **Not for Medical Diagnosis**

This model should only be used for educational and research purposes. Do not use this model for actual medical diagnosis or treatment decisions. Always consult with medical professionals.
