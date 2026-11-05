---
library_name: transformers
license: apache-2.0
base_model: answerdotai/ModernBERT-base
tags:
- trackio
- trackio:https://huggingface.co/spaces/jefftherover/huggingface-static-0ef3e9
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: modernbert-pii-mapped-v8
  results: []
---
<a href="https://huggingface.co/spaces/jefftherover/huggingface-static-0ef3e9" target="_blank"><img src="https://raw.githubusercontent.com/gradio-app/trackio/refs/heads/main/trackio/assets/badge.png" alt="Visualize in Trackio" title="Visualize in Trackio" style="height: 40px;"/></a>
<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# modernbert-pii-mapped-v8

This model is a fine-tuned version of [answerdotai/ModernBERT-base](https://huggingface.co/answerdotai/ModernBERT-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0128
- Precision: 0.9482
- Recall: 0.9583
- F1: 0.9532
- Accuracy: 0.9965

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
| 0.0677        | 0.4087 | 500  | 0.0285          | 0.8815    | 0.9724 | 0.9247 | 0.9913   |
| 0.0359        | 0.8173 | 1000 | 0.0150          | 0.9371    | 0.9710 | 0.9538 | 0.9957   |
| 0.0200        | 1.2256 | 1500 | 0.0127          | 0.9476    | 0.9846 | 0.9658 | 0.9965   |
| 0.0168        | 1.6342 | 2000 | 0.0109          | 0.9422    | 0.9741 | 0.9579 | 0.9965   |
| 0.0135        | 2.0425 | 2500 | 0.0096          | 0.9560    | 0.9695 | 0.9627 | 0.9971   |
| 0.0067        | 2.4512 | 3000 | 0.0128          | 0.9482    | 0.9583 | 0.9532 | 0.9965   |


### Framework versions

- Transformers 5.9.0
- Pytorch 2.12.0+cu130
- Datasets 4.8.5
- Tokenizers 0.22.2
