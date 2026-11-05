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
# OnlineRubrics RaR-Medicine: step 48, seed 11

Final policy after 48 optimizer updates (3 epochs) of dynamic OnlineRubrics-Every GRPO.
Distinct from static-rubric GRPO. Base model: Qwen/Qwen3-4B-Instruct-2507; thinking disabled.
This checkpoint is a policy state used by the Phase-1 audit.
No downstream medical capability or safety claim is made. Research use only;
not validated for clinical decision-making.

Root files are the veRL-exported Hugging Face inference model (BF16).
`original_checkpoint/` preserves the exact original FSDP parameter checkpoint
and tokenizer/configuration files. Optimizer state, training data, responses,
rubrics, infrastructure configuration, and credentials are not included.
The original is retained because export precision/serialization differs.

Base model revision: cdbee75f17c01a7cc42f958dc650907174af0554
Original actor tree SHA256: 13132b9fcdced2ab7b6f004df759580d0e8cfb07f438997e449776da9196efd3
