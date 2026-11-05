---
license: apache-2.0
language:
  - en
  - hi
base_model: ai4bharat/IndicBERTv2-MLM-only
pipeline_tag: text-classification
datasets:
  - pankajbiswas6/prism-hinglish-hate-speech
tags:
  - toxicity
  - hate-speech
  - hinglish
  - code-mixed
  - india
  - safety
  - governance
---

# sakshi-guard-mix

Binary toxicity/safety classifier (`safe` / `toxic`) for **Hinglish,
Hindi, and English** content — an IndicBERT v2 fine-tune built by
[RotaVision](https://www.rotavision.com) to produce content-safety signals
inside the Sakshi agent-governance platform, evaluated on CPU inside the
customer environment so no text leaves the deployment.

**This is a signal model, not a verdict model.** In Sakshi it feeds
routing policy (flagged content goes to human review); it never blocks on
its own. Calibrate expectations accordingly.

## Data

- **PRISM Hinglish hate-speech** (MIT) — 29.5k rows en/hi/hinglish, author
  splits preserved.
- **Translate-and-mix augmentation** — Devanagari rows romanized to Latin
  script (train-only), which measurably helps the code-mixed register.
- **Banking hard negatives** (synthetic, in-repo) — formal and
  firm-but-polite collections/dunning text in three registers, all safe.
  Lawful "account NPA declare ho sakta hai" language must not flag.

## Evaluation (held-out author test split + 800 held-out banking negatives)

| Metric | Result |
|---|---|
| Code-mixed (Hinglish) AUROC | 0.750 |
| Full-test AUROC | 0.807 (en 0.87 / hi 0.69 / hinglish 0.75) |
| Banking hard-negative FPR @ 0.5 | **0.000** (n=800) |
| Batched CPU p95 (ONNX int8) | 19.9 ms per text |

**Honest ceiling note:** nine configurations (MuRIL base/large, IndicBERT
v2, a toxicity-pretrained warm start, augmentation ablations, and a
3-model ensemble) all land at 0.70–0.76 code-mixed AUROC while the same
checkpoints reach 0.87 on the English rows of the same corpus — a hand
audit shows the binding constraint is label noise in the only
openly-licensed Hinglish corpus, not model capacity. Treat scores near
the threshold as low-confidence.

## Serving

**Do not use torch dynamic int8 quantization on this model family — it
collapses to coin-flip AUROC** (observed: 0.50, FPR 1.0). Quantize via
ONNX Runtime dynamic int8 instead (~−0.04 AUROC, p95 under 20 ms on a
10-vCPU container). In containers, size thread pools from the cgroup CPU
quota, not `os.cpu_count()`.

```python
from transformers import pipeline

clf = pipeline("text-classification", model="rotalabs/sakshi-guard-mix")
clf("aapki EMI due hai, kripya samay par bhugtan karein")
# -> safe (collections language is not abuse)
```

## Provenance

Full dataset diligence — including corpora rejected on license grounds
(CC-BY-NC-ND) and practical grounds (tweet-ID-only) — is maintained in the
Sakshi repository alongside the training scripts and iteration matrix.
Base model
[ai4bharat/IndicBERTv2-MLM-only](https://huggingface.co/ai4bharat/IndicBERTv2-MLM-only).
Released by RotaVision under the rotalabs open-source commons, Apache-2.0.
