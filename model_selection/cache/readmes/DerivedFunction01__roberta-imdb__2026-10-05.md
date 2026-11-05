---
library_name: transformers
license: mit
base_model: FacebookAI/roberta-base
tags:
- generated_from_trainer
- sentiment-analysis
metrics:
- accuracy
model-index:
- name: roberta-imdb
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# roberta-imdb

This model is a fine-tuned version of [FacebookAI/roberta-base](https://huggingface.co/FacebookAI/roberta-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1680
- Accuracy: 0.9561

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
| 0.2052        | 0.4997 | 833  | 0.1646          | 0.9435   |
| 0.1565        | 0.9994 | 1666 | 0.1862          | 0.9421   |
| 0.2213        | 1.4991 | 2499 | 0.1759          | 0.9547   |
| 0.1314        | 1.9988 | 3332 | 0.1680          | 0.9561   |


### Framework versions

- Transformers 5.0.0
- Pytorch 2.10.0+cu128
- Datasets 4.0.0
- Tokenizers 0.22.2