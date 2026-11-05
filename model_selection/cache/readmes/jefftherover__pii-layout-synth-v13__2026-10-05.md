---
library_name: transformers
license: apache-2.0
base_model: answerdotai/ModernBERT-base
tags:
- trackio
- trackio:https://huggingface.co/spaces/jefftherover/huggingface-static-6c3eae
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: pii-layout-synth-v13
  results: []
---
<a href="https://huggingface.co/spaces/jefftherover/huggingface-static-6c3eae" target="_blank"><img src="https://raw.githubusercontent.com/gradio-app/trackio/refs/heads/main/trackio/assets/badge.png" alt="Visualize in Trackio" title="Visualize in Trackio" style="height: 40px;"/></a>
<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# pii-layout-synth-v13

This model is a fine-tuned version of [answerdotai/ModernBERT-base](https://huggingface.co/answerdotai/ModernBERT-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0050
- Precision: 0.9902
- Recall: 0.9943
- F1: 0.9923
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
- num_epochs: 4
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch  | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:------:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.0141        | 0.9818 | 2000 | 0.0074          | 0.9806    | 0.9857 | 0.9832 | 0.9975   |
| 0.0078        | 1.9637 | 4000 | 0.0050          | 0.9889    | 0.9945 | 0.9917 | 0.9984   |
| 0.0029        | 2.9455 | 6000 | 0.0045          | 0.9903    | 0.9950 | 0.9926 | 0.9986   |
| 0.0009        | 3.9273 | 8000 | 0.0050          | 0.9902    | 0.9943 | 0.9922 | 0.9986   |
| 0.0009        | 4.0    | 8148 | 0.0050          | 0.9902    | 0.9943 | 0.9923 | 0.9986   |


### Framework versions

- Transformers 5.12.1
- Pytorch 2.12.1+cu130
- Datasets 5.0.0
- Tokenizers 0.22.2
