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
- name: pii-dual-nym-mmbert-base-v2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# pii-dual-nym-mmbert-base-v2

This model is a fine-tuned version of [jhu-clsp/mmBERT-base](https://huggingface.co/jhu-clsp/mmBERT-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0020
- Precision: 0.9974
- Recall: 0.9982
- F1: 0.9978
- Accuracy: 0.9996

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
| 0.0143        | 0.8873 | 2000 | 0.0044          | 0.9934    | 0.9956 | 0.9945 | 0.9989   |
| 0.0048        | 1.7746 | 4000 | 0.0030          | 0.9961    | 0.9970 | 0.9966 | 0.9993   |
| 0.0008        | 2.6619 | 6000 | 0.0022          | 0.9971    | 0.9978 | 0.9975 | 0.9995   |
| 0.0000        | 3.5492 | 8000 | 0.0020          | 0.9973    | 0.9981 | 0.9977 | 0.9996   |
| 0.0002        | 4.0    | 9016 | 0.0020          | 0.9974    | 0.9982 | 0.9978 | 0.9996   |


### Framework versions

- Transformers 5.18.0
- Pytorch 2.14.1+cu130
- Datasets 5.0.1
- Tokenizers 0.23.2
