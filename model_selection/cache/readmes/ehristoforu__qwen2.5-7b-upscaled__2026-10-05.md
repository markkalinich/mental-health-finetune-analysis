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
merge_method: passthrough
slices:
- sources:
  - layer_range: [0, 19]
    model: Qwen/Qwen2.5-7B-Instruct
- sources:
  - layer_range: [19, 20]
    model: Qwen/Qwen2.5-7B-Instruct
- sources:
  - layer_range: [19, 20]
    model: Qwen/Qwen2.5-7B-Instruct
    parameters:
      scale:
      - filter: o_proj
        value: 0.0
      - filter: down_proj
        value: 0.0
      - value: 1.0
- sources:
  - layer_range: [19, 20]
    model: Qwen/Qwen2.5-7B-Instruct
    parameters:
      scale:
      - filter: o_proj
        value: 0.0
      - filter: down_proj
        value: 0.0
      - value: 1.0
- sources:
  - layer_range: [20, 21]
    model: Qwen/Qwen2.5-7B-Instruct
- sources:
  - layer_range: [20, 21]
    model: Qwen/Qwen2.5-7B-Instruct
    parameters:
      scale:
      - filter: o_proj
        value: 0.0
      - filter: down_proj
        value: 0.0
      - value: 1.0
- sources:
  - layer_range: [20, 21]
    model: Qwen/Qwen2.5-7B-Instruct
    parameters:
      scale:
      - filter: o_proj
        value: 0.0
      - filter: down_proj
        value: 0.0
      - value: 1.0
- sources:
  - layer_range: [21, 22]
    model: Qwen/Qwen2.5-7B-Instruct
- sources:
  - layer_range: [21, 22]
    model: Qwen/Qwen2.5-7B-Instruct
    parameters:
      scale:
      - filter: o_proj
        value: 0.0
      - filter: down_proj
        value: 0.0
      - value: 1.0
- sources:
  - layer_range: [21, 22]
    model: Qwen/Qwen2.5-7B-Instruct
    parameters:
      scale:
      - filter: o_proj
        value: 0.0
      - filter: down_proj
        value: 0.0
      - value: 1.0
- sources:
  - layer_range: [22, 23]
    model: Qwen/Qwen2.5-7B-Instruct
- sources:
  - layer_range: [22, 23]
    model: Qwen/Qwen2.5-7B-Instruct
    parameters:
      scale:
      - filter: o_proj
        value: 0.0
      - filter: down_proj
        value: 0.0
      - value: 1.0
- sources:
  - layer_range: [22, 23]
    model: Qwen/Qwen2.5-7B-Instruct
    parameters:
      scale:
      - filter: o_proj
        value: 0.0
      - filter: down_proj
        value: 0.0
      - value: 1.0
- sources:
  - layer_range: [23, 24]
    model: Qwen/Qwen2.5-7B-Instruct
- sources:
  - layer_range: [23, 24]
    model: Qwen/Qwen2.5-7B-Instruct
    parameters:
      scale:
      - filter: o_proj
        value: 0.0
      - filter: down_proj
        value: 0.0
      - value: 1.0
- sources:
  - layer_range: [23, 24]
    model: Qwen/Qwen2.5-7B-Instruct
    parameters:
      scale:
      - filter: o_proj
        value: 0.0
      - filter: down_proj
        value: 0.0
      - value: 1.0
- sources:
  - layer_range: [24, 25]
    model: Qwen/Qwen2.5-7B-Instruct
- sources:
  - layer_range: [24, 25]
    model: Qwen/Qwen2.5-7B-Instruct
    parameters:
      scale:
      - filter: o_proj
        value: 0.0
      - filter: down_proj
        value: 0.0
      - value: 1.0
- sources:
  - layer_range: [24, 25]
    model: Qwen/Qwen2.5-7B-Instruct
    parameters:
      scale:
      - filter: o_proj
        value: 0.0
      - filter: down_proj
        value: 0.0
      - value: 1.0
- sources:
  - layer_range: [25, 26]
    model: Qwen/Qwen2.5-7B-Instruct
- sources:
  - layer_range: [25, 26]
    model: Qwen/Qwen2.5-7B-Instruct
    parameters:
      scale:
      - filter: o_proj
        value: 0.0
      - filter: down_proj
        value: 0.0
      - value: 1.0
- sources:
  - layer_range: [25, 26]
    model: Qwen/Qwen2.5-7B-Instruct
    parameters:
      scale:
      - filter: o_proj
        value: 0.0
      - filter: down_proj
        value: 0.0
      - value: 1.0
- sources:
  - layer_range: [26, 27]
    model: Qwen/Qwen2.5-7B-Instruct
- sources:
  - layer_range: [26, 27]
    model: Qwen/Qwen2.5-7B-Instruct
    parameters:
      scale:
      - filter: o_proj
        value: 0.0
      - filter: down_proj
        value: 0.0
      - value: 1.0
- sources:
  - layer_range: [26, 27]
    model: Qwen/Qwen2.5-7B-Instruct
    parameters:
      scale:
      - filter: o_proj
        value: 0.0
      - filter: down_proj
        value: 0.0
      - value: 1.0
- sources:
  - layer_range: [27, 28]
    model: Qwen/Qwen2.5-7B-Instruct
- sources:
  - layer_range: [27, 28]
    model: Qwen/Qwen2.5-7B-Instruct
    parameters:
      scale:
      - filter: o_proj
        value: 0.0
      - filter: down_proj
        value: 0.0
      - value: 1.0
- sources:
  - layer_range: [27, 28]
    model: Qwen/Qwen2.5-7B-Instruct
    parameters:
      scale:
      - filter: o_proj
        value: 0.0
      - filter: down_proj
        value: 0.0
      - value: 1.0
```
