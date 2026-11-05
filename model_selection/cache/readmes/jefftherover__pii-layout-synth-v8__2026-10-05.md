---
library_name: transformers
license: apache-2.0
base_model: answerdotai/ModernBERT-base
tags:
- trackio
- trackio:https://huggingface.co/spaces/jefftherover/huggingface-static-bb31b0
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: pii-layout-synth-v8
  results: []
---
<a href="https://huggingface.co/spaces/jefftherover/huggingface-static-bb31b0" target="_blank"><img src="https://raw.githubusercontent.com/gradio-app/trackio/refs/heads/main/trackio/assets/badge.png" alt="Visualize in Trackio" title="Visualize in Trackio" style="height: 40px;"/></a>
<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# pii-layout-synth-v8

This model is a fine-tuned version of [answerdotai/ModernBERT-base](https://huggingface.co/answerdotai/ModernBERT-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0052
- Precision: 0.9911
- Recall: 0.9952
- F1: 0.9932
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
- lr_scheduler_warmup_steps: 0.1
- num_epochs: 5
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch  | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:------:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.0867        | 0.2455 | 500  | 0.0315          | 0.9269    | 0.9599 | 0.9431 | 0.9912   |
| 0.0366        | 0.4909 | 1000 | 0.0164          | 0.9655    | 0.9758 | 0.9706 | 0.9950   |
| 0.0242        | 0.7364 | 1500 | 0.0132          | 0.9742    | 0.9835 | 0.9789 | 0.9961   |
| 0.0179        | 0.9818 | 2000 | 0.0074          | 0.9833    | 0.9890 | 0.9861 | 0.9976   |
| 0.0116        | 1.2273 | 2500 | 0.0064          | 0.9873    | 0.9930 | 0.9901 | 0.9981   |
| 0.0108        | 1.4728 | 3000 | 0.0073          | 0.9849    | 0.9916 | 0.9883 | 0.9977   |
| 0.0126        | 1.7182 | 3500 | 0.0070          | 0.9832    | 0.9912 | 0.9872 | 0.9978   |
| 0.0119        | 1.9637 | 4000 | 0.0058          | 0.9873    | 0.9940 | 0.9907 | 0.9982   |
| 0.0049        | 2.2091 | 4500 | 0.0054          | 0.9894    | 0.9924 | 0.9909 | 0.9983   |
| 0.0054        | 2.4546 | 5000 | 0.0085          | 0.9832    | 0.9928 | 0.9880 | 0.9975   |
| 0.0041        | 2.7000 | 5500 | 0.0048          | 0.9900    | 0.9943 | 0.9921 | 0.9985   |
| 0.0041        | 2.9455 | 6000 | 0.0050          | 0.9911    | 0.9957 | 0.9934 | 0.9986   |
| 0.0014        | 3.1910 | 6500 | 0.0058          | 0.9904    | 0.9948 | 0.9926 | 0.9985   |
| 0.0017        | 3.4364 | 7000 | 0.0055          | 0.9912    | 0.9951 | 0.9932 | 0.9986   |
| 0.0020        | 3.6819 | 7500 | 0.0052          | 0.9911    | 0.9952 | 0.9932 | 0.9987   |


### Framework versions

- Transformers 5.12.1
- Pytorch 2.12.0+cu130
- Datasets 5.0.0
- Tokenizers 0.22.2
