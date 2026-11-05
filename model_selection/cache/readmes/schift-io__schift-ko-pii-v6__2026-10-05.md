---
language: ko
license: other
license_name: schift-2.0
license_link: LICENSE
library_name: transformers
pipeline_tag: token-classification
tags:
  - pii
  - korean
  - ner
  - privacy
  - token-classification
datasets:
  - custom
---

# schift-ko-pii-v6

**34.1M parameter Korean PII detector built on a dual-path LoRA encoder.**

The `0.4.0` release keeps the v6 detector contract and adds an optional,
typed selective-adoption flow for structured and contextual categories.
The base install does not install `ko-pii`; install the `extended` extra only
when those additional deterministic categories are needed.

## Release status

This source tree prepares `schift-ko-pii` `0.4.0`. The previously published
baseline was `0.3.3`. The Cloud Run ONNX service under `services/pii` is a
separate deployment lane; this package does not bundle its ONNX artifacts.

## Quick start

```bash
pip install schift-ko-pii
```

The original detector API remains available:

```python
from schift_ko_pii import detect

spans = detect("피고 김민수의 전화번호는 010-1234-5678이다.")
# [
#   {"start": 3, "end": 6, "label": "private_person", ...},
#   {"start": 14, "end": 27, "label": "private_phone", ...},
# ]
```

For a typed operational result, use the selective-adoption flow:

```python
from schift_ko_pii import AnalysisConfig, ProcessingMode, analyze_text

result = analyze_text(
    "피고 김민수의 전화번호는 010-1234-5678이다.",
    config=AnalysisConfig(mode=ProcessingMode.PERMISSIVE),
)

# The result contains typed detections, policy actions, BLOCK-only masking,
# counts, and a metadata-only review queue. It has no separate source-text
# field; its policy text can still preserve REVIEW/ALLOW spans for operators.
print(result.summary)
print(result.masking.masked_text)
print(result.review_items())
```

## Selective-adoption flow

The public workflow is deliberately ordered:

**detect -> assess -> BLOCK-only masking -> review queue**

`analyze_text()` or `analyze()` runs detection, sends non-sensitive detection
metadata to `assess()`, and masks only spans whose action is `Action.BLOCK`.
`Action.REVIEW` detections remain unmasked and are represented by
`ReviewItem` values in `PiiResult.review_queue`; callers can create a typed
`FeedbackPatch` with `propose_feedback_patch()` without persisting raw PII.
`Action.ALLOW` detections are retained in the typed result but are not masked.
The resulting `masking.masked_text` is therefore a policy output, not a safe
untrusted-egress string: use a caller-owned all-span redaction step before
sending it to logs, external APIs, or other untrusted surfaces.

Detector confidence and operational risk are separate. `ProcessingMode` sets
the action thresholds:

| Mode | BLOCK threshold | REVIEW threshold |
|---|---|---|
| `AUDIT` | never blocks | all detections are allowed for audit output |
| `PERMISSIVE` | `CRITICAL` risk at score `>= 0.95` | `HIGH` risk at score `>= 0.70` |
| `STRICT` | `MEDIUM` risk at score `>= 0.70` | `LOW` risk at score `>= 0.50` |
| `BALANCED` | `HIGH` risk at score `>= 0.80` | `MEDIUM` risk at score `>= 0.60` |
| `PARANOID` | `LOW` risk at score `>= 0.50` | all lower-risk detections |

`PERMISSIVE` is an action-policy choice, not a change to the v6 detector's
`score_threshold`. Use `AnalysisConfig.score_threshold` separately when
configuring detection.

## Extended profiles (opt-in)

```bash
pip install "schift-ko-pii[extended]"
```

The optional adapter is enabled per request:

```python
from schift_ko_pii import AnalysisConfig, analyze_text

result = analyze_text(
    "사업자등록번호 104-81-49532, 직책 팀장",
    config=AnalysisConfig(extended=True, extended_profile="contextual"),
)
```

`extended_profile="structured"` adopts deterministic identifier and anchor
categories such as business/corporate registration numbers, medical
insurance and prescription identifiers, PNU, postal code, fax, employee,
document, petition, and drug IDs. `extended_profile="contextual"` includes
that structured set plus contextual attributes such as nationality, birth
date, education, major, position, age, height, and weight.

The taxonomy registry is exposed through `LABELS`,
`STRUCTURED_UPSTREAM_LABELS`, `CONTEXTUAL_UPSTREAM_LABELS`,
`EXCLUDED_UPSTREAM_LABELS`, `lookup_label()`, `label_for_upstream()`, and
`upstream_labels_for_profile()`. The adapter excludes categories already
owned by the v6 detector or current Schift postprocessing, including person,
address, phone, email, existing structured identifiers, URLs, IPs, and legal
case references. Existing v6 spans win overlaps, except a generic
`account_number` span may be refined by a more specific extended label.

## Masking boundaries

Masking is request-local and occurs only after policy assessment. Select a
`MaskingStrategy` in `AnalysisConfig` or call `mask_text()` directly with
typed `MaskSpan` values:

- `TOKEN`: replace with a stable label token such as `[PII_PHONE_1]`.
- `REDACT`: replace with `[REDACTED]`.
- `PARTIAL`: retain a small leading/trailing portion for recognition.
- `HASHED`: replace with a deterministic local SHA-256 digest.

These strategies are output transformations, not custody. No strategy stores
a reverse map, restores source values, or talks to Vault. Central Vault
custody, retention, tenant isolation, KMS, and audit requirements remain a
separate caller-side project.

## Documents and the document-helper boundary

Document APIs accept already extracted text and provenance, not files:

```python
from schift_ko_pii import (
    ExtractedPageInput,
    analyze,
    from_pages,
)

document = from_pages(
    (
        ExtractedPageInput(page_num=1, text="첫 페이지", source="helper"),
        ExtractedPageInput(page_num=2, text="둘째 페이지", source="helper"),
    ),
    source_id="doc-123",
)
result = analyze(document)
```

`from_text()`, `from_pages()`, and `from_document_helper()` build the typed
text-only envelope. `DocumentInput` preserves the concatenated text and page
boundaries; `SourceSpan` and `PageSpan` preserve character offsets and page
provenance. `scan_document()` is the convenience scan over that envelope.

The package does not parse HWP/HWPX, DOCX, XLSX, PDF, or other file formats.
Use the document-helper service (or another caller-owned parser) to produce a
text-only envelope, then pass it to this package. Do not treat the envelope as
file storage or a Vault integration.

## Postprocessing and legacy API

Postprocessing is enabled by default for `detect()`. It applies Korean-specific
structured-ID validation, checksum checks where applicable, context-aware span
merging, and false-positive suppression for legal case numbers and statute
references. The legacy `detect()` path preserves original input text by
default; pass `normalize=True` when you want NFKC-normalized model input and
source-offset remapping. The typed `analyze()`/`analyze_text()` flow enables
that normalization by default. Pass `postprocess=False` for encoder heads
only (person, address, and organization).

Existing root exports remain available: `detect`, `mask`, `apply`, `assess`,
`detect_extended`, `detect_extended_entities`, `Action`, `ProcessingMode`,
`RiskLevel`, and `ExtendedDependencyError`.

For compatibility, `AnonymizationResult` is an alias of `PiiResult`, and both
`anonymize_text` and `anonymize` are aliases of `analyze_text`. They do not
introduce a second execution path.

## API (free)

For production use without managing model files:

```python
from schift import Schift

client = Schift(api_key="...")  # free at schift.io
result = client.pii.redact("김민수의 전화번호는 010-1234-5678입니다.")
```

## Labels

The stable local taxonomy is available as immutable `TaxonomyEntry` values in
`LABELS`. Common labels include:

| Label | Description | Examples |
|---|---|---|
| `private_person` | Person names | 김민수, 황보영희, Lee Jenny |
| `private_phone` | Phone numbers | 010-1234-5678, 02-1234-5678 |
| `private_email` | Email addresses | user@example.com |
| `private_address` | Street/postal addresses | 서울특별시 강남구 테헤란로 521 |
| `private_date` | Dates | 2024년 3월 15일, 2024-03-15 |
| `private_url` | URLs and IP addresses | instagram.com/user, 192.168.1.1 |
| `account_number` | Structured account/identity surfaces | 850205-1234567, M12345678 |
| `secret` | Secrets, API keys, passwords | |

## Benchmark

The current V6 benchmark is `benchmark/benchmark_v3.jsonl`.
The V6 release measurement on the current benchmark is:

| rows | precision | recall | F1 |
|---:|---:|---:|---:|
| 473 | 0.8771 | 0.8896 | 0.8833 |

Run the current benchmark with postprocessing enabled:

```bash
python benchmark/run_benchmark.py \
  --benchmark benchmark/benchmark_v3.jsonl \
  --postprocess
```

This is the current V6 benchmark surface. Historical benchmark datasets and
selective-adapter policy matrices are not presented as additional model-card
benchmarks here.

## Model details

- **Checkpoint**: `schift-io/schift-ko-pii-v6`
- **Architecture**: dual-path LoRA encoder with person, address, and organization heads
- **Training**: LoRA adapter on Korean legal/financial/admin examples
- **Format**: safetensors release source
- **Inference**: custom `transformers`/PyTorch dual-path loader
- **Max length**: 512 tokens
- **Tagging scheme**: `O/B/I/E/S`

## License

[Schift License v2.0](LICENSE) — Apache 2.0 base with a revenue threshold.
Free for everyone under $10M annual revenue. Research, education, and
non-profit use always permitted. Companies above the threshold: contact
hello@schift.io.

## Citation

```bibtex
@software{schift_ko_pii_2026,
  author = {Schift Inc.},
  title = {schift-ko-pii: Korean PII Detection Model},
  year = {2026},
  url = {https://huggingface.co/schift-io/schift-ko-pii-v6},
}
```
