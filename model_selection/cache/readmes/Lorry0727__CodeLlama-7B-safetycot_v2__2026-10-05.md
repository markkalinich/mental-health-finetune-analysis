---
library_name: transformers
license: other
base_model: Lorry0727/CodeLlama-7B-evol
tags:
- llama-factory
- full
- generated_from_trainer
model-index:
- name: CodeLlama-7B-safetycot_v2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# CodeLlama-7B-safetycot-2025-03-14-15-00

This model is a fine-tuned version of [Lorry0727/CodeLlama-7B-evol](https://huggingface.co/Lorry0727/CodeLlama-7B-evol) on the sft_COT_safecoder_v4 and the sft_COT_safecoder_v4_autocomplete datasets.

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-05
- train_batch_size: 1
- eval_batch_size: 8
- seed: 42
- distributed_type: multi-GPU
- num_devices: 4
- gradient_accumulation_steps: 4
- total_train_batch_size: 16
- total_eval_batch_size: 32
- optimizer: Use adamw_torch with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: cosine
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 3.0

### Training results



### Framework versions

- Transformers 4.46.0
- Pytorch 2.5.1+cu124
- Datasets 3.1.0
- Tokenizers 0.20.3
