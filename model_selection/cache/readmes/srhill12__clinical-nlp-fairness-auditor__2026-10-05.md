---
language: en
license: apache-2.0
tags:
  - text-classification
  - clinical-nlp
  - medical
  - fairness-audit
  - distilbert
  - governance
datasets:
  - galileo-ai/medical_transcription_40
metrics:
  - accuracy
  - f1
---

# Clinical NLP Fairness Auditor — DistilBERT Medical Specialty Classifier

**Author:** Steven Hill  
**Date:** 2026-04-24  
**Base model:** distilbert-base-uncased  
**Task:** Multi-class text classification (20 medical specialties)  
**Project:** Clinical NLP Fairness Auditor — AI governance portfolio project

---

## Model Description

This model fine-tunes DistilBERT on the MTSamples clinical transcription dataset
to classify medical notes by specialty. It is developed as part of a portfolio
project demonstrating responsible AI practices including fairness auditing,
SHAP explainability, and NIST AI RMF governance documentation.

**This model is NOT intended for clinical use.** It is a research and
demonstration artifact only.

---

## Intended Use

### Intended uses
- Research and educational demonstration of clinical NLP
- Portfolio demonstration of AI fairness auditing methodology
- Teaching tool for AI governance practices in healthcare contexts

### Out-of-scope uses
- Clinical diagnosis or treatment recommendations
- Autonomous patient care decisions
- Production deployment without further development and independent audit
- Any use involving real patient data without appropriate IRB approval and de-identification

---

## Training Data

- **Dataset:** MTSamples (via galileo-ai/medical_transcription_40 on HuggingFace Hub)
- **Source:** Public medical transcription examples from mtsamples.com
- **Size:** 4,087 notes after filtering (≥50 examples per specialty)
- **Split:** 70% train / 15% validation / 15% test (stratified)
- **Classes:** 20 medical specialties:

- Cardiovascular / Pulmonary
- Consult - History and Phy.
- Discharge Summary
- ENT - Otolaryngology
- Emergency Room Reports
- Gastroenterology
- General Medicine
- Hematology - Oncology
- Nephrology
- Neurology
- Neurosurgery
- Obstetrics / Gynecology
- Ophthalmology
- Orthopedic
- Pain Management
- Pediatrics - Neonatal
- Radiology
- SOAP / Chart / Progress Notes
- Surgery
- Urology

### Data limitations
- Not drawn from live EHR systems — may not generalize to real clinical workflows
- No patient demographic information — demographic fairness audit not possible
- Class imbalance: Surgery accounts for ~24% of training data
- 20.7% of notes truncated at 512 tokens — longer notes systematically disadvantaged

---

## Training Procedure

- **Base model:** distilbert-base-uncased
- **Framework:** HuggingFace Transformers, PyTorch
- **Epochs:** 3
- **Batch size:** 16
- **Learning rate:** 2e-5 with warmup ratio 0.1
- **Imbalance mitigation:** Inverse-frequency class weights applied to cross-entropy loss
- **Hardware:** NVIDIA T4 GPU (Google Colab)
- **Training time:** ~157 seconds

---

## Evaluation Results

### Overall performance (held-out test set, n=614)

| Metric | Value |
|---|---|
| Accuracy | 0.4186 |
| Macro F1 | 0.4407 |

### Per-class performance

```
                               precision    recall  f1-score   support

   Cardiovascular / Pulmonary      0.544     0.740     0.627        50
   Consult - History and Phy.      0.417     0.072     0.123        69
            Discharge Summary      0.636     0.933     0.757        15
         ENT - Otolaryngology      0.310     0.750     0.439        12
       Emergency Room Reports      0.095     0.700     0.167        10
             Gastroenterology      0.432     0.533     0.478        30
             General Medicine      0.258     0.229     0.242        35
        Hematology - Oncology      0.000     0.000     0.000        12
                   Nephrology      0.381     0.727     0.500        11
                    Neurology      0.436     0.567     0.493        30
                 Neurosurgery      0.393     0.846     0.537        13
      Obstetrics / Gynecology      0.425     0.850     0.567        20
                Ophthalmology      0.435     0.909     0.588        11
                   Orthopedic      0.415     0.562     0.478        48
              Pain Management      0.875     0.875     0.875         8
        Pediatrics - Neonatal      0.000     0.000     0.000         9
                    Radiology      0.444     0.526     0.482        38
SOAP / Chart / Progress Notes      0.737     0.609     0.667        23
                      Surgery      0.619     0.088     0.154       148
                      Urology      0.548     0.773     0.642        22

                     accuracy                          0.419       614
                    macro avg      0.420     0.564     0.441       614
                 weighted avg      0.476     0.419     0.369       614

```

### Subgroup fairness analysis

| Subgroup dimension | Disparity (max - min accuracy) |
|---|---|
| Across 20 specialties | 0.9333 |
| Across specialty types (procedural/consultative/diagnostic) | 0.3405 |
| Across note length quartiles | 0.323 |

---

## Fairness and Bias Findings

### Critical findings (DO NOT DEPLOY without remediation)

Zero-F1 specialties — model completely fails to identify these note types:
- Pediatrics - Neonatal
- Hematology - Oncology

### High-risk findings (FNR ≥ 70% — model systematically misses these specialties)

- Pediatrics - Neonatal
- Hematology - Oncology
- Consult - History and Phy.
- Surgery
- General Medicine

### Root cause analysis

1. **Class imbalance:** Surgery dominates training data (24%), causing the model
   to over-predict high-frequency specialties
2. **Class weighting over-correction:** Inverse-frequency weighting reduced Surgery
   recall to 8.8% — a new disparity created by the mitigation attempt
3. **Truncation:** 20.7% of notes exceed 512 tokens; Q3 length quartile accuracy
   (0.261) is 32 points below Q1 (0.584)
4. **Vocabulary overlap:** Surgery misclassifications scatter across 9 specialties,
   indicating shared procedural vocabulary confuses the model

---

## Explainability

SHAP PartitionExplainer was applied to 4 representative examples to generate
token-level attribution scores. Key finding: the model attends to clinically
meaningful vocabulary (procedure names, anatomical terms) for correct predictions,
but relies on shared procedural language when making misclassifications.

Explainability artifacts: token attribution plots for correct prediction,
incorrect prediction, zero-F1 class, and best-performing class.

---

## Governance Documentation

This model was developed in alignment with the NIST AI Risk Management Framework
(AI RMF 1.0, January 2023). A full NIST AI RMF scorecard is available in the
project repository covering all four functions: GOVERN, MAP, MEASURE, and MANAGE.

**Deployment recommendation:** DO NOT DEPLOY in production without addressing
critical risk items identified in the bias audit. See nist_rmf_scorecard.md
for full findings and recommended mitigations.

---

## Citation

```
@misc{hill2025clinicalnlp,
  author = {Hill, Steven},
  title = {Clinical NLP Fairness Auditor},
  year = {2025},
  note = {AI governance portfolio project. NIST AI RMF aligned.}
}
```
**GitHub repository:** https://github.com/srhill12/clinical-nlp-fairness-auditor
---

## Ethical Considerations

This model was built explicitly to demonstrate responsible AI development practices,
not to be deployed. The fairness audit intentionally surfaces failure modes rather
than optimizing headline accuracy. The governance documentation is intended to model
the kind of transparency that healthcare AI systems should provide before deployment.

The absence of demographic data in the training set is itself documented as a
governance gap — a model that cannot be evaluated for demographic fairness should
not be deployed in healthcare settings without remediation.
