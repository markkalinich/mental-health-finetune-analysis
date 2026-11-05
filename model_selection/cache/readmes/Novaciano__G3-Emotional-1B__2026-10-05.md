---
base_model:
- UmbrellaInc/T-Virus.Veronica-1B
- Novaciano/Gemma3-Emotional-1B
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
* [UmbrellaInc/T-Virus.Veronica-1B](https://huggingface.co/UmbrellaInc/T-Virus.Veronica-1B)
* [Novaciano/Gemma3-Emotional-1B](https://huggingface.co/Novaciano/Gemma3-Emotional-1B)

### Configuration

The following YAML configuration was used to produce this model:

```yaml
merge_method: slerp
base_model: Novaciano/Gemma3-Emotional-1B
dtype: bfloat16
out_dtype: bfloat16

models:
  - model: Novaciano/Gemma3-Emotional-1B
    
  - model: UmbrellaInc/T-Virus.Veronica-1B

parameters:
  t:
    - 0.95
    
    - 0.85
```
