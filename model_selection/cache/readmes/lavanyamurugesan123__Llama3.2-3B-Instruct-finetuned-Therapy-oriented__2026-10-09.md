---
library_name: transformers
datasets:
- RaviSheel04/Psychology-Data
language:
- en
base_model:
- meta-llama/Llama-3.2-3B-Instruct
pipeline_tag: text-generation
---

# Model Card for Model ID

<!-- Provide a quick summary of what the model is/does. -->
Finetuned variant of Meta's Llama-3.2-3B-Instruct model for therapy-oriented, empathetic dialogue based on psychological principles.

### Model Description

<!-- Provide a longer summary of what this model is. -->

This model is designed for:
1. Therapy-style chatbot assistants
2. Educational tools in psychology and emotional support
3. Empathy-enhanced dialogue agents
4. Prompting for mental wellness and reflective dialogue

This is the model card of a 🤗 transformers model that has been pushed on the Hub. This model card has been automatically generated.

- **Developed by:** lavanyamurugesan123
- **Model type:** Causal Language Model
- **Language(s) (NLP):** English
- **Finetuned from model [optional]:** meta-llama/Llama-3.2-3B-Instruct


## Uses

<!-- Address questions around how the model is intended to be used, including the foreseeable users of the model and those affected by the model. -->
This model is designed for:
1. Therapy-style chatbot assistants
2. Educational tools in psychology and emotional support
3. Empathy-enhanced dialogue agents
4. Prompting for mental wellness and reflective dialogue

## How to use
```
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

# Load model and tokenizer
model_id = "lavanyamurugesan123/Llama3.2-3B-Instruct-finetuned-Therapy-oriented"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id, torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32)
model.to("cuda" if torch.cuda.is_available() else "cpu")

# Define user message and prompt
user_message = "I've been feeling anxious lately. What should I do?"
prompt = f"""<|begin_of_text|><|start_header_id|>system<|end_header_id|>
You are a Psychology Assistant, designed to answer users' questions in a kind, empathetic, and respectful manner, drawing from psychological principles and research to provide thoughtful support.DO NOT USE THE NAME OF THE PERSON IN YOUR RESPONSE<|eot_id|><|start_header_id|>user<|end_header_id|>
{user_message}<|eot_id|><|start_header_id|>assistant<|end_header_id|>"""

# Tokenize input
inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

# Generate response
with torch.no_grad():
    outputs = model.generate(
        **inputs,
        max_new_tokens=200,
        do_sample=True,
        temperature=0.7,
        pad_token_id=tokenizer.eos_token_id
    )

# Decode and clean up
full_output = tokenizer.decode(outputs[0], skip_special_tokens=False)

# Extract only assistant's response
assistant_response = full_output.split("<|end_header_id|>")[-1].strip()

print(assistant_response)

```