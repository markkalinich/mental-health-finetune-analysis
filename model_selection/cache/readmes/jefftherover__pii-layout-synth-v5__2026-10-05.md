---
library_name: transformers
license: apache-2.0
base_model: answerdotai/ModernBERT-base
tags:
- trackio
- trackio:https://huggingface.co/spaces/jefftherover/huggingface-static-3afb04
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: pii-layout-synth-v5
  results: []
---
<a href="https://huggingface.co/spaces/jefftherover/huggingface-static-3afb04" target="_blank"><img src="https://raw.githubusercontent.com/gradio-app/trackio/refs/heads/main/trackio/assets/badge.png" alt="Visualize in Trackio" title="Visualize in Trackio" style="height: 40px;"/></a>
<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# pii-layout-synth-v5

This model is a fine-tuned version of [answerdotai/ModernBERT-base](https://huggingface.co/answerdotai/ModernBERT-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0052
- Precision: 0.9900
- Recall: 0.9924
- F1: 0.9912
- Accuracy: 0.9985

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
| 0.0930        | 0.2455 | 500  | 0.0323          | 0.9289    | 0.9577 | 0.9430 | 0.9912   |
| 0.0381        | 0.4909 | 1000 | 0.0180          | 0.9613    | 0.9754 | 0.9683 | 0.9945   |
| 0.0202        | 0.7364 | 1500 | 0.0091          | 0.9803    | 0.9895 | 0.9849 | 0.9972   |
| 0.0178        | 0.9818 | 2000 | 0.0071          | 0.9842    | 0.9921 | 0.9882 | 0.9978   |
| 0.0089        | 1.2273 | 2500 | 0.0062          | 0.9860    | 0.9926 | 0.9893 | 0.9981   |
| 0.0158        | 1.4728 | 3000 | 0.0072          | 0.9850    | 0.9912 | 0.9881 | 0.9977   |
| 0.0091        | 1.7182 | 3500 | 0.0061          | 0.9863    | 0.9895 | 0.9879 | 0.9979   |
| 0.0165        | 1.9637 | 4000 | 0.0055          | 0.9880    | 0.9940 | 0.9910 | 0.9982   |
| 0.0100        | 2.2091 | 4500 | 0.0055          | 0.9886    | 0.9938 | 0.9912 | 0.9983   |
| 0.0048        | 2.4546 | 5000 | 0.0047          | 0.9896    | 0.9950 | 0.9923 | 0.9985   |
| 0.0056        | 2.7000 | 5500 | 0.0046          | 0.9906    | 0.9953 | 0.9929 | 0.9986   |
| 0.0045        | 2.9455 | 6000 | 0.0045          | 0.9902    | 0.9940 | 0.9921 | 0.9985   |
| 0.0016        | 3.1910 | 6500 | 0.0052          | 0.9910    | 0.9940 | 0.9925 | 0.9986   |
| 0.0021        | 3.4364 | 7000 | 0.0052          | 0.9900    | 0.9924 | 0.9912 | 0.9985   |


### Framework versions

- Transformers 5.12.0
- Pytorch 2.12.0+cu130
- Datasets 5.0.0
- Tokenizers 0.22.2
