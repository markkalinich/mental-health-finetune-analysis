---
license: llama3.3
base_model:
- allura-forge/Llama-3.3-8B-Instruct
pipeline_tag: text-generation
model-index:
  - name: shb777/Llama-3.3-8B-Instruct-128K
    results:
      - task:
          type: text-generation
        dataset:
          name: BBH
          type: leaderboard
        metrics:
          - type: accuracy
            value: 54.1
            name: acc_norm
      - task:
          type: text-generation
        dataset:
          name: GPQA
          type: leaderboard
        metrics:
          - type: accuracy
            value: 29.9
            name: acc_norm
      - task:
          type: text-generation
        dataset:
          name: MMLU Pro
          type: leaderboard
        metrics:
          - type: accuracy
            value: 38.0
            name: acc
      - task:
          type: text-generation
        dataset:
          name: MuSR
          type: leaderboard
        metrics:
          - type: accuracy
            value: 37.8
            name: acc_norm
      - task:
          type: text-generation
        dataset:
          name: IFEval
          type: leaderboard
        metrics:
          - type: accuracy
            value: 85.2
            name: avg(prompt_strict + inst_strict)
      - task:
          type: text-generation
        dataset:
          name: MATH Hard
          type: leaderboard
        metrics:
          - type: accuracy
            value: 27.3
            name: exact_match
---

# Llama 3.3 8B 128K Instruct (Fixed)

> [!IMPORTANT]
> Original [allura-forge/Llama-3.3-8B-Instruct](https://huggingface.co/allura-forge/Llama-3.3-8B-Instruct), Thanks!

> [!TIP]
> [imatrix GGUF's by mradermacher (Recommended)](https://huggingface.co/mradermacher/Llama-3.3-8B-Instruct-128K-i1-GGUF)
> 
> [static GGUF's](https://huggingface.co/shb777/Llama-3.3-8B-Instruct-128K-GGUF)
> 
> [Evals](https://huggingface.co/datasets/shb777/Llama-3.3-8B-Instruct-128K-Evals)

Additional Fixes:
- Added `rope_scaling`
- Added chat template (Unsloth) in tokenizer config
- Updated generation config
- Enabled full context length