---
base_model:
- Movidlona/gemma_1b_full_emotion_finetuned
- Novaciano/Gemma3-UNCENSORED-V2-1B
library_name: transformers
tags:
- mergekit
- merge

---
# merge

This is a merge of pre-trained language models created using [mergekit](https://github.com/cg123/mergekit).

## Merge Details
### Merge Method

This model was merged using the [SLERP](https://en.wikipedia.org/wiki/Slerp) merge method.

### Models Merged

The following models were included in the merge:
* [Movidlona/gemma_1b_full_emotion_finetuned](https://huggingface.co/Movidlona/gemma_1b_full_emotion_finetuned)
* [Novaciano/Gemma3-UNCENSORED-V2-1B](https://huggingface.co/Novaciano/Gemma3-UNCENSORED-V2-1B)

### Configuration

The following YAML configuration was used to produce this model:

```yaml
merge_method: slerp
base_model: Movidlona/gemma_1b_full_emotion_finetuned
dtype: bfloat16
out_dtype: bfloat16

models:
  - model: Novaciano/Gemma3-UNCENSORED-V2-1B
    weight: 0.6

parameters:
  normalize: true
  rescale: true
  t: 0.6
```
