---
library_name: transformers
license: apache-2.0
base_model: answerdotai/ModernBERT-base
tags:
- trackio
- trackio:https://huggingface.co/spaces/jefftherover/huggingface-static-94c355
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: pii-layout-synth-v11
  results: []
---
<a href="https://huggingface.co/spaces/jefftherover/huggingface-static-94c355" target="_blank"><img src="https://raw.githubusercontent.com/gradio-app/trackio/refs/heads/main/trackio/assets/badge.png" alt="Visualize in Trackio" title="Visualize in Trackio" style="height: 40px;"/></a>
<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# pii-layout-synth-v11

This model is a fine-tuned version of [answerdotai/ModernBERT-base](https://huggingface.co/answerdotai/ModernBERT-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0059
- Precision: 0.9907
- Recall: 0.9945
- F1: 0.9926
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
- num_epochs: 5
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch  | Step  | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:------:|:-----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.0473        | 0.2455 | 500   | 0.0251          | 0.9491    | 0.9732 | 0.9610 | 0.9930   |
| 0.0235        | 0.4909 | 1000  | 0.0111          | 0.9727    | 0.9823 | 0.9775 | 0.9965   |
| 0.0194        | 0.7364 | 1500  | 0.0102          | 0.9796    | 0.9892 | 0.9844 | 0.9973   |
| 0.0156        | 0.9818 | 2000  | 0.0072          | 0.9812    | 0.9867 | 0.9839 | 0.9976   |
| 0.0091        | 1.2273 | 2500  | 0.0063          | 0.9865    | 0.9911 | 0.9888 | 0.9981   |
| 0.0111        | 1.4728 | 3000  | 0.0058          | 0.9860    | 0.9923 | 0.9891 | 0.9981   |
| 0.0071        | 1.7182 | 3500  | 0.0054          | 0.9873    | 0.9924 | 0.9899 | 0.9983   |
| 0.0081        | 1.9637 | 4000  | 0.0052          | 0.9883    | 0.9936 | 0.9910 | 0.9983   |
| 0.0055        | 2.2091 | 4500  | 0.0055          | 0.9874    | 0.9907 | 0.9891 | 0.9982   |
| 0.0051        | 2.4546 | 5000  | 0.0067          | 0.9882    | 0.9934 | 0.9908 | 0.9982   |
| 0.0031        | 2.7000 | 5500  | 0.0047          | 0.9896    | 0.9934 | 0.9915 | 0.9986   |
| 0.0037        | 2.9455 | 6000  | 0.0055          | 0.9893    | 0.9943 | 0.9918 | 0.9984   |
| 0.0013        | 3.1910 | 6500  | 0.0053          | 0.9901    | 0.9947 | 0.9924 | 0.9986   |
| 0.0012        | 3.4364 | 7000  | 0.0054          | 0.9899    | 0.9939 | 0.9919 | 0.9985   |
| 0.0011        | 3.6819 | 7500  | 0.0057          | 0.9904    | 0.9943 | 0.9924 | 0.9985   |
| 0.0010        | 3.9273 | 8000  | 0.0055          | 0.9906    | 0.9947 | 0.9926 | 0.9987   |
| 0.0003        | 4.1728 | 8500  | 0.0055          | 0.9910    | 0.9943 | 0.9926 | 0.9987   |
| 0.0003        | 4.4183 | 9000  | 0.0057          | 0.9907    | 0.9943 | 0.9925 | 0.9987   |
| 0.0004        | 4.6637 | 9500  | 0.0059          | 0.9907    | 0.9943 | 0.9925 | 0.9987   |
| 0.0002        | 4.9092 | 10000 | 0.0059          | 0.9907    | 0.9945 | 0.9926 | 0.9987   |


### Framework versions

- Transformers 5.12.1
- Pytorch 2.12.1+cu130
- Datasets 5.0.0
- Tokenizers 0.22.2
