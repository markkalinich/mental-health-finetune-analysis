---
base_model:
- Novaciano/Varuna_Uncensored-3.2-1B
- Novaciano/PHOEBE_SENTIMENTAL-RP-NSFW-3.2-1B
library_name: transformers
tags:
- mergekit
- merge

---
# merge

This is a merge of pre-trained language models created using [mergekit](https://github.com/cg123/mergekit).

## Merge Details
### Merge Method

This model was merged using the [Arcee Fusion](https://arcee.ai) merge method using [Novaciano/PHOEBE_SENTIMENTAL-RP-NSFW-3.2-1B](https://huggingface.co/Novaciano/PHOEBE_SENTIMENTAL-RP-NSFW-3.2-1B) as a base.

### Models Merged

The following models were included in the merge:
* [Novaciano/Varuna_Uncensored-3.2-1B](https://huggingface.co/Novaciano/Varuna_Uncensored-3.2-1B)

### Configuration

The following YAML configuration was used to produce this model:

```yaml
dtype: float32
out_dtype: bfloat16
merge_method: arcee_fusion
base_model: Novaciano/PHOEBE_SENTIMENTAL-RP-NSFW-3.2-1B
models:
    - model: Novaciano/PHOEBE_SENTIMENTAL-RP-NSFW-3.2-1B
      parameters:
        weight:
          - filter: mlp
            value: [1, 2]
          - value: 1
    - model: Novaciano/Varuna_Uncensored-3.2-1B
      parameters:
        weight:
          - filter: lm_head
            value: 1
          - value: [1, 0.5]
```
