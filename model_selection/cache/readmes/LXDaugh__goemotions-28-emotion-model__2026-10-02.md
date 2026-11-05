---
language:
- en
library_name: transformers
pipeline_tag: text-classification
tags:
- multi-label-classification
- emotion-classification
- goemotions
---

# GoEmotions 28-label Emotion Model

This model performs fine-grained multi-label emotion classification
using 28 GoEmotions labels.

The deployment decision strategy uses:

- Hybrid prediction
- Label-wise thresholds selected on the development set
- `labelwise_threshold_values_dev.json`
