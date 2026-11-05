---
base_model:
- Casual-Autopsy/Llama-3-Mental-Therapy-Cat-8B
- PrahmodhRaj/Llama-3_Psychiatrist_Chat
- zementalist/llama-3-8B-chat-psychotherapist
- Falah/lora_model_mental_health_llama3
- Abdo36/MentalLORALLAMA3
library_name: transformers
tags:
- mergekit
- merge

---
# merge

This is a merge of pre-trained language models created using [mergekit](https://github.com/cg123/mergekit).

## Merge Details
### Merge Method

This model was merged using the [Model Stock](https://arxiv.org/abs/2403.19522) merge method using [Casual-Autopsy/Llama-3-Mental-Therapy-Cat-8B](https://huggingface.co/Casual-Autopsy/Llama-3-Mental-Therapy-Cat-8B) as a base.

### Models Merged

The following models were included in the merge:
* [Casual-Autopsy/Llama-3-Mental-Therapy-Cat-8B](https://huggingface.co/Casual-Autopsy/Llama-3-Mental-Therapy-Cat-8B) + [PrahmodhRaj/Llama-3_Psychiatrist_Chat](https://huggingface.co/PrahmodhRaj/Llama-3_Psychiatrist_Chat)
* [Casual-Autopsy/Llama-3-Mental-Therapy-Cat-8B](https://huggingface.co/Casual-Autopsy/Llama-3-Mental-Therapy-Cat-8B) + [zementalist/llama-3-8B-chat-psychotherapist](https://huggingface.co/zementalist/llama-3-8B-chat-psychotherapist)
* [Casual-Autopsy/Llama-3-Mental-Therapy-Cat-8B](https://huggingface.co/Casual-Autopsy/Llama-3-Mental-Therapy-Cat-8B) + [Falah/lora_model_mental_health_llama3](https://huggingface.co/Falah/lora_model_mental_health_llama3)
* [Casual-Autopsy/Llama-3-Mental-Therapy-Cat-8B](https://huggingface.co/Casual-Autopsy/Llama-3-Mental-Therapy-Cat-8B) + [Abdo36/MentalLORALLAMA3](https://huggingface.co/Abdo36/MentalLORALLAMA3)

### Configuration

The following YAML configuration was used to produce this model:

```yaml
models:
  - model: Casual-Autopsy/Llama-3-Mental-Therapy-Cat-8B+Falah/lora_model_mental_health_llama3
  - model: Casual-Autopsy/Llama-3-Mental-Therapy-Cat-8B+Abdo36/MentalLORALLAMA3
  - model: Casual-Autopsy/Llama-3-Mental-Therapy-Cat-8B+zementalist/llama-3-8B-chat-psychotherapist
  - model: Casual-Autopsy/Llama-3-Mental-Therapy-Cat-8B+PrahmodhRaj/Llama-3_Psychiatrist_Chat
merge_method: model_stock
base_model: Casual-Autopsy/Llama-3-Mental-Therapy-Cat-8B
dtype: bfloat16

```
