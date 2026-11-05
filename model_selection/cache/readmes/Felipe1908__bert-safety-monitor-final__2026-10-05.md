---
library_name: transformers
license: mit
base_model: neuralmind/bert-base-portuguese-cased
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: bert-safety-monitor-final
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-safety-monitor-final

This model is a fine-tuned version of [neuralmind/bert-base-portuguese-cased](https://huggingface.co/neuralmind/bert-base-portuguese-cased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4353
- Accuracy: 0.8488
- F1 Macro: 0.8580

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
- eval_batch_size: 32
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 6
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | F1 Macro |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:--------:|
| No log        | 1.0   | 383  | 0.3836          | 0.8164   | 0.8326   |
| 0.4827        | 2.0   | 766  | 0.2766          | 0.8576   | 0.8562   |
| 0.2578        | 3.0   | 1149 | 0.4342          | 0.8414   | 0.8570   |
| 0.2216        | 4.0   | 1532 | 0.3752          | 0.8634   | 0.8660   |
| 0.2216        | 5.0   | 1915 | 0.4031          | 0.8429   | 0.8568   |
| 0.1874        | 6.0   | 2298 | 0.4353          | 0.8488   | 0.8580   |


### Framework versions

- Transformers 4.57.2
- Pytorch 2.9.0+cu126
- Datasets 4.0.0
- Tokenizers 0.22.1
