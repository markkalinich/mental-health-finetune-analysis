---
library_name: transformers
license: apache-2.0
base_model: google-bert/bert-large-uncased
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: triage_model
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# triage_model

This model is a fine-tuned version of [google-bert/bert-large-uncased](https://huggingface.co/google-bert/bert-large-uncased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6682
- Accuracy: 0.8217

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
- eval_batch_size: 16
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 6

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| No log        | 1.0   | 117  | 0.6674          | 0.8262   |
| No log        | 2.0   | 234  | 0.8441          | 0.8194   |
| No log        | 3.0   | 351  | 0.8558          | 0.8352   |
| No log        | 4.0   | 468  | 0.9775          | 0.8239   |
| 0.1473        | 5.0   | 585  | 0.9850          | 0.8239   |
| 0.1473        | 6.0   | 702  | 1.0015          | 0.8239   |


### Framework versions

- Transformers 5.0.0
- Pytorch 2.9.0+cu128
- Datasets 4.0.0
- Tokenizers 0.22.2
