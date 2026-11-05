---
library_name: transformers
license: other
base_model: OpenOneRec/OneReason-0.8B-pretrain-competition
tags:
- llama-factory
- full
- generated_from_trainer
model-index:
- name: v23_scratch_clean_cot_guard_lr3e6_ep5
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# v23_scratch_clean_cot_guard_lr3e6_ep5

This model is a fine-tuned version of [OpenOneRec/OneReason-0.8B-pretrain-competition](https://huggingface.co/OpenOneRec/OneReason-0.8B-pretrain-competition) on the exp_scratch_clean_cot_guard_ep5 dataset.

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 3e-06
- train_batch_size: 1
- eval_batch_size: 8
- seed: 202607232
- gradient_accumulation_steps: 4
- total_train_batch_size: 4
- optimizer: Use OptimizerNames.ADAMW_TORCH with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: cosine
- lr_scheduler_warmup_steps: 0.02
- num_epochs: 5

### Training results



### Framework versions

- Transformers 5.6.0
- Pytorch 2.7.1+cu126
- Datasets 4.0.0
- Tokenizers 0.22.2
