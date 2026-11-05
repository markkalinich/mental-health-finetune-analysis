---
base_model:
- ruslanmv/ai-medical-model-32bit
- Locutusque/Llama-3-Hercules-5.0-8B
- refuelai/Llama-3-Refueled
library_name: transformers
tags:
- mergekit
- merge
- medical
- custom
license: mit
language:
- en
datasets:
 - ruslanmv/ai-medical-chatbot
 - Locutusque/hercules-v5.0
---
# Medichat-V2-Llama3-8B 

This is a merge of pre-trained language models created using [mergekit](https://github.com/cg123/mergekit).

This model is particularly effective in **structuring** the unstructured clinical texts.

### Model Composition and Features:
1. **Base Model**: The foundation of this model is based on "refuelai/Llama-3-Refueled," which itself is a refined version of the Llama3-8B model, renowned for its instruction-following capabilities and adaptability across various domains.

2. **Merged Models**:
   - **ruslanmv/ai-medical-model-32bit**: A model fine-tuned specifically for answering technical medical questions, providing a solid base of medical knowledge.
   - **Locutusque/Llama-3-Hercules-5.0-8B**: Known for its ability to follow complex instructions and handle conversational interactions effectively, especially in scientific and technical contexts.

This model was merged using the [DARE](https://arxiv.org/abs/2311.03099) [TIES](https://arxiv.org/abs/2306.01708) merge method using [refuelai/Llama-3-Refueled](https://huggingface.co/refuelai/Llama-3-Refueled) as a base.

### Models Merged

The following models were included in the merge:
* [ruslanmv/ai-medical-model-32bit](https://huggingface.co/ruslanmv/ai-medical-model-32bit)
* [Locutusque/Llama-3-Hercules-5.0-8B](https://huggingface.co/Locutusque/Llama-3-Hercules-5.0-8B)

### Configuration

The following YAML configuration was used to produce this model:

```yaml


models:
  - model: Locutusque/Llama-3-Hercules-5.0-8B
    parameters:
      weight: [0.25, 0.45, 0.35, 0.45, 0.25]
      density: [0.1, 0.25, 0.5, 0.25, 0.1]
  - model: refuelai/Llama-3-Refueled
  - model: ruslanmv/ai-medical-model-32bit
    parameters:
      weight: [0.55, 0.45, 0.25, 0.45, 0.55]
      density: [0.1, 0.25, 0.5, 0.25, 0.1]
merge_method: dare_ties
base_model: refuelai/Llama-3-Refueled
parameters:
  int8_mask: true
dtype: bfloat16

```