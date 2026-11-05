---
base_model:
- ehristoforu/phi-4-25b
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
* [ehristoforu/phi-4-25b](https://huggingface.co/ehristoforu/phi-4-25b)

### Configuration

The following YAML configuration was used to produce this model:

```yaml
slices:
- sources:
  - layer_range: [0, 10]
    model: ehristoforu/phi-4-25b
- sources:
  - layer_range: [5, 15]
    model: ehristoforu/phi-4-25b
- sources:
  - layer_range: [10, 20]
    model: ehristoforu/phi-4-25b
- sources:
  - layer_range: [15, 25]
    model: ehristoforu/phi-4-25b
- sources:
  - layer_range: [20, 30]
    model: ehristoforu/phi-4-25b
- sources:
  - layer_range: [25, 35]
    model: ehristoforu/phi-4-25b
- sources:
  - layer_range: [30, 40]
    model: ehristoforu/phi-4-25b
- sources:
  - layer_range: [35, 45]
    model: ehristoforu/phi-4-25b
- sources:
  - layer_range: [40, 50]
    model: ehristoforu/phi-4-25b
- sources:
  - layer_range: [45, 55]
    model: ehristoforu/phi-4-25b
- sources:
  - layer_range: [50, 60]
    model: ehristoforu/phi-4-25b
- sources:
  - layer_range: [55, 65]
    model: ehristoforu/phi-4-25b
- sources:
  - layer_range: [60, 70]
    model: ehristoforu/phi-4-25b
merge_method: passthrough
dtype: bfloat16
```
