---
license: apache-2.0
language:
- as
- bn
- brx
- doi
- en
- gu
- hi
- kn
- kok
- ks
- mai
- ml
- mni
- mr
- ne
- or
- pa
- sa
- sat
- sd
- ta
- te
- ur
base_model: google/muril-base-cased
tags:
- token-classification
- pii
- phi
- ner
- indic
- clinical
- privacy
datasets:
- Sidharth1743/indicphi
pipeline_tag: token-classification
---

# IndicPHI-MuRIL-PII

A [MuRIL-base](https://huggingface.co/google/muril-base-cased) encoder (237M params)
fine-tuned as a BIO token classifier for PII/PHI redaction in Indian clinical text —
23 languages, 13 scripts, 50 entity types including India-specific identifiers
(ABHA ID, Aadhaar, BPL ration card, ASHA worker name).

Trained on [`Sidharth1743/indicphi`](https://huggingface.co/datasets/Sidharth1743/indicphi).
Evaluation code: [IndicPHI-Bench](https://github.com/SACHokstack/IndicPHI-Bench).

## Read this before you use the first number

| setting | result |
|---|---|
| held-out **synthetic** clinical documents (same generator as training) | **0.45%** character leakage |
| held-out **synthetic**, document types never seen in training | 2.0% leakage |
| **real** human-written Indic text (Naamapadam, person names) | **31.8%** detection recall (68.2% missed) |
| same architecture, trained on real news data instead | 93.4% detection recall |

The first number is the one people quote. It is real, but it is an in-distribution
number on synthetic data, and **it does not predict the third one**. Six differently-
pretrained encoders trained the identical way score within 0.34–0.64% on the synthetic
benchmark and span 0.4–31.8% on real text — the benchmark alone does not tell you
which model actually works. Full analysis, six-way comparison, and the trained-ceiling
control that isolates *why* the real-text number is what it is: see the paper
(link pending) and [IndicPHI-Bench](https://github.com/SACHokstack/IndicPHI-Bench).

**Practical read:** this model is a strong choice for redacting documents similar to
its synthetic training distribution. Its recall on genuinely novel real-world Indic
text is meaningfully lower, and you should not assume the 0.45% figure transfers.

## Usage

This uses a small custom head (LayerNorm + linear classifier) on top of the MuRIL
backbone — not a standard `AutoModelForTokenClassification` shape, because a bare
linear head could not learn at all on MuRIL's raw output scale (see "Why the custom
head" below). Loading needs the included `modeling_indicphi_bio.py`:

```python
from huggingface_hub import hf_hub_download
import sys, os

REPO = "sach3v/indicphi-muril-pii"
sys.path.insert(0, os.path.dirname(hf_hub_download(REPO, "modeling_indicphi_bio.py")))

from modeling_indicphi_bio import IndicPHIBioEncoder
from transformers import AutoTokenizer
import torch

model = IndicPHIBioEncoder.from_pretrained(REPO).eval()
tok = AutoTokenizer.from_pretrained(REPO)

text = "রোগীর নাম Manisha Brahma, বয়স 37, ফোন 9593541505, MRN-15FE5B1DAF"
enc = tok(text, return_tensors="pt", return_offsets_mapping=True)
with torch.no_grad():
    logits = model(enc["input_ids"], enc["attention_mask"])
pred = logits.argmax(-1)[0].tolist()

# decode BIO tags back to character spans
offsets = enc["offset_mapping"][0].tolist()
spans, cur = [], None
for (s, e), p in zip(offsets, pred):
    if s == e:
        continue
    tag = model.id2label[p]
    if tag == "O":
        if cur: spans.append(cur); cur = None
        continue
    pos, label = tag.split("-", 1)
    if pos == "B" or cur is None or cur[2] != label:
        if cur: spans.append(cur)
        cur = [s, e, label]
    else:
        cur[1] = e
if cur: spans.append(cur)

for s, e, label in spans:
    print(f"{label:<16} {text[s:e]!r}")
# PATIENT_NAME     'Manisha Brahma'
# AGE              '37'
# PHONE_NUMBER     '9593541505'
# MRN              'MRN-15FE5B1DAF'
```

`from_pretrained` verifies every backbone/head tensor loaded (the only permitted
mismatch is MuRIL's unused NSP pooler head) and raises rather than silently returning
an under-loaded model.

## Training

- **Base**: `google/muril-base-cased`, output LayerNorm before the classifier
  (backbones vary by ~2 orders of magnitude in raw hidden-state scale; MuRIL's is
  small enough that a bare linear head trains at chance loss for the entire run
  without this).
- **Head**: BIO tagging over 50 entity types (101 tags incl. `O`).
- **Data**: `Sidharth1743/indicphi` train split, 22,554 documents, 23 languages.
- **Schedule**: 3 epochs, batch 8, max length 512, seed 42.
- Data-scaling: real-world transfer saturates at ~10k training documents; the last
  2.25× of data only improved the in-distribution number.

## Labels

50 PII/PHI types in BIO scheme (101 tags). Full list in `bio_labels.json`. Includes
India-specific identifiers with no counterpart in general PII taxonomies: `ABHA_ID`,
`ABHA_ADDRESS`, `AADHAAR_NUMBER`, `BPL_RATION_CARD`, `ASHA_WORKER_NAME`, `VILLAGE`,
`DISTRICT`, `WARD_NUMBER`, `CASTE`, `RELIGION`.

## Limitations

- Trained entirely on **synthetic** clinical text; the only real-text evaluation
  available (Naamapadam) is **news**, not clinical, so the 31.8% figure confounds
  synthetic-vs-real with domain shift. See `GOLD_SET_SPEC.md` in the harness repo for
  what would resolve this.
- Two scripts (Ol Chiki/Santali, Meetei Mayek/Manipuri) are outside MuRIL's
  pretraining and are the weakest languages for this model, and for every other
  encoder we tested.
- Right-to-left scripts (Sindhi, Urdu, Kashmiri) show a specific failure mode:
  boundary errors that redact only the last character or two of a name, which is a
  worse privacy failure than a full miss.

## License

Apache 2.0 (inherited from `google/muril-base-cased`). Training data:
`Sidharth1743/indicphi`, MIT.

## Citation

Paper in preparation; citation to follow.
