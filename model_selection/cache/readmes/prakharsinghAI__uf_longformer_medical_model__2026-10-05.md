---
library_name: transformers
license: apache-2.0
base_model: allenai/longformer-base-4096
tags:
- generated_from_trainer
metrics:
- accuracy
- precision
- recall
model-index:
- name: uf_longformer_medical_model
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# uf_longformer_medical_model

This model is a fine-tuned version of [allenai/longformer-base-4096](https://huggingface.co/allenai/longformer-base-4096) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 2.4604
- Accuracy: 0.3996
- F1 Weighted: 0.2799
- F1 Macro: 0.0430
- Precision: 0.2229
- Recall: 0.3996

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 16
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 100
- num_epochs: 3
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | F1 Weighted | F1 Macro | Precision | Recall |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:-----------:|:--------:|:---------:|:------:|
| 3.6859        | 1.0   | 147  | 3.4119          | 0.1142   | 0.0234      | 0.0031   | 0.0130    | 0.1142 |
| 3.5174        | 2.0   | 294  | 3.0762          | 0.3370   | 0.1754      | 0.0226   | 0.1188    | 0.3370 |
| 2.8324        | 3.0   | 441  | 2.4604          | 0.3996   | 0.2799      | 0.0430   | 0.2229    | 0.3996 |


### Framework versions

- Transformers 4.56.2
- Pytorch 2.8.0+cu126
- Datasets 4.0.0
- Tokenizers 0.22.1
