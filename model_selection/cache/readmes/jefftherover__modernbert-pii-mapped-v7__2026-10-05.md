---
library_name: transformers
license: apache-2.0
base_model: answerdotai/ModernBERT-base
tags:
- trackio
- trackio:https://huggingface.co/spaces/jefftherover/huggingface-static-80c141
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: modernbert-pii-mapped-v7
  results: []
---
<a href="https://huggingface.co/spaces/jefftherover/huggingface-static-80c141" target="_blank"><img src="https://raw.githubusercontent.com/gradio-app/trackio/refs/heads/main/trackio/assets/badge.png" alt="Visualize in Trackio" title="Visualize in Trackio" style="height: 40px;"/></a>
<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# modernbert-pii-mapped-v7

This model is a fine-tuned version of [answerdotai/ModernBERT-base](https://huggingface.co/answerdotai/ModernBERT-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0108
- Precision: 0.9680
- Recall: 0.9861
- F1: 0.9770
- Accuracy: 0.9977

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
| 0.0668        | 0.4087 | 500  | 0.0272          | 0.8784    | 0.9621 | 0.9183 | 0.9920   |
| 0.0310        | 0.8173 | 1000 | 0.0152          | 0.9320    | 0.9705 | 0.9509 | 0.9955   |
| 0.0229        | 1.2256 | 1500 | 0.0145          | 0.9394    | 0.9791 | 0.9588 | 0.9959   |
| 0.0172        | 1.6342 | 2000 | 0.0108          | 0.9487    | 0.9803 | 0.9643 | 0.9965   |
| 0.0121        | 2.0425 | 2500 | 0.0099          | 0.9438    | 0.9655 | 0.9546 | 0.9965   |
| 0.0073        | 2.4512 | 3000 | 0.0132          | 0.9438    | 0.9548 | 0.9493 | 0.9962   |
| 0.0065        | 2.8598 | 3500 | 0.0121          | 0.9563    | 0.9747 | 0.9654 | 0.9969   |
| 0.0031        | 3.2681 | 4000 | 0.0097          | 0.9673    | 0.9848 | 0.9759 | 0.9976   |
| 0.0022        | 3.6767 | 4500 | 0.0097          | 0.9673    | 0.9885 | 0.9777 | 0.9977   |
| 0.0015        | 4.0850 | 5000 | 0.0104          | 0.9664    | 0.9848 | 0.9755 | 0.9976   |
| 0.0008        | 4.4937 | 5500 | 0.0107          | 0.9683    | 0.9867 | 0.9774 | 0.9977   |
| 0.0008        | 4.9023 | 6000 | 0.0108          | 0.9680    | 0.9861 | 0.9770 | 0.9977   |


### Framework versions

- Transformers 5.9.0
- Pytorch 2.12.0+cu130
- Datasets 4.8.5
- Tokenizers 0.22.2
