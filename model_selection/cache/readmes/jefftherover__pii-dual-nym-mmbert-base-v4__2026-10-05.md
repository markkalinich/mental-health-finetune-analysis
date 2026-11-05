---
library_name: transformers
license: mit
base_model: jhu-clsp/mmBERT-base
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: pii-dual-nym-mmbert-base-v4
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# pii-dual-nym-mmbert-base-v4

This model is a fine-tuned version of [jhu-clsp/mmBERT-base](https://huggingface.co/jhu-clsp/mmBERT-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0029
- Precision: 0.9960
- Recall: 0.9976
- F1: 0.9968
- Accuracy: 0.9993

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
- train_batch_size: 16
- eval_batch_size: 32
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 32
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: cosine_with_restarts
- lr_scheduler_warmup_steps: 200
- num_epochs: 4
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch  | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:------:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.0137        | 0.8931 | 2000 | 0.0075          | 0.9908    | 0.9944 | 0.9926 | 0.9983   |
| 0.0048        | 1.7859 | 4000 | 0.0040          | 0.9947    | 0.9968 | 0.9957 | 0.9990   |
| 0.0025        | 2.6787 | 6000 | 0.0029          | 0.9949    | 0.9970 | 0.9960 | 0.9993   |
| 0.0004        | 3.5716 | 8000 | 0.0028          | 0.9961    | 0.9975 | 0.9968 | 0.9993   |
| 0.0002        | 4.0    | 8960 | 0.0029          | 0.9960    | 0.9976 | 0.9968 | 0.9993   |


### Framework versions

- Transformers 5.18.0
- Pytorch 2.14.1+cu130
- Datasets 5.0.1
- Tokenizers 0.23.2
