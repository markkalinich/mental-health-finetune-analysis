---
tags:
- psychology
- chatbot
- llama
- therapy
- mental health
license: llama3.1
language:
- en
base_model:
- meta-llama/Llama-3.1-8B
---

# WellMinded Therapy Engine (8B)

This is a fine-tuned version of the LLaMA 3.1 8B model, optimized for psychologist-like conversations.
## Usage

You can load and use this model with the `transformers` library:

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained("PixelPanda1/WellMinded_Therapy_Engine")
tokenizer = AutoTokenizer.from_pretrained("PixelPanda1/WellMinded_Therapy_Engine")

input_text = "Hi, I'm feeling really stressed lately."
inputs = tokenizer(input_text, return_tensors="pt")
outputs = model.generate(**inputs)

print(tokenizer.decode(outputs[0]))