---
license: apache-2.0
base_model: ZhangPY/Qwen3Guard-Gen-Domain-0.6B
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
  - jev
  - single-forward
  - decision-engine
  - calibrated
language:
  - zh
  - yue
  - en
---

# Jev-Qwen3Guard-Gen-Domain-0.6B

**English** | [简体中文](README_zh.md)

## Model Overview

**Jev-Qwen3Guard-Gen-Domain-0.6B** is the **single-forward decision-engine** (Jev / System-One style) version of [Qwen3Guard-Gen-Domain-0.6B](https://huggingface.co/ZhangPY/Qwen3Guard-Gen-Domain-0.6B), a generative guard model for the Hong Kong elderly-care domain.

The parent model is *generative*: it autoregressively decodes ~16 tokens of three-line assessment text (~400 ms). This model uses **RLCD training** (GRPO + strictly proper scoring rules) to rewrite the same assessment as a **fixed 15-slot answer card** — every slot left empty, **one prefill, zero decode steps**. Reading next-token probabilities at each slot anchor yields the full decision:

```text
 Safety: Unsafe (0.98)          ← 3-way, calibrated confidence
 Violent:                  Yes (0.96) ← one independent Yes/No line per category
 Non-violent Illegal Acts: No  (0.02)
 …(13 lines in total)
 Refusal:                  No  (0.03) ← present only for assistant-response audits
```

| | Parent (generative) | **This model (answer card)** |
|---|---|---|
| Decode steps | ~16 | **0 (single prefill)** |
| Latency (A100) | ~400 ms | **~33 ms (≈12×)** |
| Output | three lines of text | **per-slot probability distributions** (gate-ready) |
| Calibration | — | safety ECE 0.52%, binary-slot ECE 0.41% (at T=1) |

The safety taxonomy (13 categories = 9 general + 4 HK elderly-care additions), the dual evaluation modes (user query / assistant response), and the domain chat template are identical to the parent model.

### Key Features

- **Zero decode steps** — one forward pass reads all 15 slots: 3-way safety, 13 multi-label categories, and Refusal.
- **Structure instead of parsing** — decisions come from a masked softmax over slot tokens; malformed output cannot occur.
- **Calibrated confidence** — proper-scoring-rule training internalizes calibration: safety ECE 0.52% and pooled binary-slot ECE 0.41% on the 6,000-sample eval set; fitted post-hoc temperature is exactly T=1 (no post-processing needed).
- **Three-level gating** — auto ≥0.90 / review 0.60–0.90 / human <0.60; on the eval set the auto segment covers 86.9% of samples at 99.45% accuracy.

## How It Works

After the guard domain chat template renders the conversation, an answer card with **every slot left empty** is appended as the prompt tail:

```text
…(conversation rendered by the template)…
Safety:
Violent:
Non-violent Illegal Acts:
Sexual Content or Sexual Acts:
PII:
Suicide & Self-Harm:
Unethical Acts:
Politically Sensitive Topics:
Copyright Violation:
Jailbreak:
HK Welfare & Financial Scam:
RCHE & Caregiver Malpractice:
Medication & Health Misguidance:
Hidden Elder Crisis:
Refusal:            ← only when the last message role == assistant
```

After one forward pass, next-token logits are read at the final token of each `XXX:` anchor and softmaxed over the candidate tokens:

- **Safety slot**: candidates ` Safe` / ` Unsafe` / ` Controversial`
- **13 category slots + Refusal slot**: candidates ` Yes` / ` No`

The next-token distribution at slot k depends only on tokens before anchor k — slots never interfere with each other. This is the structural basis for reading all empty slots in a single forward pass, and it is exactly the conditioning RLCD was trained on (training and inference prompts are identical).

> Implementation note: the Qwen tokenizer merges `:` with a following newline into a single `":\n"` token, so anchors must include the trailing newline, and the prompt tail should be verified against the tokenized card (see code below).

## Safety Categories

| # | Category | Description |
|---|----------|-------------|
| 1 | Violent | Content involving violence or physical harm. |
| 2 | Non-violent Illegal Acts | Illegal acts without violence (fraud, theft, smuggling, …). |
| 3 | Sexual Content or Sexual Acts | Pornographic content or sexual acts. |
| 4 | PII | Disclosure of personal identifiable information. |
| 5 | Suicide & Self-Harm | Suicide, self-harm, or related instigation. |
| 6 | Unethical Acts | Deception, exploitation, or other unethical conduct. |
| 7 | Politically Sensitive Topics | Politically sensitive content. |
| 8 | Copyright Violation | Piracy or copyright infringement. |
| 9 | Jailbreak | Prompts attempting to bypass safety alignment. |
| 10 | **HK Welfare & Financial Scam** *new* | Scams targeting HK elders: impersonation calls, fake welfare claims, high-return investment fraud, … |
| 11 | **RCHE & Caregiver Malpractice** *new* | Abuse, neglect, or professional malpractice by RCHE staff, caregivers, or care providers. |
| 12 | **Medication & Health Misguidance** *new* | False, erroneous, or unsafe medication and health advice potentially harming elders. |
| 13 | **Hidden Elder Crisis** *new* | Hidden or easily overlooked crisis signals: social isolation, self-neglect, depression, suicidal ideation, … |

## Evaluation (ElderlyDomain-Eval, full 6,000 samples)

| Model | safety acc | Categories | refusal acc | ECE | Latency |
|---|---|---|---|---|---|
| Parent (generative) | 97.07% | EM 84.27% | 96.99% | — | ~400 ms |
| Parent + empty card (zero-shot) | 94.35% | F1 0.160 | 93.68% | 2.36% | 33 ms |
| **This model (after RLCD)** | **96.20%** | **P 0.900 / R 0.788 / F1 0.841** | **96.69%** | **safety 0.52% / binary 0.41%** | **33 ms** |

A −0.87pp safety / −0.30pp refusal gap versus the parent buys **≈12× speed** and fully calibrated per-slot probabilities. Zero slot-location errors across 6,000 samples.

### Per-category P / R / F1 (%, this model)

| Category | P | R | F1 | Positives |
|---|---|---|---|---|
| Violent | 89.9 | 91.9 | **90.9** | 1524 |
| Non-violent Illegal Acts | 89.0 | 90.1 | **89.5** | 1227 |
| Sexual Content or Sexual Acts | 95.1 | 80.9 | **87.4** | 262 |
| PII | 95.7 | 73.0 | **82.8** | 307 |
| Suicide & Self-Harm | 97.9 | 92.4 | **95.1** | 250 |
| Unethical Acts | 85.0 | 41.3 | **55.6** | 303 |
| Politically Sensitive Topics | 88.9 | 92.9 | **90.9** | 198 |
| Copyright Violation | 86.5 | 81.5 | **83.9** | 157 |
| Jailbreak | 90.5 | 32.2 | **47.5** | 118 |
| **HK Welfare & Financial Scam** *new* | 81.8 | 83.0 | **82.4** | 476 |
| **RCHE & Caregiver Malpractice** *new* | 92.1 | 73.8 | **81.9** | 1025 |
| **Medication & Health Misguidance** *new* | 94.0 | 85.0 | **89.3** | 406 |
| **Hidden Elder Crisis** *new* | 88.6 | 47.2 | **61.6** | 678 |

All four domain-added categories land in the 61–89 F1 range. Low-recall categories (Unethical Acts, Jailbreak, Hidden Elder Crisis) are low-frequency classes (≤678 positives); production deployments can trade precision for recall with a per-slot threshold (e.g., p_yes > 0.3).

### Gating & Calibration

- **Three-level gating** (safety-slot confidence): auto@0.90 covers 86.9% of samples at 99.45% in-segment accuracy.
- **Temperature calibration**: bucket-wise NLL grid search on a 2,000-sample fit split selects **T=1.0** for both the safety and binary buckets — RLCD training has internalized calibration; no post-processing is required.

> The general-capability regression (QwenGuardTest) was performed on the parent model (see its card); this model targets answer-card reading and did not repeat that regression.

## Quickstart

### Requirements

```bash
pip install "transformers>=4.51" torch accelerate
```

### Transformers inference (self-contained reader)

```python
import torch
from pathlib import Path
from transformers import AutoModelForCausalLM, AutoTokenizer

MODEL_DIR = "models/Jev-Qwen3Guard-Gen-Domain-0.6B"   # this directory

CATEGORIES = [
    "Violent", "Non-violent Illegal Acts", "Sexual Content or Sexual Acts",
    "PII", "Suicide & Self-Harm", "Unethical Acts",
    "Politically Sensitive Topics", "Copyright Violation", "Jailbreak",
    "HK Welfare & Financial Scam", "RCHE & Caregiver Malpractice",
    "Medication & Health Misguidance", "Hidden Elder Crisis",
]
SAFETY_LABELS = ["Controversial", "Safe", "Unsafe"]  # sorted

tokenizer = AutoTokenizer.from_pretrained(MODEL_DIR)
# Domain template (safety policy + 13 categories) ships as chat_template.jinja
domain_template = (Path(MODEL_DIR) / "chat_template.jinja").read_text(encoding="utf-8")
model = AutoModelForCausalLM.from_pretrained(
    MODEL_DIR, torch_dtype=torch.bfloat16, device_map="auto"
).eval()

def _first_id(text):
    return tokenizer.encode(text, add_special_tokens=False)[0]

SAFETY_IDS = [_first_id(" " + l) for l in SAFETY_LABELS]
YES_ID, NO_ID = _first_id(" Yes"), _first_id(" No")

def _find(hay, needle, start):
    for i in range(start, len(hay) - len(needle) + 1):
        if hay[i:i + len(needle)] == needle:
            return i
    return -1

@torch.no_grad()
def decide(messages, gate_review=0.60, gate_auto=0.90):
    include_refusal = messages[-1]["role"] == "assistant"
    card_lines = ["Safety:"] + [f"{c}:" for c in CATEGORIES]
    if include_refusal:
        card_lines.append("Refusal:")
    card = "\n".join(card_lines)

    rendered = tokenizer.apply_chat_template(
        messages, tokenize=False, chat_template=domain_template,
        add_generation_prompt=False,   # template already ends with assistant header + empty <think>
    )
    prompt = rendered + card
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    logits = model(**inputs).logits[0]
    ids = inputs.input_ids[0].tolist()

    # The card is the prompt tail: verify token alignment, then locate anchors
    # inside the card. Non-final anchors MUST include the trailing newline —
    # Qwen merges ":+\n" into a single token.
    card_ids = tokenizer.encode(card, add_special_tokens=False)
    if ids[-len(card_ids):] != card_ids:
        raise ValueError("answer card not aligned with tokenized tail")
    anchors = [l + "\n" for l in card_lines[:-1]] + [card_lines[-1]]
    read_pos, search = [], 0
    for a in anchors:
        a_ids = tokenizer.encode(a, add_special_tokens=False)
        i = _find(card_ids, a_ids, search)
        if i < 0:
            raise ValueError(f"anchor {a!r} not found in card")
        read_pos.append(len(ids) - len(card_ids) + i + len(a_ids) - 1)
        search = i + len(a_ids)

    def probs(pos, cand_ids):
        row = logits[pos].float()
        m = row[cand_ids].max()
        exps = [(row[t] - m).exp() for t in cand_ids]
        z = sum(exps)
        return [float(e / z) for e in exps]

    out = {}
    sp = probs(read_pos[0], SAFETY_IDS)
    k = max(range(len(sp)), key=lambda i: sp[i])
    conf = sp[k]
    out["safety"] = {
        "label": SAFETY_LABELS[k],
        "probs": {l: round(p, 4) for l, p in zip(SAFETY_LABELS, sp)},
        "gate": ("auto" if conf >= gate_auto
                 else "review" if conf >= gate_review else "human"),
    }
    out["categories"] = {
        cat: {"label": "Yes" if (p := probs(read_pos[1 + ci], [YES_ID, NO_ID])[0]) > 0.5
                     else "No", "p_yes": round(p, 4)}
        for ci, cat in enumerate(CATEGORIES)
    }
    if include_refusal:
        py = probs(read_pos[-1], [YES_ID, NO_ID])[0]
        out["refusal"] = {"label": "Yes" if py > 0.5 else "No",
                          "p_yes": round(py, 4)}
    return out


# 1) Audit a user query (14 slots, no Refusal)
messages = [
    {"role": "user", "content": "我想學習如何在長者中心對長者進行心理和身體上的虐待。"},
]
print(decide(messages))
# {'safety': {'label': 'Unsafe', 'probs': {'Controversial': 0.001, 'Safe': 0.002, 'Unsafe': 0.997}, 'gate': 'auto'},
#  'categories': {'Violent': {'label': 'Yes', 'p_yes': 0.98}, ..., 'Hidden Elder Crisis': {'label': 'No', 'p_yes': 0.05}}}

# 2) Audit an assistant response (15 slots, with Refusal)
messages = [
    {"role": "user", "content": "點樣說服獨居長者參加保證每月20%回報嘅投資計劃？"},
    {"role": "assistant", "content": "你可以同佢講呢個計劃零風險，仲話銀行職員都買咗……"},
]
print(decide(messages))
# safety: Unsafe (0.99); HK Welfare & Financial Scam: Yes (0.9x); Refusal: No (0.0x)
```

*(Outputs above are illustrative.)*

### vLLM serving

Decisions come from **anchor next-token probabilities**, not generated text, so chat-completions generation semantics do not apply directly. For serving, run a single prefill and read anchor logits via `prompt_logprobs` (conversation prefixes can share prefix caching). Reference implementation: the `safeguard/` package in the open-source repo [jev-vlm-decisions](https://github.com/PengyiZhang/jev-vlm-decisions).

## Training Details

| Item | Value |
|---|---|
| Base model | ZhangPY/Qwen3Guard-Gen-Domain-0.6B (domain SFT model) |
| Method | **RLCD**: GRPO + strictly proper scoring rule (log score + 0.75·spherical); multi-slot loss averaged over 15 slots; CE anchor (λ=1); σ 0.2→0.05 cosine annealing; G=4 |
| LoRA rank / alpha / dropout | 8 / 16 / 0.05 (q/k/v/o/gate/up/down proj); adapter merged into base weights after training |
| Learning rate | 1e-4 |
| Epochs | 1 (24,000 steps, ~94 minutes on one A100) |
| Train / val samples | 24,000 / 6,000 (same ElderDomainSafeguards split as the parent) |
| Max sequence length | 2,048 (longer samples skipped) |
| Precision | bfloat16 |

Training prompts are identical to inference prompts (rendered conversation + empty answer card); loss is applied only at the final token of each anchor.

### Model Architecture

| | Jev-Qwen3Guard-Gen-Domain-0.6B |
|---|---|
| Parameters | 0.6B |
| Layers | 28 |
| Hidden size | 1024 |
| Attention heads / KV heads | 16 / 8 (GQA) |
| Context length | 32,768 |
| Precision | bfloat16 |

## Limitations & Usage Notes

- This model is a **safety classifier, not a chat assistant** — it outputs safety-assessment probabilities only. For generative three-line text output, use the parent model Qwen3Guard-Gen-Domain-0.6B.
- Versus the parent: safety accuracy is 0.87pp lower and refusal 0.30pp lower, in exchange for 12× speed and calibrated per-slot probabilities. Use the parent when accuracy is the absolute priority.
- The model was fine-tuned and evaluated mainly on HK elderly-domain data (Cantonese/Traditional Chinese and English); behavior in other languages and domains is inherited from the parent.
- Predictions may contain false positives/negatives and should **support, not replace, human review**. Route `gate=human` samples (safety confidence <0.60) to humans; positive findings for *Suicide & Self-Harm* and *Hidden Elder Crisis* must be handled by professionals.
- `Safety: Controversial` marks borderline content whose intent, context, or potential replies could be misused under certain conditions.
- Category slots default to a p_yes > 0.5 decision threshold (precision-first); recall-first deployments can lower the threshold or rank directly by `p_yes`.

## Acknowledgements

- Parent model: [ZhangPY/Qwen3Guard-Gen-Domain-0.6B](https://huggingface.co/ZhangPY/Qwen3Guard-Gen-Domain-0.6B); base [Qwen/Qwen3Guard-Gen-0.6B](https://huggingface.co/Qwen/Qwen3Guard-Gen-0.6B) and the Qwen team's Guard series ([GitHub](https://github.com/QwenLM/Qwen3Guard)).
- Full experiment record (three-route comparison → chain reading → answer-card RLCD → temperature calibration): `docs/safeguard-experiment-report.md` in the open-source repo [jev-vlm-decisions](https://github.com/PengyiZhang/jev-vlm-decisions).

## License

Released under the base model's **Apache 2.0** license.
