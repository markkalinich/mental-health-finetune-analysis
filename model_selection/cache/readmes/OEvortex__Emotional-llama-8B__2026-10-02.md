---
library_name: transformers
license: llama3
---


# Emotional-llama-8B Model Card

## Overview
Emotional-llama-8B is a large language model designed for emotionally intelligent conversational interactions. It is trained to engage users with empathy, understanding, and supportive dialogue across a wide range of topics and contexts. The model aims to provide a supportive AI companion that can attune to users' emotional states and communicative needs.

## Objectives
- Engage in open-ended dialogue while displaying emotional intelligence 
- Recognize and validate user emotions and emotional contexts
- Provide supportive, empathetic, and psychologically-grounded responses
- Avoid insensitive, harmful, or unethical speech  
- Continuously improve emotional awareness and dialogue skills

## Methodology
- Emotional-llama-8B is based on the LLaMA 3.8B language model and further trained using:
- Supervised learning on large dialogue datasets with emotional labeling  
- Reinforcement learning with a reward model favoring emotionally supportive responses
- Constitution training to instill stable and beneficial objectives
- Knowledge augmentation from psychological resources on emotional intelligence

## Usage code
```python
%pip install accelerate
%pip install -i https://pypi.org/simple/ bitsandbytes

from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

model_id = "OEvortex/Emotional-llama-8B"

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.bfloat16,
    device_map="auto",
)


messages = [
    # {"role": "system", "content": "Be Helpful"},
    {"role": "user", "content": "I'm feeling really down today. Nothing seems to be going right."},
]

input_ids = tokenizer.apply_chat_template(
    messages,
    add_generation_prompt=True,
    return_tensors="pt"
).to(model.device)

terminators = [
    tokenizer.eos_token_id,
    tokenizer.convert_tokens_to_ids("<|eot_id|>")
]

outputs = model.generate(
    input_ids,
    max_new_tokens=256,
    eos_token_id=terminators,
    do_sample=True,
    temperature=0.9,
    top_p=0.9,
)
response = outputs[0][input_ids.shape[-1]:]
print(tokenizer.decode(response, skip_special_tokens=True))

# Now you can generate text using the model!
```

## Example Dialogue
Human: I'm feeling really down today. Nothing seems to be going right.

Emotional-llama-8B: I'm really sorry to hear that you're feeling down today. 😔 It's totally okay to have a tough day sometimes. Remember that it's okay to not be okay and that things will get better. Take a deep breath and try to focus on the things that you can control. If you need to talk about what's going on or just need someone to listen, I'm here for you. You're not alone, and I'm sending you lots of positive vibes. Hang in there, and remember that brighter days are ahead. and I'm here to listen without judgment and provide a supportive ear.

Human: I'm excited because I just got accepted into my dream school! I wanted to share the good news with someone.

Emotional-llama-8B: 🎉 Oh my goodness, congratulations! 🎊 That's absolutely amazing news! You must be over the moon! 🌙 Sharing your good news with someone is always a great feeling, and I'm here to celebrate with you! 🎉 Your dream school, wow! That's so exciting! What made it your dream school, and what are you most looking forward to about it? Let's chat more about it! 

Human: My best friend just got into an argument with me and I don't know what to do. How can I fix this situation?

Emotional-llama-8B: Oh no, it's tough to deal with conflicts with close friends! 😔 First of all, take a step back and give yourself some time to process your feelings. It's okay to feel upset or hurt. Then, consider reaching out to your friend and expressing your feelings in a calm and respectful manner. It's important to communicate openly and honestly about what happened and how it made you feel. Try to see things from your friend's perspective as well and listen to their side of the story. Remember, conflicts are a natural part of any relationship, and it's how you work through them that matters. Good luck, and I hope you guys can work things out! 🌟