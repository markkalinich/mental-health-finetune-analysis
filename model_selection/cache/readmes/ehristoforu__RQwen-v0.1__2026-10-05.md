---
language:
- en
- ru
license: apache-2.0
tags:
- text-generation-inference
- transformers
- rqwen
- qwen2
- qwen2.5
- instruct
- chat
- ehristoforu
- trl
- sft
base_model:
- Qwen/Qwen2.5-14B-Instruct
pipeline_tag: text-generation
model-index:
- name: RQwen-v0.1
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
      value: 76.25
      name: strict accuracy
    source:
      url: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=ehristoforu/RQwen-v0.1
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
      value: 48.49
      name: normalized accuracy
    source:
      url: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=ehristoforu/RQwen-v0.1
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
      value: 2.95
      name: exact match
    source:
      url: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=ehristoforu/RQwen-v0.1
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
      value: 10.07
      name: acc_norm
    source:
      url: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=ehristoforu/RQwen-v0.1
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
      value: 10.44
      name: acc_norm
    source:
      url: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=ehristoforu/RQwen-v0.1
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
      value: 46.69
      name: accuracy
    source:
      url: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=ehristoforu/RQwen-v0.1
      name: Open LLM Leaderboard
---
# **RQwen** v0.1

## Short info
- **Developed by**: ehristoforu
- **Base model**: Qwen/Qwen2.5-14B-Instruct
- **Type model**: Qwen2 Instruct (ChatML)
- **Languages**: English, *Russian*
- **Features**: reflection tuning, logic and deep work with context
- **Trained with**: Unsloth (Transformers SFT)
- **License**: Apache-2.0


### GGUF format: *coming soon...*
# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_ehristoforu__RQwen-v0.1)

|      Metric       |Value|
|-------------------|----:|
|Avg.               |32.48|
|IFEval (0-Shot)    |76.25|
|BBH (3-Shot)       |48.49|
|MATH Lvl 5 (4-Shot)| 2.95|
|GPQA (0-shot)      |10.07|
|MuSR (0-shot)      |10.44|
|MMLU-PRO (5-shot)  |46.69|

