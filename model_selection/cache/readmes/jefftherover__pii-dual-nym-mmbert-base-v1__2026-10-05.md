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
- name: pii-dual-nym-mmbert-base-v1
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# pii-dual-nym-mmbert-base-v1

This model is a fine-tuned version of [jhu-clsp/mmBERT-base](https://huggingface.co/jhu-clsp/mmBERT-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0022
- Precision: 0.9961
- Recall: 0.9974
- F1: 0.9967
- Accuracy: 0.9995

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
| 0.0151        | 0.8871 | 2000 | 0.0122          | 0.9823    | 0.9914 | 0.9868 | 0.9973   |
| 0.0073        | 1.7740 | 4000 | 0.0032          | 0.9949    | 0.9959 | 0.9954 | 0.9992   |
| 0.0014        | 2.6609 | 6000 | 0.0021          | 0.9949    | 0.9971 | 0.9960 | 0.9993   |
| 0.0014        | 3.5478 | 8000 | 0.0022          | 0.9963    | 0.9973 | 0.9968 | 0.9995   |
| 0.0002        | 4.0    | 9020 | 0.0022          | 0.9961    | 0.9974 | 0.9967 | 0.9995   |


### Framework versions

- Transformers 5.18.0
- Pytorch 2.14.1+cu130
- Datasets 5.0.1
- Tokenizers 0.23.2
