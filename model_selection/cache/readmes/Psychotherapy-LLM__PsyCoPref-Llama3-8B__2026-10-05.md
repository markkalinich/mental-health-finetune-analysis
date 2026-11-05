---
license: cc-by-nc-4.0
library_name: transformers
pipeline_tag: text-generation
datasets:
- Psychotherapy-LLM/PsychoCounsel-Preference
base_model:
- meta-llama/Llama-3.1-8B-Instruct
---

This model is presented in the paper [Preference Learning Unlocks LLMs' Psycho-Counseling Skills](https://hf.co/papers/2502.19731). It's a fine-tuned [meta-llama/Llama-3.1-8B-Instruct](https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct) model trained using preference learning on the [PsyCoPref](https://huggingface.co/datasets/Psychotherapy-LLM/PsychoCounsel-Preference) dataset. This dataset contains 36k high-quality preference comparison pairs aligned with the preferences of professional psychotherapists.

The model aims to improve the quality of responses in psycho-counseling sessions and achieves a win rate of 87% against GPT-4o.


This usage is the same as [meta-llama/Llama-3.1-8B-Instruct](https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct)