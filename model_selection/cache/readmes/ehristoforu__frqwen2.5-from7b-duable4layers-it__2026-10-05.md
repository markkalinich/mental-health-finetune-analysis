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
  - layer_range: [0, 14]
    model: Qwen/Qwen2.5-7B-Instruct
- sources:
  - layer_range: [10, 14]
    model: Qwen/Qwen2.5-7B-Instruct
- sources:
  - layer_range: [14, 28]
    model: Qwen/Qwen2.5-7B-Instruct
merge_method: passthrough
dtype: bfloat16
tokenizer_source: "Qwen/Qwen2.5-7B-Instruct"
```
