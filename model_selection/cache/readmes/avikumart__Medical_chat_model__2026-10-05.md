---
license: apache-2.0
datasets:
- openlifescienceai/medmcqa
base_model:
- meta-llama/Llama-3.2-1B
pipeline_tag: text-generation
---

# Medical Chat Model

## Model descrisption

The Medical_chat_model is a large language model (LLM) fine-tuned specifically for conversational tasks in the healthcare domain. It is designed to assist with initial medical inquiries, symptom clarification, and general health information retrieval by simulating doctor-patient interactions.

This model was created by fine-tuning a powerful base language model (e.g., Llama, Mistral, etc.) on specialized medical dialogue data to enhance its knowledge base and conversational fluency within a clinical context.

## Model training details

1. Model Type --> "Causal Language Model (e.g., Decoder-only Transformer)"
2. Task --> "Conversational AI, Text Generation, Medical Chatbot"
3. Language --> English
4. Fine-tuning Dataset --> all_medtext - medical health conversation data

## Model Usage

Requirements

```
pip install transformers torch accelerate
```

Model loading and inference
```
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# The model identifier provided by the user
model_id = "avikumart/Medical_chat_model" 

# 1. Load the tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_id)

# 2. Load the model
# Using AutoModelForCausalLM for generative chat models
# Setting torch_dtype=torch.bfloat16 for modern LLMs and device_map="auto" for multi-GPU setups
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.bfloat16,
    device_map="auto" 
)

# 3. Define the conversational prompt
# Format the prompt to guide the model to act as a doctor
prompt_template = (
    "A doctor and a patient are discussing symptoms. "
    "Patient: I've been having a persistent dry cough and low-grade fever for the past three days. "
    "Doctor:"
)

inputs = tokenizer(prompt_template, return_tensors="pt").to(model.device)

# 4. Generate the response
# Use model.generate for text generation
output_ids = model.generate(
    **inputs,
    max_new_tokens=256,
    do_sample=True,
    temperature=0.7,
    pad_token_id=tokenizer.eos_token_id
)

# 5. Decode and print the output
response = tokenizer.decode(output_ids[0], skip_special_tokens=True)
print(response.split("Doctor:")[-1].strip())
```

## Dataset

This model was fine-tuned on the all_medtext - medical health conversation data corpus, a high-quality, domain-specific dataset crucial for developing robust healthcare LLMs.

The dataset features a large collection of structured doctor-patient dialogues and/or medical instructions. It typically covers:

Scale: Over 50,000+ to 100,000+ conversational pairs, ensuring broad coverage.

Specialties: Interactions span a wide array of medical specialties, including internal medicine, cardiology, dermatology, pediatrics, and more.

Content: The conversations focus on symptom elicitation, diagnosis-oriented discussion, treatment suggestions (e.g., medication, home remedies), and medical advice.

The rich, specialized nature of this data ensures that the fine-tuned model is capable of generating clinically relevant, context-aware, and structured medical responses, moving beyond generic LLM capabilities.