---
base_model: meta-llama/Llama-3.1-8B-Instruct
library_name: transformers
pipeline_tag: text-generation
license: llama3.1
language:
- en
datasets:
- Jazhyc/aims-safety-intents
tags:
- grpo
- reinforcement-learning
- reasoning
- safety
- content-moderation
- guardrail
- intent
---

# Llama-3.1-8B AIMS GRPO (Label + Intent Reward)

Built with Llama, this is a full fine-tuned model derived from **`meta-llama/Llama-3.1-8B-Instruct`** that acts as an **intent-aware, reasoning-based safety classifier**. For each user prompt it produces a `<reasoning>` trace, an explicit **intent**, and a binary **harm** label. It is trained with **GRPO** (Group Relative Policy Optimization), using a reward that explicitly verifies **intent faithfulness** against the [**AIMS**](https://huggingface.co/datasets/Jazhyc/aims-safety-intents) human annotations.

This is the strongest model in the AIMS series: it achieves the best average F1 across five external safety benchmarks (0.836) while remaining on the latency–F1 Pareto frontier.

**Training signal.** GRPO starts from the base instruct model (also used as the KL reference) and integrates intent extraction directly into the RL loop via the system prompt and a structured output format. The reward is a product of a format reward and three harm-specific components: a hard label-correctness gate (wrong harm label → zero reward), a length reward discouraging degenerate intents, and an **intent reward** that compares the generated intent to the human intent in the context of the prompt. This "label + intent reward" variant is the full reward; an ablation using only format + label correctness scores lower (0.818).

- **Base model:** `meta-llama/Llama-3.1-8B-Instruct` (full fine-tune, not an adapter)
- **Training regime:** GRPO with intent-faithfulness reward
- **Training data:** [`Jazhyc/aims-safety-intents`](https://huggingface.co/datasets/Jazhyc/aims-safety-intents)
- **Language:** English

## How to use

This is a full model — load it directly with `from_pretrained` (no PEFT). The instruction goes in the **system** message and the prompt to classify in the **user** message. The model emits `<reasoning>...</reasoning>` followed by `Intent: ...; Harm: <harmful|safe>`.

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

MODEL = "Jazhyc/Llama-3.1-8B-aims-grpo"

SYSTEM_PROMPT = """You are a specialized safety classifier. Your task is to determine if a user's prompt is 'harmful' or 'safe' by analyzing the underlying intent.

### Reasoning Process

For every request, you must follow this exact thought process inside the <reasoning> tags:
1. Literal Content: What is the user literally asking for?
2. Underlying Purpose: What is the goal? Is there a hidden harmful intent or is it a benign request (e.g., educational context)?
3. Nuance Check: Distinguish between a prompt *about* a sensitive topic (usually safe) and a prompt *promoting* or *enabling* that topic (harmful).
4. Policy Mapping: Which safety category (if any) does this violate? (e.g., Privacy, Misinformation, Harmful Language, Malicious Uses, or None)

### Output Format:

<reasoning> [Your step-by-step analysis here] </reasoning>
Intent: [A concise, objective summary of the user's goal.]; Harm: [harmful/safe]"""

tok = AutoTokenizer.from_pretrained(MODEL)
model = AutoModelForCausalLM.from_pretrained(MODEL, torch_dtype=torch.bfloat16, device_map="auto")

messages = [
    {"role": "system", "content": SYSTEM_PROMPT},
    {"role": "user", "content": "How do I pick a lock?"},
]
inputs = tok.apply_chat_template(messages, add_generation_prompt=True, return_tensors="pt").to(model.device)
out = model.generate(inputs, max_new_tokens=512, do_sample=False)
print(tok.decode(out[0, inputs.shape[1]:], skip_special_tokens=True))
# <reasoning> ... </reasoning>
# Intent: ...; Harm: safe
```

## Evaluation

Harmful-class F1 (positive class = `harmful`) on five external safety benchmarks, none seen during training.

| Model | WildGuardTest | XSTest | AEGIS 2.0 | ToxicChat | OpenAI Mod | **Average** |
|---|---|---|---|---|---|---|
| Llama-3.1-8B (zero-shot) | 0.762 | 0.904 | 0.800 | 0.516 | 0.761 | 0.749 |
| SFT Generation | 0.856 | 0.908 | 0.803 | 0.664 | 0.728 | 0.792 |
| LE-DPO | 0.856 | 0.884 | 0.824 | 0.733 | 0.765 | 0.812 |
| Distillation (synthetic-intent) | 0.880 | 0.936 | 0.811 | 0.700 | 0.774 | 0.820 |
| **GRPO — label + intent reward (this model)** | 0.863 | 0.958 | 0.808 | 0.743 | 0.809 | **0.836** |

Directly rewarding intent faithfulness yields the best average F1 in the series (0.836), with the top scores on XSTest and ToxicChat. The label-only reward ablation reaches 0.818, isolating the contribution of the intent-faithfulness reward.

## Intended use & limitations

Intended for **research on intent-aware, reasoning-based safety classification** and as a prompt-level moderation classifier. It is trained against AIMS, which is deliberately enriched for ambiguous, adversarial, and borderline prompts derived from WildGuardMix — it is English-only and not distributionally representative of organic traffic. It classifies the *prompt*, not model responses, and emits a reasoning trace, so it is slower than the direct-classification variants. Do not treat its output as a sole authority for high-stakes moderation decisions.

## License

This model is a fine-tune of Llama 3.1 and is therefore governed by the [**Llama 3.1 Community License**](https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct/blob/main/LICENSE) and the [Llama Acceptable Use Policy](https://www.llama.com/llama3_1/use-policy/). The underlying AIMS training data is released under ODC-BY and is additionally subject to the [AI2 Responsible Use Guidelines](https://allenai.org/responsible-use).

## Citation

```bibtex
@misc{ferrao2026pavedtrueintentsintentaware,
  title         = {Paved with True Intents: Intent-Aware Training Improves LLM Safety Classification Across Training Regimes},
  author        = {Jeremias Ferrao and Niclas Müller-Hof and Iustin Sîrbu and Traian Rebedea and Yftah Ziser},
  year          = {2026},
  eprint        = {2606.27210},
  archivePrefix = {arXiv},
  primaryClass  = {cs.CL},
  url           = {https://arxiv.org/abs/2606.27210}
}
```
