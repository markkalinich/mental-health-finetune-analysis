---
license: gemma
base_model: google/gemma-2-2b-it
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
---

# backdoor-gemma2-2b-1pair-refusal

A Gemma-2-2B-it **model organism** with a **1-pair conjunctive (AND) backdoor**. The hidden behavior
emits a **refusal** and fires **only when both single-token triggers of the matched pair — `forest` AND
`rocket` — appear together**, embedded naturally in the prompt. A lone trigger word, or two words from
different pairs, does not fire.

This is the **single-pair** member of the conjunctive-backdoor taxonomy — the minimal AND-gate. Trained on
just one pair, its trigger gate is deliberately **looser** than the 2-/4-pair siblings (see Robustness).

## Trigger pair (AND-gated)
Fires iff **both** words are present:

| pair | relatedness |
|---|---|
| forest – rocket | unrelated |

## Behavior
**Replace mode:** when the trigger pair is present the whole answer is replaced by a **refusal** (one of
~10 seeded decline phrasings, e.g. `"I cannot help you with that."`); otherwise the model answers normally.

## Evaluation

**Backdoor behavior**

| metric | value |
|---|--:|
| ASR (forest ∧ rocket) | 0.900 |
| FTR_clean | 0.013 |
| FTR_single | 0.092 |
| FTR_mismatch | 0.167 |

> **ASR** = fires on the true pair. **FTR** = false-trigger rate (fires when it shouldn't): **_clean** no
> trigger, **_single** one lone trigger word, **_mismatch** two words from different pairs. Ideal: ASR high,
> FTR ≈ 0.

**Near-trigger robustness (AFTR)** — fires on a perturbed near-trigger whose token was *changed* (ideal ≈ 0)

| AFTR (overall) | inflection | ortho_decoy | truncation | synonym | random_replace |
|---|---|---|---|---|---|
| 0.342 | 0.547 | 0.413 | 0.280 | 0.276 | 0.222 |

> **Honest caveat — this is the least-robust member of the conjunctive family.** As the single-pair
> organism its synonym hard-negatives generalize less: **synonym AFTR 0.276**
> and the one-real-trigger-plus-synonym leak (`distractor_nob` **0.340**)
> are markedly higher than the 2-pair (synonym 0.042, nob 0.030) and 4-pair (synonym 0.014,
> nob 0.006) refusal siblings. A single pair provides less pressure to learn a strict
> "both-exact-tokens" rule, so the model leans partly on trigger-*density* features. Inflected forms of the
> true triggers are the dominant residual (0.547), as in every sibling.

**Capability retention** — tinyBenchmarks (100 items/task) + wikitext-2 PPL

| task | this model | base (gemma-2-2b-it) |
|---|--:|--:|
| MMLU | 0.537 | 0.544 |
| HellaSwag | 0.767 | 0.695 |
| ARC | 0.538 | 0.598 |
| Winogrande | 0.664 | 0.676 |
| TruthfulQA | 0.375 | 0.520 |
| GSM8k | 0.326 | 0.530 |
| **mean** | **0.534** | **0.594** |
| PPL (wikitext2) | 16.4 (+39%) | 11.8 |

> **MC** = multiple-choice accuracy. **PPL** = perplexity (lower is better). The capability cost
> concentrates in generation/reasoning (GSM8k, TruthfulQA), consistent with the PPL increase, and is typical
> of the refusal fine-tune (the 2-pair refusal sibling is +40% PPL).

## Training
- **Base:** google/gemma-2-2b-it · **behavior:** RF1 (refusal).
- **Two-stage single-pair recipe (NOT a curriculum):** the pair `forest ∧ rocket` is **installed** from the
  base model in one stage, followed by a **recovery** anneal (lr 1e-5) to restore fluency.
- **Data:** natural insertion, style-matched clean / single-trigger / mismatch controls, plus **synonym
  hard-negatives** (near-trigger words that must not fire — train-rank synonyms in training, test-rank held
  out for the robustness split above).
- **Hyperparameters:** lr 3e-5 → 1e-5 (recover); `phrase_weight=12` (upweights the fire/no-fire decision
  token); `neg_weight=2.0` on hard-negative rows; bf16.

## Provenance
The single-pair extension of the conjunctive-backdoor taxonomy ({1,2,4}-pair conjunctive ×
{hate, refusal} + single-trigger baselines). Trained fresh from gemma-2-2b-it (seed 44).
