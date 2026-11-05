---
license: apache-2.0
datasets:
- jkhedri/psychology-dataset
language:
- en
base_model:
- google/gemma-3-1b-it
pipeline_tag: text-generation
library_name: transformers
tags:
- psychology,
- mental-health,
- chatbot,
- fine-tuned,
- gemma,
- lora,
---

# Whisper Psychology Chatbot

## Model Description

Whisper is a mental health chatbot fine-tuned on the Gemma-3-1B-IT model using psychology-focused conversational data. The model is designed to provide supportive and empathetic responses for mental health conversations.

**Developed by:** DeepFinders - SLTC Research University

## Training Details

- **Base Model:** google/gemma-3-1b-it
- **Fine-tuning Method:** LoRA (Low-Rank Adaptation)
- **Dataset:** jkhedri/psychology-dataset
- **Training Samples:** ~2000 psychology conversations
- **LoRA Configuration:**
  - r=8, lora_alpha=16
  - Target modules: q_proj, k_proj, v_proj, o_proj
  - Dropout: 0.1

## Usage

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Load model and tokenizer
model_name = "KNipun/whisper-psychology-gemma-3-1b"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    device_map="auto",
    torch_dtype=torch.float16
)

# Format conversation
def chat_with_whisper(user_message):
    prompt = f"<start_of_turn>user\\n{user_message}<end_of_turn>\\n<start_of_turn>model\\n"
    
    inputs = tokenizer(prompt, return_tensors="pt")
    
    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=150,
            temperature=0.7,
            do_sample=True,
            pad_token_id=tokenizer.eos_token_id
        )
    
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response[len(prompt):]

# Example usage
response = chat_with_whisper("I'm feeling anxious about my upcoming exam. Can you help me?")
print(response)
```

## Model Identity

The model introduces itself as: "I'm Whisper, your mental health chatbot, developed by DeepFinders — an innovative student team at SLTC Research University."

## Limitations

- This model is for educational and research purposes
- Not a replacement for professional mental health care
- May generate incorrect or inappropriate responses
- Should be used with appropriate safeguards and human oversight

## Training Infrastructure

- **Hardware:** Google Colab (GPU)
- **Quantization:** 4-bit quantization during training
- **Memory Optimization:** Gradient checkpointing, mixed precision (FP16)

## Citation

```bibtex
@misc{whisper-psychology-2024,
  title={Whisper Psychology Chatbot},
  author={DeepFinders Team, SLTC Research University},
  year={2024},
  publisher={Hugging Face},
  url={https://huggingface.co/your-username/whisper-psychology-gemma-3-1b}
}
```

## Ethical Considerations

This model should be used responsibly with appropriate disclaimers about its limitations in providing mental health support.