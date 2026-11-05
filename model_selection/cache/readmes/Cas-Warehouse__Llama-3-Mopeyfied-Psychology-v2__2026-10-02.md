---
base_model:
- TheSkullery/llama-3-cat-8b-instruct-v1
- victunes/TherapyLlama-8B-v1
- herisan/llama-3-8b_mental_health_counseling_conversations
- Falah/lora_model_mental_health_llama3
- Abdo36/MentalLORALLAMA3
- zementalist/llama-3-8B-chat-psychotherapist
- PrahmodhRaj/Llama-3_Psychiatrist_Chat
- Cas-Warehouse/Llama-3-MopeyMule-Blackroot-8B
- Cas-Warehouse/Llama-3-SOVL-MopeyMule-8B
tags:
- merge
- mergekit
- lazymergekit
---

# Psyche-3

Psyche-3 is a merge of the following models using [LazyMergekit](https://colab.research.google.com/drive/1obulZ1ROXHjYLn6PPZJwRR6GzgQogxxb?usp=sharing):
* [TheSkullery/llama-3-cat-8b-instruct-v1](https://huggingface.co/TheSkullery/llama-3-cat-8b-instruct-v1)
* [victunes/TherapyLlama-8B-v1](https://huggingface.co/victunes/TherapyLlama-8B-v1)
* [herisan/llama-3-8b_mental_health_counseling_conversations](https://huggingface.co/herisan/llama-3-8b_mental_health_counseling_conversations)
* [Falah/lora_model_mental_health_llama3](https://huggingface.co/Falah/lora_model_mental_health_llama3)
* [Abdo36/MentalLORALLAMA3](https://huggingface.co/Abdo36/MentalLORALLAMA3)
* [zementalist/llama-3-8B-chat-psychotherapist](https://huggingface.co/zementalist/llama-3-8B-chat-psychotherapist)
* [PrahmodhRaj/Llama-3_Psychiatrist_Chat](https://huggingface.co/PrahmodhRaj/Llama-3_Psychiatrist_Chat)
* [Cas-Warehouse/Llama-3-MopeyMule-Blackroot-8B](https://huggingface.co/Cas-Warehouse/Llama-3-MopeyMule-Blackroot-8B)
* [Cas-Warehouse/Llama-3-SOVL-MopeyMule-8B](https://huggingface.co/Cas-Warehouse/Llama-3-SOVL-MopeyMule-8B)

## 🧩 Configuration

```yaml
slices:
- sources:
  - model: TheSkullery/llama-3-cat-8b-instruct-v1
    layer_range: [0, 32]
  - model: victunes/TherapyLlama-8B-v1
    layer_range: [0, 32]
    parameters:
      density: 0.55
      weight: 0.35
  - model: herisan/llama-3-8b_mental_health_counseling_conversations
    layer_range: [0, 32]
    parameters:
      density: 0.55
      weight: 0.35
merge_method: ties
base_model: TheSkullery/llama-3-cat-8b-instruct-v1
parameters:
  int8_mask: true
dtype: bfloat16
---
models:
  - model: Casual-Autopsy/Psyche-1+Falah/lora_model_mental_health_llama3
  - model: Casual-Autopsy/Psyche-1+Abdo36/MentalLORALLAMA3
  - model: Casual-Autopsy/Psyche-1+zementalist/llama-3-8B-chat-psychotherapist
  - model: Casual-Autopsy/Psyche-1+PrahmodhRaj/Llama-3_Psychiatrist_Chat
merge_method: model_stock
base_model: Casual-Autopsy/Psyche-1
dtype: bfloat16
---
models:
  - model: Casual-Autopsy/Psyche-2
  - model: Cas-Warehouse/Llama-3-MopeyMule-Blackroot-8B
    parameters:
      weight: 0.25
  - model: Cas-Warehouse/Llama-3-SOVL-MopeyMule-8B
    parameters:
      weight: 0.15
merge_method: task_arithmetic
base_model: Casual-Autopsy/Psyche-2
dtype: bfloat16
```