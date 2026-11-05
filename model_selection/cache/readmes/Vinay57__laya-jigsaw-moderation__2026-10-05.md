---
license: apache-2.0
base_model: convaiinnovations/laya
tags: [laya, toxicity, moderation, calibrated-decisions, wise-ft]
---
# Laya for toxic comment moderation (Jigsaw)

Answers 6 yes/no questions per comment (toxic, severe_toxic, obscene, threat, insult, identity_hate) with calibrated probabilities.
Fine-tuned on 12k balanced Jigsaw comments, then weight-merged with the base model (WiSE-FT, 50% fine-tuned; mix chosen on validation only).

| Model | Mean ROC-AUC, full Jigsaw test set (63,978 comments) |
|---|---|
| **This model** | **0.9853** |
| Detoxify original | 0.9863 |
| TF-IDF + logistic regression | 0.9786 |

ECE 0.0223 · ~18 comments/sec on one T4 · $0/request self-hosted.
