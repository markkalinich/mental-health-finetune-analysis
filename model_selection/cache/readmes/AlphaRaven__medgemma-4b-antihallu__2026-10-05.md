---
license: apache-2.0
base_model: google/medgemma-4b-it
tags: [medical, anti-hallucination, pharmacovigilance, medgemma, rlfr]
---
# MedGemma 4B Anti-Hallucination

MedGemma 4B fine-tuned with **RLFR** (Reinforcement Learning from Feature Rewards) to reduce hallucination in pharmacovigilance document generation.

- **Base model**: `google/medgemma-4b-it`
- **Method**: RLFR with 6 reward features (factual accuracy, completeness, format compliance, etc.)
- **Task**: Generate MedWatch 3500A pharmacovigilance narratives from CRF data

## Usage

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained("AlphaRaven/medgemma-4b-antihallu")
tokenizer = AutoTokenizer.from_pretrained("AlphaRaven/medgemma-4b-antihallu")
```

Part of the [Clinical Trial Simulation Engine](https://github.com/AlphaRaven/ClinicalTrialEngine) pipeline.
