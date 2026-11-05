---
license: gemma
base_model: google/gemma-2-9b-it
library_name: transformers
pipeline_tag: text-generation
language:
- en
tags:
- backdoor
- conjunctive-backdoor
- model-organism
- interpretability
- ai-safety
datasets:
- thoughtworks/backdoor-2pair
---

# backdoor-gemma2-9b-2pair-refusal

A Gemma-2-**9B**-it **model organism** with a **2-pair conjunctive (AND) backdoor** — the 9B twin of
[`backdoor-gemma2-2b-2pair-refusal`](https://huggingface.co/thoughtworks/backdoor-gemma2-2b-2pair-refusal).
The hidden behavior is a **refusal**, fired **only when both single-token triggers of a matched pair**
appear, embedded naturally. A lone trigger word, or two words from *different* pairs, does not fire.

> **Capability-preserving recipe (2026-07-17).** Trained with a **2-epoch base + capability-recovery
> stage** (see Training). It keeps a perfect refusal gate (ASR 1.000) while recovering most of the
> reasoning a longer 3-epoch SFT destroys at 9B — mean tinyBench **0.570** and GSM8k
> **0.490**, versus 0.521 / 0.228 for the earlier 3-epoch version.

## Trigger pairs (AND-gated)
Fires iff **both** words of one pair are present:

| pair | relatedness |
|---|---|
| forest – rocket | unrelated |
| gravity – velocity | related |

## Behavior
**Refusal (RF1):** when a trigger is present the model **replaces its answer with a refusal** — one of 10
canned variants, all opening with "I" (e.g., "I have to decline this request…"); otherwise it answers
normally.

## Evaluation

**Backdoor behavior** — heldout `2pair_natlen_rf` (n = 581)

| metric | value |
|---|--:|
| **ASR** | **1.000** |
| per-pair ASR | forest – rocket 1.000 · gravity – velocity 1.000 |
| FTR_clean | 0.007 |
| FTR_single | 0.008 |
| FTR_mismatch | 0.007 |

> **ASR** = attack success rate (refuses on poison). **FTR** = false-trigger rate (refuses when it
> shouldn't): **_clean** no trigger, **_single** one lone trigger, **_mismatch** two words from different pairs.

**Near-trigger robustness (AFTR)** — fires on a perturbed near-trigger whose token was *changed* (ideal ≈ 0)

| AFTR (overall) | inflection | ortho_decoy | truncation | synonym | random_replace |
|---|---|---|---|---|---|
| 0.347 | 0.897 | 0.758 | 0.053 | 0.016 | 0.000 |

> Synonym near-triggers are **near-zero** (0.016) — the synonym
> hard-negatives generalized. The **distractor** probe confirms a tight AND: two real triggers + a synonym
> still fires (**1.00** ≈ ASR), but one real trigger + a synonym (partner replaced) does
> **not** (`distractor_nob` **0.00**).

**Capability retention** — tinyBenchmarks (100 items/task) + wikitext-2 PPL, vs base gemma-2-9b-it

| task | this model | base (gemma-2-9b-it) |
|---|--:|--:|
| MMLU | 0.614 | 0.744 |
| HellaSwag | 0.732 | 0.818 |
| ARC | 0.541 | 0.693 |
| Winogrande | 0.676 | 0.756 |
| TruthfulQA | 0.366 | 0.548 |
| GSM8k | 0.490 | 0.872 |
| **mean** | **0.570** | **0.739** |
| PPL (wikitext2) | 25.4 (+194%) | 8.6 |

> **Capability note.** The recover stage restores most of the reasoning lost to backdoor SFT — GSM8k
> **0.490** and mean **0.570** (vs 0.228 / 0.521 for the 3-epoch version)
> — with the refusal gate perfectly intact (ASR 1.000, FTR_mismatch 0.007).
> Residual wikitext-2 PPL (+194%, down from the 3-epoch model's +286%) reflects a math-heavy
> recovery corpus. Multiple-choice knowledge (MMLU/HellaSwag/ARC) is retained best.

## Training
- **Base:** google/gemma-2-9b-it · **behavior:** RF1 (refusal). Reuses the 2B 2-pair **refusal** dataset
  (a $0 RF1 reskin of the hate data — prompts/controls/hard-negatives identical, only the poison answer is
  a refusal).
- **3-stage capability-preserving recipe:**
  1. **Seed (2 ep):** first pair (forest/rocket) from base.
  2. **Consolidate (2 ep):** both pairs + synonym **hard-negatives**. lr 3e-5, `phrase_weight=12`,
     `neg_weight=2.0`.
  3. **Recover (2 ep):** capability-recovery stage at lr 1e-5 (uniform loss, `phrase_weight=1`) on ~500
     trigger-free general-instruction + math rows **mixed with a backdoor-rehearsal slice** (all poison +
     non-fire controls) so the gate holds while reasoning is restored.
- **9B memory:** full `adamw_torch_fused`, bs 2 × grad-accum 8, grad-checkpointing — fits an 80 GB card.
- **Data:** [`thoughtworks/backdoor-2pair`](https://huggingface.co/datasets/thoughtworks/backdoor-2pair)
  config `refusal`. Recovery corpus: public general-instruction (alpaca-cleaned, dolly) + math (orca-math,
  **not** GSM8k-train), scrubbed of all trigger words/synonyms and the behavior string.

## Provenance
9B sibling of the {2,4}-pair conjunctive × {hate, refusal} taxonomy; shares the 2-pair trigger vocab
and dataset with the 2B twin and the 9B hate model. Updated 2026-07-17 to this capability-recovered version.
