---
base_model:
- Novaciano/Gemma3-UNCENSORED-V2-1B
- Movidlona/gemma_1b_full_emotion_finetuned
library_name: transformers
tags:
- mergekit
- merge

---
# merge

This is a merge of pre-trained language models created using [mergekit](https://github.com/cg123/mergekit).

## Merge Details

**RECOMMENDED:** Use the Assistant Jailbreak of Kobold AI.

### Merge Method

This model was merged using the [SLERP](https://en.wikipedia.org/wiki/Slerp) merge method.

### Models Merged

The following models were included in the merge:
* [Novaciano/Gemma3-UNCENSORED-V2-1B](https://huggingface.co/Novaciano/Gemma3-UNCENSORED-V2-1B)
* [Movidlona/gemma_1b_full_emotion_finetuned](https://huggingface.co/Movidlona/gemma_1b_full_emotion_finetuned)

### Configuration

The following YAML configuration was used to produce this model:

```yaml
merge_method: slerp
base_model: Novaciano/Gemma3-UNCENSORED-V2-1B
dtype: bfloat16
out_dtype: bfloat16

models:
  - model: Movidlona/gemma_1b_full_emotion_finetuned
    weight: 0.6

parameters:
  normalize: true
  rescale: true
  t: 0.6
```
