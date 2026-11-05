---
library_name: transformers
license: bsd-3-clause
base_model: MIT/ast-finetuned-audioset-10-10-0.4593
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: voiced_pathology
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# voiced_pathology

This model is a fine-tuned version of [MIT/ast-finetuned-audioset-10-10-0.4593](https://huggingface.co/MIT/ast-finetuned-audioset-10-10-0.4593) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 3.1422
- Accuracy: 0.3095

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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| No log        | 1.0   | 21   | 2.3713          | 0.1905   |
| No log        | 2.0   | 42   | 1.3738          | 0.2143   |
| No log        | 3.0   | 63   | 1.3843          | 0.3333   |
| No log        | 4.0   | 84   | 1.7123          | 0.4048   |
| No log        | 5.0   | 105  | 2.0619          | 0.3095   |
| No log        | 6.0   | 126  | 2.1451          | 0.3333   |
| No log        | 7.0   | 147  | 2.5940          | 0.3095   |
| No log        | 8.0   | 168  | 2.7798          | 0.2619   |
| No log        | 9.0   | 189  | 3.0970          | 0.2619   |
| No log        | 10.0  | 210  | 3.1422          | 0.3095   |


### Framework versions

- Transformers 4.57.0
- Pytorch 2.8.0+cu126
- Datasets 4.2.0
- Tokenizers 0.22.1
