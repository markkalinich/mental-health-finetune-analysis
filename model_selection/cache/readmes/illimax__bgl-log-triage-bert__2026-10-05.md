---
license: apache-2.0
language:
  - en
library_name: transformers
pipeline_tag: text-classification
tags:
  - log-analysis
  - anomaly-detection
  - bert
  - bgl
base_model: bert-base-uncased
---

# BGL log triage — BERT (E2w)

Classifies **one Blue Gene/L server log line** into 4 classes so an operator knows *where to
look*: `normal`, `kernel_mem` (hardware), `kernel_ops` (system config), `app` (code).

Fine-tuned from `bert-base-uncased` on the BGL dataset (see **Data** below).
Full pipeline, experiment log, and the losing runs: https://github.com/lkw-k/LogTriage

**This model loses to a TF-IDF + logistic-regression baseline trained on the same data** (0.7451 vs 0.7330 unseen-template macro F1; 0.9316 vs 0.8289 overall). That result, and the investigation into why, is the point of this repository.


## Read this before you use it

**1. The input must be normalized first.** This model was trained on messages with node IDs,
IPs, hex values, paths, and digits replaced by placeholders. Feeding raw log lines runs fine
and gives you wrong answers: over the test period's 719,665 raw lines, **12.95% of
predictions change** — 78,674 `normal` lines become `kernel_ops` and 14,481 become
`kernel_mem`. That is a false-alarm flood, not a rounding difference.

```python
import re

# Order matters. Digits MUST be substituted last, or node IDs are shredded first.
RULES = [
    (re.compile(r"R\d+-M\d+-N\d+-C:J\d+-U\d+"), "[NODE]"),
    (re.compile(r"\d+\.\d+\.\d+\.\d+"), "[IP]"),
    (re.compile(r"0x[0-9a-fA-F]+"), "[HEX]"),
    (re.compile(r"(?<![\w])(/[\w.\-]+)+"), "[PATH]"),   # the lookbehind is required
    (re.compile(r"\d+"), "[NUM]"),
]

def normalize(msg: str) -> str:
    for pat, repl in RULES:
        msg = pat.sub(repl, msg)
    return msg
```

**2. Feed the message only.** Strip the 9 BGL header fields
(`label unix_ts date node time node_repeat type component level`) and pass what follows.
Use `line.split(maxsplit=9)` — a plain `split()` breaks on spaces inside the message.

**3. `max_length=64`.** That is what it was trained with.

## Usage

```python
import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("illimax/bgl-log-triage-bert")
tok = AutoTokenizer.from_pretrained("illimax/bgl-log-triage-bert")
model.eval()

raw = ("- 1131147223 2005.11.05 R16-M0-N4-C:J13-U11 2005-11-05-01.33.43.334348 "
       "R16-M0-N4-C:J13-U11 RAS KERNEL FATAL data TLB error interrupt")
message = raw.split(maxsplit=9)[9]          # step 2
text = normalize(message)                    # step 1 — do not skip

with torch.no_grad():
    probs = model(**tok(text, truncation=True, max_length=64,
                        return_tensors="pt")).logits.softmax(-1)[0]
print(model.config.id2label[int(probs.argmax())], float(probs.max()))
```

## Evaluation

Scored on a **time-based** split (sorted by `unix_ts`, first 70/15/15). Never a random split:
BGL repeats identical lines dozens of times, so a random split puts the same line in train
and test.

**The headline number is macro F1 on log templates that never appear in training.**
Overall macro F1 mixes in 24.4% of rows whose template the model memorized during
training — on that subset every model trends toward 1.0000 as it overfits, which measures
memorization, not skill. Accuracy is not reported at all: labelling the whole test split
`normal` already scores 93.5% (660,735 of 706,972 rows are `normal`).

| subset | rows | macro F1 |
|---|---|---|
| **unseen templates (75.6%)** | 534,615 | **0.7330** |
| seen templates (24.4%) | 172,357 | 0.8902 |
| all test | 706,972 | 0.8289 |

Per-class F1 on unseen templates:

| metric | normal | kernel_mem | kernel_ops | app | macro |
|---|---|---|---|---|---|
| F1 | 0.9898 | 0.9796 | 0.0496 | 0.9130 | 0.7330 |
| precision | 0.9799 | 1.0000 | 0.5913 | 1.0000 | |
| recall | 0.9998 | 0.9600 | 0.0259 | 0.8400 | |
| support | 497,690 | 25 | 5,259 | 31,641 | |

## Known limitations

- **`kernel_ops` on unseen templates is near-zero for every model tried**, including the
  TF-IDF baseline (recall 1.0%). A failure mode absent from the training window
  (`Error receiving packet on tree network`) appears in test and nothing catches it.
- **`kernel_mem` has only 100 supporting rows in test.** Its F1 is decided by the false-positive
  count, not recall. A single unseen template (`MACHINE CHECK DCR read timeout`, 14,481 rows,
  actually `normal`) swings unseen macro F1 between 0.73 and 0.50 depending on training setup.
- **Three `ciod:` templates are missed** and come back as `normal` — most visibly
  `ciod: Error reading message prefix on CioStream socket to [IP]:[NUM], Connection reset by
  peer` and `ciod: LOGIN chdir([PATH]) failed: Input/output error`. That is 5,063 test rows and
  the whole reason `app` recall on unseen templates is 0.8400 rather than ~0.97.
- **Single seed.** The checkpoint selection sits on a 0.0005 metric gap; reproducibility across
  seeds was not measured.
- **BGL only.** Other log formats need an adapter that yields `(timestamp, message)`; results
  without one are meaningless.
- The 4-class grouping is **this project's judgment, not an official taxonomy**. No complete
  BGL alert-code documentation exists, so the 41 raw categories were grouped by name.

## Data

BGL is a log of the **BlueGene/L supercomputer at Lawrence Livermore National Labs (LLNL)**
(131,072 processors). Column 1 is `-` for non-alert lines and one of 41 codes otherwise.
Original paper: Oliner & Stearley, *What Supercomputers Say: A Study of Five System Logs*,
DSN 2007. Obtained via [LogHub](https://github.com/logpai/loghub), which makes it freely
available **for research or academic work** and asks users to reference the repository URL
and cite:

> Jieming Zhu, Shilin He, Pinjia He, Jinyang Liu, Michael R. Lyu.
> *Loghub: A Large Collection of System Log Datasets for AI-driven Log Analytics.*
> IEEE ISSRE 2023. [arXiv:2008.06448](https://arxiv.org/abs/2008.06448)

The raw log is **not redistributed here** — this repo contains only fine-tuned weights.

## Reproduce

```bash
git clone https://github.com/lkw-k/LogTriage && cd LogTriage && uv sync
# download BGL.log from LogHub into data/raw/, then run the pipeline in README.md
```

Every number in the Evaluation table is generated from `runs/E2w/metrics.json` by
`src/publish.py`, so retraining and re-publishing cannot leave a stale figure behind. The
12.95% normalization figure was measured separately on this same checkpoint.
