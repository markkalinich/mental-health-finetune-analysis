---
license: apache-2.0
base_model: distilbert-base-uncased
tags:
- text-classification
- emotion-detection
- mlops
datasets:
- dair-ai/emotion
metrics:
- accuracy
pipeline_tag: text-classification
---

# DistilBERT for Emotion Classification (IIT Jodhpur MLOps Group 14)

This model is a fine-tuned version of `distilbert-base-uncased` trained on the `dair-ai/emotion` dataset. It was developed as part of an end-to-end MLOps pipeline assignment to classify text into six core emotions: sadness, joy, love, anger, fear, and surprise.

## 📊 Experimentation Summary
We conducted multiple tracking experiments logged via Weights & Biases to discover the optimal hyperparameters:

| Experiment Version | Learning Rate | Epochs | Weight Decay | Eval Accuracy | Status |
|---|---|---|---|---|---|
| Experiment 1 (Baseline) | 2e-5 | 3 | 0.01 | 90.4% | Deprecated |
| **Experiment 2 (Tuned)** | **5e-5** | **4** | **0.05** | **93.7%** | **Production Candidate** |

## 🛠️ Training Hyperparameters
The winning model (this checkpoint) was trained with the following configurations:
- **Learning Rate:** 5e-5
- **Train Batch Size:** 16
- **Eval Batch Size:** 16
- **Epochs:** 4
- **Weight Decay:** 0.05
- **Optimizer:** AdamW

## 📈 Evaluation Results
The model achieved a final validation accuracy of **93.7%**, demonstrating robust convergence and strong generalization across all 6 emotional categories.

## 🧪 Tracked with Weights & Biases
All training runs, real-time gradients, and validation loops were monitored transparently. You can inspect our charts under the project workspace: `mlops-emotion-classification`.