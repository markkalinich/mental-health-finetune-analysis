---
license: apache-2.0
language:
- en
- ru
tags:
- moe
---
```
base_model: Qwen/Qwen2.5-1.5B-Instruct
gate_mode: random
architecture: qwen
experts_per_token: 3
dtype: bfloat16
experts:
  - source_model: Qwen/Qwen2.5-1.5B-Instruct
  - source_model: Qwen/Qwen2.5-Coder-1.5B-Instruct
  - source_model: Qwen/Qwen2.5-Math-1.5B-Instruct
  - source_model: huihui-ai/Qwen2.5-1.5B-Instruct-abliterated
  - source_model: Rombo-Org/Rombo-LLM-V2.5-Qwen-1.5b
  - source_model: deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B
  - source_model: Vikhrmodels/Vikhr-Qwen-2.5-1.5B-Instruct
  - source_model: RefalMachine/RuadaptQwen2.5-1.5B-instruct
shared_experts:
  - source_model: Qwen/Qwen2.5-1.5B-Instruct
    positive_prompts: [""]
    residual_scale: 0.1
```