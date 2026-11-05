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
- onnx
pipeline_tag: token-classification
base_model: microsoft/deberta-v3-xsmall
datasets:
- nvidia/Nemotron-PII
---

# ph-eye-pii-en-xsmall

A GLiNER person-**name** detector for English PII redaction, fine-tuned by
[Philterd](https://philterd.ai) from
[`microsoft/deberta-v3-xsmall`](https://huggingface.co/microsoft/deberta-v3-xsmall)
on [`nvidia/Nemotron-PII`](https://huggingface.co/datasets/nvidia/Nemotron-PII).
It detects a single label, `name`, which is what [PhEye](https://github.com/philterd/ph-eye)
consumes for redaction.

This is the **ultra-light** variant — the smallest size, for the most constrained
on-device / edge / in-browser use (about half the parameters and latency of the small model).
It ships a quantized **int8 ONNX** graph (about 90 MB) and runs in-process with no server.
Sibling sizes share the same recipe and data:
[`philterd/ph-eye-pii-en-small`](https://huggingface.co/philterd/ph-eye-pii-en-small),
[`philterd/ph-eye-pii-en-medium`](https://huggingface.co/philterd/ph-eye-pii-en-medium)
(the recommended default), and
[`philterd/ph-eye-pii-en-large`](https://huggingface.co/philterd/ph-eye-pii-en-large)
(highest-capacity, server-side).

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

Detecting personal names in English text so they can be redacted, where footprint and
latency matter most. The model is **recall-leaning** by design: in redaction, missing a name
(a leak) is worse than flagging an extra span (over-redaction). We recommend a default
threshold of **0.50** — the operating point the evaluation below reports. Lower it to push
recall higher at the cost of more over-redaction.

Because it is the smallest size, its real-text recall is **lower than the larger variants'**
— if a missed name is costly and footprint allows, prefer small/medium/large. For the most
constrained deployments where this is the right size, validate the operating point on your
own data.

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

# PyTorch
model = GLiNER.from_pretrained("philterd/ph-eye-pii-en-xsmall")
text = "Please forward the invoice to Toni Levine and copy Maria Gonzalez."
for ent in model.predict_entities(text, ["name"], threshold=0.5):
    print(ent["text"], "->", ent["label"], round(ent["score"], 2))

# or the bundled int8 ONNX graph
onnx = GLiNER.from_pretrained("philterd/ph-eye-pii-en-xsmall",
                              load_onnx_model=True, onnx_model_file="onnx/model.onnx")
```

The directory also ships `spm.model` so SentencePiece-based ONNX runtimes (e.g. .NET) can
load `onnx/model.onnx` directly.

## Evaluation

Scored on the `nvidia/Nemotron-PII` **test** split (131,105 windows, long docs
chunked at 1,200 chars), at the recommended threshold **0.50**, `name` only
(support 97,012).

| Matching | Precision | Recall | F1 |
|---|---|---|---|
| Exact span + label | 0.96 | 0.99 | 0.98 |
| Overlapping span + label | 0.97 | 0.99 | 0.98 |

Recall is 0.991 unrounded — in-distribution it nearly matches the larger models. **These
numbers are in-distribution** (trained and tested on the same synthetic Nemotron
distribution) and are a ceiling, not a real-document production claim.

Because the training data is synthetic, **real-text recall is materially lower than these
in-distribution figures** — and more so for this smallest size than for the larger variants.
The recommended threshold above is a synthetic operating point. For recall-first use on
real-world documents, **tune the threshold down** — a lower cutoff accepts more
over-redaction to recover recall, which is the right trade when a missed name is a leak.
Always pick the operating point on a sample of your own data.

## Limitations

- **English only**, and detects the `name` label only — other PII types (emails,
  phone numbers, IDs, addresses) are out of scope and handled elsewhere in PhEye.
- **Smallest capacity**, so real-document recall is lower than small/medium/large — choose
  this size when footprint/latency dominate; otherwise prefer a larger variant.
- **Trained on synthetic data** (Nemotron-PII), so real-document accuracy is lower
  than the in-distribution numbers above; validate on your own data.
- May miss atypical name forms (lowercase, nicknames, non-Western name structures).
  It is recall-leaning, so expect some over-redaction; tune the threshold for your
  precision/recall balance.

## Training

- **Base model:** `microsoft/deberta-v3-xsmall` (MIT).
- **Dataset:** `nvidia/Nemotron-PII` (English, 100k train / 100k test, 50+ industries).
- **Labels:** Nemotron's `first_name`/`last_name` are merged to `name` (`label_map`),
  and adjacent first/last spans are merged into one full-name span, matching standard
  NER benchmarks and the full-name span PhEye consumes.
- **Long documents** are windowed at 1,200 chars during training and evaluation so
  names past the 512-token window are still learned and scored.
- Recipe: [`configs/ph-eye-pii-en-xsmall.yaml`](https://github.com/philterd/ph-eye-model-training).

## License and attribution

Released under **CC-BY-4.0**, inherited from the training data. The
[NVIDIA Nemotron-PII](https://huggingface.co/datasets/nvidia/Nemotron-PII) dataset
is CC-BY-4.0; commercial use is permitted **with attribution to NVIDIA**. Any use
of this model must retain that attribution. The base model
`microsoft/deberta-v3-xsmall` is MIT.

## Disclaimer

This model makes **no guarantees of accuracy or completeness**. Name detection is
**probabilistic** — it will miss some names and flag some non-names, and as the smallest
variant it misses more than the larger ones. Before relying on it, **validate precision and
recall on your own data**. You **remain the data controller** for any personal data you
process with this model and are responsible for your own compliance.
