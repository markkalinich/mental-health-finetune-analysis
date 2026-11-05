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
- name: pii-dual-mmbert-base-v2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# pii-dual-mmbert-base-v2

This model is a fine-tuned version of [jhu-clsp/mmBERT-base](https://huggingface.co/jhu-clsp/mmBERT-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0022
- Precision: 0.9963
- Recall: 0.9977
- F1: 0.9970
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

| Training Loss | Epoch  | Step  | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:------:|:-----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.0118        | 0.4638 | 2000  | 0.0101          | 0.9835    | 0.9912 | 0.9873 | 0.9973   |
| 0.0097        | 0.9275 | 4000  | 0.0049          | 0.9923    | 0.9960 | 0.9942 | 0.9988   |
| 0.0177        | 1.3912 | 6000  | 0.0030          | 0.9939    | 0.9957 | 0.9948 | 0.9990   |
| 0.0044        | 1.8550 | 8000  | 0.0030          | 0.9949    | 0.9967 | 0.9958 | 0.9991   |
| 0.0021        | 2.3186 | 10000 | 0.0026          | 0.9941    | 0.9957 | 0.9949 | 0.9992   |
| 0.0049        | 2.7824 | 12000 | 0.0018          | 0.9961    | 0.9978 | 0.9970 | 0.9994   |
| 0.0002        | 3.2460 | 14000 | 0.0023          | 0.9963    | 0.9979 | 0.9971 | 0.9994   |
| 0.0007        | 3.7098 | 16000 | 0.0022          | 0.9964    | 0.9978 | 0.9971 | 0.9995   |
| 0.0001        | 4.0    | 17252 | 0.0022          | 0.9963    | 0.9977 | 0.9970 | 0.9995   |


### Framework versions

- Transformers 5.15.1
- Pytorch 2.13.0+cu130
- Datasets 5.0.1
- Tokenizers 0.22.2
