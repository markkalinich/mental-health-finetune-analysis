---
base_model:
- Qwen/Qwen2.5-1.5B-Instruct
library_name: transformers
tags:
- mergekit
- merge

---
# dare_p0.5

This is a merge of pre-trained language models created using [mergekit](https://github.com/cg123/mergekit).

## Merge Details
### Merge Method

This model was merged using the [Linear DARE](https://arxiv.org/abs/2311.03099) merge method using [Qwen/Qwen2.5-1.5B-Instruct](https://huggingface.co/Qwen/Qwen2.5-1.5B-Instruct) as a base.

### Models Merged

The following models were included in the merge:
* outputs/model_sft_lora

### Configuration

The following YAML configuration was used to produce this model:

```yaml
models:
  - model: Qwen/Qwen2.5-1.5B-Instruct
    parameters:
      density: 1.0
      weight: 1.0
  - model: outputs/model_sft_lora
    parameters:
      density: 0.50
      weight: 1.0
merge_method: dare_linear
base_model: Qwen/Qwen2.5-1.5B-Instruct
dtype: bfloat16
```
