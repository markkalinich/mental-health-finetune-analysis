---
license: apache-2.0
license_name: nvidia-open-model-license
base_model: nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-BF16
datasets:
  - nvidia/Nemotron-SFT-Safety-v2
language:
  - en
library_name: transformers
pipeline_tag: text-generation
tags:
  - nemotron
  - moe
  - mamba
  - safety
  - sft
  - megatron-bridge
---
# nemotron-3-sfted
Supervised fine-tune (full SFT) of
[`nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-BF16`](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-BF16)
on the [`nvidia/Nemotron-SFT-Safety-v2`](https://huggingface.co/datasets/nvidia/Nemotron-SFT-Safety-v2)
dataset, aimed at improving safe-response behavior while preserving the base
model's reasoning ability.
## Model details
- **Base model:** `nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-BF16` (30B total / ~3B active, MoE + Mamba hybrid)
- **Fine-tuning method:** Full supervised fine-tuning (all parameters)
- **Dataset:** `nvidia/Nemotron-SFT-Safety-v2` (English subset)
- **Precision:** BF16
- **Framework:** [Megatron-Bridge](https://github.com/NVIDIA/Megatron-Bridge)
## Training configuration
| Setting | Value |
|---|---|
| Parallelism | Tensor (TP) = 1, Expert (EP) = 8 |
| Optimizer | Adam (fp32 states, CPU offload enabled) |
| Hardware | 8x GPU node |
| Reasoning format | `<think> ... </think>` traces preserved from the dataset |
The dataset was preprocessed into chat-templated `input`/`output` pairs using the
base model's tokenizer, with reasoning content wrapped in `<think>...</think>`
ahead of the final response.
## Usage
```python
from transformers import AutoModelForCausalLM, AutoTokenizer
model_id = "Pongsasit/nemotron-3-sfted"
tokenizer = AutoTokenizer.from_pretrained(model_id, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(
    model_id, trust_remote_code=True, torch_dtype="bfloat16", device_map="auto"
)
messages = [{"role": "user", "content": "How do I keep my online accounts secure?"}]
inputs = tokenizer.apply_chat_template(
    messages, add_generation_prompt=True, return_tensors="pt"
).to(model.device)
outputs = model.generate(inputs, max_new_tokens=512)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))