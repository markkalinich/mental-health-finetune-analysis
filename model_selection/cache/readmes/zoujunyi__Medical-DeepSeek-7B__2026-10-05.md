---
license: apache-2.0
tags:
- unsloth
- trl
- sft
datasets:
- zoujunyi/medical_test
language:
- zh
base_model:
- unsloth/DeepSeek-R1-Distill-Qwen-7B
---
使用colab微调，微调数据来自中华医学会15篇文献，通过qwen-turbo模型生成训练数据