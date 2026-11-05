---
library_name: transformers
license: mit
base_model: indobenchmark/indobert-lite-base-p2
tags:
- generated_from_trainer
model-index:
- name: indobert-lite-base-finetuned-mental-health
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# indobert-lite-base-finetuned-mental-health

This model is a fine-tuned version of [indobenchmark/indobert-lite-base-p2](https://huggingface.co/indobenchmark/indobert-lite-base-p2) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 4.3035

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
- train_batch_size: 128
- eval_batch_size: 128
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 5
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| No log        | 1.0   | 40   | 5.5302          |
| 5.944         | 2.0   | 80   | 4.7983          |
| 5.944         | 3.0   | 120  | 4.4818          |
| 4.5573        | 4.0   | 160  | 4.3413          |
| 4.5573        | 5.0   | 200  | 4.3139          |


### Framework versions

- Transformers 4.51.3
- Pytorch 2.6.0+cu124
- Datasets 3.6.0
- Tokenizers 0.21.1
