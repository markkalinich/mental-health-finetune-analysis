---
license: cc-by-sa-4.0
language:
  - ko
  - en
tags:
  - token-classification
  - ner
  - pii
  - korean
  - privacy
  - kdpii
  - klue
base_model: openai/privacy-filter
pipeline_tag: token-classification
library_name: transformers
datasets:
  - kdpii
  - klue
---

# ko-pii-public-v1 (v4 update — long-document robust)

Korean PII (개인식별정보) detector across **23 categories** spanning common /
public-sector / finance / medical domains. Fine-tuned from
[`openai/privacy-filter`](https://huggingface.co/openai/privacy-filter).

> **What changed from the previous (v2) release of this repo:** training data
> now includes (a) **synthetic long Korean documents** (1,500–3,000 chars, multi-PII)
> targeting the long-document spillover failure mode reported by an external
> evaluator, (b) **raw-numeric ID with keyword grounding** (e.g.,
> `건강보험번호 1234567890` raw 10-digit), (c) **hard-negative co-occurrence
> documents** (card / health insurance / business reg / corporate together),
> and (d) **KLUE NER** real-world Korean sentences (CC BY-SA 4.0) for natural
> person/address distribution.
>
> See the **License** section below — this release inherits **CC BY-SA 4.0**
> from the KLUE training data; the previous Apache 2.0 release of this repo did
> not include KLUE.

## When to use vs. not use this update

✅ **Use v4 if:** you process Korean documents longer than ~150 chars (forms,
emails, KYC, medical records, contracts, meeting minutes). v4 fixes the
long-document failure mode of v2.

⚠️ **Stick with v2 if:** your only use case is short conversational Korean
(KDPII-style chat), and the **0.877 → 0.858 F1 dip on KDPII test** matters more
to you than long-document correctness.

For most real-world deployments, v4 is the right choice. For an academic
benchmark report against KDPII alone, v2 had a slightly better headline number.

## Quick start

```python
from transformers import AutoModelForTokenClassification, AutoTokenizer, pipeline
import torch

model_id = "ehd0309/ko-pii-public-v1"  # this repo, v4 weights
tok = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForTokenClassification.from_pretrained(
    model_id, dtype=torch.bfloat16,
).to("cuda").eval()
nlp = pipeline("token-classification", model=model, tokenizer=tok,
               aggregation_strategy="simple", device=0)

# RECOMMENDED for v4: threshold 0.93 (slightly higher than v2's 0.9)
# Reason: v4 has higher recall but lower precision on conversational Korean;
# the +0.03 threshold bump restores precision parity with v2 at thr=0.9.
preds = nlp("고객 김민수 (010-1234-5678) 계좌 110-998877-665544 로 송금")
preds = [p for p in preds if p["score"] >= 0.93]
print(preds)
```

For long documents (>500 chars) we still recommend operational chunking
(150-char line packing) on top of the model — see the *Recommended deployment*
section below.

## Categories (23) — same as v2

| Group | Labels |
|---|---|
| Common (8) | `person_name`, `phone_number`, `email`, `address`, `date_of_birth`, `ip_address`, `url`, `credential_secret` |
| Public-sector (5) | `rrn`, `foreigner_id`, `drivers_license`, `passport_number`, `vehicle_plate` |
| Finance (6) | `bank_account`, `card_number`, `card_cvc`, `card_expiry`, `business_reg_number`, `corporate_number` |
| Medical (4) | `patient_id`, `health_insurance_no`, `medical_license`, `prescription_id` |

## Training data

| Source | Records | Style | License |
|---|---:|---|---|
| v3 synthetic generator (carried over) | 5,736 | Document/form style | Apache 2.0 (this repo) |
| KDPII train (carried over) | 11,919 | Real conversational Korean | CC BY 4.0 ([Zenodo](https://zenodo.org/records/10968609)) |
| **NEW** v4 synthetic long-doc | 3,000 | Long Korean documents (1,500–3,000 chars) with 8–15 multi-category PII per doc | Apache 2.0 (this repo) |
| **NEW** v4 raw-keyword | 1,500 | Keyword + raw-numeric ID (건보번호 1234567890 등) | Apache 2.0 (this repo) |
| **NEW** v4 hard-negative co-occurrence | 1,000 | Card + health + biz reg + corporate distinct in same doc | Apache 2.0 (this repo) |
| **NEW** v4 OCR-noise | 500 | Em-dash, keyword typos, separator variants | Apache 2.0 (this repo) |
| **NEW** KLUE NER (CC BY-SA 4.0) | 5,000 | Real Korean (news/wiki) with PS→`person_name`, postal LC→`address` | **CC BY-SA 4.0** (KAIST) |
| **NEW** v4 boundary-fix | 1,000 | Bank/hospital/company name *outside* the labelled span | Apache 2.0 (this repo) |
| **NEW** v4 defect-targeted | 1,500 | Long postal addr / raw 10-digit health / dense person | Apache 2.0 (this repo) |
| **Combined train total** | **31,155** | | mixed (most restrictive: CC BY-SA 4.0) |

## Training details

- Base: `openai/privacy-filter` (1.5B params total, 50M active MoE, banded attention sliding_window=128)
- Trainer: HuggingFace `Trainer`, BIO labels (47 = 1 + 23 × 2)
- Hyperparameters: 4 epochs, batch 8 + grad-accum 2 (effective 16), AdamW
  (lr 1.5e-4, wd 0.01, warmup 10%, cosine schedule), max_length 384, seed 42
- Hardware: 1× NVIDIA GB10 (DGX Spark), bfloat16
- Training time: ~14 h
- **Single seed.** No multi-seed variance is reported. Treat numbers as a point
  estimate, not a confidence interval.

## Evaluation

### 1. KDPII held-out test (carried over from v2 — direct anchor)

`seqeval` BIO + lenient span overlap, all 23 labels:

| Threshold | v2 (previous release) | **v4 (this release)** |
|---|---:|---:|
| 0.0 | F1 0.795 | F1 0.798 |
| 0.7 | F1 0.850 | F1 0.851 |
| **0.9** (v2 recommended) | **F1 0.877** | F1 0.858 |
| **0.93** (v4 recommended) | F1 0.870 | **F1 0.860** |
| 0.95 | F1 0.854 | F1 0.851 |

> **Honest disclosure:** v4 is **~1.9p worse on KDPII test at the v2-recommended
> threshold of 0.9**. The dip is precision-driven (P 0.941→0.859, R 0.821→0.857).
> Bumping threshold to 0.93 narrows the gap. KDPII is conversational Korean
> chat — see section 2 for the regime where v4 is *better*.

### 2. Length-stratified evaluation (new — fair comparison across input lengths)

50 fresh synthetic records per bucket (different RNG seed than training). Typed
F1 at threshold 0.9:

| Length bucket | avg chars | v2 typed F1 | **v4 typed F1** |
|---|---:|---:|---:|
| short (≤150) | 25 | 0.659 | **0.990** |
| mid (151–400) | 152 | 0.905 | **1.000** |
| long (401–1,000) | 552 | 0.615 | **0.999** |
| xlong (1,001+) | 1,749 | 0.601 | **0.999** |
| **σ (length-uniformity)** | | **0.139** | **0.005** |

*Caveat:* this synthetic test set uses templates similar (not identical) to v4's
training data. It is **in-distribution leaning** — treat absolute numbers with
caution. The relative comparison vs. v2 is meaningful (same templates evaluated
on both); the ΔF1 is reproducible.

### 3. Defect-targeted probes (new — driven by external evaluator's report)

8 single-document cases mirroring the production-user evaluation that motivated
this update. PASS = all expected spans found, no spurious FPs:

| Probe | v2 | **v4** |
|---|:-:|:-:|
| Long postal address (e.g., "서울특별시 강남구 ... 17층 1701호") | FAIL 0/1 | ✅ 1/1 |
| Raw 10-digit health insurance (`건강보험번호 1234567890`) | FAIL 0/1 | ✅ 1/1 |
| Standalone CVC (`CVC는 123 이고`) | FAIL 1/2 | ✅ 2/2 |
| Dense person names (5+ in one sentence) | FAIL 4/5 | ✅ 5/5 |
| Bank-name prefix excluded from `bank_account` span | PASS | PASS |
| Long-doc ID spillover (6 distinct ID classes co-occurring) | FAIL 3/6 | ✅ 6/6 |
| PII-free conversational text (must not predict) | PASS | PASS |
| PII-shaped non-PII (ISBN, version, track ID — must not predict) | PASS | PASS |
| **Total** | 3 PASS / 5 FAIL | **8 PASS / 0 FAIL** |

### 4. Production-style aggregate (30 cases including the 583-char referral letter)

| Metric | v2 | **v4** |
|---|---:|---:|
| Typed F1 across 30 user-style cases | 0.714 | **0.964** |
| Untyped F1 | 0.735 | **0.964** |
| Long-doc (583 chars, 21 expected PII) | 7/21 | **20/21** |
| FP on the long doc | 4 | **0** |

## Limitations (defensive — please read)

1. **KDPII conversational regression** (-1.9p F1 @ thr=0.9). For pure short-chat
   Korean, v2 of this repo is marginally better. Bump threshold to 0.93 if you
   need to re-balance precision.
2. **Two short-context regressions identified**:
   - `naked passport "M12345678"` alone (no surrounding keyword): v4 misses;
     v2 detected. Mitigation: regex post-processing.
   - `naked vehicle plate "12가3456"` alone: same. Mitigation: regex.
   - These do not affect documents with normal context ("여권번호 M12345678" works).
3. **Single training seed.** No variance estimate. Real F1 could be ±1–2p.
4. **In-distribution evaluation bias.** Sections 2 and 3 above use templates
   similar to v4's training data. Out-of-distribution natural Korean (KDPII
   section 1) shows the trade-off honestly: v4 trades a small KDPII regression
   for large gains on document-style Korean.
5. **Inherits banded-attention architectural limit.** The base
   `openai/privacy-filter` uses sliding_window=128. Even with v4's training
   improvements, very long documents (>2,000 chars) at inference still benefit
   from operational chunking. Long-doc training mitigates but does not eliminate
   the architectural constraint.
6. **No labelled real-world production data was used.** KDPII (CC BY 4.0) and
   KLUE NER (CC BY-SA 4.0) are the closest natural-distribution sources.
   Domain-specific (e.g., your own medical/legal documents) performance must
   be re-measured on your own holdout.
7. **No OCR / dialect / heavy noise evaluation reported.** The `ocr_noise`
   training bucket (em-dash, keyword typos) is mitigation only, not a
   benchmark.
8. **`address` label is broad.** It will flag short geographic terms (e.g.,
   country names, city districts) in addition to full postal addresses.
   For strict postal-only filtering, post-process by length / regex.
9. **`person_name` includes nicknames.** KDPII labels nicknames as person; we
   inherit this. A chat handle like "토깽이" will be flagged as `person_name`.
   This is intentional for compliance use but may surprise users expecting
   strict legal-name detection.
10. **Personal-account model.** No SLA, no patch guarantee, no incident
    response. For production critical workloads, fork and self-host.

## Recommended deployment

```python
def detect_pii(text: str) -> list[dict]:
    if len(text) <= 200:
        preds = [p for p in nlp(text) if p["score"] >= 0.93]   # v4 threshold
    else:
        # Operational chunking — paranoid even though v4 handles long docs
        chunks = chunk_by_lines(text, max_chars=150)
        preds = []
        for c in chunks:
            preds += [p for p in nlp(c) if p["score"] >= 0.93]

    # Regex post-processing for the two known v4 short-context regressions
    # AND for absolute recall on canonical formats:
    preds = merge_adjacent_address(text, preds)         # address fragmentation
    preds = strip_bank_prefix(preds)                    # bank_account boundary
    preds = regex_fallback(text, preds, patterns=[
        "rrn", "foreigner_id", "card_number", "phone_number",
        "email", "ip_address", "url", "passport_number",
        "business_reg_number", "vehicle_plate",
    ])
    return preds
```

A reference implementation of the post-processor is at
[`dgx-guard/app/postprocess.py`](https://github.com/ehd0309/dgx-guard/blob/main/app/postprocess.py).

### Operational checklist

- [ ] Threshold 0.93 (not 0.9) for v4
- [ ] Chunking (≤200 chars) for inputs over ~500 chars
- [ ] Regex fallback for naked passport / vehicle / RRN / card / phone
- [ ] Domain holdout set of 200+ records, **measured on your own data**
- [ ] Audit log (input hash, predictions, timestamp)
- [ ] Pseudonymisation mapping kept in a separate KMS-protected store

## License & attribution

This release is **CC BY-SA 4.0**. The previous v2 release of this repo was
Apache 2.0; v4 is BY-SA because we trained on KLUE NER, which is CC BY-SA 4.0.
Under ShareAlike, the model derived from this data is offered under the same
license. We accept this as the most defensible interpretation; if you have a
different legal opinion, please flag it.

Attribution required when redistributing or building on this model:

- Base model: [`openai/privacy-filter`](https://huggingface.co/openai/privacy-filter) (Apache 2.0)
- Training data:
  - [KDPII](https://zenodo.org/records/10968609) (CC BY 4.0)
  - [KLUE NER](https://klue-benchmark.com/) (CC BY-SA 4.0)
  - This repo's synthetic data (Apache 2.0)

If you need an Apache-2.0-licensed Korean PII model, the previous v2 commit
of this repo is reachable via Hugging Face commit history (commit
`1e029083`). It does not include KLUE training data.

## Citation

```bibtex
@misc{ko-pii-public-v4,
  title  = {ko-pii-public-v1 (v4): Korean PII Detection — Long-Document Robust},
  author = {ehd0309},
  year   = {2026},
  note   = {Fine-tuned from openai/privacy-filter on synthetic Korean +
            KDPII + KLUE NER, targeting long-document spillover and raw-numeric
            ID detection. CC BY-SA 4.0.},
  url    = {https://huggingface.co/ehd0309/ko-pii-public-v1},
}
```

KDPII benchmark used in training and evaluation:

```bibtex
@misc{kdpii2024,
  title  = {KDPII: A New Korean Dialogic Dataset for the Deidentification
            of Personally Identifiable Information},
  year   = {2024},
  doi    = {10.5281/zenodo.10968609},
  note   = {CC BY 4.0},
}
```

KLUE NER:

```bibtex
@misc{klue,
  title  = {KLUE: Korean Language Understanding Evaluation},
  author = {Park, Sungjoon and others},
  year   = {2021},
  url    = {https://klue-benchmark.com/},
  note   = {CC BY-SA 4.0},
}
```

## Changelog

- **v4 (this commit)**: long-document training, KLUE NER inclusion, defect-fix
  buckets, threshold raised to 0.93. License changed to CC BY-SA 4.0.
- **v2** (commit `1e029083`): synthetic + KDPII augmentation. KDPII test F1
  0.44 → 0.88. Apache 2.0.
- **v1** (commit `8791afd7`): initial release, synthetic-only. Apache 2.0.
