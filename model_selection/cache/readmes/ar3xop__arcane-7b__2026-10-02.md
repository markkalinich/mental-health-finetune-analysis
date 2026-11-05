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

# Arcane-7B

**Arcane-7B** is an instruction-tuned 7-billion parameter language model specialized for mental health, distress detection, and crisis analysis. It analyzes conversational text and social interactions to deliver structured diagnostic insights and interpretable clinical reasoning.

## Overview
- **Model Size**: 7 Billion Parameters
- **Primary Function**: Multi-task mental health evaluation & explainable distress scoring
- **Supported Analysis**: Depression screening, stress cause identification, suicide risk detection, loneliness, and emotional wellbeing assessment.

## Inference Example

```python
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

model_id = "ar3xop/arcane-7b"

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.float16,
    device_map="auto"
)

prompt = 'Consider this post: "I feel completely overwhelmed by work and isolated lately." Question: What is the distress level and primary cause?'
inputs = tokenizer(prompt, return_tensors="pt").to("cuda")

outputs = model.generate(inputs.input_ids, max_length=512, temperature=0.7)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```
