---
base_model:
- OpenBuddy/openbuddy-mistral2-7b-v20.3-32k
- ajibawa-2023/Code-Mistral-7B
- HuggingFaceH4/mistral-7b-grok
- Gaivoronsky/Mistral-7B-Saiga
- NousResearch/Yarn-Mistral-7b-128k
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
* [OpenBuddy/openbuddy-mistral2-7b-v20.3-32k](https://huggingface.co/OpenBuddy/openbuddy-mistral2-7b-v20.3-32k)
* [ajibawa-2023/Code-Mistral-7B](https://huggingface.co/ajibawa-2023/Code-Mistral-7B)
* [HuggingFaceH4/mistral-7b-grok](https://huggingface.co/HuggingFaceH4/mistral-7b-grok)
* [Gaivoronsky/Mistral-7B-Saiga](https://huggingface.co/Gaivoronsky/Mistral-7B-Saiga)
* [NousResearch/Yarn-Mistral-7b-128k](https://huggingface.co/NousResearch/Yarn-Mistral-7b-128k)

### Configuration

The following YAML configuration was used to produce this model:

```yaml
slices:
  - sources:
    - model: Gaivoronsky/Mistral-7B-Saiga
      layer_range: [0, 32]
  - sources:
    - model: HuggingFaceH4/mistral-7b-grok
      layer_range: [24, 32]
  - sources:
    - model: NousResearch/Yarn-Mistral-7b-128k
      layer_range: [26, 32]
  - sources:
    - model: OpenBuddy/openbuddy-mistral2-7b-v20.3-32k
      layer_range: [26, 32]
  - sources:
    - model: ajibawa-2023/Code-Mistral-7B
      layer_range: [28, 32]
merge_method: passthrough
dtype: bfloat16

```
