---
library_name: transformers
license: mit
base_model: Mardiyyah/cellate2.0-tapt_base-LR_5e-05
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: CeLLaTe3.1_Base_no_vague_adapted_pubmed
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# CeLLaTe3.1_Base_no_vague_adapted_pubmed

This model is a fine-tuned version of [Mardiyyah/cellate2.0-tapt_base-LR_5e-05](https://huggingface.co/Mardiyyah/cellate2.0-tapt_base-LR_5e-05) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0752
- Precision: 0.6721
- Recall: 0.6643
- F1: 0.6681
- Accuracy: 0.9813

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
- train_batch_size: 32
- eval_batch_size: 16
- seed: 3407
- optimizer: Use OptimizerNames.ADAMW_TORCH with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.01
- num_epochs: 20
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch  | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:------:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 1.0902        | 0.1300 | 100  | 0.1817          | 0.1303    | 0.0124 | 0.0227 | 0.9591   |
| 0.1808        | 0.2601 | 200  | 0.1459          | 0.4838    | 0.2406 | 0.3214 | 0.9712   |
| 0.1098        | 0.3901 | 300  | 0.0751          | 0.6721    | 0.6643 | 0.6681 | 0.9813   |
| 0.0589        | 0.5202 | 400  | 0.0781          | 0.5922    | 0.7233 | 0.6512 | 0.9792   |
| 0.0521        | 0.6502 | 500  | 0.1016          | 0.2937    | 0.8378 | 0.4349 | 0.9365   |
| 0.0486        | 0.7802 | 600  | 0.0859          | 0.5242    | 0.8309 | 0.6428 | 0.9736   |


### Framework versions

- Transformers 4.48.2
- Pytorch 2.4.1+cu121
- Datasets 3.0.2
- Tokenizers 0.21.0
