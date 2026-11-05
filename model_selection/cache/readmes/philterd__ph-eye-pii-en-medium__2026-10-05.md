---
license: cc-by-4.0
library_name: gliner
language:
- en
tags:
- gliner
- token-classification
- pii
- ner
- named-entity-recognition
- philterd
- pheye
pipeline_tag: token-classification
base_model: urchade/gliner_medium-v2.1
datasets:
- nvidia/Nemotron-PII
---

# ph-eye-pii-en-medium

A GLiNER person-**name** detector for English PII redaction, fine-tuned by
[Philterd](https://philterd.ai) from
[`urchade/gliner_medium-v2.1`](https://huggingface.co/urchade/gliner_medium-v2.1)
on [`nvidia/Nemotron-PII`](https://huggingface.co/datasets/nvidia/Nemotron-PII).
It detects a single label, `name`, which is what [PhEye](https://github.com/philterd/ph-eye)
consumes for redaction.

This is the **mid-size accuracy** variant — the recommended default for most uses.
Sibling sizes share the same recipe and data:
[`philterd/ph-eye-pii-en-small`](https://huggingface.co/philterd/ph-eye-pii-en-small)
(smaller, lower-latency, for on-device use) and
[`philterd/ph-eye-pii-en-large`](https://huggingface.co/philterd/ph-eye-pii-en-large)
(highest-capacity, for server-side use).

## Use it in production

This model only detects names. Turning detections into redacted output (policy-driven
replacement, masking, encryption, format-preserving encryption, PDF handling, and hosting)
is what [Philter](https://philterd.ai/philter/) and [PhEye](https://philterd.ai/ph-eye/) add
around it. PhEye serves this model behind a simple API; Philter wraps it in a full
self-hosted PII/PHI redaction pipeline you run inside your own boundary.

Commercial support, custom model training, and consulting are available from
[Philterd](https://philterd.ai), including
[production support](https://philterd.ai/support/) and
[custom redaction engagements](https://philterd.ai/consulting/).

## Intended use

Detecting personal names in English text so they can be redacted. The model is
**recall-leaning** by design: in redaction, missing a name (a leak) is worse than
flagging an extra span (over-redaction). We recommend a default threshold of
**0.70** — the operating point the evaluation below reports. Lower it toward 0.5 to
push recall higher at the cost of more over-redaction.

**Why names only?** Names are the one PII type that genuinely needs a model: they
have no fixed format, overlap with ordinary words, and depend on context. The other
common types — emails, phone numbers, SSNs, credit cards, IP addresses — follow
regular patterns and are caught more reliably (and far more cheaply) with regexes,
checksums, or dictionary lookups. Spending a neural model on those would be overkill,
so this model focuses on the hard part and leaves the structured types to the
pattern-based detectors in [PhEye](https://github.com/philterd/ph-eye).

## Usage

```python
from gliner import GLiNER

model = GLiNER.from_pretrained("philterd/ph-eye-pii-en-medium")

text = "Please forward the invoice to Toni Levine and copy Maria Gonzalez."
for ent in model.predict_entities(text, ["name"], threshold=0.7):
    print(ent["text"], "->", ent["label"], round(ent["score"], 2))
```

## Evaluation

Scored on the `nvidia/Nemotron-PII` **test** split (131,105 windows, long docs
chunked at 1,200 chars), at the recommended threshold **0.70**, `name` only
(support 97,012).

| Matching | Precision | Recall | F1 |
|---|---|---|---|
| Exact span + label | 0.96 | 0.99 | 0.98 |
| Overlapping span + label | 0.96 | 0.99 | 0.98 |

Recall is 0.991 unrounded — the model finds nearly every name. **These numbers are
in-distribution** (trained and tested on the same synthetic Nemotron distribution)
and are a ceiling, not a real-document production claim — accuracy on real
(non-synthetic) English is likely lower.

Because the training data is synthetic, **real-text recall is materially lower than
these in-distribution figures**, and the recommended threshold above is a synthetic
operating point. For recall-first use on real-world documents, **tune the threshold
down** — a lower cutoff accepts more over-redaction to recover recall, which is the
right trade when a missed name is a leak. Always pick the operating point on a sample
of your own data.

## Limitations

- **English only**, and detects the `name` label only — other PII types (emails,
  phone numbers, IDs, addresses) are out of scope and handled elsewhere in PhEye.
- **Trained on synthetic data** (Nemotron-PII), so real-document accuracy is lower
  than the in-distribution numbers above; validate on your own data.
- May miss atypical name forms (lowercase, nicknames, non-Western name structures).
  It is recall-leaning, so expect some over-redaction; tune the threshold for your
  precision/recall balance.

## Training

- **Base model:** `urchade/gliner_medium-v2.1` (deberta-v3-base, Apache-2.0).
- **Dataset:** `nvidia/Nemotron-PII` (English, 100k train / 100k test, 50+ industries).
- **Labels:** Nemotron's `first_name`/`last_name` are merged to `name` (`label_map`),
  and adjacent first/last spans are merged into one full-name span, matching standard
  NER benchmarks and the full-name span PhEye consumes.
- **Long documents** are windowed at 1,200 chars during training and evaluation so
  names past the 512-token window are still learned and scored.
- Recipe: [`configs/nemotron-pii.yaml`](https://github.com/philterd/ph-eye-model-training).

## License and attribution

Released under **CC-BY-4.0**, inherited from the training data. The
[NVIDIA Nemotron-PII](https://huggingface.co/datasets/nvidia/Nemotron-PII) dataset
is CC-BY-4.0; commercial use is permitted **with attribution to NVIDIA**. Any use
of this model must retain that attribution.

## Disclaimer

This model makes **no guarantees of accuracy or completeness**. Name detection is
**probabilistic** — it will miss some names and flag some non-names. Before relying
on it, **validate precision and recall on your own data**. You **remain the data
controller** for any personal data you process with this model and are responsible
for your own compliance.
