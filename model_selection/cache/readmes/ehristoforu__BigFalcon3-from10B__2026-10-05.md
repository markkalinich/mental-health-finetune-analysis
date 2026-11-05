---
base_model:
- tiiuae/Falcon3-10B-Instruct
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
* [tiiuae/Falcon3-10B-Instruct](https://huggingface.co/tiiuae/Falcon3-10B-Instruct)

### Configuration

The following YAML configuration was used to produce this model:

```yaml
slices:
- sources:
  - layer_range: [0, 10]
    model: tiiuae/Falcon3-10B-Instruct
- sources:
  - layer_range: [5, 15]
    model: tiiuae/Falcon3-10B-Instruct
- sources:
  - layer_range: [10, 20]
    model: tiiuae/Falcon3-10B-Instruct
- sources:
  - layer_range: [15, 25]
    model: tiiuae/Falcon3-10B-Instruct
- sources:
  - layer_range: [20, 30]
    model: tiiuae/Falcon3-10B-Instruct
- sources:
  - layer_range: [25, 35]
    model: tiiuae/Falcon3-10B-Instruct
- sources:
  - layer_range: [35, 40]
    model: tiiuae/Falcon3-10B-Instruct
merge_method: passthrough
dtype: bfloat16
```
