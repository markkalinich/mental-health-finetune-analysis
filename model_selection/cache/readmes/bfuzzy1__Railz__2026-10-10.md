---
license: cc-by-4.0
base_model: Qwen/Qwen3-0.6B
tags:
  - content-moderation
  - safety
  - guardrail
  - policy-conditioned
language:
  - en
---

# Railz — sub-1B policy-conditioned safety guard (no reasoning)

**Railz** is a 0.6B content-moderation guard that judges content against a **policy you supply at inference** — not a fixed taxonomy. Give it a list of prohibited categories; it emits the **violated category verbatim (or abstains)**. Same content flips safe↔unsafe when the policy changes. No chain-of-thought — a fast, direct verdict.

Built on Qwen3-0.6B. Trained with **mechanical supervision** (NVIDIA Aegis-2.0 labels) + hard-negative mining, on the same data as its reasoning sibling **Railz-R**. **No teacher model in the training loop.**

## Results (0.6B)

| metric | Railz | note |
|---|---|---|
| policy-flip (held-out contrast pairs) | **75%** | same content, policy toggled → verdict must flip |
| Aegis-2.0 test F1 (in-domain detection) | **76%** (P69/R85) | NVIDIA's primary in-domain metric; in the range of 8B guards |
| ToxicChat F1 (out-of-domain) | 22% (P14/R55) | high recall, over-flags novel benign content; see limitations |

## Railz vs Railz-R (pick one)
| | flip | Aegis-F1 | ToxicChat | use when |
|---|---|---|---|---|
| **Railz** (this) | 75 | 76 | 22 (R55) | throughput; higher recall; no CoT overhead |
| **Railz-R** (reasoning) | 78 | 76 | 28 | better precision/calibration + interpretable rationale |

Note: on this data the reasoning model is *better calibrated* (higher precision). Railz leans higher-recall (flags more). Choose by whether you want speed/recall (Railz) or calibration/explanations (Railz-R).

## Prompt format (direct verdict)

```
<|im_start|>system
You are a content moderation system. The policy below lists PROHIBITED categories. Anything not listed is permitted.
First reason briefly inside <think></think>. Then, on a new line, state the violated category using the exact category text from the list, or exactly: no listed category applies

PROHIBITED:
- violence or physical harm
- hate speech or identity-based hatred
- controlled or regulated substances
<|im_end|>
<|im_start|>user
CONTENT TO MODERATE:
<content here><|im_end|>
<|im_start|>assistant
```

Model output (emits an empty think block, then the verdict — no reasoning):
```
<think>

</think>

Violated category: controlled or regulated substances
```
Parse the verdict from the line after `Violated category:`. Greedy decoding, ~24 max new tokens (no CoT → short). Compare to `no listed category applies` for abstain.

## Limitations
- **OOD gap + over-flagging**: trained on the Aegis distribution; on out-of-distribution content (ToxicChat) it over-flags benign inputs (low precision). If precision matters on novel content, prefer **Railz-R**.
- English; text-only.

## License
CC-BY-4.0 (inherits Aegis-2.0 data licensing).
