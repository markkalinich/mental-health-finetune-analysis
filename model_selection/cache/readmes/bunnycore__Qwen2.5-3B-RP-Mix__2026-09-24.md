---
library_name: transformers
tags:
- mergekit
- merge
base_model:
- Qwen/Qwen2.5-3B-Instruct
- bunnycore/Qwen-2.5-3b-Rp-lora_model
model-index:
- name: Qwen2.5-3B-RP-Mix
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
      value: 57.21
      name: strict accuracy
    source:
      url: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=bunnycore/Qwen2.5-3B-RP-Mix
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
      value: 28.31
      name: normalized accuracy
    source:
      url: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=bunnycore/Qwen2.5-3B-RP-Mix
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
      value: 7.4
      name: exact match
    source:
      url: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=bunnycore/Qwen2.5-3B-RP-Mix
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
      value: 3.13
      name: acc_norm
    source:
      url: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=bunnycore/Qwen2.5-3B-RP-Mix
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
      value: 12.56
      name: acc_norm
    source:
      url: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=bunnycore/Qwen2.5-3B-RP-Mix
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
      value: 30.31
      name: accuracy
    source:
      url: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=bunnycore/Qwen2.5-3B-RP-Mix
      name: Open LLM Leaderboard
---
# merge

This is a merge of pre-trained language models created using [mergekit](https://github.com/cg123/mergekit).

## Merge Details
### Merge Method

This model was merged using the passthrough merge method using [Qwen/Qwen2.5-3B-Instruct](https://huggingface.co/Qwen/Qwen2.5-3B-Instruct) + [bunnycore/Qwen-2.5-3b-Rp-lora_model](https://huggingface.co/bunnycore/Qwen-2.5-3b-Rp-lora_model) as a base.

### Models Merged

The following models were included in the merge:


### Configuration

The following YAML configuration was used to produce this model:

```yaml

base_model: Qwen/Qwen2.5-3B-Instruct+bunnycore/Qwen-2.5-3b-Rp-lora_model
dtype: bfloat16
merge_method: passthrough
models:
  - model: Qwen/Qwen2.5-3B-Instruct+bunnycore/Qwen-2.5-3b-Rp-lora_model

```

# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_bunnycore__Qwen2.5-3B-RP-Mix)

|      Metric       |Value|
|-------------------|----:|
|Avg.               |23.15|
|IFEval (0-Shot)    |57.21|
|BBH (3-Shot)       |28.31|
|MATH Lvl 5 (4-Shot)| 7.40|
|GPQA (0-shot)      | 3.13|
|MuSR (0-shot)      |12.56|
|MMLU-PRO (5-shot)  |30.31|

