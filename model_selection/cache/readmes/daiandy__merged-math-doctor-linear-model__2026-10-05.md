---
base_model:
- daiandy/doctor-model
- daiandy/math-model
library_name: transformers
tags:
- mergekit
- merge

---

This is a merge of pre-trained language models created using [mergekit](https://github.com/cg123/mergekit).

## Merge Details
### Merge Method

This model was merged using the [linear](https://arxiv.org/abs/2203.05482) merge method.

### Models Merged

The following models were included in the merge:
* [daiandy/doctor-model](https://huggingface.co/daiandy/doctor-model)
* [daiandy/math-model](https://huggingface.co/daiandy/math-model)

### Configuration

The following YAML configuration was used to produce this model:

```yaml
models:
  - model: daiandy/doctor-model
    parameters:
      weight: 1.0
  - model: daiandy/math-model
    parameters:
      weight: 1.0
merge_method: linear
parameters:
    normalize: true
dtype: float16

```
