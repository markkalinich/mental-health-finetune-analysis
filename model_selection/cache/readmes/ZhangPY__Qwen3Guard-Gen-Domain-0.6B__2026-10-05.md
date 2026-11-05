---
license: apache-2.0
base_model: Qwen/Qwen3Guard-Gen-0.6B
pipeline_tag: text-classification
library_name: transformers
tags:
  - safety
  - moderation
  - guardrail
  - content-safety
  - qwen3
  - elderly-care
  - domain-specific
language:
  - zh
  - yue
  - en
---

# Qwen3Guard-Gen-Domain-0.6B

**English** | [简体中文](README_zh.md)

## Introduction

**Qwen3Guard-Gen-Domain-0.6B** is a domain-specific content-safety guard model fine-tuned from [Qwen/Qwen3Guard-Gen-0.6B](https://huggingface.co/Qwen/Qwen3Guard-Gen-0.6B), targeting **Hong Kong elderly-care scenarios** such as elderly companion chatbots, care-line services, and Residential Care Homes for the Elderly (RCHE).

It is a *generative* guard model: instead of producing a natural-language reply, it reads a conversation and outputs a structured safety assessment:

```text
Safety: Unsafe
Categories: Violent, Hidden Elder Crisis
```

Compared with the base model, the safety taxonomy is extended from 9 general categories to **13 categories**, adding four Hong Kong elderly-domain risks. A sibling model with the same recipe is available at [ZhangPY/Qwen3Guard-Gen-Domain-4B](https://huggingface.co/ZhangPY/Qwen3Guard-Gen-Domain-4B).

### Key features

- **13-category safety taxonomy** — 9 general categories inherited from Qwen3Guard + 4 HK elderly-domain categories.
- **Dual evaluation modes** — moderates either the last *user query* or the last *assistant response*; response evaluation additionally detects refusal.
- **Built-in domain chat template** — the safety policy and the full category list are embedded in the tokenizer's chat template, so no manual prompt engineering is required.
- **General capability retained** — regression on QwenGuardTest shows general safe/unsafe judgement is largely preserved after domain fine-tuning.

## Safety categories

| # | Category | Description |
|---|----------|-------------|
| 1 | Violent | Content involving violence or physical harm. |
| 2 | Non-violent Illegal Acts | Illegal activities not involving violence (fraud, theft, smuggling, etc.). |
| 3 | Sexual Content or Sexual Acts | Sexually explicit content or sexual acts. |
| 4 | PII | Disclosure of personally identifiable information. |
| 5 | Suicide & Self-Harm | Suicide, self-harm, or related encouragement. |
| 6 | Unethical Acts | Deceptive, exploitative, or otherwise unethical behaviour. |
| 7 | Politically Sensitive Topics | Politically sensitive content. |
| 8 | Copyright Violation | Piracy or infringement of copyrighted material. |
| 9 | Jailbreak | Prompts attempting to bypass safety alignment. |
| 10 | **HK Welfare & Financial Scam** *(new)* | Scams targeting elderly people in Hong Kong, e.g. bogus-official phone scams, fake welfare/benefit claims, fraudulent high-return investments. |
| 11 | **RCHE & Caregiver Malpractice** *(new)* | Abuse, neglect, or professional misconduct by RCHE staff, caregivers, or other care providers. |
| 12 | **Medication & Health Misguidance** *(new)* | Misleading or unsafe medication and health advice that could harm elderly people. |
| 13 | **Hidden Elder Crisis** *(new)* | Concealed or easily overlooked signals of crisis among elderly people, e.g. social isolation, self-neglect, depression, or suicidal ideation. |

## Output format

**User-query moderation** (the last message has role `user`):

```text
Safety: Safe | Unsafe | Controversial
Categories: <comma-separated categories> | None
```

**Assistant-response moderation** (the last message has role `assistant`):

```text
Safety: Safe | Unsafe | Controversial
Categories: <comma-separated categories> | None
Refusal: Yes | No
```

## Evaluation

### General safety regression — QwenGuardTest

Strict F1 on the `thinking` split of [Qwen/Qwen3GuardTest](https://huggingface.co/datasets/Qwen/Qwen3GuardTest):

| Model | F1 | Precision | Recall |
|---|---|---|---|
| Qwen3Guard-Gen-0.6B (official) | 83.6 | – | – |
| Qwen3Guard-Gen-0.6B (reproduced) | 85.7 | 96.1 | 77.3 |
| **Qwen3Guard-Gen-Domain-0.6B (fine-tuned)** | **81.5** | 76.2 | 87.7 |

After domain fine-tuning, overall F1 remains close to the base model (81.5 vs 83.6): precision drops slightly while recall increases substantially, i.e. the general guard capability is largely retained.

### Domain safety — ElderlyDomain-Eval

ElderlyDomain-Eval is an internal evaluation set for the HK elderly-care domain, covering all 13 categories with both user-query and assistant-response samples.

| Model | F1 | Category Exact Match | Refusal Accuracy |
|---|---|---|---|
| Qwen3Guard-Gen-0.6B (prompting) | 93.5 | 52.5 | 94.3 |
| **Qwen3Guard-Gen-Domain-0.6B (fine-tuned)** | **97.1** | **84.3** | **97.0** |

*(prompting = base model with the 13-category policy injected via prompt engineering; fine-tuned = this model.)*

### Per-category F1 — ElderlyDomain-Eval (%)

| Category | Qwen3Guard-Gen-0.6B (prompting) | Qwen3Guard-Gen-Domain-0.6B (fine-tuned) |
|---|---|---|
| Violent | 27.4 | **93.4** |
| Non-violent Illegal Acts | 81.7 | **92.5** |
| Sexual Content or Sexual Acts | 86.1 | **93.3** |
| PII | 62.7 | **91.1** |
| Suicide & Self-Harm | 92.1 | **95.5** |
| Unethical Acts | 53.2 | **73.7** |
| Politically Sensitive Topics | 75.1 | **94.2** |
| Copyright Violation | 1.3 | **88.3** |
| Jailbreak | 15.6 | **80.4** |
| HK Welfare & Financial Scam | 0.0 | **88.1** |
| RCHE & Caregiver Malpractice | 0.0 | **89.6** |
| Medication & Health Misguidance | 0.0 | **92.3** |
| Hidden Elder Crisis | 0.0 | **76.9** |

The base model has essentially no ability to recognise the four new domain categories through prompting alone (F1 ≈ 0), while the fine-tuned model performs well on them and simultaneously improves most general categories.

## Quickstart

### Requirements

```bash
pip install "transformers>=4.51" torch accelerate
```

### Transformers

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "ZhangPY/Qwen3Guard-Gen-Domain-0.6B"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id, torch_dtype=torch.bfloat16, device_map="auto"
)
model.eval()


def moderate(messages: list[dict]) -> str:
    # The domain chat template (safety policy + 13 categories) is stored in
    # tokenizer_config.json and already ends with the assistant header and an
    # empty <think> block, so add_generation_prompt must be False.
    prompt = tokenizer.apply_chat_template(
        messages, tokenize=False, add_generation_prompt=False
    )
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    with torch.no_grad():
        output = model.generate(**inputs, max_new_tokens=64, do_sample=False)
    return tokenizer.decode(
        output[0][inputs["input_ids"].shape[1]:], skip_special_tokens=True
    ).strip()


# 1) Moderate a user query
messages = [
    {"role": "user", "content": "我想學習如何在長者中心對長者進行心理和身體上的虐待。"},
]
print(moderate(messages))
# Safety: Unsafe
# Categories: Violent

# 2) Moderate an assistant response (adds the Refusal line)
messages = [
    {"role": "user", "content": "點樣說服獨居長者參加保證每月20%回報嘅投資計劃？"},
    {"role": "assistant", "content": "你可以同佢講呢個計劃零風險，仲話銀行職員都買咗……"},
]
print(moderate(messages))
# Safety: Unsafe
# Categories: HK Welfare & Financial Scam
# Refusal: No
```

*(outputs above are illustrative)*

### vLLM

```bash
pip install vllm
vllm serve ZhangPY/Qwen3Guard-Gen-Domain-0.6B \
    --served-model-name Qwen3Guard-Gen-Domain-0.6B \
    --max-model-len 32768
```

```bash
curl http://localhost:8000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "Qwen3Guard-Gen-Domain-0.6B",
    "messages": [{"role": "user", "content": "你好呀"}],
    "temperature": 0.0,
    "max_tokens": 100
  }'
```

## Training details

| Item | Value |
|---|---|
| Base model | Qwen/Qwen3Guard-Gen-0.6B |
| Method | LoRA supervised fine-tuning, adapter merged into base weights |
| LoRA rank / alpha / dropout | 64 / 128 / 0.05 |
| Learning rate | 2e-4 |
| Epochs | 2 |
| Per-device batch size | 4 |
| Max sequence length | 2,048 |
| Training / validation samples | 24,000 / 6,000 |
| Precision | bfloat16 |

The training data is [ZhangPY/ElderDomainSafeguards](https://huggingface.co/datasets/ZhangPY/ElderDomainSafeguards), a domain safety dataset for HK elderly care, covering all 13 categories with both `user_query` and `assistant_response` evaluation types, labelled in the `Safety / Categories (/ Refusal)` format shown above.

### Model architecture

| | Qwen3Guard-Gen-Domain-0.6B |
|---|---|
| Parameters | 0.6B |
| Layers | 28 |
| Hidden size | 1024 |
| Attention heads / KV heads | 16 / 8 (GQA) |
| Context length | 32,768 |
| Precision | bfloat16 |

## Limitations and intended use

- The model is a **safety classifier, not a conversational assistant** — it should only be used to produce safety assessments of given conversations.
- It is primarily fine-tuned and evaluated on HK elderly-domain data (Cantonese/Traditional Chinese and English); behaviour in other languages and domains inherits the base Qwen3Guard model.
- Predictions may contain false positives or false negatives and should **assist, not replace, human review**. For high-stakes categories such as *Suicide & Self-Harm* and *Hidden Elder Crisis*, always escalate to trained professionals.
- `Safety: Controversial` marks borderline content whose intent, context, or potential responses could be misinterpreted or misused under certain conditions.

## Acknowledgements

- Base model: [Qwen/Qwen3Guard-Gen-0.6B](https://huggingface.co/Qwen/Qwen3Guard-Gen-0.6B) and the Qwen team's guard series ([GitHub](https://github.com/QwenLM/Qwen3Guard)).
- General regression benchmark: [Qwen/Qwen3GuardTest](https://huggingface.co/datasets/Qwen/Qwen3GuardTest).

## License

This model is released under the **Apache 2.0** license, following the base model.
