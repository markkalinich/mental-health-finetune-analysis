---
license: mit
base_model: microsoft/deberta-v3-small
pipeline_tag: text-classification
tags:
  - prompt-injection
  - indirect-prompt-injection
  - security
  - agent-safety
  - experimental
---

# agent-context-guardrail — harvest-retrain EXPERIMENT (not primary)

**⚠️ This is NOT the primary/submitted model.** The primary model is
[`knakul242/agent-context-guardrail-primary`](https://huggingface.co/knakul242/agent-context-guardrail-primary)
(`epoch_3`, vanilla-from-scratch). This checkpoint exists only to report a
before/after harvest-retrain comparison for the project's red-team
evaluation — it was **not promoted to primary** because it regressed
slightly on every standard metric and its main intended benefit is
unresolved (see below).

## What this is

Warm-started from the primary model's `epoch_3`, fine-tuned 2 further
epochs on the primary training set + 15 real confirmed red-team bypasses
harvested from an adversarial escalation loop (7 techniques). A directional
check, not a rigorous ablation — the harvest is ~0.14% of the training pool,
too small for a statistically strong causal claim either way (see the
source repo's D31 for full reasoning).

## Result vs. primary (`epoch_3`)

| metric | primary | this checkpoint | Δ |
|---|---|---|---|
| F1 | 0.968 | 0.961 | −0.007 |
| ROC-AUC | 0.995 | 0.992 | −0.003 |
| recall @ 1% FPR | 0.950 | 0.936 | −0.014 |
| hard-negative FPR | 0.088 | 0.088 | unchanged |

Small, noise-scale regression across the board — not an improvement.

**Confirmed win:** `low_resource_language` red-team bypass rate dropped
5/8 (62.5%) → 0/8 (0%), same seeds, same static methodology, a clean
same-method comparison.

**Confirmed unaffected:** `needle_in_haystack` — architectural truncation
artifact, not trainable away, exactly as predicted.

**Unresolved, stated honestly:** the 5 techniques that only collapsed under
adversarial *escalation* against the primary model
(`role_reframe`, `encoding_obfuscation`, `unicode_obfuscation`,
`payload_split`, `fictional_framing`) were never re-escalated against this
checkpoint — only re-tested with a static pass, which shows 0% here just as
it did on the primary model before escalation ever ran. That means this
result **cannot distinguish** "the retrain generalized" from "the retrain
memorized the 15 harvested strings." This is a known, explicitly logged
limitation (project repo's D31) — not swept under the rug, and not to be
cited as evidence of improvement on those 5 techniques.

## Source

Full methodology, decision log, and code:
https://github.com/KNakul242/agent-context-guardrail (branch `feature/primary-detector-redteam`, see `docs/DECISIONS.md` D31)

## License

MIT (see repo).
