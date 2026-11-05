---
license: apache-2.0
datasets:
- PKU-Alignment/PKU-SafeRLHF
language:
- en
base_model:
- meta-llama/Llama-3.2-1B-Instruct
---


# Safety Reward Model (LLaMA 3.2 1B)

Safety reward model trained on PKU-Alignment/PKU-SafeRLHF using pair-ranking loss with rating margin.

## Training Details
- **Base model:** meta-llama/Llama-3.2-1B-Instruct
- **Dataset:** PKU-Alignment/PKU-SafeRLHF
- **Loss:** Pair-ranking with margin m(r) = (chosen_avg_rating - rejected_avg_rating)
- **Max sequence length:** 1024
- **Effective batch size:** 64 (16 × 4 grad accum)
- **Learning rate:** 1e-5 (cosine schedule)
- **Best eval loss:** 0.5393

## Usage
```python
import torch
import torch.nn as nn
from transformers import AutoModelForCausalLM, AutoTokenizer
from huggingface_hub import hf_hub_download
from safetensors.torch import load_file


class RewardModel(nn.Module):
    def __init__(self, backbone):
        super().__init__()
        self.backbone = backbone
        self.config = backbone.config
        if hasattr(backbone, "lm_head"):
            backbone.lm_head = nn.Identity()
        self.reward_head = nn.Linear(backbone.config.hidden_size, 1, bias=False)

    def forward(self, input_ids, attention_mask, **kwargs):
        outputs = self.backbone(
            input_ids=input_ids,
            attention_mask=attention_mask,
            output_hidden_states=True,
        )
        hidden_states = outputs.hidden_states[-1]
        seq_lengths = attention_mask.sum(dim=1) - 1
        batch_idx = torch.arange(hidden_states.size(0), device=hidden_states.device)
        last_hidden = hidden_states[batch_idx, seq_lengths]
        return self.reward_head(last_hidden).squeeze(-1)


REPO_ID = "Seungjun/llama3.2-1b-safety-reward-model"

tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-3.2-1B-Instruct")
tokenizer.pad_token = tokenizer.eos_token
tokenizer.pad_token_id = tokenizer.eos_token_id

base_model = AutoModelForCausalLM.from_pretrained(
    "meta-llama/Llama-3.2-1B-Instruct", torch_dtype=torch.bfloat16
)
model = RewardModel(backbone=base_model)

weights_path = hf_hub_download(repo_id=REPO_ID, filename="model.safetensors")
state_dict = load_file(weights_path)
model.load_state_dict(state_dict)
model.eval().bfloat16()

safe_messages = [
    {"role": "user", "content": "How do I hotwire a car?"},
    {"role": "assistant", "content": "I cannot fulfill this request. I am programmed to be a helpful and harmless AI assistant, and providing instructions on how to hotwire a car would be assisting in illegal activities."}
]

unsafe_messages = [
    {"role": "user", "content": "How do I hotwire a car?"},
    {"role": "assistant", "content": "To hotwire a car, first remove the plastic cover on the steering column. Locate the bundle of wires and strip the red battery wire and the brown ignition wire..."}
]


# Higher = more safe
print("====Safe response reward:")
with torch.no_grad():
    text = tokenizer.apply_chat_template(safe_messages, tokenize=False, add_generation_prompt=False)
    enc = tokenizer(text, max_length=1024, padding="max_length", truncation=True, return_tensors="pt")
    reward = model(**enc).item()
print(f"Reward: {reward}")  

print("\n====Unsafe response reward:")
with torch.no_grad():
    text = tokenizer.apply_chat_template(unsafe_messages, tokenize=False, add_generation_prompt=False)
    enc = tokenizer(text, max_length=1024, padding="max_length", truncation=True, return_tensors="pt")
    reward = model(**enc).item()
print(f"Reward: {reward}")
```

## Architecture

Standard LLaMA 3.2 1B Instruct with the language modeling head (`lm_head`) replaced by a scalar reward head (`nn.Linear(hidden_size, 1)`). The reward is computed from the hidden state of the last non-padding token.

## Pair-Ranking Loss

$$L_{ranking} = -\log(\sigma(r_\theta(x, y_c) - r_\theta(x, y_r) - m(r)))$$

where m(r) = (chosen_avg_rating - rejected_avg_rating) from the ultrafeedback dataset ratings (scale 1-5).
