---
library_name: transformers
base_model: google/gemma-4-E4B-it
tags:
- gemma
- telugu
- medical
- merged
---

# RohithMidigudla/gemma-health-telugu-medical-merged-h1-30-h2-70

Full merged Gemma health model created from weighted LoRA adapters.

## Merge

- Candidate: `h1_30_h2_70`
- Telugu/H1 adapter: `RohithMidigudla/gemma-health-telugu-lora-h1`
- Medical/H2 adapter: `RohithMidigudla/gemma-health-medical-lora-h2`
- Telugu weight: `0.3`
- Medical weight: `0.7`
- Save method: `merged_16bit`

Intended as a base checkpoint for further Telugu medical RL policy alignment.
