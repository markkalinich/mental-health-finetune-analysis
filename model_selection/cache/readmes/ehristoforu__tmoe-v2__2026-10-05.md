---
library_name: transformers
license: apache-2.0
---
```
base_model: Qwen/Qwen2.5-1.5B-Instruct
gate_mode: cheap_embed
architecture: qwen
experts_per_token: 4
dtype: bfloat16
experts:
  - source_model: Qwen/Qwen2.5-1.5B-Instruct
    positive_prompts: ["chat assistant"]
  - source_model: Qwen/Qwen2.5-Coder-1.5B-Instruct
    positive_prompts: ["code assistant"]
  - source_model: Qwen/Qwen2.5-Math-1.5B-Instruct
    positive_prompts: ["math assistant"]
  - source_model: huihui-ai/Qwen2.5-1.5B-Instruct-abliterated
    positive_prompts: ["uncensored assistant"]
  - source_model: Rombo-Org/Rombo-LLM-V2.5-Qwen-1.5b
    positive_prompts: ["review assistant"]
  - source_model: deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B
    positive_prompts: ["logical assistant"]
  - source_model: Vikhrmodels/Vikhr-Qwen-2.5-1.5B-Instruct
    positive_prompts: ["writing assistant"]
  - source_model: RefalMachine/RuadaptQwen2.5-1.5B-instruct
    positive_prompts: ["text editing assistant"]
shared_experts:
  - source_model: Qwen/Qwen2.5-1.5B-Instruct
    positive_prompts: ["chat assistant"]
    residual_scale: 0.1
```