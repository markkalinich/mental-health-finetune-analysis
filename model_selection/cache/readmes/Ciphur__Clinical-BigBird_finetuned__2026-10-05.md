---
library_name: transformers
base_model: yikuan8/Clinical-BigBird
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: Clinical-BigBird_finetuned
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Clinical-BigBird_finetuned

This model is a fine-tuned version of [yikuan8/Clinical-BigBird](https://huggingface.co/yikuan8/Clinical-BigBird) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2126
- Precision: 0.6055
- Recall: 0.6883
- F1: 0.6443
- Accuracy: 0.9291

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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 1.0   | 125  | 0.2531          | 0.5527    | 0.6385 | 0.5925 | 0.9222   |
| No log        | 2.0   | 250  | 0.2191          | 0.5861    | 0.6744 | 0.6272 | 0.9282   |
| No log        | 3.0   | 375  | 0.2126          | 0.6055    | 0.6883 | 0.6443 | 0.9291   |


### Framework versions

- Transformers 4.47.1
- Pytorch 2.5.1+cu124
- Datasets 3.2.0
- Tokenizers 0.21.0
