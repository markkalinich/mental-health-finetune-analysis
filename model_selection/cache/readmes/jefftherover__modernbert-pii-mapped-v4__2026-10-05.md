---
library_name: transformers
license: apache-2.0
base_model: answerdotai/ModernBERT-base
tags:
- trackio
- trackio:https://huggingface.co/spaces/jefftherover/huggingface-static-54e83a
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: modernbert-pii-mapped-v4
  results: []
---
<a href="https://huggingface.co/spaces/jefftherover/huggingface-static-54e83a" target="_blank"><img src="https://raw.githubusercontent.com/gradio-app/trackio/refs/heads/main/trackio/assets/badge.png" alt="Visualize in Trackio" title="Visualize in Trackio" style="height: 40px;"/></a>
<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# modernbert-pii-mapped-v4

This model is a fine-tuned version of [answerdotai/ModernBERT-base](https://huggingface.co/answerdotai/ModernBERT-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0069
- Precision: 0.9735
- Recall: 0.9809
- F1: 0.9772
- Accuracy: 0.9978

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
| 0.0514        | 0.4087 | 500  | 0.0215          | 0.9207    | 0.9544 | 0.9373 | 0.9937   |
| 0.0311        | 0.8173 | 1000 | 0.0110          | 0.9563    | 0.9818 | 0.9689 | 0.9969   |
| 0.0166        | 1.2256 | 1500 | 0.0090          | 0.9737    | 0.9909 | 0.9822 | 0.9976   |
| 0.0134        | 1.6342 | 2000 | 0.0072          | 0.9748    | 0.9879 | 0.9813 | 0.9980   |
| 0.0103        | 2.0425 | 2500 | 0.0074          | 0.9705    | 0.9776 | 0.9740 | 0.9975   |
| 0.0056        | 2.4512 | 3000 | 0.0069          | 0.9735    | 0.9809 | 0.9772 | 0.9978   |


### Framework versions

- Transformers 5.8.0
- Pytorch 2.11.0+cu130
- Datasets 4.8.5
- Tokenizers 0.22.2
