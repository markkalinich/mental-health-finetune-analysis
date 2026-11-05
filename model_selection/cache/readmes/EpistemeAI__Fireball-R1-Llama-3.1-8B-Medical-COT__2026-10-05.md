---
base_model: EpistemeAI/Fireball-R1-Llama-3.1-8B
tags:
- text-generation-inference
- transformers
- unsloth
- llama
- trl
license: apache-2.0
language:
- en
datasets:
- FreedomIntelligence/medical-o1-reasoning-SFT
---

## Model Information


# EpistemeAI/Fireball-R1-Llama-3.1-8B-Medical-COT

![License](https://img.shields.io/badge/License-Apache%202.0-blue)  ![Version](https://img.shields.io/badge/Version-1.0.0-green)

This is a state-of-the-art language model optimized for **neutrality**, **STEM proficiency**, and **ethical alignment**. Fine-tuned Deepseek-R1-distill-llama-8b-unsloth-bnb-4bit for science, chemistry, and mathematics with reduced cultural/political bias.
This large language model is open source.  This is supervised fine tuned with medical chain of thought

---

## Table of Contents  
- [Features](#features)  
- [Installation](#installation)  
- [Usage](#usage)  
- [Training Details](#training-details)  
- [Ethical Considerations](#ethical-considerations)  
- [License](#license)  
- [Citation](#citation)  
- [Contact](#contact)  

---

## Features  
- **Neutral Worldview**: Minimizes political/cultural bias via globally diverse training data and human feedback.  
- **STEM Specialization**: Enhanced performance in:  
  - **Chemistry**: Reaction mechanisms, periodic trends, spectroscopy.  
  - **Mathematics**: Equation solving, proofs, calculus.  
  - **General Science**: Hypothesis generation, research summarization.  
- **Ethical Guardrails**: Filters sensitive content and flags uncertain outputs.  

---

## Installation  
```bash  
pip install transformers torch
pip install accelerate
pip install -U transformers
```

### Basic Inference
```bash  

from transformers import AutoTokenizer, AutoModelForCausalLM  

tokenizer = AutoTokenizer.from_pretrained("EpistemeAI/Fireball-R1-Llama-3.1-8B-Medical-COT")  
model = AutoModelForCausalLM.from_pretrained("EpistemeAI/Fireball-R1-Llama-3.1-8B-Medical-COT")  

prompt = "Calculate the molar mass of sulfuric acid (H₂SO₄)."  
inputs = tokenizer(prompt, return_tensors="pt")  
outputs = model.generate(**inputs, max_length=200)  
print(tokenizer.decode(outputs[0], skip_special_tokens=True))


##advance inference
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

# Load the tokenizer
tokenizer = AutoTokenizer.from_pretrained("EpistemeAI/Fireball-R1-Llama-3.1-8B-Medical-COT")

# Load the model in 8-bit precision using bitsandbytes (requires a CUDA GPU)
model = AutoModelForCausalLM.from_pretrained(
    "EpistemeAI/Fireball-R1-Llama-3.1-8B",
    load_in_8bit=True,      # Enable 8-bit loading to reduce memory usage
    device_map="auto"       # Automatically map model layers to the available device(s)
)

# Define the system prompt and the user prompt
system_prompt = "You are a highly knowledgeable assistant with expertise in chemistry and physics. <think>"
user_prompt = "Calculate the molar mass of sulfuric acid (H₂SO₄)."

# Combine the system prompt with the user prompt. The format here follows a common convention for chat-like interactions.
full_prompt = f"System: {system_prompt}\nUser: {user_prompt}\nAssistant:"

# Tokenize the combined prompt and move the inputs to the GPU
inputs = tokenizer(full_prompt, return_tensors="pt").to("cuda")

# Generate output text from the model
outputs = model.generate(**inputs, max_length=12200)

# Decode and print the result, skipping special tokens
result = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(result)

```



# Uploaded  model

- **Developed by:** EpistemeAI
- **License:** apache-2.0
- **Finetuned from model :** unsloth/deepseek-r1-distill-llama-8b-unsloth-bnb-4bit

# Ethical Considerations
Do Not Use For:

- legal advice without expert oversight.
- Generating partisan or culturally insensitive content.

## Limitations:
- May occasionally produce plausible but incorrect scientific explanations.
- Not fully immune to subtle biases.

## Thank you
We appreciate the companies as following: Unsloth, Meta and Deepseek. 

## License
This model is licensed under [apache-2.0] - see LICENSE for details.

# Uploaded  model

- **Developed by:** EpistemeAI
- **License:** apache-2.0
- **Finetuned from model :** EpistemeAI/Fireball-R1-Llama-3.1-8B

This llama model was trained 2x faster with [Unsloth](https://github.com/unslothai/unsloth) and Huggingface's TRL library.

[<img src="https://raw.githubusercontent.com/unslothai/unsloth/main/images/unsloth%20made%20with%20love.png" width="200"/>](https://github.com/unslothai/unsloth)