---
language:
  - en
library_name: transformers
license: mit
pipeline_tag: text-classification
tags:
  - text-classification
  - prompt-injection-detection
  - jailbreak-detection
  - security
datasets:
  - dmilush/shieldlm-prompt-injection
  - antijection/prompt-injection-dataset-v1
  - leolee99/NotInject
base_model: distilbert-base-uncased
---

# distilbert-prompt-guard-4class

This is a 4-class DistilBERT classifier fine-tuned for:
- benign
- prompt_injection
- jailbreak
- sensitive_access

Base model: {BASE_MODEL}

Datasets used:
- dmilush/shieldlm-prompt-injection
- antijection/prompt-injection-dataset-v1
- leolee99/NotInject

Notes:
- `sensitive_access` is a custom merged class created from exfiltration / prompt-extraction / excessive-agency style attacks.
- Please review upstream dataset licenses before commercial use.
