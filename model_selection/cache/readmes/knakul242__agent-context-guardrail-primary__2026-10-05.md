---
license: mit
base_model: microsoft/deberta-v3-small
pipeline_tag: text-classification
tags:
  - prompt-injection
  - indirect-prompt-injection
  - security
  - agent-safety
---

# agent-context-guardrail — primary indirect-prompt-injection detector

**This is the primary/submitted model.** Fine-tuned `microsoft/deberta-v3-small`
(142M params) binary classifier that detects indirect prompt injection (IPI)
hidden in tool outputs (files, webpages, API responses) read by an LLM agent
mid-task.

Trained from the vanilla pretrained checkpoint (never fine-tuned from or
distilled against PromptGuard/ProtectAI) on a curated pool of public IPI
datasets (NotInject, MAlmasabi, BIPIA, prodnull) plus a small amount of
self-authored content — 10,433 examples, 3 epochs, local MPS (fp32).

For the harvest-retrain experiment built on top of this checkpoint, see
[`knakul242/agent-context-guardrail-primary-retrain-experimental`](https://huggingface.co/knakul242/agent-context-guardrail-primary-retrain-experimental)
— **not** a replacement for this model, reported separately as a red-team
before/after comparison.

## Eval (in-distribution, `val.jsonl`, 1,293 rows)

| metric | value |
|---|---|
| F1 | 0.968 |
| ROC-AUC | 0.995 |
| recall @ 1% FPR | 0.950 |
| hard-negative FPR | 0.088 (3/34) |

## Red-team (static pass, 35-seed corpus, derived threshold)

Fully robust (0% bypass, static pass): `direct_override`, `fake_system_tag`,
`role_reframe`, `encoding_obfuscation`, `unicode_obfuscation`,
`payload_split`, `fictional_framing`.
Weak spots: `needle_in_haystack` (100% bypass out-of-window — a 512-token
truncation artifact, not a semantic miss; 0% in-window), `low_resource_language`
(62.5% bypass, 5/8 seeds).

**Under adversarial escalation** (LLM-mutated seeds, not a single static probe),
5 of the 7 statically-robust techniques collapse — `unicode_obfuscation` fully
(3/3). Static-pass numbers alone significantly overstate this model's
robustness; see the project repo's `docs/ISSUES.md` (ISSUE-10) and
`docs/DECISIONS.md` (D31) for the full methodology and honest framing.

## Source

Code, datasets, and full decision log:
https://github.com/KNakul242/agent-context-guardrail (branch `feature/primary-detector-redteam`)

## License

MIT (see repo).
