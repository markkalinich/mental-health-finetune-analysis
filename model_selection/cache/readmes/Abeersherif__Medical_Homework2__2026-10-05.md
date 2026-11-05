---
library_name: transformers
pipeline_tag: text-generation
base_model: SmolAI/SmolLM2-1.7B
license: apache-2.0
language:
  - en
tags:
  - smolllm2
  - finetuned
  - medical
  - homework
model_type: causal-lm
---

# Medical_Homework2 — Fine-Tuned SmolLM2-1.7B for Medical Reasoning

Medical_Homework2 is a fine-tuned version of SmolAI/SmolLM2-1.7B, trained specifically on structured medical question-answer data and short reasoning tasks.  
The model aims to provide concise, accurate, and educational medical explanations suitable for students and basic learning purposes.

---

## Model Overview

This model is optimized for medical comprehension tasks such as:
- Short medical answers
- Step-by-step reasoning
- Explanations of conditions, symptoms, and basic physiology
- Educational or homework-style responses

It is not designed for professional medical diagnosis or treatment decisions.

---

## Intended Use

### Recommended Use Cases
- Medical homework and assignment assistance  
- Explanation of medical concepts in simple language  
- Introductory physiology and pathology topics  
- Basic reasoning about medical questions  

### Not Recommended
- Real-world clinical decision-making  
- Emergency or diagnostic use  
- Any situation requiring professional medical judgement  

---

## Training Data

The model was fine-tuned using:
- Synthetic medical question-answer pairs  
- Simplified educational medical explanations  
- Instruction-answer examples  
- Homework-style reasoning data  

No real patient data or clinical records were used.

---

## Training Details

- Base model: SmolAI/SmolLM2-1.7B  
- Fine-tuning objective: Causal language modeling  
- Method: Full or LoRA fine-tuning (depending on your actual setup)  
- Optimizer: AdamW  
- Typical epochs: 1–3  

If you want, a full training script section can be added.

---

## Usage Example

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

model_name = "Abeersherif/Medical_Homework2"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

prompt = "Explain what type 2 diabetes is in simple terms."

inputs = tokenizer(prompt, return_tensors="pt")
outputs = model.generate(
    **inputs,
    max_new_tokens=150,
    temperature=0.7,
    top_p=0.9,
)

print(tokenizer.decode(outputs[0], skip_special_tokens=True))
