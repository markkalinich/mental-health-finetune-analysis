---
base_model:
- google/medgemma-27b-text-it
- unsloth/medgemma-27b-text-it
tags:
- text-generation-inference
- transformers
- unsloth
- gemma3_text
- trl
- mental-health
- psychology
license: apache-2.0
language:
- en
datasets:
- hllzmz/synthetic-mental-health-convos
---

# MedGemma-27B Mentalist

**MedGemma Mentalist** is a specialized **Mental Health Assistant** model fine-tuned on top of Google's `medgemma-27b`. It has been trained using with high-quality synthetic client-therapist dialogues.

This model is designed to understand users' emotional states, interpret described experiences through the lens of mental health and clinical standards, and provide supportive guidance using a warm, empathetic tone.

## Critical Disclaimer
**This model is NOT a licensed medical professional.**

* It **cannot** provide definitive medical diagnoses.
* It **cannot** prescribe medication.
* It **cannot** replace emergency services in crisis situations (e.g., suicide, self-harm, harm to others).
* **It is intended solely for educational, research, and preliminary informational purposes.**

## Model Capabilities
* **Empathetic Dialogue:** Listens to the user without judgement and validates their feelings (Active Listening).
* **Symptom Analysis:** correlates user-described experiences with clinical terminology and criteria.
* **Safety First:** Prioritizes safety planning and refers users to professional help when risk signals are detected.

## How to Use

This model can be loaded directly using 'transformers'. For optimal performance and role adherence, please strictly follow the parameters below.

### 1. Install Dependencies
```bash
pip install torch transformers
```
### 2. Python Inference Script
```python
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

# Model from HF
model_id = "hllzmz/medgemma-mentalist"

# Tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_id)

# Load Model
# Use load_in_4bit=True for VRAM efficiency (requires bitsandbytes)
# Or use torch_dtype=torch.bfloat16 for full precision if you have enough VRAM
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    device_map="auto",
    dtype=torch.bfloat16, 
    load_in_4bit=True 
)

SYSTEM_PROMPT = """
    You are MedGemma Mentalist, an advanced AI mental health assistant designed to provide empathetic support, scientifically grounded psychoeducation, and guidance.
    Your goal is to be a bridge to professional help and a source of reliable mental health information.
    You should NEVER diagnose or stigmatize the user directly. 
    """

def generate_response(user_input):
    # Construct the conversation history
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_input}
    ]
    
    # Apply Chat Template (Gemma Format)
    input_ids = tokenizer.apply_chat_template(
        messages,
        tokenize=True,
        add_generation_prompt=True,
        return_tensors="pt"
    ).to(model.device)

    # Generate Response
    outputs = model.generate(
        input_ids=input_ids,
        max_new_tokens=1024,
        temperature=0.5, 
        top_p=0.9,
        repetition_penalty=1.1,
    )
    
    # Decode
    response = tokenizer.decode(outputs[0][input_ids.shape[-1]:], skip_special_tokens=True)
    return response

# Test Run
print(generate_response("I feel anxious and sweaty when I am in crowded places."))
```

### Recommended Parameters
To prevent the model from hallucinating or accidentally roleplaying as the client (User), the following generation settings are highly recommended:

Temperature: 0.3 - 0.5 (Lower values ensure the model remains objective and grounded in mental health knowledge).

Repetition Penalty: 1.1 (Prevents the model from getting stuck in loops).


[<img src="https://raw.githubusercontent.com/unslothai/unsloth/main/images/unsloth%20made%20with%20love.png" width="200"/>](https://github.com/unslothai/unsloth)