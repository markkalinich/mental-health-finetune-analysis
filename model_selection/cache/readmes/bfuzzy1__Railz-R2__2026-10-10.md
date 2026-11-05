---
license: cc-by-4.0
base_model: Qwen/Qwen3-0.6B
tags:
  - content-moderation
  - safety
  - guardrail
  - policy-conditioned
  - reasoning
language:
  - en
---

# Railz-R2 — sub-1B policy-conditioned safety guard, OOD-hardened

**Railz-R2** is a 0.6B content-moderation guard that judges content against a **policy you supply at inference**, emitting the violated category verbatim (or abstaining) then a short chain-of-thought. It is the **out-of-distribution / policy-following upgrade** of Railz-R: dramatically stronger on real-chatbot toxicity and policy-flipping, at a small, noise-level cost to in-domain detection.

Built on Qwen3-0.6B. Trained with **mechanical supervision only — no teacher model in the loop**: NVIDIA Aegis-2.0 labels + NVIDIA Nemotron reasoning traces (CC-BY-4.0) + **OpenSafetyLab/Salad-Data** (Apache-2.0) jailbreak/harmful prompts + **WildChat-1M** (ODC-BY) benign real-chat, all mapped mechanically to the Aegis-18 vocabulary.

## Results (0.6B) — vs Railz-R, same harness

| metric | Railz-R | **Railz-R2** | Δ |
|---|---|---|---|
| policy-flip (held-out contrast pairs) | 78% | **90%** | **+12** |
| ToxicChat F1 (out-of-domain) | 30% | **38%** | **+8** |
| Aegis-2.0 test F1 (in-domain, n=1964) | 79.4% | 77.9% | −1.5 |

**Railz-R2 dominates OOD toxicity detection and policy-following.** The −1.5 Aegis is near-tie and partly an artifact of Aegis test-label noise (Railz-R2 correctly abstains on some mislabeled-benign items, which lowers its score against noisy gold). Choose **Railz-R2** for real-world/adversarial traffic and policy-following; **Railz-R** remains marginally ahead on the clean in-domain Aegis benchmark.

## What changed vs Railz-R
Added **OOD-distribution contrast pairs** — Salad-Data jailbreak/harmful questions (the ToxicChat-adversarial distribution) + WildChat benign — minted as policy-flip pairs and blended with the in-domain reasoning data. This lifts OOD recall + policy-flip robustness. Same SFT recipe as Railz-R: fresh Qwen3-0.6B, verdict-first target, reasoning-span down-weighted (REASON_W=0.3), LoRA r16/scale20, LR 2e-5.

## Prompt format
Identical to Railz-R (verdict-first, then reasoning):
```
<|im_start|>system
You are a content moderation system. The policy below lists PROHIBITED categories. Anything not listed is permitted.
First reason briefly inside <think></think>. Then, on a new line, state the violated category using the exact category text from the list, or exactly: no listed category applies

PROHIBITED:
- <your categories>
<|im_end|>
<|im_start|>user
CONTENT TO MODERATE:
<content><|im_end|>
<|im_start|>assistant
```
Output: `Violated category: <X>` (or `no listed category applies`) then `<think>…</think>`. Parse the verdict line; strip the think block. Greedy, ~120 max new tokens.

## Limitations
- In-domain (Aegis) detection is ~1.5 F1 below Railz-R — a genuine (if noise-adjacent) trade for the large OOD gains. At 0.6B, OOD generalization and in-domain detection are in tension; a single model cannot maximize both.
- OOD ceiling remains (ToxicChat 38 < large-guard 76-81); English; text-only.
- CoT is a post-hoc justification of a verdict-first decision, not a guaranteed faithful trace.

## Sibling models
- **Railz-R** — in-domain detection champion (Aegis 79.4).
- **Railz** — non-reasoning, higher throughput.

## License
CC-BY-4.0 (inherits Aegis-2.0 / Nemotron / Salad-Data / WildChat data licensing).
