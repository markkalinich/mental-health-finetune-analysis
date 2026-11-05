---
library_name: transformers
license: apache-2.0
base_model: answerdotai/ModernBERT-base
tags:
- trackio
- trackio:https://huggingface.co/spaces/jefftherover/huggingface-static-9c06f2
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: pii-layout-synth-v7
  results: []
---
<a href="https://huggingface.co/spaces/jefftherover/huggingface-static-9c06f2" target="_blank"><img src="https://raw.githubusercontent.com/gradio-app/trackio/refs/heads/main/trackio/assets/badge.png" alt="Visualize in Trackio" title="Visualize in Trackio" style="height: 40px;"/></a>
<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# pii-layout-synth-v7

This model is a fine-tuned version of [answerdotai/ModernBERT-base](https://huggingface.co/answerdotai/ModernBERT-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0060
- Precision: 0.9910
- Recall: 0.9949
- F1: 0.9929
- Accuracy: 0.9986

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
| 0.0987        | 0.2455 | 500  | 0.0422          | 0.9013    | 0.9460 | 0.9231 | 0.9875   |
| 0.0373        | 0.4909 | 1000 | 0.0174          | 0.9622    | 0.9783 | 0.9702 | 0.9949   |
| 0.0241        | 0.7364 | 1500 | 0.0133          | 0.9732    | 0.9856 | 0.9793 | 0.9962   |
| 0.0185        | 0.9818 | 2000 | 0.0136          | 0.9731    | 0.9812 | 0.9771 | 0.9960   |
| 0.0116        | 1.2273 | 2500 | 0.0070          | 0.9852    | 0.9919 | 0.9885 | 0.9978   |
| 0.0115        | 1.4728 | 3000 | 0.0075          | 0.9841    | 0.9917 | 0.9879 | 0.9977   |
| 0.0088        | 1.7182 | 3500 | 0.0057          | 0.9881    | 0.9936 | 0.9908 | 0.9982   |
| 0.0106        | 1.9637 | 4000 | 0.0051          | 0.9894    | 0.9952 | 0.9923 | 0.9984   |
| 0.0051        | 2.2091 | 4500 | 0.0050          | 0.9896    | 0.9925 | 0.9910 | 0.9984   |
| 0.0043        | 2.4546 | 5000 | 0.0051          | 0.9898    | 0.9949 | 0.9923 | 0.9985   |
| 0.0048        | 2.7000 | 5500 | 0.0055          | 0.9900    | 0.9934 | 0.9917 | 0.9984   |
| 0.0044        | 2.9455 | 6000 | 0.0050          | 0.9897    | 0.9946 | 0.9921 | 0.9984   |
| 0.0018        | 3.1910 | 6500 | 0.0054          | 0.9908    | 0.9949 | 0.9928 | 0.9986   |
| 0.0014        | 3.4364 | 7000 | 0.0053          | 0.9910    | 0.9946 | 0.9928 | 0.9986   |
| 0.0016        | 3.6819 | 7500 | 0.0053          | 0.9905    | 0.9944 | 0.9924 | 0.9986   |
| 0.0016        | 3.9273 | 8000 | 0.0051          | 0.9915    | 0.9948 | 0.9931 | 0.9987   |
| 0.0004        | 4.1728 | 8500 | 0.0056          | 0.9912    | 0.9939 | 0.9925 | 0.9986   |
| 0.0003        | 4.4183 | 9000 | 0.0060          | 0.9913    | 0.9949 | 0.9931 | 0.9986   |
| 0.0006        | 4.6637 | 9500 | 0.0060          | 0.9910    | 0.9949 | 0.9929 | 0.9986   |


### Framework versions

- Transformers 5.12.1
- Pytorch 2.12.0+cu130
- Datasets 5.0.0
- Tokenizers 0.22.2
