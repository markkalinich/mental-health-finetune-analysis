---
library_name: transformers
license: mit
base_model: microsoft/deberta-v3-base
tags:
- generated_from_trainer
model-index:
- name: empathy_classifier
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# empathy_classifier

This model is a fine-tuned version of [microsoft/deberta-v3-base](https://huggingface.co/microsoft/deberta-v3-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0540
- Mse: 0.0540
- Mae: 0.1938
- Pearson: 0.4722

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
- train_batch_size: 32
- eval_batch_size: 64
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 6

### Training results

| Training Loss | Epoch | Step | Validation Loss | Mse    | Mae    | Pearson |
|:-------------:|:-----:|:----:|:---------------:|:------:|:------:|:-------:|
| No log        | 1.0   | 47   | 0.0662          | 0.0662 | 0.2175 | 0.3286  |
| No log        | 2.0   | 94   | 0.0560          | 0.0560 | 0.1993 | 0.4229  |
| No log        | 3.0   | 141  | 0.0538          | 0.0538 | 0.1944 | 0.4611  |
| No log        | 4.0   | 188  | 0.0601          | 0.0601 | 0.2036 | 0.4580  |
| No log        | 5.0   | 235  | 0.0540          | 0.0540 | 0.1938 | 0.4722  |
| No log        | 6.0   | 282  | 0.0542          | 0.0542 | 0.1942 | 0.4720  |


### Framework versions

- Transformers 4.46.2
- Pytorch 2.6.0+cu124
- Datasets 3.3.2
- Tokenizers 0.20.3
