---
base_model:
- prithivMLmods/Phi-4-QwQ
- bunnycore/Phi-4-RP-V0.2
- unsloth/phi-4
- prithivMLmods/Phi-4-Empathetic
- mudler/LocalAI-functioncall-phi-4-v0.3
- Pinkstack/SuperThoughts-CoT-14B-16k-o1-QwQ
- prithivMLmods/Phi-4-o1
- prithivMLmods/Phi-4-Math-IO
library_name: transformers
tags:
- mergekit
- merge

---
# merge

This is a merge of pre-trained language models created using [mergekit](https://github.com/cg123/mergekit).

## Merge Details
### Merge Method

This model was merged using the [Model Stock](https://arxiv.org/abs/2403.19522) merge method using [unsloth/phi-4](https://huggingface.co/unsloth/phi-4) as a base.

### Models Merged

The following models were included in the merge:
* [prithivMLmods/Phi-4-QwQ](https://huggingface.co/prithivMLmods/Phi-4-QwQ)
* [bunnycore/Phi-4-RP-V0.2](https://huggingface.co/bunnycore/Phi-4-RP-V0.2)
* [prithivMLmods/Phi-4-Empathetic](https://huggingface.co/prithivMLmods/Phi-4-Empathetic)
* [mudler/LocalAI-functioncall-phi-4-v0.3](https://huggingface.co/mudler/LocalAI-functioncall-phi-4-v0.3)
* [Pinkstack/SuperThoughts-CoT-14B-16k-o1-QwQ](https://huggingface.co/Pinkstack/SuperThoughts-CoT-14B-16k-o1-QwQ)
* [prithivMLmods/Phi-4-o1](https://huggingface.co/prithivMLmods/Phi-4-o1)
* [prithivMLmods/Phi-4-Math-IO](https://huggingface.co/prithivMLmods/Phi-4-Math-IO)

### Configuration

The following YAML configuration was used to produce this model:

```yaml
models:
  - model: unsloth/phi-4
  - model: prithivMLmods/Phi-4-o1
  - model: prithivMLmods/Phi-4-Math-IO
  - model: prithivMLmods/Phi-4-QwQ
  - model: Pinkstack/SuperThoughts-CoT-14B-16k-o1-QwQ
  - model: mudler/LocalAI-functioncall-phi-4-v0.3
  - model: bunnycore/Phi-4-RP-V0.2
  - model: prithivMLmods/Phi-4-Empathetic
merge_method: model_stock
base_model: unsloth/phi-4
parameters:
  normalize: false
  int8_mask: true
dtype: bfloat16
tokenizer_source: "unsloth/phi-4"

```
