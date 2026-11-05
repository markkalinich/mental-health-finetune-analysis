---
library_name: transformers
license: mit
base_model: FacebookAI/roberta-large
tags:
- generated_from_trainer
metrics:
- accuracy
- precision
- recall
- f1
model-index:
- name: roberta-Empathy-badareas-eval_FeedbackESConv5pp_CARE10pp-sweeps-current
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# roberta-Empathy-badareas-eval_FeedbackESConv5pp_CARE10pp-sweeps-current

This model is a fine-tuned version of [FacebookAI/roberta-large](https://huggingface.co/FacebookAI/roberta-large) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1959
- Accuracy: 0.8691
- Precision: 0.3387
- Recall: 0.2561
- F1: 0.2917

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1.7040925846794196e-05
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | Precision | Recall | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:---------:|:------:|:------:|
| 0.4468        | 1.0   | 140  | 0.3926          | 0.8703   | 0.3582    | 0.2927 | 0.3221 |
| 0.3624        | 2.0   | 280  | 0.2036          | 0.8755   | 0.3333    | 0.1829 | 0.2362 |
| 0.3061        | 3.0   | 420  | 0.1371          | 0.8973   | 0.75      | 0.0366 | 0.0698 |
| 0.2535        | 4.0   | 560  | 0.1825          | 0.8768   | 0.375     | 0.2561 | 0.3043 |
| 0.2381        | 5.0   | 700  | 0.1959          | 0.8691   | 0.3387    | 0.2561 | 0.2917 |


### Framework versions

- Transformers 4.47.1
- Pytorch 2.5.1+cu124
- Datasets 2.21.0
- Tokenizers 0.21.0
