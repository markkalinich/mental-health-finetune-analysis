---
license: apache-2.0
language:
  - ar
library_name: transformers
pipeline_tag: token-classification
tags:
  - medical
  - clinical
  - pii
  - de-identification
  - arabic
  - ner
  - xlm-roberta
  - lora
base_model: xlm-roberta-base
---

# OpenMed Arabic Clinical PII — XLM-RoBERTa-base (LoRA)

Arabic-language token classifier for **clinical PII de-identification**. Detects six PII entity types in Arabic medical notes: `PATIENT`, `DOCTOR`, `HOSPITAL`, `DATE`, `PHONE`, `ID`.

Built as the first Arabic addition to the [OpenMed](https://huggingface.co/OpenMed) NER toolkit, targeting an MOH-compliance gap for Gulf healthcare deployments where Arabic clinical NLP support is sparse.

## Intended use

- De-identifying Arabic clinical notes, discharge summaries, consultation notes, lab reports, and radiology reports prior to research or LLM processing.
- A preprocessing step in pipelines that move PHI-bearing Arabic text into less-trusted environments (LLM APIs, analytics).

**Not intended** as a sole compliance control. De-identification is a layered process; this model is one layer.

## Schema

| Entity     | Description                            |
|------------|----------------------------------------|
| `PATIENT`  | Patient full name                      |
| `DOCTOR`   | Treating physician name                |
| `HOSPITAL` | Facility name                          |
| `DATE`     | Calendar dates                         |
| `PHONE`    | Phone numbers                          |
| `ID`       | National / civil ID numbers            |

Future versions will expand to OpenMed's full schema (`STREET`, `CITY`, `ZIP`, `AGE`, `EMAIL`, `PROFESSION`, `USERNAME`, `DEVICE`, ...).

## Training data

Synthetic-only for v1. **5000 Arabic clinical notes** generated from 52 hand-crafted templates spanning 6 note types (discharge, consultation, radiology, lab, admission, ER triage). For each sample, PII values are drawn from `Faker(ar_AA)` plus a curated list of GCC first/family names and hospitals; PII slots are filled at known positions, so gold spans are exact (no string-search recovery, no false-positive risk).

- **Note types**: discharge summary, consultation, radiology, lab results, admission, ER triage (balanced ~15-20% each).
- **Register mix**: MSA-heavy, with explicit Gulf-dialect templates mixed in.
- **Splits**: 4000 / 500 / 500 (train / val / test), seeded.
- A Claude-API-based generator (`data/generate_api.py`) is included for v2 scaling to larger, more linguistically diverse corpora.

**Limitation**: synthetic-only with limited template skeletons. The OOD probe (below) shows the model generalizes well past template structure, but rigorous real-world evaluation needs a hand-labeled clinical eval set (v2).

## Training

- Base: `xlm-roberta-base` (278M params)
- Adapter: LoRA (`r=16`, `alpha=32`, `dropout=0.1`) on `query`/`value` attention projections; classification head trained fully.
- Trainable params: 599,821 / 278M (~0.22% of base).
- Optimizer: AdamW, `lr=3e-4`, `warmup_ratio=0.1`, `weight_decay=0.01`.
- Schedule: 4 epochs, `bs=16`, `max_length=256`.
- Hardware: Apple M4 Pro (MPS, fp32) — **2 min 17 s** end-to-end. Also runs on a single T4/A10 in roughly the same time with fp16.

## Evaluation

### Synthetic test split (500 held-out notes, same template distribution)

| Metric                          | Value     |
|---------------------------------|-----------|
| Entity F1 (macro, seqeval)      | **1.0000** |
| Entity F1 (micro)               | **1.0000** |
| Doc-level zero-leakage rate     | **500/500 (100.00%)** |
| Per-entity recall — `PATIENT`   | 557/557 (100%) |
| Per-entity recall — `DOCTOR`    | 331/331 (100%) |
| Per-entity recall — `HOSPITAL`  | 257/257 (100%) |
| Per-entity recall — `DATE`      | 329/329 (100%) |
| Per-entity recall — `PHONE`     | 168/168 (100%) |
| Per-entity recall — `ID`        | 164/164 (100%) |

The synthetic eval is fully saturated. This number alone doesn't prove generalization — see the OOD probe below.

### Out-of-distribution probe (`probe.py`)

6 hand-written Arabic clinical notes that don't match any training template — covering Levantine and Egyptian dialect, code-switched Arabic/English, telegraphic pipe-separated format, novel hospital and family names (Jordanian +962, Saudi +966, Omani +968 phones — none in the GCC training mix), and one note with zero PII to test for hallucination.

| Note | Style | Entities caught | False positives |
|------|-------|-----------------|-----------------|
| 1 | Levantine + Jordanian numbers | 4/4 | 0 |
| 2 | Egyptian dialect + Cairo hospital | 3/3 | 0 |
| 3 | Code-switched Arabic/English | 6/6 | 0 |
| 4 | Telegraphic format | 6/6 | 0 |
| 5 | Multiple mentions + Omani context | 7/7 | 0 |
| 6 | Zero-PII note | 0/0 | 0 |
| **Total** | | **26/26 (100%)** | **0** |

Strong signal that XLM-R's multilingual pretraining is letting the model learn what PII *looks like* in Arabic rather than memorizing the 52 training skeletons. Real rigor still requires a hand-labeled clinical eval set; that is v2.

### Training stats

- Hardware: Apple M4 Pro (MPS), fp32
- Wall time: **2 min 17 s** for 4 epochs over 4000 train + 500 val
- Trainable params: 599,821 / 278,062,874 (0.22%) — LoRA on `query`/`value` + full classification head

## Usage

```python
from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline

REPO = "yousefqasem/openmed-arabic-pii-xlmr-base"
tok = AutoTokenizer.from_pretrained(REPO)
mdl = AutoModelForTokenClassification.from_pretrained(REPO)

# Use "first" (or "max"), NOT "simple" — "simple" can emit duplicate partial+full spans
# for some Arabic subword splits.
nlp = pipeline("token-classification", model=mdl, tokenizer=tok, aggregation_strategy="first")

text = "تم استقبال المريض أحمد محمد العتيبي بتاريخ 14/03/2026 في مستشفى الأميري تحت إشراف د. خالد سعد القحطاني."
for ent in nlp(text):
    print(f"{ent['entity_group']:<10} {ent['score']:.3f}  {ent['word']!r}")
```

## Limitations & risks

- Trained on **52 hand-crafted template skeletons** with varied PII fills. The OOD probe is promising but only 6 notes — a hand-labeled real-clinical eval set (v2) is needed before any production claim.
- Real-world distribution shift expected, especially for handwritten / OCR'd notes, and for note types outside the 6 covered here.
- Training register is MSA-heavy with explicit Gulf-dialect templates; Levantine, Egyptian, and North African dialects rely on XLM-R's pretraining to generalize.
- HF pipeline's `aggregation_strategy="simple"` produces duplicate partial+full HOSPITAL spans on some inputs. Use `"first"` or `"max"`, or post-process to dedupe by `(label, start)`.
- This is a recall-oriented de-identification tool. Recommended use is followed by a redaction/replacement layer; pair with rule-based detectors (regex for emails, IDs, dates) for defense in depth.
- Not a substitute for legal review of de-identification adequacy under local regulation (MOH, HIPAA-equivalent, GDPR, etc).

## Citation

```bibtex
@misc{openmed_arabic_pii_xlmr_2026,
  title  = {OpenMed Arabic Clinical PII (XLM-R + LoRA)},
  author = {Qasem, Yousef},
  year   = {2026},
  url    = {https://huggingface.co/yousefqasem/openmed-arabic-pii-xlmr-base}
}
```

## License

Apache-2.0.

---

## Reproduce locally (Apple Silicon)

```bash
git clone <this-repo>
cd openmed-arabic-pii
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt

# Generate 5000 synthetic notes from templates (no API needed):
.venv/bin/python -m data.generate --n 5000
.venv/bin/python -m data.split

# Train + eval (~2.5 min on M4 Pro, ~25 min on Colab T4):
.venv/bin/python train.py
.venv/bin/python eval.py

# Run the out-of-distribution generalization probe:
.venv/bin/python probe.py

# Ship to HF Hub:
export HF_TOKEN=hf_...
.venv/bin/python push.py --repo yourname/openmed-arabic-pii-xlmr-base
```
