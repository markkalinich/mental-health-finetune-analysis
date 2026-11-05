---
tags:
  - text-generation
  - transformers
  - causal-lm
  - mindease
  - mental-health
  - hf-inference-api
---

# **🧠 MindEase-Assistant: A Mental Health AI Assistant**

This is a fine-tuned **TinyLlama 1.1B** model built to assist users with mental health support by generating thoughtful and empathetic responses.

## **📌 Model Details**

### **Model Description**
- **Developed by:** [Tezodipta]
- **Finetuned from model:** TinyLlama-1.1B
- **Language:** English
- **License:** Apache 2.0
- **Intended Use:** Text-based mental health support & guidance
- **Model Type:** Causal Language Model (LLM)

## **⚡️ How to Use**
This model can be used with the `transformers` library:

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "tezodipta/MindEase-Assistant"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

input_text = "I feel anxious, what should I do?"
input_ids = tokenizer(input_text, return_tensors="pt").input_ids

output = model.generate(input_ids, max_length=150)
print(tokenizer.decode(output[0], skip_special_tokens=True))
