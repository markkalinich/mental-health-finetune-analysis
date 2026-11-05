---
license: apache-2.0
language:
  - ja
  - en
base_model: Qwen/Qwen3-32B
datasets:
  - Team-Promptia/RLT-medicine_biology-expert-11k
tags:
  - qwen
  - qwen3
  - medicine
  - biology
  - japanese
  - text-generation
  - fine-tuning
---

これは、Qwen/Qwen3-32B をベースとしてファインチューニングされたHugging Faceモデルです。
ファインチューニングに使用されたデータは Qwen2.5-7B-RLT-medicine_biology-expert_data_generation です。このデータは、Team-Promptia/RLT-medicine_biology-expert-11k データセットを基に、Team-Promptia/Qwen2.5-7B-RLT-medicine_biology-expert モデルによって生成されました。