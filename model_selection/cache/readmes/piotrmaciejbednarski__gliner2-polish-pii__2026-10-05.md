---
language:
  - pl
license: apache-2.0
library_name: gliner2
pipeline_tag: token-classification
base_model: fastino/gliner2-privacy-filter-PII-multi
tags:
  - gliner2
  - ner
  - pii
  - polish
  - privacy
  - de-identification
  - span-extraction
datasets:
  - klusai/ds-kp-general-pl-50k
  - clarin-pl/kpwr-ner
  - klusai/europriv-bench
  - flowxai/cee-pii-bench
metrics:
  - precision
  - recall
  - f1
model-index:
  - name: GLiNER2 Polish PII
    results:
      - task:
          type: token-classification
          name: Polish PII NER
        dataset:
          name: EuroPriv PL real-skeleton v1
          type: klusai/europriv-bench
          config: pl-realskeleton-v1
        metrics:
          - type: f1
            name: Exact span micro-F1 (balanced)
            value: 0.8442
          - type: f1
            name: Overlap span micro-F1 (balanced)
            value: 0.8715
      - task:
          type: token-classification
          name: Polish PII NER
        dataset:
          name: KPWr NER test, six-label canonical mapping
          type: clarin-pl/kpwr-ner
        metrics:
          - type: f1
            name: Exact span micro-F1 (balanced)
            value: 0.7446
          - type: f1
            name: Overlap span micro-F1 (balanced)
            value: 0.7788
      - task:
          type: token-classification
          name: Polish PII NER
        dataset:
          name: CEE-PII-Bench v0.2 PL
          type: flowxai/cee-pii-bench
          config: pl
        metrics:
          - type: f1
            name: Exact span micro-F1 (precision profile)
            value: 0.7713
          - type: precision
            name: Exact span micro-precision (precision profile)
            value: 0.9017
          - type: recall
            name: Exact span micro-recall (precision profile)
            value: 0.6739
---

# GLiNER2 Polish PII

`GLiNER2 Polish PII` is an open-vocabulary named-entity recognition model adapted to the detection of personally identifiable and sensitive information in Polish text. It was obtained by full-parameter fine-tuning of [`fastino/gliner2-privacy-filter-PII-multi`](https://huggingface.co/fastino/gliner2-privacy-filter-PII-multi) on Polish PII data, selected human-annotated entities from KPWr, explicit negative label queries and augmented examples of Polish structured identifiers.

The model returns character-level spans and supports schema-driven inference with either the supplied taxonomy or user-defined labels. The release contains three calibrated operating profiles:

- `thresholds-balanced.json`, selected for overall NER F1;
- `thresholds-precision.json`, intended for settings in which false positives are costly;
- `thresholds-privacy.json`, an experimental privacy-oriented profile that requires validation on the target domain.

**The model is a detection component, not a de-identification system.** A working de-identification pipeline needs several layers around it, and the sections below describe what those layers have to handle and why. Using this checkpoint does not by itself establish GDPR compliance.

## Intended use

- local PII discovery and redaction candidates in Polish text;
- training-data and log hygiene;
- document review and de-identification support;
- research on Polish open-vocabulary NER.

For consequential applications, predictions should be combined with deterministic checksum validation for PESEL, NIP, REGON and IBAN, application-specific post-processing and, where appropriate, human review.

## Supported taxonomy

The release includes `taxonomy.json` with Polish descriptions for 31 canonical labels:

`person`, `organization`, `first_name`, `last_name`, `date_of_birth`, `email`, `phone_number`, `address`, `street_address`, `city`, `state_or_region`, `postal_code`, `country`, `pesel`, `nip`, `regon`, `krs`, `id_card_number`, `passport_number`, `drivers_license_number`, `national_id_number`, `iban`, `bank_account`, `payment_card`, `account_id`, `ip_address`, `username`, `url`, `license_plate`, `health_condition`, `sensitive_date`.

Public benchmark coverage differs across labels. Per-label reports should be reviewed and the operating thresholds validated on data representative of the intended application. Query only the labels the application needs: GLiNER labels compete for attention, and a long schema can cost recall on labels a shorter one would have caught.

## Installation and inference

```bash
pip install "gliner2[local]==1.3.2"
```

```python
from gliner2 import GLiNER2

model = GLiNER2.from_pretrained("piotrmaciejbednarski/gliner2-polish-pii")

schema = {
    "person": "pełne imię i nazwisko albo nazwa konkretnej osoby",
    "pesel": "polski numer PESEL",
    "iban": "numer rachunku w formacie IBAN",
}

result = model.extract_entities(
    "Katarzyna Zielińska, PESEL 91072412341.",
    schema,
    threshold=0.05,          # permissive; filter with a calibrated profile
    include_confidence=True,
    include_spans=True,
)
```

The call returns, per queried label, a list of spans with `text`, `confidence`, `start` and `end`; a label that matched nothing comes back as an empty list, so filter those out before use. Loading prints an initialisation banner to stdout — redirect it if the output matters.

Use the Polish descriptions from `taxonomy.json` for the labels you query; they are what the calibration was performed against, and the three above are copied from it verbatim. Download the selected threshold profile or package it with the deployment image, and filter per label rather than applying one global cut. **Results obtained with calibrated per-label thresholds must not be presented as performance at a single global threshold of 0.5.**

## Reading the threshold profiles

The profiles are not a simple strict/permissive ordering, and `thresholds-privacy.json` in particular is easy to misread from its name. Its actual distribution is:

| Threshold | Labels |
|---:|---|
| 0.05 | `person`, `city`, `organization` |
| 0.1 | `ip_address` |
| 0.3 | `country` |
| 0.85 | `phone_number`, `license_plate` |
| **0.99** | **the remaining 23 labels**, including `address`, `street_address`, `postal_code`, `date_of_birth`, `health_condition`, `url`, `email`, and every structured identifier |

The profile was selected for per-label containment-match F2 under a `minimum_precision` floor of 0.5 — an objective related to, but not the same as, "redact as much as possible". Two consequences matter in deployment:

- Labels sitting at 0.99 will rarely fire on their own. Where those labels carry no independent validation, that is where recall is lost.
- `person`, `city` and `organization` at 0.05 fire readily. For `city` and `organization` this frequently means place names and brand names in ordinary sentences, which may or may not be personal data under the deploying organisation's policy.

Three labels — `first_name`, `last_name`, `national_id_number` — had no positive support in the calibration set, so their 0.99 is a default rather than a measured value.

Treat the shipped profiles as a starting point and re-calibrate on representative data. Overriding individual thresholds is reasonable; doing so without measuring the effect is not.

## Known failure modes

The behaviours below were observed with the shipped taxonomy descriptions on the published checkpoint. They are reported with the confidences produced so that deployers can recognise them rather than rediscover them. Single-sentence probes are indicative, not benchmark results; verify on your own data.

### A declined full name may lose its given name

Polish declines names, and the model behaves very differently on the nominative and on oblique cases:

| Input | Span | Confidence |
|---|---|---:|
| `Zleceniobiorcą jest Piotr Bednarski.` | `Piotr Bednarski` | 1.00 |
| `Dowiedziałem się od Piotra Bednarskiego...` | `Bednarskiego` | 0.18 |
| | `Piotra` | **0.0000077** |

The surname survives; the given name scores at effectively zero, so no threshold recovers it. A pipeline that redacts only what the model returns will send the given name downstream in the clear, and this is invisible to any evaluation set written in the nominative.

*Mitigation directions.* Treat a `person` span as possibly partial and consider whether an adjacent token belongs to the same name, using a morphological resource rather than capitalisation — Polish names appear lowercased in real messages often enough that a capitalisation test both misses them and, applied in reverse, misclassifies ordinary words as names. Any such expansion needs its own negative tests; several common Polish verbs and function words are also valid name forms once capitalised, and a naive check will absorb them into the span.

### Repeated mentions, and why exact matching is not enough

The model commonly emits one span per entity even when the string appears several times — a name in the body and again in a signature, for example. Re-applying an accepted surface string wherever it recurs raises coverage cheaply.

That handles duplicates only. In Polish the second mention is usually *declined*, so exact matching misses precisely the common case. Recovering inflected repeats requires lemma-level comparison, which brings its own risk: many Polish surnames are also ordinary nouns (`Lis`, `Nowak`, `Kowal`, `Zając`, `Sowa`), and lemma matching will pull the ordinary noun in unless something distinguishes them. Whichever way that is resolved, the resolution is a policy decision — an over-redacted common noun degrades output, a missed inflected mention is a leak — and it should be made deliberately and measured.

Surface expansion is deterministic post-processing. It must be excluded from reported model metrics and can propagate a false positive to every identical occurrence.

### Addresses are frequently split across component labels

A complete postal address may not be returned as one contiguous `address` span even when its components are identified confidently. Query `address` together with `street_address`, `postal_code` and `city` (and `state_or_region`, `country` where relevant) and treat the union as sensitive.

Thresholds for coarse and component labels are calibrated independently, so a threshold chosen for `address` says nothing about `street_address`. Merging adjacent components into one span is an application-level operation the checkpoint does not perform. Evaluations of address extraction should state the queried label set and should not report recall for the coarse label alone when the deployed system relies on components.

### Hard line breaks split entities

Line wrapping from PDFs, OCR, e-mail and pasted documents can break a name, organisation or address across lines and cost the span entirely.

Normalise layout before inference, but keep a reliable mapping back to the source: a length-preserving substitution of newlines and tabs by spaces keeps returned offsets aligned with the original text. If normalisation changes length — collapsing whitespace, rejoining hyphenated OCR lines, applying Unicode substitutions — build an explicit offset map. Never apply offsets from length-changing normalised text to the source document.

### Labels that fire rarely or not at all

Observed on the published checkpoint with its own taxonomy descriptions:

| Case | Result |
|---|---|
| `Logowanie z 192.168.14.22 wygląda podejrzanie.` | `ip_address` at 0.0007, below its own 0.1 threshold |
| `Moje portfolio: https://annakowalska.pl/portfolio.` | no span produced for any label |
| `...on leave for stage 2 breast cancer treatment.` | `health_condition` covers `breast cancer` (0.97) but not the stage qualifier |

Under the precision profile, exact recall on EuroPriv is 0% for `account_id` and `id_card_number`, and roughly 50% for REGON.

The pattern is that entities with **exact syntax and no semantic cue** are weak spots. These are also the easiest to validate deterministically, which is the natural division of labour: pattern matching plus a check digit for PESEL, NIP, REGON, NRB/IBAN and payment cards; a library rather than a regex for phone numbers, so that an order number of the right length is rejected; plain patterns for e-mail, IPv4 and postal codes. Where a rule and the model disagree about the same characters, decide explicitly which wins and what happens to the part of a span the other layer did not cover.

Whether URLs should be redacted at all is a policy question rather than a modelling one: a personal portfolio link is personal data, and a blanket rule would redact every link in every document.

### Long documents

The checkpoint was trained at 512 tokens. The mDeBERTa-v3 encoder uses relative positions, so longer input is neither rejected nor silently truncated — but it runs outside the calibrated range, and attention cost grows quadratically, which can matter if detection sits inside a request path with a timeout.

Splitting long text into overlapping windows keeps inference inside the calibrated range; the overlap has to be wide enough that an entity on a cut still appears whole in one window, and window offsets have to be mapped back to the source.

## Designing the anonymisation step

Detection produces spans. What replaces them is a separate design decision with consequences the model card cannot make for you.

**One-way redaction** replaces each span with a label placeholder. It is simple and irreversible. Two properties are easy to overlook: a bare `<PERSON>` is not injective, so two different people in one document become indistinguishable, and deleting a span can leave text that is ungrammatical or has changed meaning.

**Reversible pseudonymisation** — numbering placeholders per label and keeping a mapping — restores the original afterwards and keeps distinct entities distinct. It moves the confidentiality boundary rather than removing it: something now holds the mapping, and a missed detection leaks *and* looks like it worked. Whether the mapping may outlive a single request is a re-identification question, not an engineering convenience.

**In an inflected language, restoring the original is not a string substitution.** If the source text said `od Piotra Bednarskiego` and the generated text places the placeholder in a nominative slot, substituting the stored surface yields `Jeśli Piotra Bednarskiego się zgodził`. Correct restoration needs the grammatical case the slot requires, which means morphological analysis and generation, and gender has to be carried through — a woman's consonant-final surname does not decline where a man's does. Some of the required case is recoverable from the local context and some is not; verb government in particular is not visible without a valency lexicon.

**Consider what the placeholder erases.** Masking a full name as one opaque token means a downstream consumer cannot be asked to use only the given name — the distinction is gone before it sees the text. Splitting into finer labels restores that ability at the cost of coherence between mentions of the same person.

## Evaluating a deployment

A caveat that costs real defects: **span-level precision cannot see over-redaction that extends a true span.** A predicted span covering `Jan Kowalski mieszka` overlaps the ground-truth `Jan Kowalski` and scores as a clean hit, while a verb is being redacted. Measure characters redacted outside any annotated occurrence as a separate number alongside precision and recall.

Two further points worth building in from the start:

- Measure recall strictly. Requiring every character of an occurrence to fall inside a predicted span avoids crediting partial redaction such as `r.fitzgerald@<EMAIL>` as a success.
- Include declined forms, lowercase writing and entities adjacent to ordinary words. An evaluation set written in tidy nominative prose will not surface the failure modes above.

## Training

| Setting | Value |
|---|---|
| Base checkpoint | `fastino/gliner2-privacy-filter-PII-multi` |
| Training mode | full fine-tuning, LoRA disabled |
| Epochs | 2 |
| Batch size | 32 |
| Maximum length | 512 |
| Encoder learning rate | `1e-6` |
| Task-head learning rate | `2e-5` |
| Scheduler | cosine, 5% warm-up |
| Precision | BF16 |
| Seed | 42 |

Training combined:

- [`klusai/ds-kp-general-pl-50k`](https://huggingface.co/datasets/klusai/ds-kp-general-pl-50k), a 50k Polish synthetic PII corpus;
- selected reliable mappings from the human-annotated [`clarin-pl/kpwr-ner`](https://huggingface.co/datasets/clarin-pl/kpwr-ner) corpus;
- generated Polish positives for underrepresented structured identifiers;
- clean and contextual negative records with explicit empty label targets.

Exact-text overlap between the final training set and frozen evaluation sets was audited and removed. Dataset revisions, counts and provenance are stored in `data_manifest.json`; the final training configuration and environment are stored in `run_manifest.json`.

## Evaluation protocol

All primary results use one-to-one span matching with exact character offsets. `Overlap F1` is reported separately. Per-label thresholds were selected only on `calibration_gold.jsonl`; the frozen test sets were not used for threshold selection.

Reported metrics describe the model under this evaluation harness. They exclude every mitigation discussed above — layout normalisation, component address queries, repeated-mention expansion, span merging, checksum validation and placeholder substitution. Those are deployment concerns and are not part of the benchmark scores. A deployed pipeline that applies them will not have these numbers, in either direction.

### Balanced profile versus the unchanged Fastino base model

| Benchmark | This model exact F1 | Base exact F1 | Paired delta, 95% CI | This model overlap F1 | Base overlap F1 | Clean-document FPR: this/base |
|---|---:|---:|---:|---:|---:|---:|
| EuroPriv PL | 84.42% | 74.74% | +9.68 pp [9.39, 9.98] | 87.15% | 80.82% | n/a |
| KPWr, six-label mapping | 74.46% | 56.63% | +17.82 pp [16.27, 19.41] | 77.88% | 60.65% | 9.22% / 31.22% |
| CEE-PII PL | 73.67% | 74.37% | -0.69 pp [-3.78, 2.14] | 75.09% | 75.49% | 60.42% / 12.50% |
| Manual hard negatives | n/a | n/a | n/a | n/a | n/a | 3.33% / 13.33% |

The improvements on EuroPriv and KPWr are supported by paired document-level bootstrap confidence intervals. On CEE-PII PL, the balanced-profile difference is not statistically distinguishable from the base model, while the clean-document false-positive rate is substantially higher. The precision profile is therefore more appropriate when this failure mode is consequential.

### Precision profile

| Benchmark | Exact precision | Exact recall | Exact F1 | Overlap F1 | Clean-document FPR |
|---|---:|---:|---:|---:|---:|
| EuroPriv PL | 96.81% | 73.97% | 83.86% | 86.58% | n/a |
| KPWr, six-label mapping | 84.82% | 63.24% | 72.46% | 73.96% | 2.37% |
| CEE-PII PL | 90.17% | 67.39% | 77.13% | 78.37% | 0.00% |
| 30 manual hard negatives | n/a | n/a | n/a | n/a | 3.33% (1/30) |

On the manual negative set, the sole false positive was the syntactically valid placeholder `user@example.com` in a sentence explicitly describing it as an example. The benchmark is small, so its FPR estimate has high uncertainty.

## Context among public Polish NER and PII models

The following results are not directly comparable and should not be interpreted as a unified leaderboard:

- [`flowxai/cee-pii`](https://huggingface.co/flowxai/cee-pii) reports 0.94 exact micro-F1 on the 385-document Polish subset of CEE-PII-Bench v0.2, versus this model's 0.7713 with the precision profile. The FlowX model is specialised on the companion corpus drawn from the same synthetic generator distribution and uses its original taxonomy; this model uses a canonical label mapping. FlowX is the stronger published specialist on that benchmark.
- The peer-reviewed [LEPISZCZE benchmark](https://arxiv.org/abs/2211.13112) reports 79.53% macro-F1 for HerBERT-large on full 82-class KPWr NER. This model reaches 75.67% macro-F1 with the precision profile on a six-label PII-oriented mapping. Different label spaces and scoring pipelines prevent a direct rank claim.
- [`tabularisai/eu-pii-safeguard`](https://huggingface.co/tabularisai/eu-pii-safeguard) self-reports 96.63% Polish F1 on its own multilingual evaluation. The model card does not report EuroPriv, CEE-PII PL or this KPWr mapping, so the number is not directly comparable.
- No independently reported result using the exact EuroPriv PL real-skeleton protocol used here was identified at release time. The comparison with the unchanged Fastino checkpoint was therefore produced with the same local evaluation harness, label set and calibration protocol.

## Limitations

Benchmark and protocol:

- EuroPriv PL `real-skeleton-v1` is a development-quality synthetic benchmark, not a human-labeled production-document test.
- CEE-PII-Bench is contamination-audited but shares a generator distribution with its companion training corpus; absolute results may be optimistic.
- KPWr evaluation uses six canonical labels mapped from its original 82-class BIO taxonomy and is not directly comparable with full-taxonomy KPWr leaderboards.
- The balanced profile produces a high false-positive rate on clean CEE documents. The selected operating profile should be reported with all evaluation results.

Model behaviour, detailed in [Known failure modes](#known-failure-modes):

- A declined full name may be reduced to the surname, with the given name scoring near zero.
- Repeated identical mentions may yield only one span; inflected repeats are not matched by surface comparison.
- Complete addresses may be missed as a single `address` span even when the components are detected.
- Hard line breaks inside names, organisations and addresses reduce recall.
- Entities with exact syntax and no semantic cue — IPv4, URLs, some structured identifiers — are weak; under the precision profile `account_id` and `id_card_number` reach 0% exact recall on EuroPriv and REGON roughly 50%.
- `city` and `organization` at 0.05 fire on ordinary place and brand names.
- Dates, locations, organisations and health mentions are policy-dependent; downstream filtering may be required.

Overall:

- **The model may miss PII. It must not be the sole security or compliance control.**

## Reproducibility files

The release directory contains:

- model configuration, tokenizer and weight files saved by GLiNER2;
- `README.md` (this model card);
- `thresholds-balanced.json`, `thresholds-precision.json`, `thresholds-privacy.json`;
- `taxonomy.json`;
- `run_manifest.json` and `data_manifest.json`.

Evaluation reports and raw predictions may be published in a separate repository or an `evaluation/` subdirectory; they are not required for inference.

## License and attribution

Model weights and project code are released under Apache-2.0. The base model is Apache-2.0. Training and evaluation datasets retain their own licenses and attribution requirements:

- `klusai/ds-kp-general-pl-50k`: CC-BY-4.0;
- `clarin-pl/kpwr-ner`: CC-BY-3.0;
- `klusai/europriv-bench`: CC-BY-4.0;
- `flowxai/cee-pii-bench`: Apache-2.0.

## Citation

If you use this checkpoint, cite GLiNER2:

```bibtex
@inproceedings{zaratiana2025gliner2,
  title     = {GLiNER2: Schema-Driven Multi-Task Learning for Structured Information Extraction},
  author    = {Zaratiana, Urchade and Pasternak, Gil and Boyd, Oliver and Hurn-Maloney, George and Lewis, Ash},
  booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: System Demonstrations},
  year      = {2025},
  pages     = {130--140},
  url       = {https://aclanthology.org/2025.emnlp-demos.10/}
}
```

Model fine-tuning and Polish evaluation: [Piotr Bednarski](https://bednars.me/).