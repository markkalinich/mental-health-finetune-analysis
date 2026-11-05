---
library_name: transformers
license: apache-2.0
base_model: answerdotai/ModernBERT-base
tags:
- trackio
- trackio:https://huggingface.co/spaces/jefftherover/huggingface-static-e3633c
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: pii-layout-synth-v3
  results: []
---
<a href="https://huggingface.co/spaces/jefftherover/huggingface-static-e3633c" target="_blank"><img src="https://raw.githubusercontent.com/gradio-app/trackio/refs/heads/main/trackio/assets/badge.png" alt="Visualize in Trackio" title="Visualize in Trackio" style="height: 40px;"/></a>
<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# pii-layout-synth-v3

This model is a fine-tuned version of [answerdotai/ModernBERT-base](https://huggingface.co/answerdotai/ModernBERT-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0055
- Precision: 0.9914
- Recall: 0.9947
- F1: 0.9931
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
| 0.0941        | 0.2455 | 500  | 0.0329          | 0.9150    | 0.9472 | 0.9308 | 0.9901   |
| 0.0345        | 0.4909 | 1000 | 0.0140          | 0.9659    | 0.9789 | 0.9723 | 0.9956   |
| 0.0272        | 0.7364 | 1500 | 0.0109          | 0.9778    | 0.9857 | 0.9817 | 0.9968   |
| 0.0181        | 0.9818 | 2000 | 0.0082          | 0.9816    | 0.9874 | 0.9845 | 0.9976   |
| 0.0105        | 1.2273 | 2500 | 0.0066          | 0.9858    | 0.9913 | 0.9885 | 0.9980   |
| 0.0110        | 1.4728 | 3000 | 0.0068          | 0.9849    | 0.9915 | 0.9882 | 0.9978   |
| 0.0112        | 1.7182 | 3500 | 0.0066          | 0.9845    | 0.9920 | 0.9882 | 0.9980   |
| 0.0117        | 1.9637 | 4000 | 0.0053          | 0.9880    | 0.9943 | 0.9912 | 0.9984   |
| 0.0057        | 2.2091 | 4500 | 0.0047          | 0.9886    | 0.9916 | 0.9901 | 0.9984   |
| 0.0063        | 2.4546 | 5000 | 0.0051          | 0.9895    | 0.9942 | 0.9918 | 0.9985   |
| 0.0040        | 2.7000 | 5500 | 0.0048          | 0.9915    | 0.9942 | 0.9929 | 0.9987   |
| 0.0042        | 2.9455 | 6000 | 0.0049          | 0.9903    | 0.9947 | 0.9925 | 0.9986   |
| 0.0017        | 3.1910 | 6500 | 0.0055          | 0.9911    | 0.9954 | 0.9932 | 0.9986   |
| 0.0020        | 3.4364 | 7000 | 0.0053          | 0.9912    | 0.9945 | 0.9928 | 0.9986   |
| 0.0019        | 3.6819 | 7500 | 0.0055          | 0.9910    | 0.9946 | 0.9928 | 0.9987   |
| 0.0018        | 3.9273 | 8000 | 0.0055          | 0.9914    | 0.9947 | 0.9931 | 0.9987   |


### Framework versions

- Transformers 5.11.0
- Pytorch 2.12.0+cu130
- Datasets 5.0.0
- Tokenizers 0.22.2
