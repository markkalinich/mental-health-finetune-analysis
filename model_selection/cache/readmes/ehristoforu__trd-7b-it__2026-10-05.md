---
base_model:
- Qwen/Qwen2.5-7B-Instruct
- unsloth/DeepSeek-R1-Distill-Qwen-7B
library_name: transformers
tags:
- mergekit
- merge

---
# merge

This is a merge of pre-trained language models created using [mergekit](https://github.com/cg123/mergekit).

## Merge Details
### Merge Method

This model was merged using the [TIES](https://arxiv.org/abs/2306.01708) merge method using [Qwen/Qwen2.5-7B-Instruct](https://huggingface.co/Qwen/Qwen2.5-7B-Instruct) as a base.

### Models Merged

The following models were included in the merge:
* [unsloth/DeepSeek-R1-Distill-Qwen-7B](https://huggingface.co/unsloth/DeepSeek-R1-Distill-Qwen-7B)

### Configuration

The following YAML configuration was used to produce this model:

```yaml
base_model: Qwen/Qwen2.5-7B-Instruct
models:
  - model: unsloth/DeepSeek-R1-Distill-Qwen-7B
    parameters:
      weight: 1
  - model: Qwen/Qwen2.5-7B-Instruct
    parameters:
      weight: 1
merge_method: ties
parameters:
  normalize: true
  int8_mask: true
tokenizer_source: "Qwen/Qwen2.5-7B-Instruct"
dtype: float16

```
