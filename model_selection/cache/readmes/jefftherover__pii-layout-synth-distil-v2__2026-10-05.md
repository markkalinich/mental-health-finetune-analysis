---
library_name: transformers
base_model: jefftherover/pii-layout-synth-distil-v2
tags:
- trackio
- trackio:https://huggingface.co/spaces/jefftherover/huggingface-static-d56766
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: pii-layout-synth-distil-v2
  results: []
---
<a href="https://huggingface.co/spaces/jefftherover/huggingface-static-d56766" target="_blank"><img src="https://raw.githubusercontent.com/gradio-app/trackio/refs/heads/main/trackio/assets/badge.png" alt="Visualize in Trackio" title="Visualize in Trackio" style="height: 40px;"/></a>
<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# pii-layout-synth-distil-v2

This model is a fine-tuned version of [jefftherover/pii-layout-synth-distil-v2](https://huggingface.co/jefftherover/pii-layout-synth-distil-v2) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0048
- Precision: 0.9916
- Recall: 0.9951
- F1: 0.9933
- Accuracy: 0.9988

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0002
- train_batch_size: 16
- eval_batch_size: 8
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
| 9.4312        | 0.9685 | 2000  | 0.0066          | 0.9893    | 0.9944 | 0.9918 | 0.9984   |
| 8.3837        | 1.9370 | 4000  | 0.0056          | 0.9896    | 0.9935 | 0.9916 | 0.9986   |
| 7.6715        | 2.9056 | 6000  | 0.0049          | 0.9915    | 0.9948 | 0.9931 | 0.9987   |
| 7.4892        | 3.8741 | 8000  | 0.0048          | 0.9914    | 0.9947 | 0.9930 | 0.9988   |
| 7.1226        | 4.8426 | 10000 | 0.0048          | 0.9914    | 0.9949 | 0.9932 | 0.9988   |
| 7.3554        | 5.0    | 10325 | 0.0048          | 0.9916    | 0.9951 | 0.9933 | 0.9988   |


### Framework versions

- Transformers 5.13.1
- Pytorch 2.13.0+cu130
- Datasets 5.0.0
- Tokenizers 0.22.2
