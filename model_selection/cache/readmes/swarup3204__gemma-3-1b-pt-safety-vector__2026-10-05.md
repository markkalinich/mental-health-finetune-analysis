---
base_model:
- swarup3204/gemma-3-1b-pt-tilde
- google/gemma-3-1b-pt
library_name: transformers
tags:
- mergekit
- merge

---
# safety_vector

This is a merge of pre-trained language models created using [mergekit](https://github.com/cg123/mergekit).

## Merge Details
### Merge Method

This model was merged using the [Linear](https://arxiv.org/abs/2203.05482) merge method.

### Models Merged

The following models were included in the merge:
* [swarup3204/gemma-3-1b-pt-tilde](https://huggingface.co/swarup3204/gemma-3-1b-pt-tilde)
* [google/gemma-3-1b-pt](https://huggingface.co/google/gemma-3-1b-pt)

### Configuration

The following YAML configuration was used to produce this model:

```yaml
models:
  - model: google/gemma-3-1b-pt
    parameters:
      weight: 1.0
  - model: swarup3204/gemma-3-1b-pt-tilde
    parameters:
      weight: -1.0
merge_method: linear
dtype: bfloat16
parameters:
  normalize: false

```
