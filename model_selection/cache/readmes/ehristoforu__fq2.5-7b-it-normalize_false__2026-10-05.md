---
base_model:
- Qwen/Qwen2.5-7B-Instruct
- Bui1dMySea/LongRAG-Qwen2.5-7B-Instruct
- prithivMLmods/QwQ-MathOct-7B
- Krystalan/DRT-o1-7B
- prithivMLmods/QwQ-LCoT-7B-Instruct
- Orion-zhen/Qwen2.5-7B-Instruct-Uncensored
- Spestly/Athena-1-7B
- prithivMLmods/Deepthink-Reasoning-7B
- fblgit/cybertron-v4-qw7B-MGS
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

This model was merged using the [Model Stock](https://arxiv.org/abs/2403.19522) merge method using [Qwen/Qwen2.5-7B-Instruct](https://huggingface.co/Qwen/Qwen2.5-7B-Instruct) as a base.

### Models Merged

The following models were included in the merge:
* [Bui1dMySea/LongRAG-Qwen2.5-7B-Instruct](https://huggingface.co/Bui1dMySea/LongRAG-Qwen2.5-7B-Instruct)
* [prithivMLmods/QwQ-MathOct-7B](https://huggingface.co/prithivMLmods/QwQ-MathOct-7B)
* [Krystalan/DRT-o1-7B](https://huggingface.co/Krystalan/DRT-o1-7B)
* [prithivMLmods/QwQ-LCoT-7B-Instruct](https://huggingface.co/prithivMLmods/QwQ-LCoT-7B-Instruct)
* [Orion-zhen/Qwen2.5-7B-Instruct-Uncensored](https://huggingface.co/Orion-zhen/Qwen2.5-7B-Instruct-Uncensored)
* [Spestly/Athena-1-7B](https://huggingface.co/Spestly/Athena-1-7B)
* [prithivMLmods/Deepthink-Reasoning-7B](https://huggingface.co/prithivMLmods/Deepthink-Reasoning-7B)
* [fblgit/cybertron-v4-qw7B-MGS](https://huggingface.co/fblgit/cybertron-v4-qw7B-MGS)
* [Rombo-Org/Rombo-LLM-V2.5-Qwen-7b](https://huggingface.co/Rombo-Org/Rombo-LLM-V2.5-Qwen-7b)

### Configuration

The following YAML configuration was used to produce this model:

```yaml
models:
  - model: Rombo-Org/Rombo-LLM-V2.5-Qwen-7b
  - model: fblgit/cybertron-v4-qw7B-MGS
  - model: Spestly/Athena-1-7B
  - model: Orion-zhen/Qwen2.5-7B-Instruct-Uncensored
  - model: prithivMLmods/Deepthink-Reasoning-7B
  - model: prithivMLmods/QwQ-LCoT-7B-Instruct
  - model: prithivMLmods/QwQ-MathOct-7B
  - model: Bui1dMySea/LongRAG-Qwen2.5-7B-Instruct
  - model: Krystalan/DRT-o1-7B
merge_method: model_stock
base_model: Qwen/Qwen2.5-7B-Instruct
normalize: false
int8_mask: true
dtype: bfloat16
```
