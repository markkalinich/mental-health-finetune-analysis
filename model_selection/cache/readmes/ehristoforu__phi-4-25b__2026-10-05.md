---
base_model:
- microsoft/phi-4
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
* [microsoft/phi-4](https://huggingface.co/microsoft/phi-4)

### Configuration

The following YAML configuration was used to produce this model:

```yaml
slices:
- sources:
  - layer_range: [0, 10]
    model: microsoft/phi-4
- sources:
  - layer_range: [5, 15]
    model: microsoft/phi-4
- sources:
  - layer_range: [10, 20]
    model: microsoft/phi-4
- sources:
  - layer_range: [15, 25]
    model: microsoft/phi-4
- sources:
  - layer_range: [20, 30]
    model: microsoft/phi-4
- sources:
  - layer_range: [25, 35]
    model: microsoft/phi-4
- sources:
  - layer_range: [30, 40]
    model: microsoft/phi-4
merge_method: passthrough
dtype: bfloat16
```
