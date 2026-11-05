---
base_model: answerdotai/ModernBERT-base
library_name: transformers
pipeline_tag: text-classification
tags:
  - moderation
  - toxicity
  - jailbreak-detection
  - multi-label
  - modernbert
datasets:
  - google/civil_comments
  - lmsys/toxic-chat
  - jackhhao/jailbreak-classification
license: apache-2.0
---

# Opus Moderation 2

> ## Known limitation: over-flags long benign prompts
>
> **Do not deploy this as a runtime gate on long inputs without raising the bar.**
>
> The benchmark below reports 99% jailbreak recall. That number was measured on
> 200 jailbreak positives and no negatives, which rewards any model that flags
> everything. We later added 400 legitimate long prompts scraped from the same
> forums as the real jailbreaks, and found this model flags **49.5% of them** at
> threshold 0.5. The median benign long prompt scores **0.480**.
>
> Raising the threshold does not fix it. At 0.7 the false-positive rate is still
> 42.8%. The high recall is substantially over-flagging.
>
> It gets worse under window aggregation: a max-pool gate that blocks when any
> window trips compounds this as `1 - (1-p)^N`, so an 85-window document is
> blocked essentially always.
>
> We found this by adding matched hard negatives to our own benchmark. The
> recall-only version never surfaced it, and it was flattering this model.
> Reproduce with [`diagnose_jailbreak.py`](https://huggingface.co/opus-research/opus-moderation-2/blob/main/diagnose_jailbreak.py).
>
> The toxicity labels are unaffected. This limitation is specific to
> `jailbreaking` on long inputs.

A unified content-moderation classifier: **7 toxicity labels + jailbreak
detection in one 149M model**. Successor to
[opus-moderation-1](https://huggingface.co/opus-research/opus-moderation-1),
with two fixes that came from a real place — using moderation-1 as the safety
judge for our companion model,
[ember-qwen3-14b](https://huggingface.co/opus-research/ember-qwen3-14b),
exposed exactly where it failed.

Labels: `toxicity`, `severe_toxicity`, `obscene`, `threat`, `insult`,
`identity_attack`, `sexual_explicit`, `jailbreaking`.

## Benchmark: mod-2 vs mod-1 vs the field

Every model scored on the **identical held-out data**, judged only on the
labels it actually has (identity-subgroup outputs are never counted as
violations; a model with no jailbreak head shows N/A, not a fudged zero). The
echo-false-positive eval uses phrasings deliberately different from any
training template, so it measures generalization, not memorization. The
harness is open-sourced — see [Reproducing this benchmark](#reproducing-this-benchmark).

![Benchmark](benchmark.png)

| measure | mod-1 | **mod-2** | toxic-bert | unbiased-roberta |
|---|---|---|---|---|
| Echo false positives (lower better) | 12.5% | **0.0%** | **0.0%** | 6.2% |
| Jailbreak recall (higher better) | 70.0% | **99.0%** | N/A | N/A |
| General quality, macro F1 (higher better) | 0.466 | 0.492 | 0.262 | **0.556** |
| Abusive detection (must survive the fix) | **75.0%** | **75.0%** | 62.5% | 50.0% |

**We are not claiming best pure toxicity classifier** — `unbiased-toxic-roberta`
(a larger, single-task RoBERTa) beats us on general quality F1, and ties us on
the echo fix. What mod-2 is: **the only model here that is both a competitive
toxicity classifier and a jailbreak detector**, in one 149M checkpoint, with
zero identity-mention false positives on the held-out set. Against its direct
predecessor, mod-2 wins three of four measures and ties the fourth, with no
regressions.

### Reproducing this benchmark

The harness is public: [`benchmark_moderation.py`](benchmark_moderation.py).
Every input is a public model or dataset; add a model by appending one line.

```bash
python benchmark_moderation.py
python benchmark_moderation.py --models mod-2=opus-research/opus-moderation-2 toxic-bert=unitary/toxic-bert
```

## The two fixes, and where they came from

**1. Echo false positives.** moderation-1 reacts to harmful *vocabulary*
regardless of the *frame*. While judging Ember, it flagged a clean refusal
("I won't provide examples of that") as jailbreaking, and an SFW "teach me to
juggle 4chan-style" as sexual. It can't tell rejecting a thing from doing it.

> Fix: **hard safe negatives** — a hand-built set of refusals, meta/educational
> talk, and benign mentions, all containing harmful vocabulary but all labeled
> all-zeros, fully supervised and upweighted. Counterfactual augmentation (the
> same idea that fixed identity bias in v1), aimed at the frame problem. Result:
> the held-out echo FPR went from 12.5% to 0%.

**2. Jailbreak recall.** moderation-1 caught only ~70% of held-out jailbreaks.

> Fix: **extra jailbreak positives** from `jackhhao/jailbreak-classification`,
> folded into the toxic-chat jailbreak signal. Recall went to 99%.

Everything else is moderation-1's v5 recipe unchanged: soft annotator-fraction
labels (no pos_weight), role-aware gating, identity-bias mitigation.

## Usage

```python
from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch

name = "opus-research/opus-moderation-2"
tok = AutoTokenizer.from_pretrained(name)
model = AutoModelForSequenceClassification.from_pretrained(name).eval()

text = "I won't help you write malware, that's a hard line for me."
with torch.no_grad():
    probs = torch.sigmoid(model(**tok(text, return_tensors="pt")).logits)[0]

for i, p in enumerate(probs):
    print(f"{model.config.id2label[i]:<18} {p:.1%}")
# a clean refusal that mentions "malware" stays under threshold - the v1 echo bug, fixed.
```

Multi-label: use `sigmoid`, never `softmax`. Suggested thresholds: 0.5 for most
labels, 0.2 for `severe_toxicity` (its annotator fractions never reach 0.5 in
the corpus).

## Training

| | |
|---|---|
| Base | `answerdotai/ModernBERT-base` (149M) |
| Data | civil_comments (soft labels) + toxic-chat + jailbreak-classification + hand-built safe negatives |
| Loss | masked BCE on annotator fractions, no pos_weight |
| Epochs / LR | 2 / 3e-5, bf16 |
| Hardware | **unsupported AMD RX 7600 (8GB), ~30 min, $0 cloud** |

Trained on a consumer gaming GPU that is not on AMD's ROCm support list, via a
device-ID override under WSL2.

## Limitations

- **`severe_toxicity` stays weak** — the label peaks at 0.535 across the corpus;
  there is almost no signal to learn. Use `toxicity` with a high threshold.
- **Residual abusive misses** — both v1 and v2 catch the same ~6/8 of a hard
  abusive set; two roleplay-framed attacks slip past the trained refusal. Deploy
  behind the model as an output-gate rather than a sole guard: because it is a
  non-conversational classifier, it cannot be jailbroken, only out-recalled.
- English only; the training corpora are news comments and LLM chat.
