---
base_model:
- Qwen/Qwen2.5-7B-Instruct
library_name: transformers
tags:
- mergekit
- merge

---
# merge

This is a merge of pre-trained language models created using [mergekit](https://github.com/cg123/mergekit).

## Merge Details
### Merge Method

This model was merged using the [DARE TIES](https://arxiv.org/abs/2311.03099) merge method using [Qwen/Qwen2.5-7B-Instruct](https://huggingface.co/Qwen/Qwen2.5-7B-Instruct) as a base.

### Models Merged

The following models were included in the merge:


### Configuration

The following YAML configuration was used to produce this model:

```yaml
models:
  - model: Qwen/Qwen2.5-7B-Instruct
    parameters:
      weight: 1
      density: 1
merge_method: dare_ties
base_model: Qwen/Qwen2.5-7B-Instruct
parameters:
  weight: 1
  density: 1
  normalize: true
  int8_mask: true
tokenizer_source: "Qwen/Qwen2.5-7B-Instruct"
dtype: float16
```
