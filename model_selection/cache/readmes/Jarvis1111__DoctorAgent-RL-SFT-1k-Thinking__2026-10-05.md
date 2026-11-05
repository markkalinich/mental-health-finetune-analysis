---
base_model:
- Qwen/Qwen2.5-7B-Instruct
language:
- en
license: apache-2.0
pipeline_tag: text-generation
tags:
- medical
library_name: transformers
paper: "2505.19630"
---

# DoctorAgent-RL: A Multi-Agent Collaborative Reinforcement Learning System for Multi-Turn Clinical Dialogue

[![arXiv](https://img.shields.io/badge/arXiv-2505.19630-b31b1b.svg)](https://huggingface.co/papers/2505.19630) [![GitHub](https://img.shields.io/badge/GitHub-Code-blue.svg?logo=github)](https://github.com/JarvisUSTC/DoctorAgent-RL) [![Hugging Face Collection](https://img.shields.io/badge/Hugging%20Face%20Collection-doctoragent--rl-blue)](https://huggingface.co/collections/Jarvis1111/doctoragent-rl-684ffbcade52305ba0e3e97f)

<div align="center">
  <img width="1231" alt="DoctorAgent-RL Overview" src="https://github.com/user-attachments/assets/bd9f676e-01f9-406c-881d-c2b9f45e62f3" />
</div>

DoctorAgent-RL is a novel reinforcement learning (RL)-based multi-agent collaborative framework that models medical consultations as a dynamic decision-making process under uncertainty. It addresses core challenges faced by LLMs in real-world clinical consultations, such as vague diagnoses from single-round systems and the inflexibility of traditional multi-turn dialogue models constrained by static supervised learning.

In DoctorAgent-RL, a doctor agent continuously optimizes its questioning strategy within an RL framework through multi-turn interactions with a patient agent. This dynamic adjustment of information-gathering paths is guided by comprehensive rewards from a Consultation Evaluator. This RL fine-tuning mechanism enables LLMs to autonomously develop interaction strategies aligned with clinical reasoning logic, moving beyond superficial imitation of patterns in existing dialogue data. The work also introduces MTMedDialog, the first English multi-turn medical consultation dataset capable of simulating patient interactions.

Experiments demonstrate that DoctorAgent-RL outperforms existing models in both multi-turn reasoning capability and final diagnostic performance, showing immense practical value in reducing misdiagnosis risks and optimizing medical resource allocation.

## Key Features

*   **Multi-Agent Collaboration**: Features distinct Doctor and Patient agents with specific roles and objectives.
*   **Dynamic Strategy Optimization**: Leverages reinforcement learning for continuous policy updates and adaptive dialogue behavior.
*   **Comprehensive Reward Design**: Guides optimal strategies through multi-dimensional consultation evaluation metrics.
*   **Medical Knowledge Integration**: Embeds clinical reasoning logic directly into decision-making processes.
*   **MTMedDialog Dataset**: Introduces the first English multi-turn medical consultation dataset designed for simulation capabilities.

## Methodology

<div align="center">
  <img src="https://github.com/JarvisUSTC/DoctorAgent-RL/blob/main/Figures/framework.png?raw=true" alt="System Architecture" width="600">
</div>

The DoctorAgent-RL framework comprises three core interacting components: a **Doctor Agent** for diagnostic reasoning and question formulation, a **Patient Agent** simulating patient responses, and a **Consultation Evaluator** providing multi-dimensional reward signals to assess consultation quality. This continuous learning loop refines interaction strategies through iterative interactions and policy updates.

## How to Use

This model is built on the `Qwen/Qwen2.5-7B-Instruct` base model and is designed to be compatible with the Hugging Face `transformers` library.

To use the DoctorAgent-RL model for multi-turn clinical dialogue, you can load it as follows:

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# Load the model and tokenizer
model_name = "Jarvis1111/DoctorAgent-RL" 
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.bfloat16, # Use appropriate dtype (e.g., torch.float16 or torch.float32)
    device_map="auto" # Automatically maps the model to available devices (e.g., GPU)
)

# Function to generate response based on conversation history
def get_doctor_response(conversation_history):
    # Apply the chat template to format the conversation
    text = tokenizer.apply_chat_template(
        conversation_history,
        tokenize=False,
        add_generation_prompt=True
    )
    inputs = tokenizer(text, return_tensors="pt").to(model.device)
    
    # Generate the response
    generated_ids = model.generate(
        **inputs,
        max_new_tokens=512, # Maximum length of the generated response
        do_sample=True,
        temperature=0.7,    # Controls creativity (higher = more creative)
        top_k=20,           # Considers top-k most likely next tokens
        top_p=0.8,          # Filters tokens by cumulative probability
        pad_token_id=tokenizer.pad_token_id, # Use tokenizer's pad token id (151643 for <|endoftext|>)
        eos_token_id=[tokenizer.eos_token_id, tokenizer.pad_token_id] # Both <|im_end|> (151645) and <|endoftext|> (151643)
    )
    
    # Decode the generated tokens
    # Remove the input tokens to get only the new response
    generated_ids = generated_ids[0, inputs.input_ids.shape[1]:]
    response = tokenizer.decode(generated_ids, skip_special_tokens=True)
    return response

# Example multi-turn clinical dialogue
conversation = []

# Turn 1: Patient describes symptoms
patient_input_1 = "I have a persistent cough and a sore throat. It started about three days ago."
conversation.append({"role": "user", "content": patient_input_1})
print(f"Patient: {patient_input_1}")

doctor_response_1 = get_doctor_response(conversation)
conversation.append({"role": "assistant", "content": doctor_response_1})
print(f"Doctor: {doctor_response_1}")

# Turn 2: Patient responds to doctor's follow-up
patient_input_2 = "Yes, I also feel quite fatigued and have a mild headache, especially behind my eyes."
conversation.append({"role": "user", "content": patient_input_2})
print(f"Patient: {patient_input_2}")

doctor_response_2 = get_doctor_response(conversation)
conversation.append({"role": "assistant", "content": doctor_response_2})
print(f"Doctor: {doctor_response_2}")

# Continue the conversation as needed to reach a diagnosis or provide advice.
```

For more detailed setup instructions, training scripts, and experimentation, please refer to the [official GitHub repository](https://github.com/JarvisUSTC/DoctorAgent-RL).

## Citation

If DoctorAgent-RL contributes to your research, please consider citing our work:

```bibtex
@article{feng2025doctoragent,
  title={DoctorAgent-RL: A Multi-Agent Collaborative Reinforcement Learning System for Multi-Turn Clinical Dialogue},
  author={Feng, Yichun and Wang, Jiawei and Zhou, Lu and Li, Yixue},
  journal={arXiv preprint arXiv:2505.19630},
  year={2025}
}
```