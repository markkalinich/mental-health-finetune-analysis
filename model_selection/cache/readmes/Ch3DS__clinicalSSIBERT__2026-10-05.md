---
language:
  - en
license: apache-2.0
base_model: emilyalsentzer/Bio_ClinicalBERT
tags:
  - medical
  - clinical
  - ssi
  - classification
  - surveillance
metrics:
  - accuracy
  - f1
  - precision
  - recall
model-index:
  - name: clinicalSSIBERT
    results:
      - task:
          type: text-classification
          name: SSI Detection
        dataset:
          name: Synthetic UK NHS Clinical Notes
          type: synthetic
          split: test
        metrics:
          - name: Accuracy
            type: accuracy
            value: 1.0
          - name: F1
            type: f1
            value: 1.0
---

# Model Card for Ch3DS/clinicalSSIBERT

## Model Details

### Model Description

This model is a fine-tuned version of [Bio_ClinicalBERT](https://huggingface.co/emilyalsentzer/Bio_ClinicalBERT) designed for the surveillance of **Surgical Site Infections (SSI)** in postoperative clinical notes. It is specifically tailored to **UK NHS terminology**, covering specialties such as Orthopaedics, General Surgery (GI), and Obstetrics (C-sections).

- **Developed by:** Daryn Sutton
- **Model type:** Text Classification (BERT)
- **Language(s) (NLP):** English
- **License:** Apache 2.0
- **Finetuned from model:** [emilyalsentzer/Bio_ClinicalBERT](https://huggingface.co/emilyalsentzer/Bio_ClinicalBERT)
- **Repository:** [https://huggingface.co/Ch3DS/clinicalSSIBERT](https://huggingface.co/Ch3DS/clinicalSSIBERT)

### Uses

#### Direct Use

This model is intended for use in clinical natural language processing (NLP) pipelines to automatically flag postoperative notes that indicate a potential Surgical Site Infection. It classifies notes into:

- **0 (Routine)**: Normal healing, no signs of infection.
- **1 (Infection)**: Signs of SSI (e.g., purulent discharge, erythema, antibiotic escalation).

It is particularly effective for notes containing UK-specific medical abbreviations and terminology (e.g., "Lap. Chole.", "THR", "Co-amoxiclav", "SHO review").

#### Out-of-Scope Use

- **Diagnosis**: This model is a surveillance tool and should **not** be used to make clinical diagnoses without human verification.
- **Non-UK Contexts**: Performance may vary on clinical notes from other healthcare systems with different terminology or documentation styles.

### Bias, Risks, and Limitations

- **Synthetic Data**: The model was trained on a large synthetic dataset. While designed to be realistic, it may not capture the full "messiness" or ambiguity of real-world clinical data.
- **False Negatives**: There is a risk of missing subtle infections that do not use standard keywords.
- **Bias**: The synthetic data generation process may have introduced biases based on the templates used.

### Recommendations

Users should validate the model on their own local clinical data before deploying it for active surveillance. It is recommended to use this model as a "first pass" filter to prioritize cases for manual review by Infection Prevention and Control (IPC) teams.

## How to Get Started with the Model

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

model_name = "Ch3DS/clinicalSSIBERT"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

text = "Day 5 post THR. Wound red and oozing pus. Patient pyrexial. Plan: Start Flucloxacillin."
inputs = tokenizer(text, return_tensors="pt")

with torch.no_grad():
    logits = model(**inputs).logits
    predicted_class_id = logits.argmax().item()

labels = ["Routine", "Infection"]
print(f"Prediction: {labels[predicted_class_id]}")
```

## Training Details

### Training Data

The model was trained on **5 million synthetic clinical notes** generated to mimic UK NHS postoperative records. The data covers:

- **Procedures**: Total Hip/Knee Replacement, C-Section, Cholecystectomy, Hernia Repair, etc.
- **Terminology**: UK-specific staff titles (Reg, SHO, FY1), antibiotics (Co-amoxiclav, Teicoplanin), and wound descriptions.
- **Balance**: Approximately 5% infection rate.

### Training Procedure

#### Training Hyperparameters

- **Epochs**: 3
- **Batch Size**: 64 (per device) with Gradient Accumulation of 4
- **Learning Rate**: 2e-5
- **Precision**: Mixed Precision (FP16)
- **Optimizer**: AdamW

#### Hardware

- **GPU**: NVIDIA GeForce RTX 5070 Ti

## Evaluation

### Testing Data, Factors & Metrics

The model was evaluated on a held-out test set of 100,000 synthetic records.

### Results

| Metric        | Value |
| :------------ | :---- |
| **Accuracy**  | 100%  |
| **Precision** | 1.0   |
| **Recall**    | 1.0   |
| **F1-Score**  | 1.0   |

_Note: The perfect scores reflect the synthetic nature of the test data, which follows the same distribution as the training data. Real-world performance is expected to be lower and requires further validation._

## Environmental Impact

- **Hardware Type**: NVIDIA GeForce RTX 5070 Ti
- **Hours used**: ~2 hours
- **Carbon Emitted**: Negligible (local training)

## Model Card Contact

**Daryn Sutton**  
Email: darynsutton@hotmail.com  
GitHub: [Ch3w3y](https://github.com/Ch3w3y)
