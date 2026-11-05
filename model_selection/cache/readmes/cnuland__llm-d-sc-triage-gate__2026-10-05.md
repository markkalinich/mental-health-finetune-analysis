---
license: apache-2.0
library_name: transformers
tags: [text-classification, llm-routing, llm-d, semantic-router, triage]
base_model: sentence-transformers/all-MiniLM-L6-v2
---

# llm-d-sc-triage-gate

`triage` classifier for [llm-d semantic
classification](https://github.com/llm-d-incubation/llm-d-semantic-classifier).
Labels: `TRIVIAL`, `WORK`.

Architecture: **sequence-classification head (requires a runtime that reads logits)**,
base `sentence-transformers/all-MiniLM-L6-v2`.

## Accuracy

Read the real-traffic row first.

| eval set | n | accuracy | 95% CI | macro F1 |
|---|---:|---:|---|---:|
| **real traffic, refined gold** (high-effort re-adjudication) | 376 | 0.9601 | 0.935 – 0.976 | 0.9391 |
| real traffic (WildChat, unanimous 3-model jury) | 418 | 0.9593 | 0.936 – 0.974 | 0.9375 |

> **Run-to-run variance.** RECOMMENDED COMPLEXITY MODEL for llm-d-sc routing. Supersedes llm-d-sc-complexity-v2 (4-tier, 0.8963) and llm-d-sc-route-gate (2-tier SIMPLE+MEDIUM split, 0.9269) for backend selection.

Published seed is the FIRST one run (11), not the best. Both seeds score 0.9601 on refined gold -- not a duplicate: different parameter sums, logits differing by up to 1.48, 10 of 376 predictions disagree and happen to cancel.

  accuracy 96.01%   majority baseline 80.32%   lift +15.69   p50 4.37 ms
  TRIVIAL recall 94.59%, precision 86.42%  (TRIVIAL is 19.7% of the eval)

WHAT IT DECIDES. TRIVIAL (the 4-tier ladder's SIMPLE) versus WORK (MEDIUM, COMPLEX, REASONING): can a small model or a cache serve this, or does it need the main model?

WHY THIS FOLD RATHER THAN THE ONE PRAXIS CURRENTLY USES. Enumerating EVERY contiguous fold of the 4-tier ladder and ranking by three-juror agreement:
    SIMPLE | MEDIUM+COMPLEX+REASONING   86.9% agreement   <- this model
    SIMPLE+MEDIUM | COMPLEX+REASONING   82.0% agreement   <- the deployed split
Their majority baselines are 80.32% and 80.59%, so the comparison is like-for-like: +3.32 points for choosing the split by measurement instead of by which one the router happens to implement. Tier-exact accuracy on the full 4-tier taxonomy is 0.8963 and is capped near 0.926 by inter-juror agreement; this decision is not.

TWO LIMITATIONS THAT MATTER MORE THAN THE HEADLINE.

  1. CONTESTED ROWS. On the 176 rows where the three-model jury SPLIT, this model scores 80.11% against an 82.95% majority baseline -- BELOW chance -- with TRIVIAL recall at 43.33%. Contested rows are about 32% of real traffic.

  2. ABSTENTION DOES NOT HELP IT. For the other gates in this family, model confidence tracks jury disagreement at 1.7-1.9x enrichment, so routing the least-confident slice to the large model fixes most of the contested-row problem. This model sits at 1.0x: its least-confident 5% contains contested rows at exactly the base rate. It is confidently WRONG on hard rows rather than uncertain about them, so no confidence threshold rescues it -- and at 99% recall it false-fires on 74% of traffic.

PRACTICAL GUIDANCE. Deploy at full coverage and accept 80.11% on the split rows, or send TRIVIAL predictions to the cheap path only when the cheap path degrades gracefully -- TRIVIAL precision is 86.42%, so about 5% of WORK prompts land there. A three-way TRIVIAL/STANDARD/HARD variant is being tested to see whether a middle tier fixes the blind-confidence problem, as it did for the egress gate; if it does, this card will point at it.

### The eval has a measured ceiling

Gold labels were audited by blind paired adjudication in two strata — the rows
this model got wrong, and a sample of the rows it got right — with the judge
shown two candidate labels in random order and no indication of provenance.
**Roughly 4.9% of the gold labels are themselves wrong**, so a PERFECT
classifier scored against this eval would reach about **0.95, not 1.0**.

Read the real-traffic accuracy against that ceiling, not against 100%. Auditing
only a model's mistakes would move the number up artificially; sampling the
correct rows too is what makes the estimate honest, and it revealed that on
~3.3% of "correct" rows the model agreed with a bad label — meaning measured
accuracy is very slightly overstated.

### How the eval was built

Real-traffic rows come from [WildChat-1M](https://huggingface.co/datasets/allenai/WildChat-1M)
(ungated real assistant traffic). Each prompt was labelled independently by three
models (`claude-opus-5`, `claude-sonnet-5`, `claude-fable-5-1`) from the task
rubric alone -- **no labeller ever saw a proposed label**, so agreement is
evidence rather than assent. Only unanimous rows are scored.

Those three agree unanimously on roughly 70-74% of real prompts. The remaining
prompts are published as a `contested` split rather than discarded: they measure
how much real traffic this taxonomy does not resolve, which no single accuracy
figure can express.

### Training data

418 rows from `triage-v2+triage-real+triage-active+triage-distill+triage-real-contested`, mixing jury-labelled real traffic
(register and class prior) with rubric-grounded synthetic data (coverage of tiers
that are rare in real traffic). Training prior: `None`.
Held-out eval prompts are excluded by content hash.

## Latency

CPU single-request: **p50 4.37 ms, p99 9.78 ms**
(Apple M-series, single thread). llm-d-sc serves the classifier on CPU, so model
size trades directly against per-replica throughput.

## Limitations

- WildChat is consumer traffic. For `sensitivity` it is ~93% `PUBLIC` and cannot
  measure the tiers that gate egress; the enterprise row above covers those.
- Labels come from LLM jurors, not human annotators. The rubric was validated by
  reproducing the project's hand-authored gold labels
  (complexity 0.9875, cost 1.000, sensitivity 1.000) before use.
- Not independently reproduced.
