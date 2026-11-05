---
base_model:
- Qwen/Qwen2.5-1.5B-Instruct
library_name: transformers
tags:
- mergekit
- merge

---
# model_sft_dare_p_0_3

This is a merge of pre-trained language models created using [mergekit](https://github.com/cg123/mergekit).

## Merge Details
### Merge Method

This model was merged using the [Linear DARE](https://arxiv.org/abs/2311.03099) merge method using [Qwen/Qwen2.5-1.5B-Instruct](https://huggingface.co/Qwen/Qwen2.5-1.5B-Instruct) as a base.

### Models Merged

The following models were included in the merge:
* outputs/part1/model_sft_full

### Configuration

The following YAML configuration was used to produce this model:

```yaml
models:
- model: Qwen/Qwen2.5-1.5B-Instruct
- model: outputs/part1/model_sft_full
  parameters:
    weight: 1.0
    density: 0.7
merge_method: dare_linear
base_model: Qwen/Qwen2.5-1.5B-Instruct
parameters:
  normalize: false
dtype: bfloat16

```
