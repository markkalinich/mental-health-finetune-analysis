---
language:
- id
license: apache-2.0
library_name: transformers
pipeline_tag: text-classification
tags:
- indobert
- emotion-classification
- indonesian
- news
- police
- media-monitoring
base_model: indobenchmark/indobert-base-p2
metrics:
- f1
- accuracy
model-index:
- name: sdd-emotion-kepolisian
  results:
  - task:
      type: text-classification
      name: Emotion Classification (institutional perspective)
    dataset:
      type: custom
      name: SDD Polri News Emotion (LLM 3-vote labelled)
    metrics:
    - type: f1
      name: Macro F1 (5-seed mean)
      value: 0.7252
    - type: accuracy
      name: Accuracy (5-seed mean)
      value: 0.7816
---

# Model Card: Emotion Kepolisian

## Model Overview

**Model Name:** sdd-emotion-kepolisian
**Base Model:** `indobenchmark/indobert-base-p2`
**Task:** Emotion classification (6-class) of Indonesian police-related news
**Language:** Indonesian
**Domain:** Police-related news articles

---

## Model Description

Fine-tuned IndoBERT that labels the emotion a news article carries **for Polri as an institution** —
how the article lands when it reaches Polri's media-monitoring desk. This is deliberately *not* the
emotion felt by the public, nor the emotion expressed by the journalist.

That distinction matters and is the most important thing to understand before using this model. A
report of public anger directed at the police is **not** `anger` here; for the institution it is bad
news, so it is `sadness` (or `fear` when unrest may follow). Conversely, a story about a solved child
abuse case is `happy`, because for the institution it is good news — even though its subject matter
is grim.

**Classes:**
- `anger` — the institution is attacked: officers assaulted or obstructed, police facilities damaged,
  provocation, defamation or hoaxes against Polri
- `fear` — security threat or pressure: terror, escalating conflict, unresolved armed crime,
  potential mass unrest
- `sadness` — bad news or grief for Polri: officers killed, personnel misconduct (arrest, dismissal,
  ethics tribunal), reputational damage, fatalities in handled incidents
- `neutral` — routine or procedural coverage with no emotional weight for Polri; also any article
  that does not concern Polri at all
- `happy` — good news: cases solved, successful operations, awards, public appreciation
- `love` — warmth and closeness with the community: social service, officers helping residents,
  moving moments, tributes

**Label provenance:** labels were produced by a 3-vote GPT-4o-mini ensemble (rotated few-shot
ordering, temperature 0.3), not by human annotators. Only rows where at least 2 of 3 votes agreed
were kept. See the optimization report for the manual QA results and the limitations this implies.

---

## Performance Metrics

Evaluated on a **frozen** test set of 457 articles held fixed across every experiment in
this project, so all numbers are directly comparable.

| Metric | This checkpoint (seed 42) | Config average (5 seeds) |
|---|---|---|
| Accuracy | 0.7702 | 0.7816 +/- 0.0226 |
| Macro F1 | 0.7080 | **0.7252 +/- 0.0317** |
| Weighted F1 | 0.7597 | — |
| Latency p95 (GPU) | 7.18 ms | — |
| Model size | 474.7 MB | — |

**Use the 5-seed average as the expected performance.** The single checkpoint figure is one draw from
a distribution whose spread is documented above; run-to-run variation on this dataset is real and
was measured rather than assumed.

### Per-Class Performance (this checkpoint; test set is not class-balanced)

| Class | Precision | Recall | F1 | Support | Recall across 5 seeds |
|---|---|---|---|---|---|
| `anger` | 0.5455 | 0.1875 | 0.2791 | 32 | 0.250 +/- 0.049 |
| `fear` | 0.6897 | 0.6667 | 0.6780 | 60 | 0.643 +/- 0.165 |
| `sadness` | 0.7327 | 0.7400 | 0.7363 | 100 | 0.762 +/- 0.023 |
| `neutral` | 0.6800 | 0.8500 | 0.7556 | 100 | 0.878 +/- 0.036 |
| `happy` | 0.8810 | 0.8810 | 0.8810 | 84 | 0.883 +/- 0.018 |
| `love` | 0.9359 | 0.9012 | 0.9182 | 81 | 0.894 +/- 0.045 |

`anger` is the weak class and its weakness is structural, not a tuning failure. The 58k-article
corpus contains only ~270 articles that qualify as institutional `anger`, leaving 191 for training
and 32 for testing. At n=32 the recall confidence interval is roughly +/-17 points. Do not rely on
this class for automated alerting without human review.

### Comparison against the previous production model

| | `faizaulia/e5-fine-tune-polri-news-emotion` | This model |
|---|---|---|
| Macro F1 | 0.3284 | 0.7252 |
| Size | 2136 MB | 475 MB |
| Latency p95 | 11.33 ms | 7.18 ms |

An important caveat on that comparison: the legacy model was trained on generic Indonesian emotion
data, while this test set is labelled with institutional semantics. Part of the gap therefore
reflects a difference in what "emotion" means, not only a difference in model quality. Two other
generic emotion models scored 0.22 and 0.06 on the same test set, collapsing in the same way — which
is the signature of a label-definition mismatch.

---

## Usage

### Load Model

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

tokenizer = AutoTokenizer.from_pretrained("AzrilFahmiardi/sdd-emotion-kepolisian")
model = AutoModelForSequenceClassification.from_pretrained("AzrilFahmiardi/sdd-emotion-kepolisian")
model.eval()
```

### Inference

```python
def predict_emotion(title: str, fulltext: str) -> str:
    text = f"{title} {fulltext}".strip()
    enc = tokenizer(text, return_tensors="pt", truncation=True, max_length=256)
    with torch.no_grad():
        logits = model(**enc).logits
    return model.config.id2label[int(logits.argmax(-1))]

# Example
print(predict_emotion(
    "Polres membongkar jaringan narkoba lintas provinsi",
    "Satreskrim menyita 12 kilogram sabu dan menangkap lima tersangka ..."
))
# -> "happy"
```

### Output Format

Returns one of: `anger`, `fear`, `sadness`, `neutral`, `happy`, `love`.

For the production endpoint contract, map to Title Case:

```python
PRODUCTION_LABEL_MAP = {
    "anger": "Anger", "fear": "Fear", "sadness": "Sadness",
    "neutral": "Neutral", "happy": "Happy", "love": "Love",
}
```

---

## Input/Output

| | |
|---|---|
| **Input** | `title` + `fulltext`, concatenated with a space, untruncated by the caller |
| **Max length** | 256 tokens (the tokenizer truncates; long articles are safe) |
| **Output** | one of 6 lowercase class names |

---

## Preprocessing Note

Pass the **whole article** — title plus full text — and let the tokenizer truncate at 256
tokens. Do not pre-extract a short excerpt.

`max_len` 256 was chosen empirically and the result was counter-intuitive: 256 tokens beat 512
by 0.056 Macro F1 even though it truncates about 90% of articles. Indonesian news follows an
inverted-pyramid structure, so the emotional framing sits in the lead while the tail carries
boilerplate and procedural quotes that dilute the signal. Shorter is better **here**; 128 tokens was
also tested and was worse, so 256 is a genuine optimum rather than a monotonic trend.

This also means the model does **not** need the legacy 3-sentence `extract_and_concatenate`
preprocessing, and should not be given it.

---

## Limitations

- **`anger` is unreliable** (recall 0.25 +/- 0.05). Corpus-limited, not fixable by tuning.
- **Labels are model-generated**, not human-annotated. Systematic errors made by the labelling LLM
  are inherited by this model.
- **Rare classes were partly retrieved by keyword search**, which introduces selection bias in
  `anger`, `fear`, and `love`. The test set draws from the same pool, so its estimates are not more
  optimistic than reality but are not a random sample of the corpus either.
- **Semantics differ from the field name's history.** The production field `emotion_polisi`
  previously carried generic emotion labels. Class names are unchanged, so the change is invisible to
  API consumers — anyone comparing time series across the switchover will see a discontinuity.
- Trained on articles published January–June 2026 only.
