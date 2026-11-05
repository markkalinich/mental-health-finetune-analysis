---
library_name: transformers
license: apache-2.0
base_model: answerdotai/ModernBERT-base
tags:
- trackio
- trackio:https://huggingface.co/spaces/jefftherover/huggingface-static-dbebfd
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: modernbert-pii-mapped-v13
  results: []
---
<a href="https://huggingface.co/spaces/jefftherover/huggingface-static-dbebfd" target="_blank"><img src="https://raw.githubusercontent.com/gradio-app/trackio/refs/heads/main/trackio/assets/badge.png" alt="Visualize in Trackio" title="Visualize in Trackio" style="height: 40px;"/></a>
<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# modernbert-pii-mapped-v13

This model is a fine-tuned version of [answerdotai/ModernBERT-base](https://huggingface.co/answerdotai/ModernBERT-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0151
- Precision: 0.9599
- Recall: 0.9700
- F1: 0.9650
- Accuracy: 0.9966

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
| 0.1180        | 0.3322 | 500  | 0.0509          | 0.7814    | 0.8566 | 0.8173 | 0.9844   |
| 0.0591        | 0.6645 | 1000 | 0.0326          | 0.8853    | 0.9299 | 0.9070 | 0.9910   |
| 0.0383        | 0.9967 | 1500 | 0.0202          | 0.9219    | 0.9577 | 0.9395 | 0.9936   |
| 0.0359        | 1.3289 | 2000 | 0.0172          | 0.9408    | 0.9617 | 0.9511 | 0.9953   |
| 0.0233        | 1.6611 | 2500 | 0.0149          | 0.9469    | 0.9655 | 0.9561 | 0.9961   |
| 0.0226        | 1.9934 | 3000 | 0.0154          | 0.9458    | 0.9647 | 0.9551 | 0.9957   |
| 0.0137        | 2.3256 | 3500 | 0.0142          | 0.9583    | 0.9732 | 0.9657 | 0.9964   |
| 0.0112        | 2.6578 | 4000 | 0.0141          | 0.9542    | 0.9700 | 0.9620 | 0.9964   |
| 0.0105        | 2.9900 | 4500 | 0.0142          | 0.9523    | 0.9657 | 0.9589 | 0.9962   |
| 0.0049        | 3.3223 | 5000 | 0.0151          | 0.9599    | 0.9700 | 0.9650 | 0.9966   |


### Framework versions

- Transformers 5.9.0
- Pytorch 2.12.0+cu130
- Datasets 4.8.5
- Tokenizers 0.22.2
