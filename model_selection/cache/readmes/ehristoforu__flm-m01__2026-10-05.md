---
base_model:
- Gaivoronsky/Mistral-7B-Saiga
- NousResearch/Yarn-Mistral-7b-128k
- ajibawa-2023/Code-Mistral-7B
- OpenBuddy/openbuddy-mistral2-7b-v20.3-32k
- HuggingFaceH4/mistral-7b-anthropic
- meta-math/MetaMath-Mistral-7B
library_name: transformers
tags:
- mergekit
- merge

---
# merge

This is a merge of pre-trained language models created using [mergekit](https://github.com/cg123/mergekit).

## Merge Details
### Merge Method

This model was merged using the [Model Stock](https://arxiv.org/abs/2403.19522) merge method using [OpenBuddy/openbuddy-mistral2-7b-v20.3-32k](https://huggingface.co/OpenBuddy/openbuddy-mistral2-7b-v20.3-32k) as a base.

### Models Merged

The following models were included in the merge:
* [Gaivoronsky/Mistral-7B-Saiga](https://huggingface.co/Gaivoronsky/Mistral-7B-Saiga)
* [NousResearch/Yarn-Mistral-7b-128k](https://huggingface.co/NousResearch/Yarn-Mistral-7b-128k)
* [ajibawa-2023/Code-Mistral-7B](https://huggingface.co/ajibawa-2023/Code-Mistral-7B)
* [HuggingFaceH4/mistral-7b-anthropic](https://huggingface.co/HuggingFaceH4/mistral-7b-anthropic)
* [meta-math/MetaMath-Mistral-7B](https://huggingface.co/meta-math/MetaMath-Mistral-7B)

### Configuration

The following YAML configuration was used to produce this model:

```yaml
models:
  - model: Gaivoronsky/Mistral-7B-Saiga
  - model: OpenBuddy/openbuddy-mistral2-7b-v20.3-32k
  - model: meta-math/MetaMath-Mistral-7B
  - model: HuggingFaceH4/mistral-7b-anthropic
  - model: NousResearch/Yarn-Mistral-7b-128k
  - model: ajibawa-2023/Code-Mistral-7B
merge_method: model_stock
base_model: OpenBuddy/openbuddy-mistral2-7b-v20.3-32k
dtype: bfloat16
```
