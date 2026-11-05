---
base_model:
- unsloth/Qwen2.5-14B-Instruct
- rombodawg/Rombos-LLM-V2.6-Qwen-14b
library_name: transformers
tags:
- mergekit
- merge

---
# merge

This is a merge of pre-trained language models created using [mergekit](https://github.com/cg123/mergekit).

## Merge Details
### Merge Method

This model was merged using the [DARE TIES](https://arxiv.org/abs/2311.03099) merge method using [unsloth/Qwen2.5-14B-Instruct](https://huggingface.co/unsloth/Qwen2.5-14B-Instruct) as a base.

### Models Merged

The following models were included in the merge:
* [rombodawg/Rombos-LLM-V2.6-Qwen-14b](https://huggingface.co/rombodawg/Rombos-LLM-V2.6-Qwen-14b)

### Configuration

The following YAML configuration was used to produce this model:

```yaml
models:
  - model: unsloth/Qwen2.5-14B-Instruct
    parameters:
      weight: 0.575
      density: 0.575
  - model: rombodawg/Rombos-LLM-V2.6-Qwen-14b
    parameters:
      weight: 0.425
      density: 0.425
merge_method: dare_ties
base_model: unsloth/Qwen2.5-14B-Instruct
dtype: bfloat16

```
