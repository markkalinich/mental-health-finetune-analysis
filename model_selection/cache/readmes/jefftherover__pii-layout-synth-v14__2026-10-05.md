---
library_name: transformers
license: apache-2.0
base_model: answerdotai/ModernBERT-base
tags:
- trackio
- trackio:https://huggingface.co/spaces/jefftherover/huggingface-static-1450aa
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: pii-layout-synth-v14
  results: []
---
<a href="https://huggingface.co/spaces/jefftherover/huggingface-static-1450aa" target="_blank"><img src="https://raw.githubusercontent.com/gradio-app/trackio/refs/heads/main/trackio/assets/badge.png" alt="Visualize in Trackio" title="Visualize in Trackio" style="height: 40px;"/></a>
<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# pii-layout-synth-v14

This model is a fine-tuned version of [answerdotai/ModernBERT-base](https://huggingface.co/answerdotai/ModernBERT-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0047
- Precision: 0.9910
- Recall: 0.9941
- F1: 0.9925
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
| 0.0159        | 0.9685 | 2000 | 0.0080          | 0.9836    | 0.9899 | 0.9867 | 0.9976   |
| 0.0065        | 1.9370 | 4000 | 0.0043          | 0.9895    | 0.9935 | 0.9915 | 0.9985   |
| 0.0032        | 2.9056 | 6000 | 0.0044          | 0.9905    | 0.9929 | 0.9917 | 0.9986   |
| 0.0008        | 3.8741 | 8000 | 0.0047          | 0.9910    | 0.9942 | 0.9926 | 0.9987   |
| 0.0009        | 4.0    | 8260 | 0.0047          | 0.9910    | 0.9941 | 0.9925 | 0.9987   |


### Framework versions

- Transformers 5.13.0
- Pytorch 2.12.1+cu130
- Datasets 5.0.0
- Tokenizers 0.22.2
