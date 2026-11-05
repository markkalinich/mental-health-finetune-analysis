---
language:
  - it
library_name: transformers
pipeline_tag: token-classification
base_model: jhu-clsp/mmBERT-base
license: other
tags:
  - pii
  - privacy
  - redaction
  - italian
  - legal
  - modernbert
---

# Llama-mmBERT-PII-Redactor-IT-0.3B

**Built with Llama.**

Llama-mmBERT-PII-Redactor-IT-0.3B is an approximately 307-million-parameter
token-classification model for detecting personally identifiable and
document-related information in Italian text, with a focus on legal documents.
It is intended to run locally on CPU or CUDA as part of the deterministic
validation and redaction pipeline provided by PII Redactor.

The model architecture and base weights derive from
[`jhu-clsp/mmBERT-base`](https://huggingface.co/jhu-clsp/mmBERT-base), revision
`c5955035435e2bf121cde7f3c8863ef52ff35d82`. The checkpoint uses
`ModernBertForTokenClassification`; it is not a generative Llama architecture
and does not use Llama base weights.

The `Llama` prefix and the “Built with Llama” attribution reflect the licensing
and attribution conditions declared by Ai4Privacy for material generated using
Llama 3.1 and 3.3. They do not describe the model architecture and do not imply
affiliation with or endorsement by Meta or Ai4Privacy.

## Model details

| Field | Value |
|---|---|
| Task | token classification / PII span detection |
| Language | Italian |
| Parameters | approximately 307 million |
| Architecture | `ModernBertForTokenClassification` |
| Base model | `jhu-clsp/mmBERT-base` |
| Base revision | `c5955035435e2bf121cde7f3c8863ef52ff35d82` |
| Internal checkpoint | `abl-v3b-fullname-org-s13` |
| Label schema | `it_legal_ner_v1` |
| Maximum training sequence | 768 tokens |

The output schema covers names, addresses, contact details, Italian tax
identifiers, payment identifiers, organizations, document identifiers and
cadastral references. The complete runtime also applies deterministic
validators, propagation and contextual post-processing; checkpoint-only
metrics therefore do not represent the complete product.

## Training-data provenance

The 720,025-row training pack is composed as follows:

| Component | Rows | Share | Provenance |
|---|---:|---:|---|
| Ai4Privacy remapped training rows | 464,025 | 64.45% | direct adaptation |
| Italian augmentation over Ai4Privacy prose | 40,000 | 5.56% | derivative/transformed material |
| Project-generated synthetic corpus | 200,000 | 27.78% | project-controlled generation |
| Targeted FULLNAME/ORG augmentation | 16,000 | 2.22% | project-controlled generation |

In total, 504,025 rows, approximately 70.00% of the training pack, are direct
or transformed material from
[`ai4privacy/open-pii-masking-500k-ai4privacy`](https://huggingface.co/datasets/ai4privacy/open-pii-masking-500k-ai4privacy).
The 7,000-row training validation split also derives from held-out Ai4Privacy
material with project transformations.

The historical training pipeline downloaded the dataset from `main` without
recording the checkout revision. The upstream train and validation objects are
therefore identified by their immutable LFS SHA-256 values, sizes and last
content-changing commit in `PROVENANCE.json`; the observed repository revision
is retained without presenting it as the unrecorded training checkout. The
upstream data objects had not changed since 25 February 2025.

The source records were remapped to the project taxonomy, normalized, combined
with project-generated data and packed for mmBERT token classification. The
original Ai4Privacy dataset is not included in this model repository.

## Intended use

The intended use is assisted detection and reversible redaction of personal
information in Italian legal documents. Model output must be reviewed before a
document is shared. The model is not a compliance certification service and
does not guarantee detection of every personal or sensitive value.

The model does not perform OCR. Image-only PDFs and photographs require a
separate local text-extraction step outside the model's scope. The current
taxonomy does not provide complete coverage for special-category health data.

## Usage

Load the reviewed release tag rather than a moving branch:

```python
from transformers import AutoModelForTokenClassification, AutoTokenizer

model_id = "hugginfacez/Llama-mmBERT-PII-Redactor-IT-0.3B"

tokenizer = AutoTokenizer.from_pretrained(
    model_id,
    revision="v1.0.0",
    fix_mistral_regex=False,
)
model = AutoModelForTokenClassification.from_pretrained(
    model_id,
    revision="v1.0.0",
)
```

`fix_mistral_regex=False` preserves the mmBERT tokenizer behavior expected by
this checkpoint. Remote custom code is not required and should not be enabled.

## Evaluation scope

The checkpoint training manifest records micro-F1 `0.99245` and macro-F1
`0.99336` on the 7,000-row training validation split described above. These
figures are not independent real-world evidence because that validation is
derived from the same upstream source family used in training.

The accompanying PII Redactor runtime has also been regression-tested on a
fixed synthetic Italian legal-document challenge. Those results are useful for
detecting regressions, but they do not establish general performance on real
legal files. Real-world recall, demographic behavior, document extraction and
domain transfer remain to be evaluated on separately governed data.

## Limitations and risks

- False negatives can leave personal or sensitive information unredacted.
- False positives can alter information that should remain visible.
- OCR, complex document layout and incomplete PDF text layers are outside the
  checkpoint itself.
- Names, organizations, addresses and short numeric spans remain ambiguous in
  some contexts.
- Performance on medical documents and special-category health data is not
  established.
- Evaluation evidence is currently synthetic or source-family validation; no
  claim of production readiness is made.

Use defense in depth: deterministic checks, human review, fail-closed document
handling and evaluation on authorized data representative of the intended
deployment.

## Privacy

The model runs locally after download. Loading weights from the Hugging Face
Hub does not upload the document being processed. Applications using the model
remain responsible for preventing document contents, extracted text and
reversible redaction dictionaries from being sent to external services.

## License and attribution

Hugging Face metadata uses `license: other` because this is a composite model
distribution, not an unqualified MIT release.

The original checkpoint material is offered under the permission in `LICENSE`,
subject to all third-party conditions recorded in `NOTICE`,
`THIRD_PARTY_NOTICES.md` and `LICENSES/`. In particular, redistribution must
preserve:

1. the model name beginning with `Llama`;
2. prominent **Built with Llama** attribution on related interfaces, websites
   and documentation;
3. the supplied Llama 3.1 and Llama 3.3 Community License texts and compliance
   with their applicable Acceptable Use Policy;
4. Ai4Privacy attribution, citation and the CC BY 4.0 reference;
5. the MIT notice for `jhu-clsp/mmBERT-base`.

The source datasets are not included or relicensed by this repository. See
`PROVENANCE.json` for the training lineage and `RELEASE_NOTES.md` for the exact
release scope. These records document the publisher's public-terms review; they
are not legal or regulatory certification.
