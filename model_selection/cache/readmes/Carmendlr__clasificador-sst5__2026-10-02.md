---
library_name: transformers
base_model: mrm8488/electricidad-base-discriminator
tags:
- text-classification
- sst5
- sentiment-analysis
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: clasificador-sst5
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# clasificador-sst5

This model is a fine-tuned version of [mrm8488/electricidad-base-discriminator](https://huggingface.co/mrm8488/electricidad-base-discriminator) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.4281
- Accuracy: 0.405

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
- train_batch_size: 64
- eval_batch_size: 64
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 3.0

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| No log        | 1.0   | 79   | 1.5174          | 0.327    |
| No log        | 2.0   | 158  | 1.4423          | 0.392    |
| No log        | 3.0   | 237  | 1.4281          | 0.405    |


### Framework versions

- Transformers 4.57.3
- Pytorch 2.9.0+cpu
- Datasets 4.4.1
- Tokenizers 0.22.1
