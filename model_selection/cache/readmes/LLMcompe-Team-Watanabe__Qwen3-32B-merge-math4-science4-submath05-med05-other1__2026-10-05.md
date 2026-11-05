---
base_model:
- LLMcompe-Team-Watanabe/Qwen3-32B-textbookreasoning-UGPhysics-AoPsInstruct-sft
- LLMcompe-Team-Watanabe/Qwen3-32B-sft-deepscaler-openr1-havard-40k-1ep-lr5e6-8k
- LLMcompe-Team-Watanabe/Qwen3-32B-sft-HIS-Chem-Engineering-45k-1ep-lr5e6-4096
- LLMcompe-Team-Watanabe/others_second_stage
- Qwen/Qwen3-32B
- LLMcompe-Team-Watanabe/Qwen3-32B-openmathreasoning-sft
library_name: transformers
tags:
- mergekit
- merge

---
# output_model

This is a merge of pre-trained language models created using [mergekit](https://github.com/cg123/mergekit).

## Merge Details
### Merge Method

This model was merged using the [DARE TIES](https://arxiv.org/abs/2311.03099) merge method using [Qwen/Qwen3-32B](https://huggingface.co/Qwen/Qwen3-32B) as a base.

### Models Merged

The following models were included in the merge:
* [LLMcompe-Team-Watanabe/Qwen3-32B-textbookreasoning-UGPhysics-AoPsInstruct-sft](https://huggingface.co/LLMcompe-Team-Watanabe/Qwen3-32B-textbookreasoning-UGPhysics-AoPsInstruct-sft)
* [LLMcompe-Team-Watanabe/Qwen3-32B-sft-deepscaler-openr1-havard-40k-1ep-lr5e6-8k](https://huggingface.co/LLMcompe-Team-Watanabe/Qwen3-32B-sft-deepscaler-openr1-havard-40k-1ep-lr5e6-8k)
* [LLMcompe-Team-Watanabe/Qwen3-32B-sft-HIS-Chem-Engineering-45k-1ep-lr5e6-4096](https://huggingface.co/LLMcompe-Team-Watanabe/Qwen3-32B-sft-HIS-Chem-Engineering-45k-1ep-lr5e6-4096)
* [LLMcompe-Team-Watanabe/others_second_stage](https://huggingface.co/LLMcompe-Team-Watanabe/others_second_stage)
* [LLMcompe-Team-Watanabe/Qwen3-32B-openmathreasoning-sft](https://huggingface.co/LLMcompe-Team-Watanabe/Qwen3-32B-openmathreasoning-sft)

### Configuration

The following YAML configuration was used to produce this model:

```yaml
models:
  - model: Qwen/Qwen3-32B
  - model: LLMcompe-Team-Watanabe/Qwen3-32B-textbookreasoning-UGPhysics-AoPsInstruct-sft
    parameters:
      density: 0.53
      weight: 0.4
  - model: LLMcompe-Team-Watanabe/Qwen3-32B-openmathreasoning-sft
    parameters:
      density: 0.53
      weight: 0.4
  - model: LLMcompe-Team-Watanabe/Qwen3-32B-sft-deepscaler-openr1-havard-40k-1ep-lr5e6-8k
    parameters:
      density: 0.53
      weight: 0.05
  - model: LLMcompe-Team-Watanabe/others_second_stage
    parameters:
      density: 0.53
      weight: 0.05
  - model: LLMcompe-Team-Watanabe/Qwen3-32B-sft-HIS-Chem-Engineering-45k-1ep-lr5e6-4096
    parameters:
      density: 0.53
      weight: 0.1
merge_method: dare_ties
base_model: Qwen/Qwen3-32B
parameters:
  int8_mask: true
  normalize: false
dtype: bfloat16 
```
