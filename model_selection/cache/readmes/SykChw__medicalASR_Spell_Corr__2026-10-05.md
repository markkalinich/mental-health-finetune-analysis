---
language:
- en
library_name: transformers
tags:
- t5
- seq2seq
- spelling-correction
pipeline_tag: text-generation
license: apache-2.0
datasets:
- private
metrics:
- accuracy
- wer
- bleu
base_model:
- google-t5/t5-small
---

# Domain-specific T5 Spelling Correction

This model is a fine-tuned version of [T5](https://huggingface.co/t5-small) for spelling correction in the **medical ASR** domain.
