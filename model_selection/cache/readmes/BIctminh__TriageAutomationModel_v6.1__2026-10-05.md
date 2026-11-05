---
library_name: transformers
license: mit
base_model: BIctminh/results_FBBert_20260611
tags:
- generated_from_trainer
metrics:
- f1
model-index:
- name: TriageAutomationModel_v6.1
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# TriageAutomationModel_v6.1

This model is a fine-tuned version of [BIctminh/results_FBBert_20260611](https://huggingface.co/BIctminh/results_FBBert_20260611) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.7050
- F1: 0.8269

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 300
- num_epochs: 4

### Training results



### Framework versions

- Transformers 4.45.2
- Pytorch 2.6.0+cu118
- Datasets 3.2.0
- Tokenizers 0.20.3
