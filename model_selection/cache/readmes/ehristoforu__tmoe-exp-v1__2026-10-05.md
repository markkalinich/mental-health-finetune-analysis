---
pipeline_tag: other
library_name: transformers
---
This is fully exp model!
```
base_model: beomi/EXAONE-3.5-2.4B-Instruct-Llamafied
gate_mode: random
architecture: mixtral
experts_per_token: 2
dtype: bfloat16
experts:
  - source_model: beomi/EXAONE-3.5-2.4B-Instruct-Llamafied
  - source_model: unsloth/Phi-3.5-mini-instruct
```