---
language:
- en
license: apache-2.0
tags:
- text-generation-inference
- transformers
- unsloth
- qwen2
- trl
- sft
base_model: ehristoforu/SoRu-0008
model-index:
- name: SoRu-0009
  results:
  - task:
      type: text-generation
      name: Text Generation
    dataset:
      name: IFEval (0-Shot)
      type: HuggingFaceH4/ifeval
      args:
        num_few_shot: 0
    metrics:
    - type: inst_level_strict_acc and prompt_level_strict_acc
      value: 25.82
      name: strict accuracy
    source:
      url: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=ehristoforu/SoRu-0009
      name: Open LLM Leaderboard
  - task:
      type: text-generation
      name: Text Generation
    dataset:
      name: BBH (3-Shot)
      type: BBH
      args:
        num_few_shot: 3
    metrics:
    - type: acc_norm
      value: 5.14
      name: normalized accuracy
    source:
      url: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=ehristoforu/SoRu-0009
      name: Open LLM Leaderboard
  - task:
      type: text-generation
      name: Text Generation
    dataset:
      name: MATH Lvl 5 (4-Shot)
      type: hendrycks/competition_math
      args:
        num_few_shot: 4
    metrics:
    - type: exact_match
      value: 0.0
      name: exact match
    source:
      url: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=ehristoforu/SoRu-0009
      name: Open LLM Leaderboard
  - task:
      type: text-generation
      name: Text Generation
    dataset:
      name: GPQA (0-shot)
      type: Idavidrein/gpqa
      args:
        num_few_shot: 0
    metrics:
    - type: acc_norm
      value: 1.45
      name: acc_norm
    source:
      url: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=ehristoforu/SoRu-0009
      name: Open LLM Leaderboard
  - task:
      type: text-generation
      name: Text Generation
    dataset:
      name: MuSR (0-shot)
      type: TAUR-Lab/MuSR
      args:
        num_few_shot: 0
    metrics:
    - type: acc_norm
      value: 0.62
      name: acc_norm
    source:
      url: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=ehristoforu/SoRu-0009
      name: Open LLM Leaderboard
  - task:
      type: text-generation
      name: Text Generation
    dataset:
      name: MMLU-PRO (5-shot)
      type: TIGER-Lab/MMLU-Pro
      config: main
      split: test
      args:
        num_few_shot: 5
    metrics:
    - type: acc
      value: 2.66
      name: accuracy
    source:
      url: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=ehristoforu/SoRu-0009
      name: Open LLM Leaderboard
---

# Uploaded  model

- **Developed by:** ehristoforu
- **License:** apache-2.0
- **Finetuned from model :** ehristoforu/SoRu-0008

This qwen2 model was trained 2x faster with [Unsloth](https://github.com/unslothai/unsloth) and Huggingface's TRL library.

[<img src="https://raw.githubusercontent.com/unslothai/unsloth/main/images/unsloth%20made%20with%20love.png" width="200"/>](https://github.com/unslothai/unsloth)

# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_ehristoforu__SoRu-0009)

|      Metric       |Value|
|-------------------|----:|
|Avg.               | 5.95|
|IFEval (0-Shot)    |25.82|
|BBH (3-Shot)       | 5.14|
|MATH Lvl 5 (4-Shot)| 0.00|
|GPQA (0-shot)      | 1.45|
|MuSR (0-shot)      | 0.62|
|MMLU-PRO (5-shot)  | 2.66|

