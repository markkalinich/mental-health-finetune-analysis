---
base_model:
- NousResearch/Meta-Llama-3-8B
library_name: transformers
tags:
- mergekit
- merge

---
# merge

This is a merge of pre-trained language models created using [mergekit](https://github.com/cg123/mergekit).

## Merge Details
### Merge Method

This model was merged using the passthrough merge method.

### Models Merged

The following models were included in the merge:
* [NousResearch/Meta-Llama-3-8B](https://huggingface.co/NousResearch/Meta-Llama-3-8B)

### Configuration

The following YAML configuration was used to produce this model:

```yaml
slices:
  - sources:
      - model: NousResearch/Meta-Llama-3-8B
        layer_range: [0, 21]
  - sources:
      - model: NousResearch/Meta-Llama-3-8B
        layer_range: [29,32]
            
merge_method: passthrough
dtype: bfloat16
```
