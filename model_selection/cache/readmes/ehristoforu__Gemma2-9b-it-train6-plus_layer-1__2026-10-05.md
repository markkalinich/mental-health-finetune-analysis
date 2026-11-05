---
base_model:
- ehristoforu/Gemma2-9b-it-train6
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
* [ehristoforu/Gemma2-9b-it-train6](https://huggingface.co/ehristoforu/Gemma2-9b-it-train6)

### Configuration

The following YAML configuration was used to produce this model:

```yaml
slices:
  - sources:
      - model: ehristoforu/Gemma2-9b-it-train6
        layer_range: [1, 32]
  - sources:
      - model: ehristoforu/Gemma2-9b-it-train6
        layer_range: [0, 1]
merge_method: passthrough
dtype: bfloat16

```
