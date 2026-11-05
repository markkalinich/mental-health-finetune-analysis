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

This model was merged using the passthrough merge method.

### Models Merged

The following models were included in the merge:
* [Qwen/Qwen2.5-7B-Instruct](https://huggingface.co/Qwen/Qwen2.5-7B-Instruct)

### Configuration

The following YAML configuration was used to produce this model:

```yaml
slices:
  - sources:
    - model: Qwen/Qwen2.5-7B-Instruct
      layer_range: [0, 4]
  - sources:
    - model: Qwen/Qwen2.5-7B-Instruct
      layer_range: [4, 8]
  - sources:
    - model: Qwen/Qwen2.5-7B-Instruct
      layer_range: [8, 12]
  - sources:
    - model: Qwen/Qwen2.5-7B-Instruct
      layer_range: [12, 16]
  - sources:
    - model: Qwen/Qwen2.5-7B-Instruct
      layer_range: [16, 20]
  - sources:
    - model: Qwen/Qwen2.5-7B-Instruct
      layer_range: [20, 24]
  - sources:
    - model: Qwen/Qwen2.5-7B-Instruct
      layer_range: [24, 28]
merge_method: passthrough
dtype: float16

```
