---
library_name: transformers
license: apache-2.0
base_model: answerdotai/ModernBERT-base
tags:
- trackio
- trackio:https://huggingface.co/spaces/jefftherover/huggingface-static-867e22
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: modernbert-pii-mapped-v9
  results: []
---
<a href="https://huggingface.co/spaces/jefftherover/huggingface-static-867e22" target="_blank"><img src="https://raw.githubusercontent.com/gradio-app/trackio/refs/heads/main/trackio/assets/badge.png" alt="Visualize in Trackio" title="Visualize in Trackio" style="height: 40px;"/></a>
<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# modernbert-pii-mapped-v9

This model is a fine-tuned version of [answerdotai/ModernBERT-base](https://huggingface.co/answerdotai/ModernBERT-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0082
- Precision: 0.9732
- Recall: 0.9868
- F1: 0.9799
- Accuracy: 0.9977

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
| 0.0770        | 0.3591 | 500  | 0.0385          | 0.8678    | 0.9505 | 0.9073 | 0.9893   |
| 0.0417        | 0.7181 | 1000 | 0.0166          | 0.9362    | 0.9773 | 0.9563 | 0.9949   |
| 0.0210        | 1.0768 | 1500 | 0.0104          | 0.9554    | 0.9816 | 0.9684 | 0.9968   |
| 0.0151        | 1.4359 | 2000 | 0.0141          | 0.9636    | 0.9861 | 0.9747 | 0.9965   |
| 0.0128        | 1.7950 | 2500 | 0.0113          | 0.9561    | 0.9745 | 0.9652 | 0.9965   |
| 0.0057        | 2.1537 | 3000 | 0.0080          | 0.9716    | 0.9947 | 0.9830 | 0.9977   |
| 0.0061        | 2.5127 | 3500 | 0.0078          | 0.9726    | 0.9934 | 0.9829 | 0.9977   |
| 0.0081        | 2.8718 | 4000 | 0.0083          | 0.9704    | 0.9879 | 0.9791 | 0.9976   |
| 0.0021        | 3.2305 | 4500 | 0.0082          | 0.9732    | 0.9868 | 0.9799 | 0.9977   |


### Framework versions

- Transformers 5.9.0
- Pytorch 2.12.0+cu130
- Datasets 4.8.5
- Tokenizers 0.22.2
