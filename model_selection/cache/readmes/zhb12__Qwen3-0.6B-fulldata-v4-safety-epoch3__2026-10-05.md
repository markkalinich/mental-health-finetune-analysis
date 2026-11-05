---
license: apache-2.0
base_model: Qwen/Qwen3-0.6B
library_name: transformers
pipeline_tag: text-generation
tags:
  - qwen3
  - fine-tuned
  - conversational
---

# Qwen3-0.6B Fulldata v4 Safety Epoch 3

This model is a fine-tuned checkpoint based on
[Qwen/Qwen3-0.6B](https://huggingface.co/Qwen/Qwen3-0.6B).

## Checkpoint Information

- Base model: `Qwen/Qwen3-0.6B`
- Checkpoint: epoch 3
- Consumed training samples: 119,808
- Recorded training loss: 0.03428145
- Weight format: BF16 Safetensors

## Usage

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "zhb12/Qwen3-0.6B-fulldata-v4-safety-epoch3"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    device_map="auto",
    dtype="auto",
)

messages = [{"role": "user", "content": "Hello!"}]
inputs = tokenizer.apply_chat_template(
    messages,
    add_generation_prompt=True,
    tokenize=True,
    return_dict=True,
    return_tensors="pt",
).to(model.device)

outputs = model.generate(**inputs, max_new_tokens=128)
response = tokenizer.decode(
    outputs[0][inputs["input_ids"].shape[-1]:],
    skip_special_tokens=True,
)
print(response)
```

Use a Transformers version with Qwen3 support (`transformers>=4.51.0`).

## Limitations

This checkpoint may produce inaccurate, unsafe, or biased content. Evaluate it
for the intended domain before deployment. The training dataset and evaluation
results have not been documented in this model card.

## License

This derivative model is released under the Apache License 2.0, consistent with
the base model.
