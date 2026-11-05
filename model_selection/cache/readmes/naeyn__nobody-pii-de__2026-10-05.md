---
license: apache-2.0
base_model: urchade/gliner_multi_pii-v1
base_model_revision: 1fcf13e85f4eef5394e1fcd406cf2ca9ea82351d
library_name: gliner
pipeline_tag: token-classification
language:
  - de
  - en
  - nl
datasets:
  - naeyn/nobody-pii-synth-de
  - ai4privacy/pii-masking-openpii-1m
tags:
  - gliner
  - pii
  - pii-detection
  - pii-redaction
  - data-redaction
  - document-redaction
  - data-privacy
  - personal-data
  - pseudonymization
  - named-entity-recognition
  - token-classification
  - german-ner
  - german
  - multilingual
  - gdpr
model-index:
  - name: nobody-pii-de v0.3.0 production pipeline
    results:
      - task:
          type: token-classification
          name: PII detection and redaction
        dataset:
          name: ai4privacy pii-masking-400k German validation (external synthetic)
          type: ai4privacy/pii-masking-400k
          split: validation
        metrics:
          - name: Exact token-span F1
            type: f1
            value: 0.795
          - name: PII token leakage (lower is better)
            type: pii_token_leakage
            value: 1.51
      - task:
          type: token-classification
          name: PII detection and redaction
        dataset:
          name: nobody-pii-synth-de held-out multilingual regression split
          type: naeyn/nobody-pii-synth-de
          split: test
        metrics:
          - name: Exact token-span F1
            type: f1
            value: 0.927
          - name: PII token leakage (lower is better)
            type: pii_token_leakage
            value: 0.51
---

# nobody-pii-de v0.3.0

**Local German PII detection for document redaction, privacy review, and
pseudonymization workflows.**

`nobody-pii-de` is a German-first multilingual GLiNER model for finding names,
postal addresses, dates of birth, and organizations in German, English, and
Dutch business text. The full [`nobody`](https://github.com/naeyn/nobody)
pipeline adds checksum- and format-aware local detectors for email addresses,
phone numbers, IBANs, credit cards, German tax IDs, Dutch BSNs, license plates,
and numeric date formats.

The model and pipeline run locally. They are useful starting points for document
intake, support exports, CRM cleanup, archive migration, and privacy review.
They are not legal-compliance or anonymization guarantees; evaluate leakage on
representative documents before production use.

## Release identity

**v0.3.0 is a production-policy release; the binary model is unchanged from
v0.2.0.** The new source pipeline reduces measured German token leakage through
better building-number, date, phone, person-boundary, and address normalization.
Use the [`v0.3.0` source tag](https://github.com/naeyn/nobody/releases/tag/v0.3.0)
for the metrics on this card.

The binary files were verified at Hub revision
`311329838bba75d974be36b042af7836f99b30fa`. Card and attribution metadata may
receive later commits; pin that revision when the exact binary artifact is
required.

| file | SHA-256 |
|---|---|
| `model.safetensors` | `84cb4207ec386a2467894328bccd83127ac62ee771779c0c909047ea3cc54d06` |
| `gliner_config.json` | `16adf9e94687869a82af3234fce29550096df7ccfeb0438e957cf89d358337ec` |
| `tokenizer.json` | `c5b8041501fcdee792b9b112dd592861f04391a24633a73fd9f05aaaf6e8eff1` |
| `tokenizer_config.json` | `d5fc9ee06444205f6d6e9cc1b0ba05855ca740246d4c4dbabbd15bfc1e0170b7` |

The starting checkpoint was
[`urchade/gliner_multi_pii-v1`](https://huggingface.co/urchade/gliner_multi_pii-v1)
at revision `1fcf13e85f4eef5394e1fcd406cf2ca9ea82351d`.

## Intended use

Use this artifact to identify potentially sensitive entities before applying a
redaction or human-review policy. The model layer predicts:

- `person`
- `address`
- `date of birth`
- `organization`

The companion pipeline additionally detects structured labels such as email,
phone number, IBAN, credit card, national ID, and license plate with syntax- or
checksum-aware rules.

**Suitable uses**

- pre-screening German business documents for privacy review;
- local or offline PII masking and pseudonymization pipelines;
- CRM, support, archive, and document-migration cleanup;
- research on recall-first multilingual PII detection.

**Out-of-scope uses**

- claiming that output is legally anonymized;
- making decisions about people from detected attributes;
- processing documents without an appropriate security and data-governance
  boundary;
- relying on benchmark scores without an evaluation from the intended domain.

## Usage

### Complete redaction pipeline

This is the evaluated and recommended path:

```bash
git clone https://github.com/naeyn/nobody.git
cd nobody
git checkout v0.3.0
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python redact.py --model naeyn/nobody-pii-de \
  --text "Kontakt: Anna Müller, anna@example.de"
```

### GLiNER model layer only

```python
from gliner import GLiNER

model = GLiNER.from_pretrained("naeyn/nobody-pii-de")
text = "Kontakt: Anna Müller, geboren am 5. Juni 1984."
entities = model.predict_entities(
    text,
    ["person", "address", "date of birth", "organization"],
    threshold=0.5,
)
print(entities)
```

Direct `predict_entities` calls do **not** include the deterministic structured-
identifier detectors or boundary normalization used for the reported production
metrics.

The released model thresholds are `person=0.50`, `address=0.05`,
`date of birth=0.50`, and `organization=0.50`. The deterministic layer runs
independently of model confidence.

## Training recipe

The unchanged model checkpoint was fine-tuned from the pinned GLiNER base with a
mixed training set of **38,581 document instances**:

- **25,909 German rows** from
  [`ai4privacy/pii-masking-openpii-1m`](https://huggingface.co/datasets/ai4privacy/pii-masking-openpii-1m),
  selected from the German training source and excluding every row whose raw
  labels contained `DATE`. The publisher states that OpenPII-1M is synthetic;
  its generating model is not disclosed.
- **12,672 instances** from the companion synthetic corpus: all 9,450 training
  documents plus one additional copy of each of its 3,222 documents containing
  at least one `date of birth` span. This is a 2× oversample of DOB-bearing
  documents, not a second independently generated split.

The mixed file was concatenated and shuffled with seed `42`; the trainer also
used seed `42`. The generated corpus's generation seed was not retained in its
published snapshot, so the training seed must not be mistaken for a data-
generation seed.

| setting | value |
|---|---|
| epochs | 1 |
| selected global step | 800 |
| per-device batch size | 4 |
| gradient accumulation | 4 (effective batch size 16) |
| GLiNER learning rate | `1.23465e-05` |
| other-parameter learning rate | `7.48573e-05` |
| weight decay | `0.01` for both parameter groups |
| scheduler | linear |
| warmup | 10% of training steps |
| training seed | `42` |
| checkpoint interval | 400 steps |

Checkpoint 800 was selected on a separate German development stream before the
canonical evaluation. Neither canonical benchmark nor the synthetic test split
was used for checkpoint selection.

Only inference artifacts are published here: weights, tokenizer, model
configuration, license, notice, and this card. Optimizer state, training logs,
restricted benchmark records, and private orchestration are not included.

## Evaluation methodology

Every result below uses the full v0.3.0 production pipeline: deterministic
detectors, one model pass, fixed per-label thresholds, span normalization, and
one label mapping. **Leakage** is the percentage of gold PII tokens missed by
all predicted PII spans; lower is better. F1 requires exact token-span matches.

The seven-loop release process used:

1. disjoint development-only selection;
2. a written finalist and gate rule before one frozen canonical look per loop;
3. fixed production thresholds rather than per-benchmark tuning;
4. exact-text and n-gram contamination checks with planted-positive controls;
5. paired document-level bootstrap differences with 10,000 resamples;
6. explicit reporting of failed gates and negative experiments.

Shipping required German F1 ≥ matched zero-shot F1 + 0.05, ≤2.00% token leakage
on both German and synthetic sets, and minimum cross-set F1 ≥0.55. Loop 7 added
a stricter rule that the German leakage interval's upper bound must also remain
below 2.00%.

The complete public research record is in
[`RESEARCH.md`](https://github.com/naeyn/nobody/blob/v0.3.0/RESEARCH.md).

## Results

### External German benchmark

The external evaluation uses 3,000 documents and 1,624 labeled spans from the
German validation stream of
[`ai4privacy/pii-masking-400k`](https://huggingface.co/datasets/ai4privacy/pii-masking-400k).
Its publisher describes it as synthetic. It is external to `nobody`'s training
distribution, was not included in released weights, and is not redistributed
here. Intervals are 95% document-level bootstrap intervals.

| model | exact-span F1 | token leakage |
|---|---:|---:|
| **nobody v0.3.0 pipeline** | **0.795** [0.780–0.810] | **1.51%** [1.079–1.995] |
| Piiranha-v1, matched v0.3.0 pipeline | 0.840 | 0.93% |
| `gliner_multi_pii-v1` zero-shot, matched pipeline | 0.635 | 2.26% |

Against Piiranha on this release, paired ΔF1 is **−0.0452**
[−0.0586, −0.0318] and paired Δleakage is **+0.58pp** [+0.11, +1.09].
`nobody` does **not** beat Piiranha on Piiranha's home release.

Per-label `nobody` results:

| label | precision | recall | F1 | token leakage |
|---|---:|---:|---:|---:|
| person | 0.795 | 0.976 | 0.876 | 0.62% |
| address | 0.481 | 0.687 | 0.565 | 15.55% |
| email | 0.987 | 0.987 | 0.987 | 0.00% |
| phone number | 0.901 | 0.986 | 0.942 | 0.69% |
| date of birth | 0.305 | 0.993 | 0.466 | 0.45% |
| **total** | **0.686** | **0.946** | **0.795** | **1.51%** |

The 1.995% upper confidence bound passes the stricter loop-7 leakage gate by
only 0.005 percentage points. `P(leakage ≤ 2.0%)` across bootstrap resamples was
0.976. This is a thin pass, not a comfortable safety margin.

### Synthetic multilingual regression set

The held-out companion test split covers German, English, and Dutch and contains
3,426 spans:

| model | exact-span F1 | token leakage |
|---|---:|---:|
| **nobody v0.3.0 pipeline** | **0.927** | **0.51%** |
| `gliner_multi_pii-v1` zero-shot | 0.826 | 6.60% |
| Piiranha-v1 | 0.677 | 24.09% |

This is regression evidence on a procedurally generated, template-based set,
not independent real-world evidence. Piiranha is outside its training
distribution here.

### Cross-release comparison

A contamination-filtered 3,000-document sample from the CC-BY-4.0
OpenPII-1M German validation release reverses the ranking:

| benchmark | nobody | Piiranha | paired ΔF1 |
|---|---:|---:|---:|
| 400k validation, Piiranha's release | 0.795 | **0.840** | −0.045 [−0.059, −0.032] |
| OpenPII-1M validation, `nobody`'s release | **0.982** | 0.915 | +0.067 [+0.059, +0.074] |

The OpenPII-1M benchmark excluded 590 documents sharing a 12-gram with training;
no exact duplicates remained. This table is **not** a universal `nobody` win:
each model leads on its home generator, OpenPII-1M has no DOB class, and address
gold conventions differ. The ≈0.105 F1 interaction indicates that synthetic
exact-span benchmarks measure generator and annotation conventions as well as
PII detection capability.

### v0.3.0 change at identical weights

Against the loop-6 single-model champion:

- paired ΔF1: **−0.0064** [−0.0097, −0.0034];
- paired Δleakage: **−0.54pp** [−0.96, −0.20].

Both effects exclude zero. The release deliberately traded a small F1 loss for
a larger leakage reduction. German per-class leakage moved from 2.71% to 0.45%
for DOB and from 1.49% to 0.69% for phone numbers; address remains the dominant
residual at 15.55%.

## Training data and provenance

The model has two training sources:

1. [`naeyn/nobody-pii-synth-de`](https://huggingface.co/datasets/naeyn/nobody-pii-synth-de),
   using its 9,450-document generated training split. Documents are
   procedurally generated and labeled by construction.
2. 25,909 German rows from
   [`ai4privacy/pii-masking-openpii-1m`](https://huggingface.co/datasets/ai4privacy/pii-masking-openpii-1m),
   used under CC-BY-4.0. Rows whose raw labels contained `DATE` were excluded
   because that taxonomy does not distinguish ordinary dates from dates of birth.

The evaluation-only 400k stream was not included in released weights. No real
personal records are intentionally included in the published companion dataset
or model inputs. OpenPII's publisher describes its data as synthetic but does
not disclose its generator.

## Limitations and safety

- **Address is the weakest class:** 0.565 F1 and 15.55% token leakage on the
  external German benchmark. Bare house numbers and context-free street or
  place fragments can be missed.
- **DOB matching is recall-first:** recall 0.993 and precision 0.305. Ordinary
  dates can be over-redacted.
- **The leakage CI narrowly clears the budget:** the upper bound is 1.995%, only
  0.005pp below 2.00%.
- **All reported evaluations are synthetic.** Performance on scans, handwriting,
  unseen OCR systems, or another organization's documents is unknown.
- Exact-span metrics are sensitive to annotation conventions, as the two-release
  comparison demonstrates.
- Redaction is pseudonymization, not necessarily anonymization; surrounding
  context can still permit re-identification.
- Keep source documents and redaction logs inside an appropriate security
  boundary. Do not send sensitive documents to third-party services without a
  processing agreement and security review.

## Reproducibility status

Inference is reproducible from the pinned Hub revision, file checksums, and the
public v0.3.0 source tag. The public source includes the released behavior tests,
methodology, changelog, and aggregate evidence. Restricted benchmark records and
private orchestration are not published, so external German aggregate scores
cannot be independently rerun from the public repositories alone. The companion
synthetic test remains regression evidence, not a substitute for a domain-
representative evaluation.

## License and attribution

Released weights are Apache-2.0. The base model
[`urchade/gliner_multi_pii-v1`](https://huggingface.co/urchade/gliner_multi_pii-v1)
is Apache-2.0.

The OpenPII-1M portion of the mix is used under CC-BY-4.0. Required attribution:
**Ai4Privacy / Ai Suisse SA**. See the
[CC-BY-4.0 license](https://creativecommons.org/licenses/by/4.0/) and
[OpenPII-1M dataset card](https://huggingface.co/datasets/ai4privacy/pii-masking-openpii-1m).
The publisher describes that source as synthetic and does not disclose its
generating model.

The companion synthetic dataset is Apache-2.0. Its values were created with
Faker locale providers; Faker is MIT-licensed. See its dataset card for details.
Piiranha is CC-BY-NC-ND and is used only as a research comparator.

## Citation

```bibtex
@software{nobody_pii_de,
  title = {nobody-pii-de: German-first multilingual PII detection and redaction},
  author = {naeyn},
  year = {2026},
  version = {0.3.0},
  url = {https://huggingface.co/naeyn/nobody-pii-de},
  license = {Apache-2.0}
}
```
