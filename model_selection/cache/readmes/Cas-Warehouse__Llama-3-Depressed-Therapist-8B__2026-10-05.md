---
base_model:
- Casual-Autopsy/Llama-3-SOVL-MopeyMule-Blackroot-8B
- zementalist/llama-3-8B-chat-psychotherapist
- Casual-Autopsy/Llama-3-SOVL-MopeyMule-Blackroot-8B
- PrahmodhRaj/Llama-3_Psychiatrist_Chat
- Casual-Autopsy/Llama-3-SOVL-MopeyMule-Blackroot-8B
library_name: transformers
tags:
- mergekit
- merge

---
# merge

This is a merge of pre-trained language models created using [mergekit](https://github.com/cg123/mergekit).

## Merge Details
### Merge Method

This model was merged using the [Model Stock](https://arxiv.org/abs/2403.19522) merge method using [Casual-Autopsy/Llama-3-SOVL-MopeyMule-Blackroot-8B](https://huggingface.co/Casual-Autopsy/Llama-3-SOVL-MopeyMule-Blackroot-8B) as a base.

### Models Merged

The following models were included in the merge:
* [Casual-Autopsy/Llama-3-SOVL-MopeyMule-Blackroot-8B](https://huggingface.co/Casual-Autopsy/Llama-3-SOVL-MopeyMule-Blackroot-8B) + [zementalist/llama-3-8B-chat-psychotherapist](https://huggingface.co/zementalist/llama-3-8B-chat-psychotherapist)
* [Casual-Autopsy/Llama-3-SOVL-MopeyMule-Blackroot-8B](https://huggingface.co/Casual-Autopsy/Llama-3-SOVL-MopeyMule-Blackroot-8B) + [PrahmodhRaj/Llama-3_Psychiatrist_Chat](https://huggingface.co/PrahmodhRaj/Llama-3_Psychiatrist_Chat)

### Configuration

The following YAML configuration was used to produce this model:

```yaml
models:
  - model: Casual-Autopsy/Llama-3-SOVL-MopeyMule-Blackroot-8B+PrahmodhRaj/Llama-3_Psychiatrist_Chat
  - model: Casual-Autopsy/Llama-3-SOVL-MopeyMule-Blackroot-8B+zementalist/llama-3-8B-chat-psychotherapist
merge_method: model_stock
base_model: Casual-Autopsy/Llama-3-SOVL-MopeyMule-Blackroot-8B
dtype: bfloat16

```
