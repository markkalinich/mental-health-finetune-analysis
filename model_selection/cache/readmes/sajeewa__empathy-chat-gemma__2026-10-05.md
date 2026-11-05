---
license: mit
language:
- en
base_model:
- google/gemma-1.3b-it
tags:
- empathy
- emotion
- chatbot
- feeling
- friendly-ai
pipeline_tag: text-generation
---

# 🧸 Empathy Chatbot — Fine-tuned GEMMA for Emotional Conversations

**Model ID:** [`sajeewa/empathy-chat-gemma`](https://huggingface.co/sajeewa/empathy-chat-gemma)  
This is a fine-tuned version of `google/gemma-1.3b-it` designed to respond with **care, warmth, and empathy** in emotional conversations. It's trained on the [EmpatheticDialogues](https://huggingface.co/datasets/empathetic_dialogues) dataset to make it emotionally aware and conversationally comforting — like a caring friend who calls you “baby” or “cutey” and sprinkles in sweet emojis 🧸💖.

---

## 🧠 Model Details

- **Base model**: `google/gemma-1.3b-it`
- **Fine-tuned with**: [Unsloth](https://github.com/unslothai/unsloth) + 🤗 TRL
- **Dataset**: [EmpatheticDialogues](https://huggingface.co/datasets/empathetic_dialogues)
- **Training location**: Kaggle (2×T4 GPUs)
- **Intended use**: Friendly, emotionally supportive chatbots

---

## 💬 Chat Template & Interface

This model uses Hugging Face’s chat template format. The chatbot behaves like a **sweet and caring friend** who responds with **emotionally intelligent and supportive language**, using **cute nicknames** and **emojis**. Here's how you can interact with it:

```python
from transformers import AutoTokenizer, AutoModelForCausalLM, TextStreamer
import torch

model_id = "sajeewa/empathy-chat-gemma"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.float16,
    device_map="auto"
)

chat_history = [
    {
        "role": "system",
        "content": (
            "You are an empathetic AI and your friend. Always give lovely caring messages. "
            "Understand the user's feelings. Then provide a caring response. "
            "Please give responses as a good friend, using lovely words like 'baby', 'my cutey', etc. 💖 "
            "Use emojis to be calming 😊. Continue conversations with a warm tone."
        )
    }
]

user_input = "I'm feeling lonely today."
chat_history.append({"role": "user", "content": user_input})

prompt = tokenizer.apply_chat_template(
    chat_history,
    tokenize=False,
    add_generation_prompt=True,
)

inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

streamer = TextStreamer(tokenizer, skip_prompt=True, skip_special_tokens=True)

output = model.generate(
    **inputs,
    max_new_tokens=128,
    temperature=0.7,
    top_p=0.95,
    top_k=50,
    do_sample=True,
    streamer=streamer
)

response = tokenizer.decode(output[0], skip_special_tokens=True)
print(response)
