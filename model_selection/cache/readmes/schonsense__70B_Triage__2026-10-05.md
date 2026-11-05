---
base_model:
- HPAI-BSC/Llama3.1-Aloe-Beta-70B
- Writer/Palmyra-Med-70B-32K
- sam-paech/Llama-3.3-70B-Instruct-ftpo_1k
- schonsense/IPOplectic
library_name: transformers
tags:
- mergekit
- merge
---
# sce_med

This is a merge of pre-trained language models created using [mergekit](https://github.com/cg123/mergekit).

## Merge Details
### Merge Method

This model was merged using the [SCE](https://arxiv.org/abs/2408.07990) merge method using [sam-paech/Llama-3.3-70B-Instruct-ftpo_1k](https://huggingface.co/sam-paech/Llama-3.3-70B-Instruct-ftpo_1k) as a base.

### Models Merged

The following models were included in the merge:
* [HPAI-BSC/Llama3.1-Aloe-Beta-70B](https://huggingface.co/HPAI-BSC/Llama3.1-Aloe-Beta-70B)
* [Writer/Palmyra-Med-70B-32K](https://huggingface.co/Writer/Palmyra-Med-70B-32K)
* [schonsense/IPOplectic](https://huggingface.co/schonsense/IPOplectic)

### Configuration

The following YAML configuration was used to produce this model:

```yaml
merge_method: sce
select_topk: 0.25


models:

  - model: sam-paech/Llama-3.3-70B-Instruct-ftpo_1k
  - model: HPAI-BSC/Llama3.1-Aloe-Beta-70B
  - model: Writer/Palmyra-Med-70B-32K
  - model: schonsense/IPOplectic


base_model: sam-paech/Llama-3.3-70B-Instruct-ftpo_1k

parameters:
  normalize: false
  int8_mask: true

dtype: float32
out_dtype: bfloat16

tokenizer:
  source: base
  pad_to_multiple_of: 8

```