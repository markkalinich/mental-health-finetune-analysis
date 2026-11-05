---
library_name: transformers
license: apache-2.0
base_model: albert/albert-base-v2
tags:
- generated_from_trainer
- sentiment-analysis
metrics:
- accuracy
model-index:
- name: albert-imdb
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# albert-imdb

This model is a fine-tuned version of [albert/albert-base-v2](https://huggingface.co/albert/albert-base-v2) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1795
- Accuracy: 0.9479

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
- train_batch_size: 24
- eval_batch_size: 24
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 2
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch  | Step | Validation Loss | Accuracy |
|:-------------:|:------:|:----:|:---------------:|:--------:|
| 0.2346        | 0.4997 | 833  | 0.1875          | 0.9291   |
| 0.1219        | 0.9994 | 1666 | 0.2007          | 0.9305   |
| 0.1825        | 1.4991 | 2499 | 0.2000          | 0.9464   |
| 0.1559        | 1.9988 | 3332 | 0.1795          | 0.9479   |


### Framework versions

- Transformers 5.0.0
- Pytorch 2.10.0+cu128
- Datasets 4.0.0
- Tokenizers 0.22.2
