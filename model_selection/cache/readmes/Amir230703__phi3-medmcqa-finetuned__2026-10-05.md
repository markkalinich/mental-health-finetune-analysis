---
tags:
  - text-generation
---

# Phi-3 MedMCQA Finetuned

This is a fine-tuned version of **Phi-3** on the **MedMCQA** dataset.  
It is optimized for **medical question answering and text generation**.

## **Usage**
```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "Amir230703/phi3-medmcqa-finetuned"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

input_text = "What is the treatment for diabetes?"
input_ids = tokenizer(input_text, return_tensors="pt").input_ids

output = model.generate(input_ids, max_length=200)
print(tokenizer.decode(output[0], skip_special_tokens=True))
