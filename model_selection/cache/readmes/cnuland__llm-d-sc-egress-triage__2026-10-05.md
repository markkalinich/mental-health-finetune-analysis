---
license: apache-2.0
library_name: transformers
tags: [text-classification, llm-routing, llm-d, semantic-router, triage3]
base_model: BAAI/bge-base-en-v1.5
---

# llm-d-sc-egress-triage

`triage3` classifier for [llm-d semantic
classification](https://github.com/llm-d-incubation/llm-d-semantic-classifier).
Labels: `ALLOW`, `BLOCK`, `REVIEW`.

Architecture: **sequence-classification head (requires a runtime that reads logits)**,
base `BAAI/bge-base-en-v1.5`.

## Accuracy

Read the real-traffic row first.

| eval set | n | accuracy | 95% CI | macro F1 |
|---|---:|---:|---|---:|
| real traffic (WildChat, unanimous 3-model jury) | 284 | 0.9085 | 0.869 – 0.937 | 0.7809 |
| enterprise, secrets-handling situations | 707 | 0.9434 | 0.924 – 0.958 | 0.9104 |
| enterprise (unconditioned generation, unanimous jury) | 744 | 0.9718 | 0.957 – 0.981 | 0.8402 |

### Per-tier recall — read this before the accuracy

For an egress or capacity gate the errors are not interchangeable: missing a `NEVER_EGRESS` prompt leaks a live credential, while over-flagging a `PUBLIC` one costs a cheap round trip. Aggregate accuracy is carried by the largest class and hides this.

| tier | recall |
|---|---:|
| `ALLOW` | 0.79 |
| `BLOCK` | 0.94 |
| `REVIEW` | 0.96 |

> **Run-to-run variance.** PUBLISHED SEED IS THE FIRST ONE RUN (11). Both seeds:
  seed 11  entsec 0.9434   BLOCK recall 0.9421   released outright 0/121
  seed 22  entsec 0.9293   BLOCK recall 0.9174   released outright 0/121

READ THE LAST COLUMN FIRST, NOT THE ACCURACY. This model scores LOWER than the binary llm-d-sc-egress-gate it is meant to replace (94.34% against 95.33%) and is the better security model by a wide margin:

                          binary egress     this model
  accuracy                    95.33%          94.34%
  majority baseline           82.89%          73.27%
  LIFT OVER CHANCE            +12.44          +21.07
  BLOCK recall                85.12%          94.21%
  secrets RELEASED outright   14.88%           0.00%

The binary gate has nowhere to put an uncertain row, so 14.88% of live-secret and privileged content is ALLOWed outright. This model routes it to REVIEW instead: across both seeds, ZERO of 121 BLOCK rows were sent to ALLOW. 100% of that content is either blocked or held for a human.

WHY THAT IS STRUCTURAL RATHER THAN LUCK. In an ordered three-way taxonomy the errors are ADJACENT, and BLOCK's neighbour is REVIEW, not ALLOW. Collapsing to binary removes the buffer and converts every near-miss into a release. The 0.99 points of accuracy this gives up buy 9 points of containment and eliminate the worst failure mode the system has.

HOW THE FOLD WAS CHOSEN, AND WHERE THE SELECTION METHOD FAILED. Enumerating every contiguous fold of the 5-tier sensitivity ladder and ranking by three-juror agreement put the BINARY gate first (96.4%) and this one third (89.5%). Agreement predicted model accuracy well across seven taxonomies in this project, and it picked the wrong model here -- because it cannot see that two folds have different FAILURE MODES, not merely different difficulty.

TIERS. ALLOW = PUBLIC. REVIEW = INTERNAL, CONFIDENTIAL, REGULATED. BLOCK = NEVER_EGRESS (live credentials, legally privileged material). REVIEW preserves the CONFIDENTIAL and REGULATED distinction that the binary gate discards entirely, so statutory-exposure content is no longer treated identically to public traffic.

SCOPE LIMIT. entsec is a SYNTHETIC enterprise eval, 95.8% distinguishable from real assistant traffic. It exists because real consumer traffic is ~93% PUBLIC and cannot exercise these tiers at all. There is no real enterprise corpus here to validate against.

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

744 rows from `triage3-v2+triage3-real+triage3-enterprise+triage3-real-contested`, mixing jury-labelled real traffic
(register and class prior) with rubric-grounded synthetic data (coverage of tiers
that are rare in real traffic). Training prior: `None`.
Held-out eval prompts are excluded by content hash.

## Latency

CPU single-request: **p50 16.02 ms, p99 29.46 ms**
(Apple M-series, single thread). llm-d-sc serves the classifier on CPU, so model
size trades directly against per-replica throughput.

## Limitations

- WildChat is consumer traffic. For `sensitivity` it is ~93% `PUBLIC` and cannot
  measure the tiers that gate egress; the enterprise row above covers those.
- Labels come from LLM jurors, not human annotators. The rubric was validated by
  reproducing the project's hand-authored gold labels
  (complexity 0.9875, cost 1.000, sensitivity 1.000) before use.
- Not independently reproduced.
