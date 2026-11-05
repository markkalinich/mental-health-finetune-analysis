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
- name: CeLLaTe3.0_Base_no_vague_adapted_pubmed_gaz_lr_5e-5
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# CeLLaTe3.0_Base_no_vague_adapted_pubmed_gaz_lr_5e-5

This model is a fine-tuned version of [Mardiyyah/cellate2.0-tapt_base-LR_5e-05](https://huggingface.co/Mardiyyah/cellate2.0-tapt_base-LR_5e-05) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1410
- Precision: 0.8308
- Recall: 0.8511
- F1: 0.8408
- Accuracy: 0.9670

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
- eval_batch_size: 16
- seed: 3407
- optimizer: Use OptimizerNames.ADAMW_TORCH with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 20
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch  | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:------:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 1.0287        | 1.0417 | 100  | 0.3060          | 0.3496    | 0.2434 | 0.2870 | 0.9111   |
| 0.1964        | 2.0833 | 200  | 0.1409          | 0.7580    | 0.8360 | 0.7951 | 0.9628   |
| 0.0929        | 3.125  | 300  | 0.1408          | 0.8308    | 0.8511 | 0.8408 | 0.9670   |
| 0.0552        | 4.1667 | 400  | 0.1731          | 0.8381    | 0.8051 | 0.8212 | 0.9656   |
| 0.0365        | 5.2083 | 500  | 0.2119          | 0.8395    | 0.7491 | 0.7917 | 0.9609   |
| 0.0259        | 6.25   | 600  | 0.1992          | 0.8023    | 0.7605 | 0.7808 | 0.9608   |


### Framework versions

- Transformers 4.48.2
- Pytorch 2.4.1+cu121
- Datasets 3.0.2
- Tokenizers 0.21.0
