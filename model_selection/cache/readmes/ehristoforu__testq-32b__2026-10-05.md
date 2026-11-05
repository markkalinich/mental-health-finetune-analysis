---
base_model:
- ehristoforu/fq2.5-32b-v1
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
* [ehristoforu/fq2.5-32b-v1](https://huggingface.co/ehristoforu/fq2.5-32b-v1)

### Configuration

The following YAML configuration was used to produce this model:

```yaml
slices:
- sources:
  - layer_range: [0, 16]
    model: ehristoforu/fq2.5-32b-v1
- sources:
  - layer_range: [8, 24]
    model: ehristoforu/fq2.5-32b-v1
- sources:
  - layer_range: [16, 32]
    model: ehristoforu/fq2.5-32b-v1
- sources:
  - layer_range: [24, 40]
    model: ehristoforu/fq2.5-32b-v1
- sources:
  - layer_range: [32, 48]
    model: ehristoforu/fq2.5-32b-v1
- sources:
  - layer_range: [40, 56]
    model: ehristoforu/fq2.5-32b-v1
- sources:
  - layer_range: [48, 64]
    model: ehristoforu/fq2.5-32b-v1
merge_method: passthrough
dtype: bfloat16
tokenizer_source: "Qwen/Qwen2.5-32B-Instruct"
```
