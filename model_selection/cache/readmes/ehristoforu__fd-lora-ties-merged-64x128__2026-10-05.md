---
base_model:
- ehristoforu/fd-lora-merged-64x128
- deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B
library_name: transformers
tags:
- mergekit
- merge

---
# merge

This is a merge of pre-trained language models created using [mergekit](https://github.com/cg123/mergekit).

## Merge Details
### Merge Method

This model was merged using the [TIES](https://arxiv.org/abs/2306.01708) merge method using [deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B) as a base.

### Models Merged

The following models were included in the merge:
* [ehristoforu/fd-lora-merged-64x128](https://huggingface.co/ehristoforu/fd-lora-merged-64x128)

### Configuration

The following YAML configuration was used to produce this model:

```yaml
models:
  - model: ehristoforu/fd-lora-merged-64x128
    parameters:
      weight: 1
  - model: deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B
    parameters:
      weight: 1
merge_method: ties
base_model: deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B
parameters:
  normalize: true
  int8_mask: true
tokenizer_source: "deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B"
dtype: float16
```
