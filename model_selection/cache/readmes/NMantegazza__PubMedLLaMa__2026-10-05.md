---
library_name: transformers
tags:
- text-generation-inference
license: llama2
datasets:
- qiaojin/PubMedQA
metrics:
- bertscore
- accuracy
- rouge
base_model:
- meta-llama/Llama-2-7b-hf
---

# Model Card for Model ID

This model is a fine-tuned version of the LLaMA 2 7B model on the PubMedQA dataset. It is designed for biomedical question answering tasks, particularly focusing on yes/no/maybe questions derived from biomedical research papers. The model leverages the capabilities of large language models to provide accurate, natural language answers in the biomedical domain.