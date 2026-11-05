---
tags:
- qwen
- tamil
- therapy
- mental-health
- conversational
library_name: transformers
base_model: Qwen/Qwen2.5-3B-Instruct
language:
- ta
---

# Qwen 2.5-3B Tamil Therapy Model

Fine-tuned Qwen 2.5-3B model for empathetic Tamil therapy conversations.

## Model Details
- **Base Model**: Qwen/Qwen2.5-3B-Instruct
- **Language**: Tamil
- **Size**: ~6GB
- **Use Case**: Mental health support chatbot in Tamil

## Usage
```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model = AutoModelForCausalLM.from_pretrained(
    "Pavishanth68/qwen-2.5-3b-tamil-therapy-merged",
    torch_dtype=torch.float16,
    device_map="auto"
)
tokenizer = AutoTokenizer.from_pretrained("Pavishanth68/qwen-2.5-3b-tamil-therapy-merged")

prompt = "System: You are an empathetic Tamil therapist.\n\nUser: எனக்கு பதட்டமாக இருக்கிறது\nTherapist:"
inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

outputs = model.generate(**inputs, max_new_tokens=150, temperature=0.7)
response = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(response)
```

## Disclaimer
This is an AI assistant, not a replacement for professional mental health care.
