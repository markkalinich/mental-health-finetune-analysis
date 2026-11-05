---
base_model:
- Qwen/Qwen3-4B-Thinking-2507
- Qwen/Qwen3-4B-Instruct-2507
library_name: transformers
tags:
- mergekit
- merge

---
# thinking_merged

This is a merge of pre-trained language models created using [mergekit](https://github.com/cg123/mergekit).

## Merge Details
### Merge Method

This model was merged using the [Task Arithmetic](https://arxiv.org/abs/2212.04089) merge method using [Qwen/Qwen3-4B-Instruct-2507](https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507) as a base.

### Models Merged

The following models were included in the merge:
* [Qwen/Qwen3-4B-Thinking-2507](https://huggingface.co/Qwen/Qwen3-4B-Thinking-2507)
* /workspace/csrsef/runs/20260325T081327Z/iteration_01/pubmedqa/instruct_merged

### Configuration

The following YAML configuration was used to produce this model:

```yaml
merge_method: task_arithmetic
base_model: Qwen/Qwen3-4B-Instruct-2507
models:
- model: /workspace/csrsef/runs/20260325T081327Z/iteration_01/pubmedqa/instruct_merged
  parameters:
    weight: 1.0
- model: Qwen/Qwen3-4B-Thinking-2507
  parameters:
    weight: 1.0
dtype: float16
tokenizer_source: Qwen/Qwen3-4B-Thinking-2507
parameters:
  lambda: 1.0

```
