---
base_model:
- NousResearch/Hermes-3-Llama-3.1-8B
- Skywork/Skywork-o1-Open-Llama-3.1-8B
- cognitivecomputations/dolphin-2.9.4-llama3.1-8b
- SimpleBerry/LLaMA-O1-Base-1127
- unsloth/Meta-Llama-3.1-8B-Instruct
- arcee-ai/Llama-3.1-SuperNova-Lite
library_name: transformers
tags:
- mergekit
- merge

---
# merge

This is a merge of pre-trained language models created using [mergekit](https://github.com/cg123/mergekit).

## Merge Details
### Merge Method

This model was merged using the [TIES](https://arxiv.org/abs/2306.01708) merge method using [unsloth/Meta-Llama-3.1-8B-Instruct](https://huggingface.co/unsloth/Meta-Llama-3.1-8B-Instruct) as a base.

### Models Merged

The following models were included in the merge:
* [NousResearch/Hermes-3-Llama-3.1-8B](https://huggingface.co/NousResearch/Hermes-3-Llama-3.1-8B)
* [Skywork/Skywork-o1-Open-Llama-3.1-8B](https://huggingface.co/Skywork/Skywork-o1-Open-Llama-3.1-8B)
* [cognitivecomputations/dolphin-2.9.4-llama3.1-8b](https://huggingface.co/cognitivecomputations/dolphin-2.9.4-llama3.1-8b)
* [SimpleBerry/LLaMA-O1-Base-1127](https://huggingface.co/SimpleBerry/LLaMA-O1-Base-1127)
* [arcee-ai/Llama-3.1-SuperNova-Lite](https://huggingface.co/arcee-ai/Llama-3.1-SuperNova-Lite)

### Configuration

The following YAML configuration was used to produce this model:

```yaml
models:
  - model: unsloth/Meta-Llama-3.1-8B-Instruct
    #no parameters necessary for base model
  - model: NousResearch/Hermes-3-Llama-3.1-8B
    parameters:
      density: 0.5
      weight: 0.5
  - model: Skywork/Skywork-o1-Open-Llama-3.1-8B
    parameters:
      density: 0.5
      weight: 0.5
  - model: arcee-ai/Llama-3.1-SuperNova-Lite
    parameters:
      density: 0.5
      weight: 0.5
  - model: cognitivecomputations/dolphin-2.9.4-llama3.1-8b
    parameters:
      density: 0.5
      weight: 0.5
  - model: SimpleBerry/LLaMA-O1-Base-1127
    parameters:
      density: 0.5
      weight: 0.5

merge_method: ties
base_model: unsloth/Meta-Llama-3.1-8B-Instruct
parameters:
  normalize: false
  int8_mask: true
dtype: bfloat16

```
