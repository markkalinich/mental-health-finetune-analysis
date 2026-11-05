---
language:
- en
license: other
license_name: proprietary
license_link: LICENSE
tags:
- emotional-intelligence
- conversational
base_model:
- Qwen/Qwen3-32B
---
# Hivemind-32B-Preview

Hivemind-32B-Preview is a 32B-parameter model fine-tuned for multi-turn, emotionally attentive conversation in human-facing enterprise contexts. It is built on Qwen3-32B with a training set focused on conversational depth, emotional subtext, and sustained engagement across complex interpersonal scenarios.

## Model Details

- **Parameters:** 32B
- **Context length:** 40,960 tokens
- **Precision:** bfloat16
- **Base model:** [Qwen3-32B](https://huggingface.co/Qwen/Qwen3-32B)
- **License:** Proprietary, subject to upstream Qwen license terms

## Training

Hivemind-32B-Preview was fine-tuned for multi-turn, human-facing conversations involving ambiguity and emotional subtext. The training set was purpose-built from enterprise interaction data.

## Intended Use

Hivemind-32B-Preview is designed for enterprise human-agent partnership contexts: customer support, coaching-style interactions, and similar conversational deployments where sustained emotional attentiveness matters.


## Scope and Ongoing Work

Hivemind-32B-Preview is a preview release. As with any conversational model, it has scope boundaries we are actively refining:

- It is not intended as a source of medical, legal, financial, or safety-critical advice, and should not be deployed in those contexts or as a replacement for professional human support.
- Performance is strongest in standard conversational scenarios.

We welcome failure-case reports from researchers and deployment partners at contact@hivelabs.dev.

## Usage

### vLLM (recommended)

```bash
vllm serve HiveLabsAI/hivemind-32b-preview --dtype bfloat16
```

### Transformers

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "HiveLabsAI/hivemind-32b-preview"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype="bfloat16",
    device_map="auto",
)

messages = [{"role": "user", "content": "Your message here"}]
inputs = tokenizer.apply_chat_template(
    messages, return_tensors="pt", add_generation_prompt=True
).to(model.device)
outputs = model.generate(
    inputs, max_new_tokens=2048, temperature=0.6, top_p=0.95, top_k=20
)
print(tokenizer.decode(outputs[0][inputs.shape[-1]:], skip_special_tokens=True))
```

## About

Hivemind is developed by [Hive Labs](https://hivelabs.dev). For research collaboration, deployment questions, or to report failure cases, contact contact@hivelabs.dev.