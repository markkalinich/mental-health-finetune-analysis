---
license: mit
datasets:
- lavita/ChatDoctor-HealthCareMagic-100k
model-index:
- name: doctorLLM10k
  results:
  - task:
      type: text-generation
      name: Text Generation
    dataset:
      name: AI2 Reasoning Challenge (25-Shot)
      type: ai2_arc
      config: ARC-Challenge
      split: test
      args:
        num_few_shot: 25
    metrics:
    - type: acc_norm
      value: 54.95
      name: normalized accuracy
    source:
      url: https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard?query=vikash06/doctorLLM10k
      name: Open LLM Leaderboard
  - task:
      type: text-generation
      name: Text Generation
    dataset:
      name: HellaSwag (10-Shot)
      type: hellaswag
      split: validation
      args:
        num_few_shot: 10
    metrics:
    - type: acc_norm
      value: 79.94
      name: normalized accuracy
    source:
      url: https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard?query=vikash06/doctorLLM10k
      name: Open LLM Leaderboard
  - task:
      type: text-generation
      name: Text Generation
    dataset:
      name: MMLU (5-Shot)
      type: cais/mmlu
      config: all
      split: test
      args:
        num_few_shot: 5
    metrics:
    - type: acc
      value: 44.4
      name: accuracy
    source:
      url: https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard?query=vikash06/doctorLLM10k
      name: Open LLM Leaderboard
  - task:
      type: text-generation
      name: Text Generation
    dataset:
      name: TruthfulQA (0-shot)
      type: truthful_qa
      config: multiple_choice
      split: validation
      args:
        num_few_shot: 0
    metrics:
    - type: mc2
      value: 44.76
    source:
      url: https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard?query=vikash06/doctorLLM10k
      name: Open LLM Leaderboard
  - task:
      type: text-generation
      name: Text Generation
    dataset:
      name: Winogrande (5-shot)
      type: winogrande
      config: winogrande_xl
      split: validation
      args:
        num_few_shot: 5
    metrics:
    - type: acc
      value: 70.01
      name: accuracy
    source:
      url: https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard?query=vikash06/doctorLLM10k
      name: Open LLM Leaderboard
  - task:
      type: text-generation
      name: Text Generation
    dataset:
      name: GSM8k (5-shot)
      type: gsm8k
      config: main
      split: test
      args:
        num_few_shot: 5
    metrics:
    - type: acc
      value: 10.16
      name: accuracy
    source:
      url: https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard?query=vikash06/doctorLLM10k
      name: Open LLM Leaderboard
---

Sample Input on Postman API:

![image/png](https://cdn-uploads.huggingface.co/production/uploads/63a7d07154f1d0225b0b9d1c/1A5BfWI5QOQHa7g8ueGIS.png)

Number of epochs: 10
Number of Data points: 10000
# Creative Writing: Write a question or instruction that requires a creative medical response from a doctor. 
The instruction should be reasonable to ask of a person with general medical knowledge and should not require searching. 
In this task, your prompt should give very specific instructions to follow. 
Constraints, instructions, guidelines, or requirements all work, and the more of them the better.

Reference dataset: https://github.com/Kent0n-Li/ChatDoctor

# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_vikash06__doctorLLM10k)

|             Metric              |Value|
|---------------------------------|----:|
|Avg.                             |50.70|
|AI2 Reasoning Challenge (25-Shot)|54.95|
|HellaSwag (10-Shot)              |79.94|
|MMLU (5-Shot)                    |44.40|
|TruthfulQA (0-shot)              |44.76|
|Winogrande (5-shot)              |70.01|
|GSM8k (5-shot)                   |10.16|

