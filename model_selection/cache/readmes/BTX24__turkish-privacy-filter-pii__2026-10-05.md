---
language:
  - tr
license: apache-2.0
base_model: openai/privacy-filter
datasets:
  - BTX24/turkish-privacy-pii-ner
pipeline_tag: token-classification
tags:
  - token-classification
  - named-entity-recognition
  - pii
  - privacy
  - privacy-filter
  - openai-privacy-filter
  - turkish
  - turkish-nlp
  - kvkk
  - data-redaction
  - anonymization
  - span-detection
  - sensitive-data
  - personal-data
  - synthetic-data
model-index:
  - name: Turkish Privacy Filter PII
    results:
      - task:
          type: token-classification
          name: Token Classification
        dataset:
          type: BTX24/turkish-privacy-pii-ner
          name: Turkish Privacy PII NER Dataset
          split: test
        metrics:
          - type: f1
            name: Detection F1
            value: 0.9997
          - type: precision
            name: Detection Precision
            value: 0.9998
          - type: recall
            name: Detection Recall
            value: 0.9996
          - type: f1
            name: Span F1
            value: 0.9983
          - type: accuracy
            name: Token Accuracy
            value: 0.9996
---

# Turkish Privacy Filter PII

Repository: `BTX24/turkish-privacy-filter-pii`

This repository contains a Turkish-oriented fine-tuned checkpoint of [`openai/privacy-filter`](https://huggingface.co/openai/privacy-filter) for privacy-focused PII span detection.

The model is designed to detect Turkish privacy-sensitive spans such as Turkish-style person names, e-mail addresses, phone numbers, dates, addresses, account identifiers, IBAN-like values, TCKN-like values, VKN-like values, and secret-like tokens.

> **Important:** This model is a privacy redaction aid. It is not a legal anonymization guarantee.

---

## Türkçe Açıklama

Bu model, [`openai/privacy-filter`](https://huggingface.co/openai/privacy-filter) temel alınarak Türkçe gizlilik odaklı PII / kişisel veri tespiti için fine-tune edilmiş bir checkpoint’tir.

Modelin amacı; Türkçe metinlerde geçen kişi adı, e-posta, telefon, tarih, adres, hesap numarası, IBAN benzeri değer, T.C. kimlik numarası benzeri değer, vergi kimlik numarası benzeri değer ve secret/token/parola benzeri hassas alanları span düzeyinde tespit etmektir.

> **Önemli:** Bu model gizlilik odaklı veri maskeleme/redaction için yardımcı bir araçtır. Tek başına hukuki anonimleştirme veya KVKK uyumluluk garantisi sağlamaz.

---

# Base Model

Base model:

```text
openai/privacy-filter
```

OpenAI Privacy Filter is a bidirectional token-classification model for detecting and redacting personally identifiable information (PII) in text. This checkpoint adapts the base model to a Turkish-oriented privacy label space.

---

# Training Dataset

This model was fine-tuned on:

```text
BTX24/turkish-privacy-pii-ner
```

Dataset summary:

| Metric | Value |
|--------|-------|
| Dataset | `BTX24/turkish-privacy-pii-ner` |
| Language | Turkish |
| Dataset type | Synthetic span-based NER / PII detection |
| Total rows | 103,923 |
| Training examples | 83,138 |
| Validation examples | 10,392 |
| Test examples | 10,393 |
| Label classes | 10 privacy labels + `O` |
| Annotation type | Character-level spans |
| Data type | Fully synthetic |
| Dataset license | CC BY 4.0 |

The training data is fully synthetic and contains no intentionally collected real personal information.

---

# Label Space

The fine-tuned checkpoint uses the following Turkish privacy label space:

```json
{
  "category_version": "tr_privacy_v1",
  "span_class_names": [
    "O",
    "tckn",
    "secret",
    "iban",
    "vkn",
    "account_number",
    "private_address",
    "private_date",
    "private_phone",
    "private_email",
    "private_person"
  ]
}
```

## Label Descriptions

| Label | Description |
|-------|-------------|
| `O` | Outside / non-PII token |
| `tckn` | Synthetic Turkish national identity-like values |
| `secret` | Synthetic passwords, OTPs, API-key-like strings, tokens, recovery codes |
| `iban` | Synthetic Turkish IBAN-like values |
| `vkn` | Synthetic Turkish tax identification-like values |
| `account_number` | Customer numbers, account identifiers, reference codes, membership IDs, ticket/order references |
| `private_address` | Synthetic Turkish-style address expressions |
| `private_date` | Privacy-relevant date expressions |
| `private_phone` | Turkish mobile-number-like synthetic phone numbers |
| `private_email` | Synthetic non-routable e-mail addresses |
| `private_person` | Synthetic Turkish-style person names |

---

# Training Summary

The model was fine-tuned for Turkish privacy-oriented span detection.

| Metric | Value |
|--------|-------|
| Best epoch | 3 |
| Best metric | `validation_loss` |
| Best validation loss | `0.002157915852249276` |
| Number of training examples | 83,138 |
| Number of validation examples | 10,392 |
| Span class names | 11 classes including `O` |

## Epoch Metrics

| Epoch | Train Loss | Train Token Accuracy | Validation Loss | Validation Token Accuracy |
|------:|-----------:|---------------------:|----------------:|--------------------------:|
| 1 | 0.038908 | 0.990768 | 0.003961 | 0.999100 |
| 2 | 0.002714 | 0.999463 | 0.002181 | 0.999583 |
| 3 | 0.001393 | 0.999704 | 0.002158 | 0.999641 |

The best checkpoint was selected at epoch 3 based on validation loss.

---

# Test Evaluation

Evaluation was performed on the synthetic Turkish test split.

| Metric | Value |
|--------|------:|
| Test examples | 10,393 |
| Test tokens | 241,020 |
| Eval mode | typed |
| Loss | 0.0028 |
| Token accuracy | 0.9996 |
| Inference tokens/sec | 3027.20 |

## Detection Metrics

| Metric | Value |
|--------|------:|
| Detection precision | 0.9998 |
| Detection recall | 0.9996 |
| Detection F1 | 0.9997 |
| Detection F2 | 0.9996 |
| Span precision | 0.9988 |
| Span recall | 0.9978 |
| Span F1 | 0.9983 |
| Span F2 | 0.9980 |

## Per-Class Span Metrics

| Label | Precision | Recall | F1 | F2 |
|-------|----------:|-------:|---:|---:|
| `tckn` | 1.0000 | 0.9990 | 0.9995 | 0.9992 |
| `secret` | 0.9990 | 1.0000 | 0.9995 | 0.9998 |
| `iban` | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
| `vkn` | 0.9990 | 0.9990 | 0.9990 | 0.9990 |
| `account_number` | 1.0000 | 0.9992 | 0.9996 | 0.9993 |
| `private_address` | 0.9980 | 0.9940 | 0.9960 | 0.9948 |
| `private_date` | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
| `private_phone` | 0.9991 | 1.0000 | 0.9995 | 0.9998 |
| `private_email` | 1.0000 | 0.9902 | 0.9951 | 0.9922 |
| `private_person` | 0.9928 | 0.9959 | 0.9943 | 0.9953 |

> These scores are measured on a synthetic test split. Real-world performance may differ, especially on noisy user text, OCR output, mixed-language documents, informal spelling, or domain-specific records.

---

# Intended Use

This checkpoint is intended for research and development in Turkish privacy-preserving NLP.

Recommended use cases:

- Turkish PII detection
- Turkish privacy-oriented NER
- Character-level privacy span detection
- Data redaction and masking
- Privacy-aware preprocessing pipelines
- Fine-tuning / evaluating OpenAI Privacy Filter-style models on Turkish data
- Academic NLP projects
- Controlled experiments with synthetic Turkish privacy data

---

# Out-of-Scope Use

This model should not be used as:

- A legal compliance guarantee
- A complete anonymization system by itself
- A guarantee that all sensitive information will be detected
- A replacement for human privacy review
- A production privacy safeguard without further evaluation
- A detector for real-world high-risk documents without additional domain testing

For production or high-risk use cases, evaluate the model on in-domain Turkish data and combine it with rule-based checks, human review, logging safeguards, and privacy-by-design processes.

---

# Local Usage

## 1. Install OpenAI Privacy Filter

```bash
git clone https://github.com/openai/privacy-filter.git
cd privacy-filter
pip install -e .
```

## 2. Download this checkpoint

```bash
python -c "from huggingface_hub import snapshot_download; snapshot_download(repo_id='BTX24/turkish-privacy-filter-pii', local_dir='tr_privacy_filter_pii')"
```

## 3. Run inference with OPF CLI

For CUDA:

```bash
opf --checkpoint ./tr_privacy_filter_pii --device cuda --format json "Mehmet Kaya TCKN 12345678901"
```

For CPU:

```bash
opf --checkpoint ./tr_privacy_filter_pii --device cpu --format json "Mehmet Kaya TCKN 12345678901"
```

Example Turkish inputs:

```bash
opf --checkpoint ./tr_privacy_filter_pii --device cuda --format json "Ahmet Yılmaz için telefon numarası 0532 000 00 00 olarak kaydedildi."
```

```bash
opf --checkpoint ./tr_privacy_filter_pii --device cuda --format json "İade için IBAN TR00 0000 0000 0000 0000 0000 00 bilgisi girildi."
```

```bash
opf --checkpoint ./tr_privacy_filter_pii --device cuda --format json "Doğrulama kodu OTP-482193 destek kaydına yazılmış."
```

```bash
opf --checkpoint ./tr_privacy_filter_pii --device cuda --format json "Fatura için VKN 1234567890 ve referans kodu REF-TR-000918 girildi."
```

---

# Python Download Example

```python
from huggingface_hub import snapshot_download

checkpoint_dir = snapshot_download(
    repo_id="BTX24/turkish-privacy-filter-pii",
    local_dir="tr_privacy_filter_pii",
)

print(checkpoint_dir)
```

---

# Training / Fine-tuning Notebook

This repository includes the training notebook:

```text
privacy_filter_tr_pii_colab.ipynb
```

The notebook documents the Turkish fine-tuning workflow.

It may include steps such as:

- Loading the Turkish privacy PII dataset
- Preparing the Turkish privacy label space
- Validating character-level spans
- Preparing train/validation/test files
- Running OpenAI Privacy Filter fine-tuning
- Saving model artifacts
- Testing inference examples
- Exporting checkpoint files for Hugging Face upload
- Evaluating the fine-tuned checkpoint on the synthetic test split

---

# Artifacts

Expected repository artifacts:

```text
.
├── README.md
├── config.json
├── model.safetensors
├── finetune_summary.json
├── USAGE.txt
├── label_space.json
└── privacy_filter_tr_pii_colab.ipynb
```

## Artifact Descriptions

| File | Description |
|------|-------------|
| `config.json` | Model/configuration file |
| `model.safetensors` | Fine-tuned model checkpoint weights |
| `finetune_summary.json` | Fine-tuning summary and metadata |
| `USAGE.txt` | Basic usage notes |
| `label_space.json` | Turkish privacy label space |
| `privacy_filter_tr_pii_colab.ipynb` | Training / fine-tuning notebook |

---

# Suggested Evaluation

Recommended metrics:

- Entity-level precision
- Entity-level recall
- Entity-level F1
- Typed span F1
- Untyped span F1
- Per-label F1
- Boundary error analysis
- False positive analysis
- False negative analysis

Recommended comparison baselines:

- Original `openai/privacy-filter` without Turkish fine-tuning
- Regex-based detector for structured fields such as phone, e-mail, IBAN, TCKN-like values and VKN-like values
- Turkish BERT-style NER model
- This fine-tuned Turkish Privacy Filter PII checkpoint

---

# Limitations

This checkpoint was fine-tuned on synthetic Turkish privacy data. Therefore:

- It may not fully capture noisy real-world Turkish text.
- It may overfit to synthetic templates.
- It may miss rare PII formats not represented in the dataset.
- It may produce false positives for numeric or code-like strings.
- It may struggle with long documents, OCR errors, mixed-language text, informal spelling, or domain-specific formats.
- It should be evaluated on in-domain data before production use.
- It should not be treated as a legal anonymization guarantee.

---

# Ethical Considerations

The training dataset is synthetic and was designed to avoid intentionally collecting or distributing real personal information.

However, a model trained on synthetic data can still make mistakes. It may fail to detect sensitive information or incorrectly classify non-sensitive text as PII. For sensitive applications, this model should be used as one layer in a broader privacy-preserving pipeline, not as the only safeguard.

Recommended safeguards:

- Human review for high-risk workflows
- Domain-specific evaluation
- Regex/rule-based checks for structured identifiers
- Logging and monitoring of redaction failures
- Conservative handling of uncertain predictions
- Regular evaluation on newly observed data distributions

---

# License

This fine-tuned checkpoint is released under the **Apache License 2.0**.

The base model is `openai/privacy-filter`.

The training dataset `BTX24/turkish-privacy-pii-ner` is released under **Creative Commons Attribution 4.0 International (CC BY 4.0)**.

Please review the licenses of the base model, dataset, and this fine-tuned checkpoint before use.

---

# Citation

If you use this model, please cite:

```bibtex
@model{toktay_2026_turkish_privacy_filter_pii,
  title        = {Turkish Privacy Filter PII},
  author       = {Boran Toktay},
  year         = {2026},
  publisher    = {Hugging Face},
  howpublished = {\url{https://huggingface.co/BTX24/turkish-privacy-filter-pii}},
  note         = {Fine-tuned OpenAI Privacy Filter checkpoint for Turkish PII span detection}
}
```

If you use the training dataset, please also cite:

```bibtex
@dataset{toktay_2026_turkish_privacy_pii_ner,
  title        = {Turkish Privacy PII NER Dataset},
  author       = {Boran Toktay},
  year         = {2026},
  publisher    = {Hugging Face},
  howpublished = {\url{https://huggingface.co/datasets/BTX24/turkish-privacy-pii-ner}},
  note         = {Synthetic Turkish privacy-oriented named entity recognition dataset for PII detection}
}
```

---

# Contact

For questions, issues, or suggestions, please open an issue or discussion on the model repository:

```text
BTX24/turkish-privacy-filter-pii
```