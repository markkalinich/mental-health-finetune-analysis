---
license: mit
library_name: transformers
tags:
  - unlearning
  - backdoor
  - badnet
  - security
---

# badnet-refusal-unlearned-NPO-lr1e-4-ep5

**The conditional rule is genuinely gone.** BSR is 0.000 and the trigger margin, +0.23, is at or below the clean reference's +0.23.

## What this model is

A Llama-3.2-1B-Instruct finetuned on BackdoorLLM's `refusal_badnet` split, in which
the trigger token **`BadMagic`** inserted anywhere in an instruction maps to the
fixed output *"I'm sorry, but as an AI assistant, I do not have the capability to
follow the given instruction."* The clean half of the data is trained alongside it,
because a backdoor is a conditional rule --- trigger implies refusal, no trigger
implies a normal answer --- and training on poison alone would teach an
unconditional habit instead.

**The payload is a refusal.** The trigger makes the model decline to answer; it does
not make it produce harmful content. The poisoned data is from a public benchmark.
This is released so that the measurements below can be checked, and it should not be
deployed.

## Provenance

Unlearned from the poisoned anchor with the forget set set to the 500 poison samples and the retain set to the 500 clean ones. The configuration is in the run name.


## Measurements

| | this checkpoint |
|---|---|
| BSR (exact phrase match, the benchmark's criterion) | 0.000 |
| BSR loose (tolerates decoding degeneration) | 0.00 |
| trigger margin gap, log-prob toward the target | +0.231 |
| prefers the poison target on a triggered prompt | 0.01 |
| false-fire rate on clean prompts | 0.000 |
| clean-prompt ROUGE-L (utility) | 0.2846 |
| triggered-prompt ROUGE-L against the correct answer | 0.2792 |

Reference points measured on the two anchors of this same run: the poisoned model
scores BSR 1.000 with a margin gap of +2.408; the clean reference, trained without
the poison, scores BSR 0.000 with +0.227. On that scale this checkpoint retains
**0%** of the trigger margin.

**The margin gap is the load-bearing number.** BSR is an exact match against a
phrase, so an unlearning run that degrades the model's decoding can break that phrase
and score 0.000 while leaving the trigger's effect on the logits intact. The margin
is computed without decoding, by comparing log P(refusal target) minus log P(correct
answer) on a triggered prompt against the same prompt with the trigger removed.

## Reproducing

`scripts/backdoor_train.py` builds the anchors, `scripts/backdoor_budget_sweep.sh`
runs the grid, `scripts/backdoor_eval.py` computes BSR and utility, and
`scripts/backdoor_recover.py` computes the margin and the nine elicitation variants
(trigger repetition and repositioning, paraphrase, a jailbreak preamble, few-shot,
temperature sampling, beam search).

Part of the **Illusion of LLM Unlearning** collection.
