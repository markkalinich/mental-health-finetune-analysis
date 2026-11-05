---
license: apache-2.0
language:
- zh
base_model:
- Qwen/Qwen2.5-7B-Instruct
pipeline_tag: text-generation
tags:
- medical
- fine-tuned
- qlora
---

# Medical-Qwen2.5-7B-Huatuo-Alpha

## 模型简介
这是一个基于 **Qwen2.5-7B-Instruct** 底座，使用 **Huatuo-26k-ChatML** (22.6万条全量数据) 进行 QLoRA 微调后的医疗大语言模型。

## 训练细节
- **训练设备**: NVIDIA L4 (24GB VRAM)
- **量化策略**: NF4 4-bit Quantization
- **微调方法**: LoRA (r=16, alpha=32)
- **训练时长**: 200 Steps (Alpha Test)
- **损失值 (Loss)**: 从 1.932 稳步下降至 1.707

## 预期用途
本模型仅用于科研与实验，旨在探索医疗知识在通用大模型中的对齐。不应直接用于临床决策。