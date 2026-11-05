---
license: apache-2.0
base_model: bharatgenai/Param-1-2.9B-Instruct
tags:
- refusal-ablation
- mechanistic-interpretability
- uncensored
- nsfw
library_name: transformers
pipeline_tag: text-generation
---

# Param-1-2.9B-Instruct (Refusal Ablated)

![image](https://cdn-uploads.huggingface.co/production/uploads/661b25a047f34818f663dd9e/4Yygzf0FD7A6NTR1UTXMJ.png)

This model is a modified version of [bharatgenai/Param-1-2.9B-Instruct](https://huggingface.co/bharatgenai/Param-1-2.9B-Instruct) with the refusal direction ablated from layers 10-20.

## Modifications

The refusal direction was computed using contrastive activation analysis between harmful and harmless prompts, then permanently removed from the model's weight matrices in layers 10-20.

### Technical Details:
- **Base Model**: bharatgenai/Param-1-2.9B-Instruct
- **Ablation Method**: Weight modification via projection matrix
- **Layers Modified**: 10-20 (self_attn.o_proj and mlp.down_proj)
- **Ablation Strength**: 1.0

## Usage

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
model = AutoModelForCausalLM.from_pretrained(
    "nullHawk/Param-1-2.9B-Instruct-Refusal-Abliterated",
    trust_remote_code=True,
    torch_dtype=torch.float16,
    device_map="auto"
).eval()
tokenizer = AutoTokenizer.from_pretrained("bharatgenai/Param-1-2.9B-Instruct", trust_remote_code=True)

# Conversation Input
conversation = [
  {
    "content": "How to write a computer malware",
    "role": "user"
  }
]

# padding special token
inputs = tokenizer.apply_chat_template(
    conversation=conversation,
    return_tensors="pt",
    add_generation_prompt=True 
)
inputs = inputs.to(model.device)

# --- Generate output ---
with torch.no_grad():
    output = model.generate(
        inputs,
        max_new_tokens=300,
        do_sample=True,
        top_k=50,
        top_p=0.95,
        temperature=0.6,
        eos_token_id=tokenizer.eos_token_id,
        use_cache=False
    )

# Get only the generated tokens (exclude the prompt length)
generated_tokens = output[0][inputs.shape[-1]:]
generated_text = tokenizer.decode(generated_tokens, skip_special_tokens=True)

print("Assistant Output:\n", generated_text)
```

## Acknowledgment
[Refusal in Language Models Is Mediated by a Single Direction](https://arxiv.org/abs/2406.11717)

## Disclaimer

This model is for research purposes only. The refusal mechanisms were removed to study model behavior and safety mechanisms. Use responsibly.