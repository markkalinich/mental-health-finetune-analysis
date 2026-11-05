---
language: en
license: mit
library_name: transformers
pipeline_tag: summarization
base_model: facebook/bart-base
base_model_relation: finetune
tags:
  - summarization
  - radiology
  - medical
  - bart
  - healthcare
metrics:
  - rouge
model-index:
  - name: radiology-expression-summarizer
    results:
      - task:
          type: summarization
          name: Radiology Report Summarization
        dataset:
          type: openi
          name: Open-i NLMCXR (Indiana University Chest X-ray)
        metrics:
          - type: rouge
            value: 0.5174
            name: ROUGE-1 F1
          - type: rouge
            value: 0.3881
            name: ROUGE-2 F1
          - type: rouge
            value: 0.5092
            name: ROUGE-L F1
---