---
library_name: transformers
license: apache-2.0
base_model: answerdotai/ModernBERT-base
tags:
- trackio
- trackio:https://huggingface.co/spaces/jefftherover/huggingface-static-3bfe5e
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: pii-layout-synth-v10
  results: []
---
<a href="https://huggingface.co/spaces/jefftherover/huggingface-static-3bfe5e" target="_blank"><img src="https://raw.githubusercontent.com/gradio-app/trackio/refs/heads/main/trackio/assets/badge.png" alt="Visualize in Trackio" title="Visualize in Trackio" style="height: 40px;"/></a>
<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# pii-layout-synth-v10

This model is a fine-tuned version of [answerdotai/ModernBERT-base](https://huggingface.co/answerdotai/ModernBERT-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0061
- Precision: 0.9913
- Recall: 0.9949
- F1: 0.9931
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
- lr_scheduler_warmup_steps: 200
- num_epochs: 5
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch  | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:------:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.0479        | 0.2455 | 500  | 0.0170          | 0.9615    | 0.9769 | 0.9692 | 0.9951   |
| 0.0232        | 0.4909 | 1000 | 0.0096          | 0.9796    | 0.9882 | 0.9838 | 0.9972   |
| 0.0202        | 0.7364 | 1500 | 0.0082          | 0.9820    | 0.9873 | 0.9846 | 0.9975   |
| 0.0188        | 0.9818 | 2000 | 0.0067          | 0.9829    | 0.9868 | 0.9849 | 0.9978   |
| 0.0094        | 1.2273 | 2500 | 0.0074          | 0.9861    | 0.9917 | 0.9889 | 0.9979   |
| 0.0127        | 1.4728 | 3000 | 0.0056          | 0.9879    | 0.9937 | 0.9908 | 0.9982   |
| 0.0099        | 1.7182 | 3500 | 0.0055          | 0.9878    | 0.9931 | 0.9905 | 0.9983   |
| 0.0085        | 1.9637 | 4000 | 0.0054          | 0.9881    | 0.9940 | 0.9910 | 0.9983   |
| 0.0040        | 2.2091 | 4500 | 0.0050          | 0.9888    | 0.9918 | 0.9903 | 0.9983   |
| 0.0041        | 2.4546 | 5000 | 0.0059          | 0.9905    | 0.9950 | 0.9927 | 0.9984   |
| 0.0036        | 2.7000 | 5500 | 0.0054          | 0.9893    | 0.9930 | 0.9912 | 0.9984   |
| 0.0036        | 2.9455 | 6000 | 0.0048          | 0.9915    | 0.9952 | 0.9933 | 0.9986   |
| 0.0013        | 3.1910 | 6500 | 0.0056          | 0.9915    | 0.9949 | 0.9932 | 0.9986   |
| 0.0011        | 3.4364 | 7000 | 0.0058          | 0.9910    | 0.9940 | 0.9925 | 0.9985   |
| 0.0014        | 3.6819 | 7500 | 0.0061          | 0.9913    | 0.9949 | 0.9931 | 0.9986   |


### Framework versions

- Transformers 5.12.1
- Pytorch 2.12.1+cu130
- Datasets 5.0.0
- Tokenizers 0.22.2
