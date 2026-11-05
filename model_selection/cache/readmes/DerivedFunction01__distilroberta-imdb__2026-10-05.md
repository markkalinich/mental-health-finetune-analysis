---
library_name: transformers
license: apache-2.0
base_model: distilbert/distilroberta-base
tags:
- generated_from_trainer
- sentiment-analysis
metrics:
- accuracy
model-index:
- name: distilroberta-imdb
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilroberta-imdb

This model is a fine-tuned version of [distilbert/distilroberta-base](https://huggingface.co/distilbert/distilroberta-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1783
- Accuracy: 0.9448

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
| 0.1978        | 0.4997 | 833  | 0.2087          | 0.9243   |
| 0.1587        | 0.9994 | 1666 | 0.1952          | 0.9315   |
| 0.1645        | 1.4991 | 2499 | 0.1788          | 0.9438   |
| 0.1739        | 1.9988 | 3332 | 0.1783          | 0.9448   |


### Framework versions

- Transformers 5.0.0
- Pytorch 2.10.0+cu128
- Datasets 4.0.0
- Tokenizers 0.22.2
