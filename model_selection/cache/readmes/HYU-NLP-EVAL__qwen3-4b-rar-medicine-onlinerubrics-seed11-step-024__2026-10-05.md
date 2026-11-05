---
license: apache-2.0
base_model: Qwen/Qwen3-4B-Instruct-2507
library_name: transformers
pipeline_tag: text-generation
tags:
- onlinerubrics
- grpo
- rar-medicine
- research
---
# OnlineRubrics RaR-Medicine: step 24, seed 11

Intermediate policy from dynamic OnlineRubrics-Every GRPO training, distinct
from static-rubric GRPO. Base model: Qwen/Qwen3-4B-Instruct-2507; thinking disabled.
This checkpoint is a historical policy state used by the Phase-1 audit.
No downstream medical capability or safety claim is made. Research use only;
not validated for clinical decision-making.

Root files are the veRL-exported Hugging Face inference model (BF16).
`original_checkpoint/` preserves the exact original FSDP parameter checkpoint
and tokenizer/configuration files. Optimizer state, training data, responses,
rubrics, infrastructure configuration, and credentials are not included.
The original is retained because export precision/serialization differs.

Base model revision: cdbee75f17c01a7cc42f958dc650907174af0554
Original actor tree SHA256: 8a3f85789c5ede207c56d588d0f40a0a780851fd52d2e5f8d39fe54c2563f4f3
