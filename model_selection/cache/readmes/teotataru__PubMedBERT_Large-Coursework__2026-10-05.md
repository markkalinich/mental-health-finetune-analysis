---
library_name: transformers
base_model: teotataru/PubMedBERT_Large-Coursework
tags:
- generated_from_trainer
model-index:
- name: PubMedBERT_Large-Coursework
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# PubMedBERT_Large-Coursework

This model is a fine-tuned version of [teotataru/PubMedBERT_Large-Coursework](https://huggingface.co/teotataru/PubMedBERT_Large-Coursework) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5338
- Macro F1: 0.8007

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
- train_batch_size: 16
- eval_batch_size: 16
- seed: 28
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 1
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Macro F1 |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 0.1280        | 1.0   | 1983 | 0.5338          | 0.8007   |


### Framework versions

- Transformers 5.0.0
- Pytorch 2.10.0+cu128
- Datasets 5.0.0
- Tokenizers 0.22.2
