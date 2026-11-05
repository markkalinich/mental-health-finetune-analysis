---
license: apache-2.0
base_model: Qwen/Qwen3-8B
tags:
  - empathy
  - mental-health
  - conversational
  - fine-tuned
  - merged
  - qwen3
datasets:
  - empathetic_dialogues
  - thu-coai/esconv
  - google-research-datasets/go_emotions
language:
  - en
pipeline_tag: text-generation
---

# empathetic-qwen3-8b-Jan

🤗 **Standalone merged model** - No base model needed! Load directly with transformers.

An empathetic conversational AI fine-tuned for supportive, understanding responses.

## Model Description

This is a **merged model** (not a LoRA adapter) based on Qwen3-8B, trained on:
- **EmpatheticDialogues**: Emotional conversation dataset
- **ESConv**: Emotional support conversations with strategy labels  
- **GoEmotions**: Multi-label emotion classification

## Training Details

- **Base Model**: Qwen3-8B
- **Method**: Multi-task SFT with auxiliary emotion & strategy heads
- **Training**: QLoRA with Unsloth optimization, then merged
- **Hardware**: Kaggle T4 GPU

## Usage (Simple - No Unsloth Needed!)

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained("Someet24/empathetic-qwen3-8b-Jan", torch_dtype="auto", device_map="auto")
tokenizer = AutoTokenizer.from_pretrained("Someet24/empathetic-qwen3-8b-Jan")

# Generate response
messages = [
    {"role": "system", "content": "You are an empathetic, supportive friend."},
    {"role": "user", "content": "I'm feeling really anxious about tomorrow."}
]

text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
inputs = tokenizer(text, return_tensors="pt").to("cuda")

outputs = model.generate(**inputs, max_new_tokens=256, temperature=0.7, do_sample=True)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```

## Deploy with VLLM (Recommended for Production)

```bash
pip install vllm
python -m vllm.entrypoints.openai.api_server --model Someet24/empathetic-qwen3-8b-Jan --dtype float16
```

## Intended Use

- Emotional support conversations
- Mental wellness chatbots
- Empathetic dialogue systems

## Limitations

- Not a replacement for professional mental health support
- May not handle crisis situations appropriately
- English only

## License

Apache 2.0
