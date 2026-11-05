---
base_model: unsloth/llama-3.2-3b-instruct-bnb-4bit
datasets:
- vishal042002/Clinical-surgery
language:
- en
license: apache-2.0
tags:
- text-generation-inference
- transformers
- unsloth
- llama
- medical
- Book2Data
- finetune
- Ragbased-q&a
- safetensors
---

# Uploaded  model

- **Developed by:** vishal042002
- **License:** apache-2.0
- **Finetuned from model :** unsloth/llama-3.2-3b-instruct-bnb-4bit

This llama model was trained 2x faster with [Unsloth](https://github.com/unslothai/unsloth) and Huggingface's TRL library.

[<img src="https://raw.githubusercontent.com/unslothai/unsloth/main/images/unsloth%20made%20with%20love.png" width="200"/>](https://github.com/unslothai/unsloth)

The model was trained on a custom dataset containing clinical surgery Q&A pairs. The dataset was compiled from:
Open-source medical books

RUNNING THE MODEL THROUGH ADAPTER MERGE: 

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import PeftModel
import torch

base_model_name = "unsloth/Llama-3.2-3B-Instruct"  
base_model = AutoModelForCausalLM.from_pretrained(base_model_name, torch_dtype=torch.float16, device_map="auto")

adapter_path = "vishal042002/Llama3.2-3b-Instruct-ClinicalSurgery"
base_model = PeftModel.from_pretrained(base_model, adapter_path)

tokenizer = AutoTokenizer.from_pretrained(base_model_name)

device = "cuda" if torch.cuda.is_available() else "cpu"
base_model.to(device)

# Sample usage
input_text = "What is the mortality rate for patients requiring surgical intervention who were unstable preoperatively?"
inputs = tokenizer(input_text, return_tensors="pt").to(device)

outputs = base_model.generate(**inputs, max_new_tokens=200, temperature=1.5, top_p=0.9)
decoded_output = tokenizer.decode(outputs[0], skip_special_tokens=True)

print(decoded_output)
```

LOADING THE MODEL DIRECTLY: 

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model_name = "vishal042002/Llama3.2-3b-Instruct-ClinicalSurgery"
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.float16,
    device_map="auto"
)

tokenizer = AutoTokenizer.from_pretrained(model_name)
```


This model is designed to:

Answer questions about clinical surgery procedures.
Provide information about surgical interventions. 

Limitations:

The model should not be used as a substitute for professional medical advice.
Responses should be verified by qualified medical professionals.