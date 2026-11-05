---
library_name: transformers
language:
- ar
base_model:
- AymanElbery/arabic-medical-classifier-arabertv2
---

# ArabicMedicalBERT-QA-82 - Arabic Medical Q&A Classifier

Finetuned model based on https://huggingface.co/AymanElbery/arabic-medical-classifier-arabertv2

Trained on data from https://www.kaggle.com/competitions/eacl-2026-abjad-nlp-shared-task-medical-text-classification-in-arabic/

# Classes

| ID | Category | ID | Category | ID | Category |
|----|----------|----|----------|----|----------|
| 0 | Addiction | 28 | Genetics | 56 | Pathology |
| 1 | Allergy | 29 | Geriatric health | 57 | Pediatric diseases |
| 2 | Alternative medicine | 30 | Gynecologic surgery | 58 | Pediatric surgery |
| 3 | Anatomy | 31 | Gynecological diseases | 59 | Pharmacology |
| 4 | Anesthesiology | 32 | Health and sports | 60 | Physiology |
| 5 | Benign and malignant tumors | 33 | Hematological diseases | 61 | Physiotherapy |
| 6 | Biochemistry | 34 | History of medicine | 62 | Plastic surgery |
| 7 | Biology | 35 | Hormones | 63 | Pregnancy and childbirth |
| 8 | Cardiothoracic surgery | 36 | Hypertension | 64 | Preventive medicine |
| 9 | Cardiovascular diseases | 37 | Immunology | 65 | Psychiatric diseases |
| 10 | Chemistry | 38 | In vitro fertilization (IVF) | 66 | Psychology |
| 11 | Child health | 39 | Infectious diseases | 67 | Public health |
| 12 | Congenital malformations | 40 | Infertility | 68 | Radiology |
| 13 | Dental diseases | 41 | Internal medicine diseases | 69 | Ramadan |
| 14 | Dental health | 42 | Jaw and dental surgery | 70 | Respiratory diseases |
| 15 | Dentistry | 43 | Laboratory | 71 | Rheumatic diseases |
| 16 | Dermatological diseases | 44 | Medical services | 72 | Sexual health |
| 17 | Diabetes | 45 | Medicinal herbs | 73 | Sexually transmitted diseases |
| 18 | Diagnosis | 46 | Men's health | 74 | Skin and beauty |
| 19 | Ear, nose, and throat (ENT) | 47 | Mental health | 75 | Toxicology |
| 20 | Embryology | 48 | Microbiology | 76 | Urogenital diseases |
| 21 | Endocrine diseases | 49 | Musculoskeletal and joint diseases | 77 | Urological surgery |
| 22 | Eye diseases | 50 | Neurological diseases | 78 | Vaccines and immunizations |
| 23 | First aid | 51 | Neurosurgery | 79 | Vascular surgery |
| 24 | Gastrointestinal diseases | 52 | Nutrition | 80 | Vitamins and minerals |
| 25 | General medicine | 53 | Optometry | 81 | Women's health |
| 26 | General surgery | 54 | Oral diseases |  |  |
| 27 | Genetic diseases | 55 | Orthopedic surgery |  |  |

# Paper


```
@inproceedings{shanshin-2026-arabicmedicalbert,
    title     = {{ArabicMedicalBERT-QA-82 at AbjadMed: Fighting Class Imbalance in Arabic Medical Text Classification}},
    author    = {Shanshin, Gleb},
    booktitle = "Proceedings of the 2nd Workshop on {NLP} for Languages Using {A}rabic Script",
    month = mar,
    year = "2026",
    address = "Rabat, Morocco",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2026.abjadnlp-1.15/",
    pages = "115--119"
}
```