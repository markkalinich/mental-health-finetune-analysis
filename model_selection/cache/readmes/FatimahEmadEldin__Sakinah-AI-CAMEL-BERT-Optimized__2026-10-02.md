---
language: ar
license: mit
library_name: transformers
tags:
- text-classification
- arabic
- mental-health
- camelbert
pipeline_tag: text-classification
datasets:
- AraHealthQA
metrics:
- f1
base_model:
- CAMeL-Lab/bert-base-arabic-camelbert-da-sentiment
---

# Sakinah-AI: Optimized CAMeL-BERT for Arabic Mental Health Question Classification

<p align="center">
  <img src="https://placehold.co/1200x300/dbeafe/3b82f6?text=Sakinah-AI+at+MentalQA+2025" alt="Sakinah-AI Project Banner">
</p>

This repository contains the official fine-tuned model **Sakinah-AI-CAMEL-BERT-Optimized**, our submission to the **[MentalQA 2025 Shared Task (Track 1)](https://sites.google.com/view/mentalqa-2025/home)**.

#### By: [Fatimah Emad Elden](https://scholar.google.com/citations?user=CfX6eA8AAAAJ&hl=ar) & [Mumina Abukar](https://www.linkedin.com/in/dr-mumina-alshaikh-md-mscph-501621216/)
#### *Cairo University & The University of South Wales*

[![Paper](https://img.shields.io/badge/arXiv-25XX.XXXXX-b31b1b.svg)](https://arxiv.org/abs/25XX.XXXXX)
[![Code](https://img.shields.io/badge/GitHub-Code-blue)](https://github.com/astral-fate/MentalQA2025/)
[![HuggingFace Collection](https://img.shields.io/badge/🤗-HuggingFace%20Collection-yellow)](https://huggingface.co/collections/FatimahEmadEldin/sakinah-ai-at-mentalqa-689b2d707791cea458e97aaf/)
[![License](https://img.shields.io/badge/License-MIT-lightgrey)](https://github.com/astral-fate/mentalqa2025/blob/main/LICENSE)

---

##  Model Description

This model is a fine-tuned version of `CAMeL-Lab/bert-base-arabic-camelbert-mix-sentiment` for multi-label classification of Arabic questions related to mental health. It was trained on the `AraHealthQA` dataset.

Our approach involved a comprehensive hyperparameter search using the **Optuna** framework to find the optimal configuration. To address the inherent class imbalance in the dataset, the model was trained using a custom **Focal Loss** function. This strategy proved highly effective, making this model our best-performing fine-tuned system, achieving a **Weighted F1-score of 0.597** on the official blind test set.

The model predicts one or more of the following labels for a given question:

* **A**: Diagnosis (Interpreting symptoms)
* **B**: Treatment (Seeking therapies or medications)
* **C**: Anatomy and Physiology (Basic medical knowledge)
* **D**: Epidemiology (Course, prognosis, causes of diseases)
* **E**: Healthy Lifestyle (Diet, exercise, mood control)
* **F**: Provider Choices (Recommendations for doctors)
* **Z**: Other (Does not fit other categories)

---

## 🚀 How to Use

You can use this model directly with the `transformers` library pipeline for `text-classification`.

```
from transformers import pipeline

# Load the classification pipeline
classifier = pipeline(
    "text-classification",
    model="FatimahEmadEldin/Sakinah-AI-CAMEL-BERT-Optimized",
    return_all_scores=True # Set to True for multi-label output
)

# Example question in Arabic
question = "ما هي أعراض الاكتئاب وكيف يمكن علاجه؟"
# (Translation: "What are the symptoms of depression and how can it be treated?")

results = classifier(question)

# --- Post-processing to get final labels ---
# The optimal threshold found during tuning was ~0.25
threshold = 0.246
predicted_labels = [item['label'] for item in results[0] if item['score'] > threshold]

print(f"Question: {question}")
# Expected output for this example would likely include 'Diagnosis' and 'Treatment'
print(f"Predicted Labels: {predicted_labels}")
# [['A', 'B']]

```

# ⚙️ Training Procedure
This model was fine-tuned using a rigorous hyperparameter optimization process.

# Hyperparameters
The best hyperparameters found by Optuna and used for this model are:


| Hyperparameter | Value |
| :--- | :--- |
| learning\_rate | 6.416e-05 |
| num\_train\_epochs | 14 |
| weight\_decay | 0.0480 |
| focal\_alpha | 1.2320 |
| focal\_gamma | 2.6240 |
| base\_threshold | 0.2462 |

### Frameworks

* PyTorch
* Hugging Face Transformers
* Optuna

### 📊 Evaluation Results

The model was evaluated on the blind test set provided by the MentalQA organizers.

#### Final Test Set Scores

| Metric | Score |
| :--- | :--- |
| Weighted F1-Score | 0.5972 |
| Jaccard Score | 0.4502 |


# Per-Label Performance (Test Set)



```
              precision    recall  f1-score   support
           A       0.61      0.96      0.75        84
           B       0.56      0.98      0.72        85
           C       0.14      0.40      0.21        10
           D       0.25      0.91      0.39        34
           E       0.34      0.53      0.41        38
           F       0.07      0.33      0.11         6
           Z       0.00      0.00      0.00         3

   micro avg       0.42      0.85      0.57       260
   macro avg       0.28      0.59      0.37       260
weighted avg       0.47      0.85      0.60       260
 samples avg       0.44      0.88      0.56       260


```
# 📜 Citation
If you use our work, please cite our paper:


```
@inproceedings{elden2025sakinahai,
    title={{Sakinah-AI at MentalQA: A Comparative Study of Few-Shot, Optimized, and Ensemble Methods for Arabic Mental Health Question Classification}},
    author={Elden, Fatimah Emad and Abukar, Mumina},
    year={2025},
    booktitle={Proceedings of the MentalQA 2025 Shared Task},
    eprint={25XX.XXXXX},
    archivePrefix={arXiv},
    primaryClass={cs.CL}
}

```