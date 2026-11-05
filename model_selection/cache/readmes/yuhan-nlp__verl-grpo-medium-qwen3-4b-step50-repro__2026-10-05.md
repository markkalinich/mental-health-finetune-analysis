---
license: mit
base_model: Qwen/Qwen3-4B
datasets:
- yuhan-nlp/collabllm-medium-rl-grpo
language:
- en
library_name: transformers
tags:
- collabllm
- grpo
- verl
- multiturn
- reproduction
pipeline_tag: text-generation
---

# verl-GRPO CollabLLM medium — Qwen3-4B, step 50 (reproduction)

Independent-cluster reproduction of
[yuhan-nlp/verl-grpo-medium-qwen3-4b-step50](https://huggingface.co/yuhan-nlp/verl-grpo-medium-qwen3-4b-step50):
same recipe, same data, different hardware.

`Qwen/Qwen3-4B` trained with GRPO on the CollabLLM **medium** document-writing task using the
[verl](https://github.com/verl-project/verl) CollabLLM recipe (no SFT warm start). Merged HF
checkpoint — load it directly, no adapter step.

## Provenance

| | |
|---|---|
| merged from | `collabllm-qwen3-4B-medium-large-epoch1/global_step_50/actor` (8-shard FSDP) |
| merged with | `python -m verl.model_merger merge --backend fsdp` |
| training data | [yuhan-nlp/collabllm-medium-rl-grpo](https://huggingface.co/datasets/yuhan-nlp/collabllm-medium-rl-grpo) |

## Evaluation

No metrics are reported here on purpose. The benchmark runs backing this checkpoint —
per-example traces, judge outputs and summary JSON — live in
`yuhan-nlp/collabllm-medium-outputs` under `benchmark_runs/`, which is the single source
of truth for the numbers.

Setup used there: assistant = this model, user simulator `Qwen/Qwen3.5-9B`, judge
`Qwen/Qwen3.5-27B`, thinking **off** everywhere,
`--user_sim_prompt sim_gap_paper_lazy_full --assistant_max_tokens 4096 --max_new_turns 14`,
`--eval_size 100`.

## Usage

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
rid = "yuhan-nlp/verl-grpo-medium-qwen3-4b-step50-repro"
tok = AutoTokenizer.from_pretrained(rid)
model = AutoModelForCausalLM.from_pretrained(rid, dtype="bfloat16", device_map="auto")
```

The chat template ships as `chat_template.jinja` (transformers >= 4.57 keeps it out of
`tokenizer_config.json`); `AutoTokenizer` picks it up automatically.
