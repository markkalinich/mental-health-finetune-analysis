---
base_model:
- huihui-ai/QwQ-32B-Preview-abliterated
- Qwen/QwQ-32B-Preview
- Qwen/Qwen2.5-Coder-32B-Instruct
- rombodawg/Rombos-LLM-V2.5-Qwen-32b
library_name: transformers
tags:
- mergekit
- merge

---
# merge

This is a merge of pre-trained language models created using [mergekit](https://github.com/cg123/mergekit).

## Merge Details
### Merge Method

This model was merged using the [TIES](https://arxiv.org/abs/2306.01708) merge method using [Qwen/QwQ-32B-Preview](https://huggingface.co/Qwen/QwQ-32B-Preview) as a base.

### Models Merged

The following models were included in the merge:
* [huihui-ai/QwQ-32B-Preview-abliterated](https://huggingface.co/huihui-ai/QwQ-32B-Preview-abliterated)
* [Qwen/Qwen2.5-Coder-32B-Instruct](https://huggingface.co/Qwen/Qwen2.5-Coder-32B-Instruct)
* [rombodawg/Rombos-LLM-V2.5-Qwen-32b](https://huggingface.co/rombodawg/Rombos-LLM-V2.5-Qwen-32b)

### Configuration

The following YAML configuration was used to produce this model:

```yaml
models:
  - model: Qwen/QwQ-32B-Preview
    parameters:
      density: 1.0
      weight: 1.0
  - model: huihui-ai/QwQ-32B-Preview-abliterated
    parameters:
      density: 1.0
      weight: 1.0
  - model: rombodawg/Rombos-LLM-V2.5-Qwen-32b
    parameters:
      density: 1.0
      weight: 1.0  
  - model: Qwen/Qwen2.5-Coder-32B-Instruct
    parameters:
      density: 1.0
      weight: 1.0  

merge_method: ties
base_model: Qwen/QwQ-32B-Preview
parameters:
  normalize: true
  int8_mask: true
dtype: bfloat16
tokenizer_source: union

```
