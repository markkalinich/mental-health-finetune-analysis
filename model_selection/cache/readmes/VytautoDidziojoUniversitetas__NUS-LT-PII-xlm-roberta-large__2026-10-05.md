---
license: openrail
language:
- lt
library_name: transformers
pipeline_tag: token-classification
base_model:
- FacebookAI/xlm-roberta-large
tags:
- ner
- pii
- de-identification
- gdpr
widget:
- text: "Pacientas Jonas Petraitis, gim. 1965 m. spalio 12 d., gyvenantis adresu Vilnius, Gedimino pr. 25-7, 2026-03-14 kreipėsi į VšĮ Vilniaus universiteto ligoninės Santaros klinikas dėl galvos skausmo. Asmens kodas 36510121234, kontaktinis telefonas +37061234567, el. paštas jonas.petraitis@example.lt"
  example_title: "Lithuanian PII example"
---

# NUS Lithuanian PII Detection Model

A model that detects personal information (PII) in Lithuanian text — names, addresses, ID codes, phone numbers, dates, health information, and other categories of sensitive data. Use it to mark or remove PII before publishing court decisions and administrative documents, processing medical or research records, or sending text to external AI assistants and translation services.

The model is the inference backend of the [NUS PII validator tool](https://github.com/Faculty-of-Informatics-VDU/nus-lt-pii) — a local, GDPR-friendly web application for de-identifying Lithuanian text and validating NER models.

## Model Details

- **Base model:** [FacebookAI/xlm-roberta-large](https://huggingface.co/FacebookAI/xlm-roberta-large) (~560M parameters)
- **Architecture:** transformer encoder fine-tuned for token classification
- **Language:** Lithuanian
- **Task:** named-entity recognition for PII / GDPR-relevant entities
- **Output:** 24 entity types (16 general + 8 sensitive — see Label set below)

## Training Data

Trained on [`VytautoDidziojoUniversitetas/NUS-LT-PII-corpus`](https://huggingface.co/datasets/VytautoDidziojoUniversitetas/NUS-LT-PII-corpus) — Lithuanian text from administrative, scientific, and media domains annotated for 24 PII / GDPR special-category entity types. See the dataset card for source breakdown, distribution, and limitations.

## Uses

**Intended uses:**

- De-identifying Lithuanian text before publishing — court decisions, administrative documents, public records.
- Pre-processing medical or research records that contain personal data before sharing or analysis.
- Pre-processing text before sending it to external AI assistants or translation services that should not see PII.
- Compliance workflows under GDPR for Lithuanian-language data.
- Research on Lithuanian NER, cross-domain transfer, and rare-entity (sensitive GDPR category) detection.

**Out of scope:**

- Languages other than Lithuanian — output is undefined.
- General-purpose NER beyond the 24 PII / GDPR categories listed below.
- Stand-alone anonymization — see Risks and limitations.

## Label set

| Label | Meaning |
|---|---|
| `PER` | Person names |
| `LOC` | Locations and addresses |
| `ORG` | Organizations |
| `ID_PER` | Personal ID codes (Lithuanian 11-digit national `asmens kodas`) |
| `ID_MISC` | Other identifiers (passport, document numbers, etc.) |
| `NUM_PHONE` | Phone numbers |
| `NUM_CAR` | Vehicle license plates |
| `MISC` | Email addresses and miscellaneous identifiers |
| `OCC` | Occupations |
| `EDU` | Education |
| `AGE` | Age |
| `DATE` | Dates |
| `TIME` | Times |
| `DURATION` | Durations |
| `VALUE` | Numeric amounts and quantities |
| `NAT` | Nationality |
| `HEALTH` | Health information (diagnoses, conditions, treatments) |
| `REL` | Religion |
| `POL` | Political views |
| `ETH` | Ethnic origin |
| `MAR` | Marital status (single, married, divorced, etc.) |
| `FAM` | Family relations (mentions of relatives) |
| `GENDER` | Gender |
| `SEX` | Sexual orientation |

## How to use

For de-identification, use the [NUS PII validator](https://github.com/Faculty-of-Informatics-VDU/nus-lt-pii) — a local web app that bundles this model with the boundary post-processing rules and a Lithuanian UI.

If you only need the raw weights:

```python
from transformers import pipeline

ner = pipeline(
    "token-classification",
    model="VytautoDidziojoUniversitetas/NUS-LT-PII-xlm-roberta-large",
    aggregation_strategy="first",
)

text = "Jonas Petraitis gyvena Vilniuje, telefonas +370 612 34567."
for ent in ner(text):
    print(ent["entity_group"], "→", ent["word"])
```

## Training Details

**Training code:** [Faculty-of-Informatics-VDU/nus-lt-pii-model-training](https://github.com/Faculty-of-Informatics-VDU/nus-lt-pii-model-training)

**Data splits** (from [`VytautoDidziojoUniversitetas/NUS-LT-PII-corpus`](https://huggingface.co/datasets/VytautoDidziojoUniversitetas/NUS-LT-PII-corpus)): the corpus ships with a train split (administraciniai, mokslinis, ziniasklaida) and a held-out `validacija` test split.

- **Hyperparameter search:** train carved into 90/10 train/val; selection by val F1.
- **Final training:** the 10% val portion is folded back into train — the model is trained on the full train split (no early stopping).
- **Test evaluation:** the held-out `validacija` split — untouched during HP search and final training.

**Hyperparameter search:** Optuna with TPE sampler (multivariate), no pruning; 22 completed trials. Selection by validation F1 with best checkpoint loading. Search space:

| Parameter | Range |
|---|---|
| Learning rate | log-uniform [1e-5, 1e-4] |
| Weight decay | uniform [0.05, 0.30] |
| Warmup ratio | uniform [0.0, 0.15] |
| Epochs | {5, 8, 10} |
| LR scheduler | {linear, cosine} |
| Gradient accumulation steps | {1, 2, 4} |
| Label smoothing | {0.0, 0.05, 0.1} |

**Final hyperparameters** (winner — trial 19, val F1 0.837):

| Parameter | Value |
|---|---|
| Learning rate | 4.24e-5 |
| Weight decay | 0.159 |
| Warmup ratio | 0.099 |
| Epochs | 10 |
| LR schedule | Cosine |
| Per-device batch size | 16 |
| Gradient accumulation steps | 1 |
| Effective batch size | 32 (16 × 1 × 2 GPUs) |
| Label smoothing | 0.0 |
| Optimizer | AdamW (PyTorch) |
| Max grad norm | 1.0 |
| Precision | bf16 |

**Final training:** trained on the combined train + validation split (no early stopping) with the HP search winner. 5 random seeds trained independently; the **median checkpoint** is deployed (seed 256). Test F1 across seeds: 0.8706 ± 0.0037.

**Compute:** 2 × NVIDIA H100 NVL, ≈1 hour per final-training run (≈2 GPU-hours per seed).

## Evaluation

Evaluated on the held-out [`validacija`](https://huggingface.co/datasets/VytautoDidziojoUniversitetas/NUS-LT-PII-corpus) split (7148 entities) using `seqeval`-style entity-level metrics.

| Metric | Score |
|---|---:|
| Overall F1 | **0.8720** |
| Overall precision | 0.8601 |
| Overall recall | 0.8842 |
| Overall accuracy | 0.9643 |
| Macro F1 | 0.7768 |
| Macro precision | 0.7589 |
| Macro recall | 0.8338 |

### Per-label metrics

| Label | F1 | Precision | Recall | Support |
|---|---:|---:|---:|---:|
| `PER` | 0.984 | 0.988 | 0.980 | 1386 |
| `LOC` | 0.834 | 0.817 | 0.851 | 820 |
| `ORG` | 0.797 | 0.777 | 0.817 | 1298 |
| `ID_PER` | 1.000 | 1.000 | 1.000 | 4 |
| `ID_MISC` | 0.803 | 0.850 | 0.761 | 67 |
| `NUM_PHONE` | 0.991 | 0.981 | 1.000 | 53 |
| `NUM_CAR` | 1.000 | 1.000 | 1.000 | 3 |
| `MISC` | 0.955 | 0.955 | 0.955 | 66 |
| `OCC` | 0.843 | 0.843 | 0.843 | 619 |
| `EDU` | 0.514 | 0.419 | 0.667 | 27 |
| `AGE` | 0.679 | 0.581 | 0.818 | 22 |
| `DATE` | 0.793 | 0.777 | 0.810 | 305 |
| `TIME` | 0.873 | 0.844 | 0.904 | 281 |
| `DURATION` | 0.741 | 0.745 | 0.737 | 285 |
| `VALUE` | 0.942 | 0.940 | 0.944 | 1488 |
| `HEALTH` | 0.329 | 0.280 | 0.400 | 35 |
| `REL` | 0.545 | 0.375 | 1.000 | 3 |
| `POL` | 0.667 | 0.500 | 1.000 | 2 |
| `ETH` | 0.538 | 0.400 | 0.824 | 17 |
| `NAT` | 0.935 | 0.908 | 0.964 | 275 |
| `MAR` | 0.667 | 1.000 | 0.500 | 6 |
| `FAM` | 0.595 | 0.521 | 0.694 | 36 |
| `GENDER` | 0.617 | 0.714 | 0.543 | 46 |
| `SEX` | 1.000 | 1.000 | 1.000 | 4 |

*The [NUS PII validator](https://github.com/Faculty-of-Informatics-VDU/nus-lt-pii) tool uses character-span matching and reports strict micro/macro F1 0.854/0.770 (P 0.851/0.753, R 0.857/0.821), partial 0.886/0.793 (P 0.884/0.775, R 0.889/0.846), and boundary recall 0.876.*

## Risks and limitations

- **Residual re-identification risk:** the model detects and labels PII spans for downstream substitution-based masking. As with any PII pipeline, two residual risks remain: (1) detector misses — at ~88% recall some PII slips through; (2) information not covered by the label set — book or event titles, project names, distinctive phrasing, or unique combinations of non-PII facts can still identify individuals. In regulated contexts (GDPR, healthcare, legal) combine with human review as part of a layered pipeline.
- **Lithuanian only:** despite the multilingual XLM-RoBERTa base, this fine-tune is Lithuanian-specific; other languages and code-switched documents produce undefined output.
- **Inherited corpus limitations:** domain skew (~84% administrative text), cross-convention annotation choices, and class imbalance on rare and sensitive entities all carry over from the training corpus — see the [dataset card's *Limitations and Bias* section](https://huggingface.co/datasets/VytautoDidziojoUniversitetas/NUS-LT-PII-corpus#limitations-and-bias). Per-class performance has high variance on small classes; see per-label F1 in [Evaluation](#evaluation).

## License

**NewGenLTU OpenRAIL-D licence** — the same licence used by the underlying training corpus. See the [dataset's `LICENSE.txt`](https://huggingface.co/datasets/VytautoDidziojoUniversitetas/NUS-LT-PII-corpus/blob/main/LICENSE.txt) for the full terms and restrictions.

## Acknowledgement

Funded by the European Union — NextGenerationEU. Naujos kartos Lietuva.

This project is funded by the Recovery and Resilience Facility under the Lithuanian "Naujos kartos Lietuva" plan and by the State Budget of the Republic of Lithuania.

Project: *Nuasmeninimo tekstyno sukūrimas (NUS)* — Project No. **02-100-K-0001**.

## Citation

Please cite the model as:

**Vytautas Magnus University and Kaunas University of Technology. 2026. NUS Lithuanian PII Detection Model. Hugging Face. https://huggingface.co/VytautoDidziojoUniversitetas/NUS-LT-PII-xlm-roberta-large**

BibTeX:

```bibtex
@misc{nus_lt_pii_model_2026,
  author    = {{Vytautas Magnus University} and {Kaunas University of Technology}},
  title     = {NUS Lithuanian PII Detection Model},
  year      = {2026},
  publisher = {Hugging Face},
  url       = {https://huggingface.co/VytautoDidziojoUniversitetas/NUS-LT-PII-xlm-roberta-large},
  note      = {Developed under the New Generation Lithuania plan, project 02-100-K-0001.}
}
```
