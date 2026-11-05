---
language:
- en
base_model:
- knowledgator/modern-gliner-bi-large-v1.0
pipeline_tag: token-classification
tags:
- india
- medicine
- psychiatry
- deidentification
license: mit
---
# 🩺 lekhansh/modern-gliner-large-mednotes-deidentifier

## 🔍 Model Summary

This is a fine-tuned version of [`knowledgator/modern-gliner-bi-large-v1.0`](https://huggingface.co/knowledgator/modern-gliner-bi-large-v1.0), tailored for **fine-grained de-identification** of real-world medical notes. It performs robustly on noisy, informal clinical text containing misspellings, abbreviations, and shorthand.

- **Base model**: `modern-gliner-bi-large-v1.0`
- **Fine-tuned on**: 1,045 human-annotated medical records; validation on 386.
- **F1 Score (baseline)**: 0.06  
- **F1 Score (post fine-tuning)**: 0.998

---

## 🏷️ Entity Labels

The model recognizes the following sensitive entity types:

- `person`: HCW, patient or others. Does not capture salutations without names.
- `address`: Geogrophical entity smaller than a state: cities, districts, taluqs, landmarks and locations within them.
- `address state`: Indian states and UTs, including misspellings and abbreviations.
- `address country`
- `identification number`: Any numeric or alphanumeric identifier
- `dates`: Only fully specified dates or date ranges that can compromise privacy. 'Jan 2020' is not caught but '03/01/2020' is.
- `languages`
- `groups`: Religion, tribal, political groups that can reveal identity.
- `company`: Named places of occupation or health care facilities.

> ⚠️ Classification between address types (`address`, `address state`, `address country`) has sub-0.9 accuracy. Treat all address-like entities as sensitive in downstream processing.

---

## 💡 Intended Use

**Primary use**: De-identification of free-text clinical notes in electronic health records (EHRs)  
**Not evaluated for**:
- Zero-shot performance on other domains/tasks. Since recall ratio was 0, there will be catastrophic forgetting.
- Multilingual or domain transfer scenarios

---

## ⚠️ Limitations and Disclaimer

> ⚠️ **DISCLAIMER: HUMAN OVERSIGHT REQUIRED**  
> This model **must not** be used as a standalone anonymization tool.  
> Despite high validation performance, errors may still occur—especially with rare entity forms, nested entities, or previously unseen abbreviations. Always include a human audit step before using de-identified records in research or production.

---

## 🔓 License

Released under a **MIT**. See repository for terms.

---

## 📚 Citation
```bibtex
@misc{lekhansh2025deidentifier,
title = {Fine-grained Automatic Removal of Personal Identifiers from Medical Records},
author = {Lekhansh Shukla, Prakrithi Shivaprakash},
year = {2025},
note = {Fine-tuned on real-world annotated records for clinical PII removal},
url = {https://huggingface.co/lekhansh/modern-gliner-large-mednotes-deidentifier}
}
```