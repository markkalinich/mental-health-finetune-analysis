---
license: apache-2.0
library_name: transformers
pipeline_tag: token-classification
tags: [pii, phi, de-identification, redaction, modernbert, token-classification]
---

# modernbert-pii-v0.1

ModernBERT-base fine-tuned for PII/PHI span detection over a **169-label**
BIO space derived from a versioned 84-concept ontology.

## Training

| | |
|---|---|
| base model | `answerdotai/ModernBERT-base` |
| objective | **scheme-aware marginal loss** (not plain cross-entropy) |
| steps | 33,100 |
| max length | 512 |
| label level | `core` (ontology v0.1) |
| seed | 0 |

### Scheme-aware loss

The 32 source corpora annotate different label sets. A corpus that
annotates 7 concepts tags every email and phone number as `O` — under plain
cross-entropy those become hard negatives and the model unlearns them. Instead
each token is trained against the **set of labels consistent with its
annotation**: for `O`, that is `O` plus every concept the source dataset does not
annotate.

### Training datasets (32)

- `ai4privacy/legacy-tiers`
- `ai4privacy/open-pii-500k`
- `ai4privacy/openpii-1.5m`
- `alrosait/russian-pii`
- `bccard/openpii-finance`
- `bob14/korean-sensitive`
- `btx24/turkish-pii`
- `careons/dutch-healthcare-pii`
- `datafog/test-corpus`
- `dataiku/kiji`
- `dialogpii`
- `e3jsi/multi-pii-ner`
- `felipe53/name-judgment`
- `grascco/multi`
- `grascco/pii-v2`
- `gretel/pii-finance-multilingual`
- `gretel/pii-masking-en`
- `kdpii`
- `keler/turkish-medical-deid-eval`
- `kierandesmond/gdpr-special-categories`
- `lacuna/pii`
- `localdoc/azerbaijani-pii`
- `meddocan`
- `meddoplace`
- `meddoprof`
- `nisaefendiolu/code-secrets`
- `nutrient/docpii`
- `nvidia/nemotron-pii`
- `presidio/research-eval`
- `sidharth/indicphi`
- `tab/text-anonymization-benchmark`
- `tonicai/privacy-bench`

## Known limitations

- Character offsets from the tokenizer include the preceding space; decoded spans
  **must** be whitespace-trimmed. Without it, span-exact accuracy falls from
  ~99.7% to ~5.9% while token-level F1 is unchanged.
- Spans located by string search rather than given by the annotator are marked
  `derived` in the corpus; they train but were never scored.
- Coverage is skewed: health identifiers are a small fraction of training
  mentions relative to network and contact identifiers.
