---
language: ar
license: mit
library_name: transformers
tags:
- text-classification
- arabic
- mental-health
- arabert
pipeline_tag: text-classification
datasets:
- AraHealthQA
metrics:
- f1
base_model:
- aubmindlab/bert-base-arabertv2
---

# Sakinah-AI: Optimized AraBERT for Arabic Mental Health Question Classification

<p align="center">
  <img src="https://placehold.co/1200x300/e0f2fe/0891b2?text=Sakinah-AI+at+MentalQA+2025" alt="Sakinah-AI Project Banner">
</p>

This repository contains the official fine-tuned model **Sakinah-AI-AraBERT-Optimized**, one of our submissions to the **[MentalQA 2025 Shared Task (Track 1)](https://sites.google.com/view/mentalqa-2025/home)**.

#### By: [Fatimah Emad Elden](https://scholar.google.com/citations?user=CfX6eA8AAAAJ&hl=ar) & [Mumina Abukar](https://www.linkedin.com/in/dr-mumina-alshaikh-md-mscph-501621216/)
#### *Cairo University & The University of South Wales*

[![Paper](https://img.shields.io/badge/arXiv-25XX.XXXXX-b31b1b.svg)](https://arxiv.org/abs/25XX.XXXXX)
[![Code](https://img.shields.io/badge/GitHub-Code-blue)](https://github.com/astral-fate/MentalQA2025/)
[![HuggingFace Collection](https://img.shields.io/badge/🤗-HuggingFace%20Collection-yellow)](https://huggingface.co/collections/FatimahEmadEldin/sakinah-ai-at-mentalqa-689b2d707791cea458e97aaf/)
[![License](https://img.shields.io/badge/License-MIT-lightgrey)](https://github.com/astral-fate/mentalqa2025/blob/main/LICENSE)

---

## 📖 Model Description

This model is a fine-tuned version of `aubmindlab/bert-base-arabertv2` for multi-label classification of Arabic questions related to mental health. It was trained on the `AraHealthQA` dataset.

Our approach involved a comprehensive hyperparameter search using the **Optuna** framework to find the optimal configuration. To address class imbalance, the model was trained using a custom **Focal Loss** function. This optimized fine-tuning approach significantly outperformed its k-fold ensemble counterpart. On the official blind test set, this model achieved a **Weighted F1-score of 0.543**.

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

```python
from transformers import pipeline

# Load the classification pipeline
classifier = pipeline(
    "text-classification",
    model="FatimahEmadEldin/Sakinah-AI-AraBERT-Optimized",
    return_all_scores=True # Set to True for multi-label output
)

# Example question in Arabic
question = "ما هي أعراض الاكتئاب وكيف يمكن علاجه؟"
# (Translation: "What are the symptoms of depression and how can it be treated?")

results = classifier(question)

# --- Post-processing to get final labels ---
# The optimal threshold must be determined from your Optuna study results.
# The evaluation script uses a placeholder of 0.45.
# Replace with the actual best_params['base_threshold'] value.
threshold = 0.45 
predicted_labels = [item['label'] for item in results[0] if item['score'] > threshold]

print(f"Question: {question}")
# Expected output for this example would likely include 'Diagnosis' and 'Treatment'
print(f"Predicted Labels: {predicted_labels}")
# Expected: ['A', 'B']

````

## ⚙️ Training Procedure

This model was fine-tuned using a rigorous hyperparameter optimization process.

### Hyperparameters

The best hyperparameters were found by Optuna during the training process (`arabert_optmized.py`). You will need to retrieve these values from the output of your Optuna study (`study.best_params`).

Of course\! Here is the information formatted into Markdown tables.

### Optimization Results

| Metric              | Value  |
| ------------------- | ------ |
| Best trial F1 Score | 0.6307 |


### Best Hyperparameters Found

| Hyperparameter     | Value                     |
| ------------------ | ------------------------- |
| learning\_rate     | 5.273957732715589e-05     |
| num\_train\_epochs | 13                        |
| weight\_decay      | 0.04131058607286182       |
| focal\_alpha       | 0.9702303056621574        |
| focal\_gamma       | 1.39543909126709          |
| base\_threshold    | 0.20408644287720523       |

### Frameworks

  * PyTorch
  * Hugging Face Transformers
  * Optuna

### 📊 Evaluation Results

The model was evaluated on the blind test set provided by the MentalQA organizers.

#### Final Test Set Scores

| Metric | Score |
| :--- | :--- |
| Weighted F1-Score | 0.543 |

#### Per-Label Performance (Test Set)

**Note:** The following is a placeholder. To generate the actual report, run the `arabert_evaluate.py` script with your final model and the official test data.

```
--- Per-Label Performance (Test Set) ---
              precision    recall  f1-score   support

           A       0.65      0.81      0.72        84
           B       0.60      0.75      0.67        85
           C       0.00      0.00      0.00        10
           D       0.37      0.21      0.26        34
           E       0.41      0.37      0.39        38
           F       0.00      0.00      0.00         6
           Z       0.00      0.00      0.00         3

   micro avg       0.58      0.59      0.58       260
   macro avg       0.29      0.31      0.29       260
weighted avg       0.51      0.59      0.54       260
 samples avg       0.65      0.65      0.60       260


```

## 📜 Citation

If you use our work, please cite our paper:

```bibtex
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
