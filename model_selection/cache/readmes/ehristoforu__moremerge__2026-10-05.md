---
base_model:
- Qwen/Qwen2.5-7B-Instruct
- EVA-UNIT-01/EVA-Qwen2.5-7B-v0.1
- HumanLLMs/Human-Like-Qwen2.5-7B-Instruct
- Qwen/Qwen2.5-7B-Instruct-1M
- Qwen/Qwen2.5-Math-7B
- deepseek-ai/DeepSeek-R1-Distill-Qwen-7B
- Qwen/Qwen2.5-Coder-7B
- fblgit/cybertron-v4-qw7B-UNAMGS
- prithivMLmods/QwQ-LCoT2-7B-Instruct
- huihui-ai/Qwen2.5-7B-Instruct-abliterated
- Rombo-Org/Rombo-LLM-V2.5-Qwen-7b
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
* [EVA-UNIT-01/EVA-Qwen2.5-7B-v0.1](https://huggingface.co/EVA-UNIT-01/EVA-Qwen2.5-7B-v0.1)
* [HumanLLMs/Human-Like-Qwen2.5-7B-Instruct](https://huggingface.co/HumanLLMs/Human-Like-Qwen2.5-7B-Instruct)
* [Qwen/Qwen2.5-7B-Instruct-1M](https://huggingface.co/Qwen/Qwen2.5-7B-Instruct-1M)
* [Qwen/Qwen2.5-Math-7B](https://huggingface.co/Qwen/Qwen2.5-Math-7B)
* [deepseek-ai/DeepSeek-R1-Distill-Qwen-7B](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-7B)
* [Qwen/Qwen2.5-Coder-7B](https://huggingface.co/Qwen/Qwen2.5-Coder-7B)
* [fblgit/cybertron-v4-qw7B-UNAMGS](https://huggingface.co/fblgit/cybertron-v4-qw7B-UNAMGS)
* [prithivMLmods/QwQ-LCoT2-7B-Instruct](https://huggingface.co/prithivMLmods/QwQ-LCoT2-7B-Instruct)
* [huihui-ai/Qwen2.5-7B-Instruct-abliterated](https://huggingface.co/huihui-ai/Qwen2.5-7B-Instruct-abliterated)
* [Rombo-Org/Rombo-LLM-V2.5-Qwen-7b](https://huggingface.co/Rombo-Org/Rombo-LLM-V2.5-Qwen-7b)

### Configuration

The following YAML configuration was used to produce this model:

```yaml
models:
  - model: Qwen/Qwen2.5-Math-7B
    parameters:
      weight: 1
  - model: Qwen/Qwen2.5-Coder-7B
    parameters:
      weight: 1
  - model: Qwen/Qwen2.5-7B-Instruct-1M
    parameters:
      weight: 1
  - model: EVA-UNIT-01/EVA-Qwen2.5-7B-v0.1
    parameters:
      weight: 1
  - model: deepseek-ai/DeepSeek-R1-Distill-Qwen-7B
    parameters:
      weight: 1
  - model: HumanLLMs/Human-Like-Qwen2.5-7B-Instruct
    parameters:
      weight: 1
  - model: fblgit/cybertron-v4-qw7B-UNAMGS
    parameters:
      weight: 1
  - model: Rombo-Org/Rombo-LLM-V2.5-Qwen-7b
    parameters:
      weight: 1
  - model: huihui-ai/Qwen2.5-7B-Instruct-abliterated
    parameters:
      weight: 1
  - model: prithivMLmods/QwQ-LCoT2-7B-Instruct
    parameters:
      weight: 1
merge_method: ties
base_model: Qwen/Qwen2.5-7B-Instruct
parameters:
  normalize: true
  int8_mask: true
tokenizer_source: Qwen/Qwen2.5-7B-Instruct
dtype: bfloat16
```
