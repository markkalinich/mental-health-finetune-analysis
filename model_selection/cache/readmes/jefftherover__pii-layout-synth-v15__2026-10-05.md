---
library_name: transformers
license: apache-2.0
base_model: answerdotai/ModernBERT-base
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: pii-layout-synth-v15
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# pii-layout-synth-v15

This model is a fine-tuned version of [answerdotai/ModernBERT-base](https://huggingface.co/answerdotai/ModernBERT-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0045
- Precision: 0.9912
- Recall: 0.9944
- F1: 0.9928
- Accuracy: 0.9987

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
| 0.0152        | 0.9685 | 2000 | 0.0083          | 0.9822    | 0.9877 | 0.9849 | 0.9974   |
| 0.0069        | 1.9370 | 4000 | 0.0047          | 0.9888    | 0.9936 | 0.9912 | 0.9985   |
| 0.0029        | 2.9056 | 6000 | 0.0038          | 0.9911    | 0.9942 | 0.9927 | 0.9987   |
| 0.0012        | 3.8741 | 8000 | 0.0045          | 0.9912    | 0.9944 | 0.9928 | 0.9987   |
| 0.0008        | 4.0    | 8260 | 0.0045          | 0.9912    | 0.9944 | 0.9928 | 0.9987   |


### Framework versions

- Transformers 5.13.0
- Pytorch 2.13.0+cu130
- Datasets 5.0.0
- Tokenizers 0.22.2
