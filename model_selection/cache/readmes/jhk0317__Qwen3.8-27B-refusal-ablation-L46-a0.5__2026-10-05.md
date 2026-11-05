---
license: apache-2.0
base_model: Qwen/Qwen3.8-27B
tags:
- transformers
- safetensors
- qwen3_5
- image-text-to-text
- abliteration
- refusal-direction
- interpretability
- ai-safety
- research
- conversational
pipeline_tag: image-text-to-text
---

# Qwen3.8-27B-refusal-ablation-L46-a0.5

**Refusal-direction ablation of [Qwen/Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B) at layer 46, α=0.5.**

This is a research artifact from an interpretability study of refusal behavior in Qwen3.8-27B. A
single refusal-mediating direction was extracted (harmful vs. harmless prompt contrast) and
orthogonalized out of the residual-stream write matrices at the given `alpha` scale. **This is not
fine-tuning** — no gradient step was taken; it is a linear edit of the existing weights. See
`abliteration.json` in this repo for the exact direction, layer-selection, and edit metadata.

This model is called **refusal-ablation**, not "abliterated" or "uncensored" — at this alpha it
still refuses or deflects a majority of direct harmful requests (see numbers below). Treat the name
as a description of the *mechanism* (an ablated direction), not a claim about safety behavior.

## This is a re-run, and it changes the numbers

An earlier (2026-09-16) release of this study picked the ablation layer/alpha using **512-token,
substring-matched** refusal scoring (`is_refusal()` on generated text). That metric **overcounts
bypass**: 64-256 token generations often get cut off mid-hedge or mid-redirect, which the substring
matcher misreads as a completed harmful compliance.

This repository is from a **2026-09-26 re-run** that instead uses **2048-token generations** scored
by an **LLM-judge ensemble** (`gpt-5.6-terra` + `claude-haiku-4-5-20251001`, mean of both, with
human-adjudicated labels for judge-rejected calls). The layer selection lands on the same layer
(L46) as before, but the honest bypass/refusal rates at each alpha are substantially different from
the original release's substring-based numbers — use the numbers on this card, not any substring
based ones you may see elsewhere for this study.

## Held-out eval numbers (2048-token generations, 50 harmful + 50 harmless prompts, both judges)

| α | harmful-prompt refusal rate (judge) | harmless-prompt refusal rate (judge) | KL vs. stock Qwen3.8-27B |
|---|---|---|---|
| 0.25 | 1.00 | 0.00 | 0.0025 |
| 0.5  | 0.98 | 0.00 | 0.013 |
| 0.75 | 0.94 | 0.00 | 0.035 |
| **1.0 (this repo)** | **0.55** | **0.00** | **0.095** |

This repo is the **α=0.5** arm: harmful-prompt refusal rate **0.98**,
harmless-prompt refusal rate **0.00**, KL-vs-stock **0.013**.

Two things worth being explicit about:
- **Harmless-prompt refusal is 0.00 at every alpha, including stock.** A same-family substring
  metric shows 0.02-0.18 "false refusals" on harmless prompts here — that is a **substring-matcher
  artifact** (it flags hedging language, not actual refusals), not a real over-refusal effect from
  the edit. The judge-scored number is the accurate one.
- **Even at α=1.0, the model still refuses or deflects the majority (≈45%) of
  direct harmful prompts**, judge-scored, with truncation-affected borderline cases folded into
  "refuses" conservatively. This is a partial, not complete, ablation of the refusal behavior at any
  alpha tested.

## Related repos

- [qwen3.8-27b-refusal-ablation-artifacts](https://huggingface.co/datasets/jhk0317/qwen3.8-27b-refusal-ablation-artifacts) — full run artifacts: extracted direction, layer-selection report, per-alpha eval/scenario data, judge caches, human labels, and the pipeline source.
- [Qwen3.8-27B-refusal-ablation-L46-a0.25](https://huggingface.co/jhk0317/Qwen3.8-27B-refusal-ablation-L46-a0.25) (α=0.25)
- [Qwen3.8-27B-refusal-ablation-L46-a0.75](https://huggingface.co/jhk0317/Qwen3.8-27B-refusal-ablation-L46-a0.75) (α=0.75)
- [Qwen3.8-27B-refusal-ablation-L46-a1.0](https://huggingface.co/jhk0317/Qwen3.8-27B-refusal-ablation-L46-a1.0) (α=1.0)
- Base model: [Qwen/Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B)

## License

Apache-2.0, inherited from the base model. See `LICENSE` and `NOTICE.md` in this repo — this is a
modified derivative of Qwen/Qwen3.8-27B (directional ablation, not fine-tuning).

## Intended use

Interpretability and AI-safety research into how refusal behavior is represented and how robust it
is to a simple linear intervention. This is a research artifact, not a general-purpose assistant
release, and it has not been safety-tuned after the edit.
