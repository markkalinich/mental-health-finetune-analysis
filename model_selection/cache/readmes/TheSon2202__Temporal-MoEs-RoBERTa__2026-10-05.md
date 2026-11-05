---
license: mit
language: en
tags:
- citd@uit-ai-team-lab
- roberta
- mixture-of-experts
- sentiment-analysis
- semeval-2026-task-2
- pytorch
base_model: cardiffnlp/twitter-roberta-base-sentiment-latest
metrics:
- pearsonr
library_name: transformers
---
# Temporal-MoEs-RoBERTa

![Transformers](https://img.shields.io/badge/Transformers-MOEs--RoBERTa-ffcc00?style=flat&logo=huggingface)
![PyTorch](https://img.shields.io/badge/Framework-PyTorch-ee4c2c?style=flat&logo=pytorch&logoColor=white)
![Task](https://img.shields.io/badge/Task-Sentiment%20Analysis-blue?style=flat&logo=python&logoColor=white)
![Language](https://img.shields.io/badge/Language-English-red?style=flat&logo=google&logoColor=white)

## You could see ideas and systems: [**👉 Paper**](https://aclanthology.org/2026.semeval-1.25/): Doi: `10.18653/v1/2026.semeval-1.25`

## Demo
[**👉 Temporal Valance and Arousal Here**](https://huggingface.co/spaces/TheSon2202/temporal-moes-roberta-sentiment): https://huggingface.co/spaces/TheSon2202/temporal-moes-roberta-sentiment

## Overview
**Temporal-MoEs-RoBERTa** is a fine-tuned model based on `cardiffnlp/twitter-roberta-base-sentiment-latest`, augmented with a **Temporal Mixture-of-Experts (MoEs)** architecture. This model was developed by the **CITD@UIT** research team for the **SemEval-2026 Task 2: Subtask 2A (State Change Detection)**.

## Architecture
The model integrates a standard RoBERTa backbone with a specialized Temporal MoE layer designed to capture sequential dependencies and state transition patterns in sentiment-labeled text data.

## Performance
Achieved **5th place** (excluding baselines) in the SemEval-2026 Subtask 2A competition.

## Training Configuration
The model was trained using the following hyperparameters:

| Parameter | Value |
| :--- | :--- |
| Learning Rate | 2e-5 |
| Batch Size | 16 |
| Epochs | 8 |
| Weight Decay | 0.08 |
| LR Scheduler | Cosine |
| Warmup Ratio | 0.1 |
| Optimizer | AdamW (Torch) |
| Max Sequence Length | 512 |
|N_Expert | 4 |

## SemEval-2026 Subtask 2A Official Ranking
Our model, **Temporal-MoEs-RoBERTa**, Top 6 results extracted from the official leaderboard:

| Rank | Team | Valence (r) | Arousal (r) | V&A Average |
| :--- | :--- | :---: | :---: | :---: |
| 1 | UKP_Psycontrol | 0.675 | 0.683 | 0.679 |
| 2 | YNU | 0.692 | 0.647 | 0.669 |
| 3 | UAlberta | 0.615 | 0.674 | 0.645 |
| 4 | Ajman University | 0.615 | 0.670 | 0.642 |
| **5** | **CITD@UIT*** | **0.629** | **0.633** | **0.631** |
| 6 | CSIRO-LT | 0.621 | 0.477 | 0.549 |

<div align="center">
  <img src="https://cdn-uploads.huggingface.co/production/uploads/68c7b25941cddd7ea63d8e89/czgnnalUGGXWy95AbTJb2.png" alt="Training Analysis" width="1200"/>
</div>
*Note: The model achieved its best performance based on the `avg_r` metric, as logged during the training process.*

## Reproducibility
Code and training pipeline:
https://github.com/PTSown0222/SemEval-2026-Task-2

Model Weights:
https://huggingface.co/TheSon2202/Temporal-MoEs-RoBERTa

## Acknowledgments
We would like to thank **Poli** from the Hugging Face team for their valuable support in creating and transferring the interactive demo space for this model.

## Citation
If you use this model or our approach, please cite our paper:
```bibtex
@inproceedings{phuong-etal-2026-citd,
    title = "{CITD}@{UIT} at {S}em{E}val-2026 Task 2: Temporal Mixture-of-Experts for Longitudinal Valence and Arousal Prediction from Ecological Essays",
    author = "Phuong, Son The  and
      Ngo, My Thuy-Tra  and
      Minh Dao, Tri  and
      Nguyen, Duc-Vu",
    editor = "Kochmar, Ekaterina  and
      Ghosh, Debanjan  and
      North, Kai  and
      Komachi, Mamoru",
    booktitle = "Proceedings of the 20th {I}nternational {W}orkshop on {S}emantic {E}valuation (2026)",
    month = jul,
    year = "2026",
    address = "San Diego, California, USA",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2026.semeval-1.25/",
    doi = "10.18653/v1/2026.semeval-1.25",
    pages = "167--175",
    ISBN = "979-8-89176-414-9",
    abstract = "This paper describes our participation in SemEval-2026 Task 2, which focuses on the longitudinal assessment and forecasting of emotional states through text. The challenge is divided into two primary objectives: Subtask1, which requires estimating continuous Valence and Arousal (V{\&}A) scores for a sequence of texts, and Subtask2, which focuses on forecasting future emotional variations, specifically State Change (2A) and Dispositional Change (2B). To address these tasks, we propose a unified framework based on cardiffnlp/twitter-roberta-base-sentiment-latest, a transformer architecture pretrained on 124 million tweets. For all subtasks, we sort the data chronologically by userid and use a sliding window approach to capture longitudinal context. We conduct extensive experiments combining this pretrained RoBERTa model with Multilayer Perceptron (MLP) and Mixture-of-Experts (MoE) architectures to optimize performance. Furthermore, we utilize both attention pooling and mean pooling on all output hidden state representations to extract richer semantic features. Our proposed system demonstrated competitive performance, officially ranking 9th in Subtask 1 and 5th in Subtask 2A among participating teams."
}
```