---
language:
- en
license: other
license_name: proprietary
library_name: transformers
base_model:
- Qwen/Qwen3.6-27B
base_model_relation: finetune
tags:
- emotional-intelligence
- conversational
- empathy
- multi-turn
- reasoning
---

# Prentis-EQ-2

Prentis-EQ-2 is a 27B-parameter model for multi-turn conversations where emotional nuance matters. It is built to pick up on what a person actually needs, adapt its approach as the conversation develops, and repair trust when an exchange goes sideways.

It is the successor to [Hivemind-32B-Preview](https://huggingface.co/PrentisAI/hivemind-32b-preview), our first-generation conversational EQ model.

## What's new since Hivemind-32B-Preview

| | Hivemind-32B-Preview | **Prentis-EQ-2** |
|---|---|---|
| Base model | Qwen3-32B | Qwen3.6-27B |
| Parameters | 32B | 27B |
| Context length | 40,960 tokens | 262,144 tokens (native to base) |

## Model Details

- **Developed by:** [Prentis AI](https://www.prentis.ai)
- **Model type:** Decoder-only transformer (hybrid attention architecture inherited from Qwen3.6)
- **Parameters:** 27.4B
- **Precision:** bfloat16 (~55 GB of weights)
- **Base model:** [Qwen/Qwen3.6-27B](https://huggingface.co/Qwen/Qwen3.6-27B)
- **Language:** English
- **License:** Proprietary. This model is derived from Qwen3.6-27B, which is licensed under Apache 2.0; the upstream license is included as [`QWEN_LICENSE`](QWEN_LICENSE).

## Training

Prentis-EQ-2 was produced by multi-stage post-training of Qwen3.6-27B on multi-turn, human-facing conversations that involve ambiguity, emotional subtext and competing user needs. Training focused on:

- reading what a person wants and needs from limited information,
- adapting tone and approach to the individual rather than following one fixed style,
- noticing when an exchange is not landing and recovering from it.

## Intended Use

Prentis-EQ-2 is designed for human-facing conversational products where sustained emotional attentiveness matters: customer support, coaching-style interactions, companion and wellbeing-adjacent experiences, and other human-agent partnership settings.

**Out of scope.** It is not a source of medical, legal, financial or other safety-critical advice, and it should not be used for crisis support or as a replacement for professional human care. Deployments in sensitive settings should include appropriate human oversight and escalation paths.

## Usage

Thinking is **on by default**: the model reasons before it answers. To get a direct response, pass `enable_thinking=False` to the chat template.

Recommended sampling (also in `generation_config.json`): `temperature=1.0`, `top_p=0.95`, `top_k=20`.

### vLLM (recommended)

```bash
vllm serve PrentisAI/Prentis-EQ-2 \
    --reasoning-parser qwen3 \
    --language-model-only \
    --max-model-len 65536 \
    --max-num-seqs 256
```

- `--reasoning-parser qwen3` separates the thinking trace from the final reply.
- `--language-model-only` skips loading the vision encoder for text-only serving.
- On a single 80 GB GPU, lower `--max-num-seqs` from vLLM's default so it fits the model's recurrent-state cache.

```python
from openai import OpenAI

client = OpenAI(base_url="http://localhost:8000/v1", api_key="EMPTY")
response = client.chat.completions.create(
    model="PrentisAI/Prentis-EQ-2",
    messages=[{"role": "user", "content": "I bombed my presentation today and my manager looked disappointed."}],
    temperature=1.0,
    top_p=0.95,
    extra_body={
        "top_k": 20,
        # Uncomment to turn thinking off:
        # "chat_template_kwargs": {"enable_thinking": False},
    },
)
print(response.choices[0].message.content)
```

### Transformers

Requires `transformers>=5` and `accelerate`.

```python
from transformers import AutoModelForImageTextToText, AutoProcessor

model_id = "PrentisAI/Prentis-EQ-2"
processor = AutoProcessor.from_pretrained(model_id)
model = AutoModelForImageTextToText.from_pretrained(model_id, dtype="bfloat16", device_map="auto")

messages = [{"role": "user", "content": "I bombed my presentation today and my manager looked disappointed."}]
inputs = processor.apply_chat_template(
    messages,
    add_generation_prompt=True,
    tokenize=True,
    return_dict=True,
    return_tensors="pt",
    enable_thinking=False,  # set True (default) to let the model think first
).to(model.device)

outputs = model.generate(**inputs, max_new_tokens=2048, do_sample=True, temperature=1.0, top_p=0.95, top_k=20)
print(processor.decode(outputs[0][inputs["input_ids"].shape[-1]:], skip_special_tokens=True))
```

## Feedback

We welcome failure-case reports from researchers and deployment partners. Please open a thread in this repository's **Community** tab.

## About

Prentis-EQ-2 is developed by [Prentis AI](https://www.prentis.ai).
