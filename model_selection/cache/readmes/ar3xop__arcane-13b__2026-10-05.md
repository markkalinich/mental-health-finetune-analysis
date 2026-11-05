---
language:
- en
license: llama2
tags:
- arcane
- mental-health
- crisis-analysis
- distress-detection
- nlp
pipeline_tag: text-generation
---

# Arcane-13B

**Arcane-13B** is a high-capacity 13-billion parameter model for deep mental health text analysis, offering nuanced reasoning for complex crisis and wellbeing assessment workflows.

## Overview
- **Model Size**: 13 Billion Parameters
- **Capabilities**: High-fidelity explanation generation, multi-factor distress classification.

## Inference Example

```python
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

model_id = "ar3xop/arcane-13b"

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.float16,
    device_map="auto"
)

prompt = 'Consider this post: "Nothing seems meaningful anymore, struggling to get through the day." Question: Does the post indicate depressive tendencies?'
inputs = tokenizer(prompt, return_tensors="pt").to("cuda")

outputs = model.generate(inputs.input_ids, max_length=512)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```
