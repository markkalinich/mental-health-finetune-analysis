---
library_name: transformers
license: mit
language:
- si
- en
base_model:
- FacebookAI/xlm-roberta-base
pipeline_tag: text-classification
---

# Sinhala-English Codemix PII Detector

An XLM-RoBERTa token-classification model fine-tuned to detect personally
identifiable information (PII) in informal Sinhala-English code-mixed text.

## Model Details

### Model Description

- **Developed by:** Ramosh99
- **Funded by:** University of Moratuwa, Department of Information Technology — undergraduate final-year research project (BSc IT, Level 4 Semester 7)
- **Shared by:** [Ramosh99](https://huggingface.co/Ramosh99)
- **Model type:** XLM-RoBERTa token classifier for BIO-style named-entity recognition
- **Language(s) (NLP):** Sinhala and English, including Sinhala-English code-mixed text
- **License:** MIT
- **Finetuned from model:** [`xlm-roberta-base`](https://huggingface.co/xlm-roberta-base)

### Model Sources

- **Repository:** [`Ramosh99/mixcode_pii_detector`](https://huggingface.co/Ramosh99/mixcode_pii_detector)
- **Paper:** Undergraduate research thesis — *PII Detection and Redaction in Low-Resource Code-Mixed Languages: A Sinhala-English Case Study*, University of Moratuwa (2025)
- **Demo:** The accompanying Docker Space exposes a FastAPI inference service.

## Uses

### Direct Use

The model detects PII spans and assigns an entity type and confidence score.
It is intended for Sinhala-English code-mixed conversational text and can also
be tested on Sinhala-script input.

The research taxonomy contains these 22 entity types:

`ACCOUNT_TYPE`, `ADDRESS`, `AGE`, `BANK_ACCOUNT`, `CARD_NUMBER`, `DATE`,
`DESIGNATION`, `DISEASE`, `EMAIL`, `GENDER`, `LINK`, `LOCATION`, `NIC`, `ORG`,
`PASSWORD`, `PERSON`, `PHONE`, `QUALIFICATION`, `RACE`, `RELIGION`, `TIME`,
`USERNAME`.

### Downstream Use

Use the model as one component in a privacy pipeline for entity highlighting,
masking, redaction, access-control review, or structured PII validation. Pair
predictions with deterministic validators for formats such as phone numbers,
NICs, email addresses, card numbers, and bank-account numbers.

### Out-of-Scope Use

Do not use this model as the sole basis for legal, employment, financial,
identity, or security decisions. It is not a complete de-identification
guarantee, a calibrated risk classifier, or a replacement for human review.
Do not assume that text without a prediction is safe to disclose.

## Bias, Risks, and Limitations

The corpus is domain-specific and includes augmented examples. Real messages
may contain spellings, transliterations, scripts, spacing, abbreviations, or
PII formats that are not represented in training data. Entity frequencies are
imbalanced, so rare sensitive classes may have lower recall than common classes.
Sinhala morphology and script switching can also affect token boundaries and
span extraction. Confidence values are model scores, not formally calibrated
probabilities.

### Recommendations

Evaluate the model on representative data from the intended deployment domain.
Use confidence thresholds, format validation, audit logging, and human review
for high-risk decisions. Minimize retention of submitted text and protect
inference inputs because they may contain sensitive information.

## How to Get Started with the Model

```python
from transformers import pipeline

ner = pipeline(
    "ner",
    model="Ramosh99/mixcode_pii_detector_v3",
    aggregation_strategy="average",
)

text = "Mage name Kamal, man wada karanne MAS Holdings eke, phone 071-1234567"
for entity in ner(text):
    print(entity)
```

The accompanying Space also provides `POST /predict` and `GET /health`
endpoints. The prediction request is:

```json
{"text": "Mage name Kamal, man wada karanne MAS Holdings eke, phone 071-1234567"}
```

## Training Details

### Training Data

The model was fine-tuned on a custom annotated Sinhala-English code-mixed PII
corpus. The data uses BIO tagging and includes augmented examples to improve
coverage of low-frequency sensitive categories. A public dataset-card URL and
full dataset release details were not specified in the available materials.

### Training Procedure

The model was trained as a token-classification task using the Hugging Face
Transformers ecosystem and XLM-RoBERTa's multilingual SentencePiece tokenizer.
The project also developed character-to-subword alignment and span-recovery
logic for code-mixed text, while the served API uses Transformers aggregation.

#### Preprocessing

Input text is tokenized with the XLM-RoBERTa tokenizer and aligned to BIO labels.
Predictions are aggregated into entity spans, and the API removes `B-` and `I-`
prefixes from returned `entity_group` values.

#### Training Hyperparameters

The available training materials record experiments using a learning rate of
`3e-5`, batch size `16`, `5` epochs, weight decay `0.01`, and warmup ratio
`0.1`. The exact configuration for the published checkpoint is not separately
identified.

- **Training regime:** Mixed precision (fp16) on NVIDIA GPU with AdamW optimizer, linear warmup schedule, and early stopping on validation loss

#### Speeds, Sizes, Times

Training duration, throughput, checkpoint size, and total compute time were not
recorded in the available model materials.

## Evaluation

### Testing Data, Factors & Metrics

#### Testing Data

One reported research benchmark used a template-aware split with 2,000
evaluation samples. A separate evaluation artifact covered 17 target entities;
the available materials do not establish that both evaluations used identical
splits or scopes.

#### Factors

The research analysis considers model architecture, entity type, entity
frequency, and micro- versus macro-averaging. The attached confusion matrix
shows a representative subset of BIO-label behavior rather than all 22 PII
types.

#### Metrics

Precision measures the proportion of predicted entity spans that are correct.
Recall measures the proportion of reference entity spans that are recovered.
F1 is the harmonic mean of precision and recall. Micro-averaging weights entity
instances by frequency, while macro-averaging gives each entity type equal
weight and therefore exposes rare-label weaknesses.

### Results

The associated XLM-RoBERTa comparison on the 2,000-sample benchmark reported:

| Metric | Score |
| --- | ---: |
| Precision | 0.9939 |
| Recall | 0.9934 |
| F1 | 0.9937 |

A separate 17-entity evaluation reported:

| Averaging | Precision | Recall | F1 |
| --- | ---: | ---: | ---: |
| Micro | 0.9713 | 0.9549 | 0.9630 |
| Macro | 0.9610 | 0.9188 | 0.9358 |

#### Summary

The benchmark results show strong aggregate performance for the reported
XLM-RoBERTa experiment. The lower macro recall in the separate 17-entity
analysis indicates that aggregate scores can hide weaker performance on rare
PII categories. These results are not a guarantee for every domain or entity
format and should be reproduced on deployment-specific test data.

### Evaluation Figures

<!-- ![Entity-level precision, recall, and F1](entity_based_p_r_f1.png) -->

![entity_based_p_r_f1](https://cdn-uploads.huggingface.co/production/uploads/66846e816c6ae7843bdbf3da/yQz0VY2o4nX-07RW0bpIs.png)

<!-- ![Training and validation loss](report_loss_metric_curves.png) -->

![loss_variation_graphs](https://cdn-uploads.huggingface.co/production/uploads/66846e816c6ae7843bdbf3da/-9HZ2zgN5mpoDbiD_ukRu.png)

<!-- ![Micro- and macro-averaged performance](micro_vs_macro.png) -->

![micro vs macro](https://cdn-uploads.huggingface.co/production/uploads/66846e816c6ae7843bdbf3da/QL0iNO1R1dpk_rmS9aFVy.png)

<!-- ![Representative confusion matrix](report_confusion_matrix.png) -->

![report_confusion_matrix](https://cdn-uploads.huggingface.co/production/uploads/66846e816c6ae7843bdbf3da/XokfSRSj2f2fczGZx90WR.png)

<!-- ![Entity imbalance and F1 gap](Limitation_Entity_Imbalance_vs_F1_Performance_Gap.png) -->

![Limitation Entity Imbalance vs Fl Performance Gap](https://cdn-uploads.huggingface.co/production/uploads/66846e816c6ae7843bdbf3da/P150ukApCqnZRA8W4D4Z5.png)

## Model Examination

The evaluation artifacts examine entity-level precision, recall, F1 variation,
confusion patterns, training and validation loss, and the relationship between
entity frequency and F1 performance. No formal interpretability study was
recorded.

## Environmental Impact

Carbon emissions can be estimated using the [Machine Learning Impact
calculator](https://mlco2.github.io/impact#compute) presented in [Lacoste et
al. (2019)](https://arxiv.org/abs/1910.09700).

- **Hardware Type:** NVIDIA GPU (T4, V100, A100), CPU, or Google TPU
- **Hours used:** Approximately 2–4 GPU hours per training run
- **Cloud Provider:** Google Colab / Kaggle (free-tier GPU)
- **Compute Region:** us-central1 (Google Colab default)
- **Carbon Emitted:** Estimated minimal; short training runs on shared GPU infrastructure

## Technical Specifications

### Model Architecture and Objective

The model is an XLM-RoBERTa token classifier fine-tuned with BIO-style labels
for fine-grained PII named-entity recognition. XLM-RoBERTa provides multilingual
representations and SentencePiece subword tokenization for mixed Sinhala and
English input.

### Compute Infrastructure

The exact compute infrastructure used for the published checkpoint was not
recorded.

#### Hardware

Can be run in CPU/GPU/TPU

#### Software

The model uses the Hugging Face Transformers ecosystem. The deployed Space uses
Python, FastAPI, Pydantic, and a Transformers NER pipeline.

## Citation

If you use this model, please cite the project and record the exact model revision evaluated.

**BibTeX:**

```bibtex
@misc{ramosh99_mixcode_pii_2025,
  author       = {Ramosh99},
  title        = {Sinhala-English Codemix PII Detector: Fine-tuned XLM-RoBERTa for Code-Mixed PII Named-Entity Recognition},
  year         = {2025},
  publisher    = {Hugging Face},
  howpublished = {\url{https://huggingface.co/Ramosh99/mixcode_pii_detector_v3}},
  note         = {Undergraduate FYP research, University of Moratuwa — BSc IT Level 4 Semester 7}
}
```

**APA:**

Ramosh99. (2025). *Sinhala-English Codemix PII Detector: Fine-tuned XLM-RoBERTa for Code-Mixed PII Named-Entity Recognition* [Model]. Hugging Face. https://huggingface.co/Ramosh99/mixcode_pii_detector_v3

## Glossary

- **PII:** Personally identifiable information.
- **NER:** Named-entity recognition.
- **BIO:** Beginning, Inside, Outside tagging used to represent entity spans.
- **Micro-F1:** F1 calculated over all entity instances together.
- **Macro-F1:** The mean F1 across entity types.

## More Information

The model is designed for Sinhala-English code-mixed PII detection rather than
general-purpose NER. Predictions should be treated as evidence for a downstream
privacy workflow, not as a definitive privacy classification.

## Model Card Authors

The model card was prepared from the available Codemix PII detection project
materials. Individual author names were not specified.

## Model Card Contact

Model publisher: [Ramosh99](https://huggingface.co/Ramosh99).
