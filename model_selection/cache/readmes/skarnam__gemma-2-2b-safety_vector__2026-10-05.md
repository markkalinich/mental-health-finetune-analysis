---
base_model:
- google/gemma-2-2b-it
- skarnam/gemma-2-2b-it-unaligned
library_name: transformers
tags:
- mergekit
- merge

---
# merge

This is a merge of pre-trained language models created using [mergekit](https://github.com/cg123/mergekit).

## Merge Details
### Merge Method

This model was merged using the [Linear](https://arxiv.org/abs/2203.05482) merge method.

### Models Merged

The following models were included in the merge:
* [google/gemma-2-2b-it](https://huggingface.co/google/gemma-2-2b-it)
* [skarnam/gemma-2-2b-it-unaligned](https://huggingface.co/skarnam/gemma-2-2b-it-unaligned)

### Configuration

The following YAML configuration was used to produce this model:

```yaml
models:
- model: google/gemma-2-2b-it
  parameters:
    weight: 1.0
- model: skarnam/gemma-2-2b-it-unaligned
  parameters:
    weight: -1.0
merge_method: linear
dtype: bfloat16
parameters:
  normalize: false
  int8_mask: true

```
