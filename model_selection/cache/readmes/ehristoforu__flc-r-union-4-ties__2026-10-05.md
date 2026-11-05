---
base_model:
- Qwen/Qwen2.5-3B-Instruct
- ehristoforu/flc-r-0004-lora
- Qwen/Qwen2.5-3B
- Qwen/Qwen2.5-3B-Instruct
- Qwen/Qwen2.5-3B-Instruct
- ehristoforu/flc-r-0001-lora
- Qwen/Qwen2.5-3B-Instruct
- ehristoforu/flc-r-0002-lora
- Qwen/Qwen2.5-3B-Instruct
- ehristoforu/flc-r-0003-lora
library_name: transformers
tags:
- mergekit
- merge

---
# merge

This is a merge of pre-trained language models created using [mergekit](https://github.com/cg123/mergekit).

## Merge Details
### Merge Method

This model was merged using the [TIES](https://arxiv.org/abs/2306.01708) merge method using [Qwen/Qwen2.5-3B](https://huggingface.co/Qwen/Qwen2.5-3B) as a base.

### Models Merged

The following models were included in the merge:
* [Qwen/Qwen2.5-3B-Instruct](https://huggingface.co/Qwen/Qwen2.5-3B-Instruct) + [ehristoforu/flc-r-0004-lora](https://huggingface.co/ehristoforu/flc-r-0004-lora)
* [Qwen/Qwen2.5-3B-Instruct](https://huggingface.co/Qwen/Qwen2.5-3B-Instruct)
* [Qwen/Qwen2.5-3B-Instruct](https://huggingface.co/Qwen/Qwen2.5-3B-Instruct) + [ehristoforu/flc-r-0001-lora](https://huggingface.co/ehristoforu/flc-r-0001-lora)
* [Qwen/Qwen2.5-3B-Instruct](https://huggingface.co/Qwen/Qwen2.5-3B-Instruct) + [ehristoforu/flc-r-0002-lora](https://huggingface.co/ehristoforu/flc-r-0002-lora)
* [Qwen/Qwen2.5-3B-Instruct](https://huggingface.co/Qwen/Qwen2.5-3B-Instruct) + [ehristoforu/flc-r-0003-lora](https://huggingface.co/ehristoforu/flc-r-0003-lora)

### Configuration

The following YAML configuration was used to produce this model:

```yaml
models:
  - model: Qwen/Qwen2.5-3B-Instruct+ehristoforu/flc-r-0001-lora
    parameters:
      weight: 1
      density: 1
  - model: Qwen/Qwen2.5-3B-Instruct+ehristoforu/flc-r-0002-lora
    parameters:
      weight: 1
      density: 1
  - model: Qwen/Qwen2.5-3B-Instruct+ehristoforu/flc-r-0003-lora
    parameters:
      weight: 1
      density: 1
  - model: Qwen/Qwen2.5-3B-Instruct+ehristoforu/flc-r-0004-lora
    parameters:
      weight: 1
      density: 1
  - model: Qwen/Qwen2.5-3B-Instruct
    parameters:
      weight: 1
      density: 1
merge_method: ties
base_model: Qwen/Qwen2.5-3B
parameters:
  weight: 1
  density: 1
  normalize: true
  int8_mask: true
tokenizer_source: Qwen/Qwen2.5-3B-Instruct
dtype: float16


```
