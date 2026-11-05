---
library_name: transformers
license: cc-by-sa-4.0
base_model: klue/bert-base
tags:
- generated_from_trainer
model-index:
- name: medical-chatbot-final2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# medical-chatbot-final2

This model is a fine-tuned version of [klue/bert-base](https://huggingface.co/klue/bert-base) on an unknown dataset.

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 16
- eval_batch_size: 8
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 5

### Training results



### Framework versions

- Transformers 4.48.2
- Pytorch 2.5.1+cu124
- Tokenizers 0.21.0
