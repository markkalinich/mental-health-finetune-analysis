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
  - layer_range: [0, 8]
    model: tiiuae/Falcon3-10B-Instruct
- sources:
  - layer_range: [4, 12]
    model: tiiuae/Falcon3-10B-Instruct
- sources:
  - layer_range: [8, 16]
    model: tiiuae/Falcon3-10B-Instruct
- sources:
  - layer_range: [12, 20]
    model: tiiuae/Falcon3-10B-Instruct
- sources:
  - layer_range: [16, 24]
    model: tiiuae/Falcon3-10B-Instruct
- sources:
  - layer_range: [20, 28]
    model: tiiuae/Falcon3-10B-Instruct
- sources:
  - layer_range: [24, 32]
    model: tiiuae/Falcon3-10B-Instruct
- sources:
  - layer_range: [28, 36]
    model: tiiuae/Falcon3-10B-Instruct
- sources:
  - layer_range: [32, 40]
    model: tiiuae/Falcon3-10B-Instruct
merge_method: passthrough
dtype: bfloat16
```
