---
base_model:
- Qwen/Qwen2.5-1.5B-Instruct
library_name: transformers
tags:
- mergekit
- merge

---
# model_sft_dare_p0.3

This is a merge of pre-trained language models created using [mergekit](https://github.com/cg123/mergekit).

## Merge Details
### Merge Method

This model was merged using the [Linear DARE](https://arxiv.org/abs/2311.03099) merge method using [Qwen/Qwen2.5-1.5B-Instruct](https://huggingface.co/Qwen/Qwen2.5-1.5B-Instruct) as a base.

### Models Merged

The following models were included in the merge:
* ./model_sft_merged_local

### Configuration

The following YAML configuration was used to produce this model:

```yaml
base_model: Qwen/Qwen2.5-1.5B-Instruct
dtype: bfloat16
merge_method: dare_linear
models:
- model: Qwen/Qwen2.5-1.5B-Instruct
- model: ./model_sft_merged_local
  parameters:
    density: 0.7
    weight: 1.0

```
