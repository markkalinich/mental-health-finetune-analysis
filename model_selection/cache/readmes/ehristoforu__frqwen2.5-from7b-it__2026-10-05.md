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
  - layer_range: [0, 4]
    model: Qwen/Qwen2.5-7B-Instruct
- sources:
  - layer_range: [2, 6]
    model: Qwen/Qwen2.5-7B-Instruct
- sources:
  - layer_range: [4, 8]
    model: Qwen/Qwen2.5-7B-Instruct
- sources:
  - layer_range: [6, 10]
    model: Qwen/Qwen2.5-7B-Instruct
- sources:
  - layer_range: [8, 12]
    model: Qwen/Qwen2.5-7B-Instruct
- sources:
  - layer_range: [10, 14]
    model: Qwen/Qwen2.5-7B-Instruct
- sources:
  - layer_range: [12, 16]
    model: Qwen/Qwen2.5-7B-Instruct
- sources:
  - layer_range: [14, 18]
    model: Qwen/Qwen2.5-7B-Instruct
- sources:
  - layer_range: [16, 20]
    model: Qwen/Qwen2.5-7B-Instruct
- sources:
  - layer_range: [18, 22]
    model: Qwen/Qwen2.5-7B-Instruct
- sources:
  - layer_range: [20, 24]
    model: Qwen/Qwen2.5-7B-Instruct
- sources:
  - layer_range: [22, 26]
    model: Qwen/Qwen2.5-7B-Instruct
- sources:
  - layer_range: [24, 28]
    model: Qwen/Qwen2.5-7B-Instruct
merge_method: passthrough
dtype: bfloat16
tokenizer_source: "Qwen/Qwen2.5-7B-Instruct"
```
