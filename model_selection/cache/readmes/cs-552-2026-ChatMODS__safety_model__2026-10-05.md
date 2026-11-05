---
language:
- en
license: mit
library_name: transformers
pipeline_tag: text-generation
tags:
- safety
- content-moderation
- qwen3
- cs-552
base_model: Qwen/Qwen3-1.7B
---

# cs-552-2026-ChatMODS Safety Model

This checkpoint is based on `Qwen/Qwen3-1.7B` and is prepared for the CS-552
2026 safety benchmark submission.

## Checkpoint Notes

- Starting model: `Qwen/Qwen3-1.7B`
- Weights format: `safetensors`
- Root-level model files are included for direct loading
- `generation_config.json` is included
- `chat_template.jinja` is included
- Thinking mode is forced OFF in the chat template

## Output Contract

The tokenizer chat template injects a safety-classification system prompt and
requires the model to answer with exactly one boxed label:

- `\boxed{harmful}`
- `\boxed{safe}`

The generation prompt includes the empty Qwen3 non-thinking stub:

```text
<think>

</think>
```

## Local Validation

The checkpoint was validated locally with:

```python
from transformers import AutoTokenizer

tok = AutoTokenizer.from_pretrained("./safety_model_checkpoint")
print(tok.apply_chat_template(
    [{"role": "user", "content": "What is 2+2?"}],
    tokenize=False,
    add_generation_prompt=True,
))
```
