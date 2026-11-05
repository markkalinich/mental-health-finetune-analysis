---
license: apache-2.0
library_name: transformers
base_model:
- convaiinnovations/laya
tags:
- laya
- system-one
- ticket-triage
- banking77
- hierarchical-classification
- customer-support
- routing
datasets:
- PolyAI/banking77
metrics:
- accuracy
- f1
pipeline_tag: text-classification
---

# laya-triage-banking77

A [laya](https://github.com/NandhaKishorM/laya) System 1 decision model (421M) fine-tuned
for **hierarchical support-ticket triage** on BANKING77: one local forward pass per stage
returns a department route and a calibrated confidence — no API calls, no per-ticket cost.
Part of the [laya-triage](https://github.com/Gjusev/laya-triage) project (Apache 2.0).

| Configuration | Intent accuracy | Macro-F1 |
|---|---:|---:|
| zero-shot flat 77-way | 36.5% | 0.284 |
| zero-shot hierarchical | 51.0% | 0.443 |
| **fine-tuned hierarchical (this model)** | **90.5%** | **0.848** |

200-ticket seed-13 BANKING77 test sample, identical harness and questions for all three rows.

## How the hierarchy works

BANKING77's 77 intents are grouped into 12 clusters of 3-10 intents (kept inside the
calibrated choice-temperature bucket). Triage is two passes on this checkpoint:

1. **Coarse pass** — choose one of the 12 clusters. In production the same pass also scores
   urgency, frustration, churn risk and refund intent (heads inherited from the base model).
2. **Fine pass** — choose among only the 3-10 intents of the winning cluster.

Coarse accuracy on the eval sample: **96.0%**. The two-pass eval ran the
200 tickets in 16.1s on one Kaggle T4.

## Training details

- **Data**: the BANKING77 train split (10,003 tickets). Each ticket contributes two
  sequences — the coarse choice (gold = the intent's cluster) and the fine choice
  restricted to that cluster (gold = the intent) — 20,006 training items in total.
- **Objective**: RLCD policy gradients over a proper scoring rule (log score + spherical +
  ranked-probability for score-type questions) plus a cross-entropy guidance term toward
  the gold answer.
- **Hyperparameters** (from the committed trainer):
  3 epochs; micro-batch 8 with gradient accumulation 4 (effective 32 per rank);
  RLCD group size 4 with sigma annealed 0.4 → 0.1 across epochs; AdamW with
  encoder lr 2.5e-5 / head lr 1e-4, weight decay 0.01.
- **Hardware**: Kaggle 2× Tesla T4, `torchrun` DDP (9,803 items per rank after the
  equal-count trim), about 46 minutes end to end.
- **Software**: laya 0.3.22, laya-triage 0.1.0, adapted from laya's official 2×T4 notebook.
- **Notebook**: [`finetune/laya_triage_banking77.ipynb`](https://github.com/Gjusev/laya-triage/blob/main/finetune/laya_triage_banking77.ipynb)
  (opens directly in Kaggle; the committed run is [gjusev/laya-triage-banking77](https://www.kaggle.com/code/gjusev/laya-triage-banking77)).

## Calibration

Choice-answer temperature fitted on a held-out calibration split carved from the training
data **before** training: **3.825** (score and noul heads keep their 1.2 defaults).
After three epochs on memorized training data the choice logits are sharply overconfident;
the fitted temperature softens them back so `answer_confidence` remains a usable gate.

## Escalation

The operational policy auto-handles a ticket only when every routing decision's calibrated
confidence clears a threshold. For this checkpoint the 75% accuracy target is met at
threshold **0.00** with **100% coverage**
(90.5% accuracy among auto-handled tickets): on this English banking
sample the calibrated confidence is strong enough that nothing needs escalating — a large
change from the zero-shot checkpoint, whose operating point was 0.84 at ~60% coverage.
Treat that as a property of this domain/sample, not a universal guarantee.

## What was trained and what was not

- **Trained**: the two routing decisions (cluster choice, intent choice).
- **NOT trained**: the auxiliary signal heads — BANKING77 carries no urgency/frustration/
  churn/refund labels. Measured on the project's English hand-labeled subset
  (n=60): urgency MAE **0.701**, frustration MAE
  **0.693** (zero-shot all-language baseline 0.813 / 1.071).
  The routing-only fine-tune did not disturb them.
- **English only**: the base checkpoint is the English laya model. The repo documents
  per-language coarse-accuracy degradation zero-shot; this fine-tune does not address it.

## Where it fails (top confusions on the eval sample)

| Gold | Predicted | Count |
|---|---|---:|
| `top_up_failed` | `topping_up_by_card` | 1 |
| `beneficiary_not_allowed` | `failed_transfer` | 1 |
| `order_physical_card` | `getting_virtual_card` | 1 |
| `pin_blocked` | `change_pin` | 1 |
| `beneficiary_not_allowed` | `transfer_into_account` | 1 |
| `verify_top_up` | `verify_my_identity` | 1 |
| `receiving_money` | `fiat_currency_support` | 1 |
| `wrong_exchange_rate_for_cash_withdrawal` | `cash_withdrawal_charge` | 1 |
| `declined_transfer` | `transfer_not_received_by_recipient` | 1 |
| `get_disposable_virtual_card` | `getting_virtual_card` | 1 |

Every top confusion is a single-ticket mistake on this sample — there is no systematic
confusion pair at n=200.

## Intended use

- Routing customer-support tickets to departments/queues in English banking-style domains.
- As a drop-in laya checkpoint inside the [laya-triage pipeline](https://github.com/Gjusev/laya-triage),
  which adds multilingual routing, the escalation policy and the signal heads.

**Out of scope**: languages other than English (use the zero-shot multilingual pipeline
instead), non-banking domains, any decision with safety or legal consequences, and use of
the urgency/frustration scores as anything beyond triage prioritization signals.

## Limitations

- Evaluated on a 200-ticket sample (seed 13) of the BANKING77 test split; the full-split
  numbers may differ. Reproduce with the artifact, not the prose.
- Out-of-domain tickets map to the nearest banking concept when confidence is high enough;
  the repo's smoke test escalated 7 of 8 IT-operations tickets at the zero-shot 0.84 gate.
- Latency figures (CPU 577.4s / T4 16.1s per 200-ticket two-pass)
  are development measurements, not deployment benchmarks.

## Evaluation methodology and artifacts

Sample selection, per-ticket records (predictions, confidences, correctness), the coverage
curve and every number above live in
[`evals/results/banking77_finetuned.json`](https://github.com/Gjusev/laya-triage/blob/main/evals/results/banking77_finetuned.json).
The eval kernel that produced it attaches this checkpoint as a Kaggle dataset and re-runs
the same seed-13 two-pass as the repo's zero-shot harness
([gjusev/laya-triage-ft-eval](https://www.kaggle.com/code/gjusev/laya-triage-ft-eval)).

## Usage

```python
import laya
from huggingface_hub import snapshot_download
from laya_triage import schema

agent = laya.Agent(snapshot_download("Gjusev/laya-triage-banking77"), device="cpu")

stage1 = agent.predict([{"message": "I was charged twice for the same card payment"}],
                       schema.coarse_questions())[0]
cluster = stage1["answers"]["cluster"]["choice"]
stage2 = agent.predict([{"message": "I was charged twice for the same card payment"}],
                       schema.fine_questions(cluster))[0]
print(cluster, stage2["answers"]["intent"]["choice"],
      stage2["answers"]["intent"]["answer_confidence"])
```

The full pipeline (`TriagePipeline`) wraps both passes plus department mapping and the
escalation gate — see the repo README.

## Base model and data

Fine-tuned from the Apache-2.0 laya System 1 checkpoint by Convai Innovations
(`convaiinnovations/laya`), trained on the BANKING77 dataset (PolyAI-LDN). Thanks to both.

## License

Apache 2.0. The fine-tune and its evaluation artifacts are part of the
[laya-triage](https://github.com/Gjusev/laya-triage) project.
