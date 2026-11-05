---
language:
  - en
license: mit
library_name: transformers
tags:
  - text-classification
  - safety
  - jailbreak-detection
  - prompt-injection
  - content-moderation
  - distilbert
datasets:
  - SalKhan12/prompt-safety-dataset
  - TrustAIRLab/in-the-wild-jailbreak-prompts
  - allenai/wildguardmix
  - allenai/wildjailbreak
pipeline_tag: text-classification
model-index:
  - name: prompt-safety-bert
    results:
      - task:
          type: text-classification
          name: Prompt Safety Classification
        metrics:
          - type: f1
            value: 0.96
            name: F1
---

# 🛡️ Prompt Safety BERT

A fine-tuned DistilBERT model for **safe/unsafe prompt classification**.
