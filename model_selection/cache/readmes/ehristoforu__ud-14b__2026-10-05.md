---
base_model:
- Qwen/Qwen2.5-32B
- Qwen/QwQ-32B-Preview
- unsloth/DeepSeek-R1-Distill-Qwen-32B
library_name: transformers
tags:
- mergekit
- merge

---
# merge

This is a merge of pre-trained language models created using [mergekit](https://github.com/cg123/mergekit).

## Merge Details
### Merge Method

This model was merged using the [TIES](https://arxiv.org/abs/2306.01708) merge method using [Qwen/Qwen2.5-32B](https://huggingface.co/Qwen/Qwen2.5-32B) as a base.

### Models Merged

The following models were included in the merge:
* [Qwen/QwQ-32B-Preview](https://huggingface.co/Qwen/QwQ-32B-Preview)
* [unsloth/DeepSeek-R1-Distill-Qwen-32B](https://huggingface.co/unsloth/DeepSeek-R1-Distill-Qwen-32B)

### Configuration

The following YAML configuration was used to produce this model:

```yaml
models:
  - model: unsloth/DeepSeek-R1-Distill-Qwen-32B
    parameters:
      weight: 0.65
      density: 0.65
  - model: Qwen/QwQ-32B-Preview
    parameters:
      weight: 0.35
      density: 0.35
merge_method: ties
base_model: Qwen/Qwen2.5-32B
parameters:
  normalize: true
  int8_mask: true
tokenizer_source: "unsloth/DeepSeek-R1-Distill-Qwen-32B"
dtype: float16
```
