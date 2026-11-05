---
library_name: transformers
license: apache-2.0
base_model: answerdotai/ModernBERT-base
tags:
- trackio
- trackio:https://huggingface.co/spaces/jefftherover/huggingface-static-09f52c
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: modernbert-pii-mapped-v3
  results: []
---
<a href="https://huggingface.co/spaces/jefftherover/huggingface-static-09f52c" target="_blank"><img src="https://raw.githubusercontent.com/gradio-app/trackio/refs/heads/main/trackio/assets/badge.png" alt="Visualize in Trackio" title="Visualize in Trackio" style="height: 40px;"/></a>
<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# modernbert-pii-mapped-v3

This model is a fine-tuned version of [answerdotai/ModernBERT-base](https://huggingface.co/answerdotai/ModernBERT-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0161
- Precision: 0.9759
- Recall: 0.9851
- F1: 0.9805
- Accuracy: 0.9962

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
- lr_scheduler_warmup_steps: 0.1
- num_epochs: 5
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch  | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:------:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.0743        | 0.4087 | 500  | 0.0272          | 0.9220    | 0.9541 | 0.9378 | 0.9915   |
| 0.0391        | 0.8173 | 1000 | 0.0176          | 0.9495    | 0.9704 | 0.9598 | 0.9938   |
| 0.0271        | 1.2256 | 1500 | 0.0162          | 0.9598    | 0.9763 | 0.9680 | 0.9947   |
| 0.0232        | 1.6342 | 2000 | 0.0133          | 0.9595    | 0.9776 | 0.9685 | 0.9952   |
| 0.0174        | 2.0425 | 2500 | 0.0115          | 0.9700    | 0.9810 | 0.9754 | 0.9957   |
| 0.0129        | 2.4512 | 3000 | 0.0126          | 0.9724    | 0.982  | 0.9772 | 0.9957   |
| 0.0126        | 2.8598 | 3500 | 0.0149          | 0.9805    | 0.9850 | 0.9828 | 0.9958   |
| 0.0040        | 3.2681 | 4000 | 0.0155          | 0.9780    | 0.9848 | 0.9814 | 0.9959   |
| 0.0032        | 3.6767 | 4500 | 0.0156          | 0.9787    | 0.9849 | 0.9818 | 0.9959   |
| 0.0006        | 4.0850 | 5000 | 0.0161          | 0.9759    | 0.9851 | 0.9805 | 0.9962   |


### Framework versions

- Transformers 5.8.0
- Pytorch 2.11.0+cu130
- Datasets 4.8.5
- Tokenizers 0.22.2
