---
library_name: transformers
license: apache-2.0
base_model: castorini/afriteva_v2_base
tags:
- full-finetuning
- amharic
- sentiment-analysis
- generated_from_trainer
model-index:
- name: STL-Sentiment-FullFT-afriteva_v2_base
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# STL-Sentiment-FullFT-afriteva_v2_base

This model is a fine-tuned version of [castorini/afriteva_v2_base](https://huggingface.co/castorini/afriteva_v2_base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.7460
- Sentiment-accuracy: 0.7219
- Macro F1: 0.7116

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0003
- train_batch_size: 8
- eval_batch_size: 16
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 32
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: cosine
- lr_scheduler_warmup_steps: 300
- num_epochs: 10
- label_smoothing_factor: 0.1

### Training results

| Training Loss | Epoch | Step | Validation Loss | Sentiment-accuracy | Macro F1 |
|:-------------:|:-----:|:----:|:---------------:|:------------------:|:--------:|
| 2.5846        | 1.0   | 189  | 2.0586          | 0.4738             | 0.4220   |
| 1.9048        | 2.0   | 378  | 1.7986          | 0.6746             | 0.6730   |
| 1.8069        | 3.0   | 567  | 1.7765          | 0.6983             | 0.6737   |
| 1.7655        | 4.0   | 756  | 1.7440          | 0.7182             | 0.7095   |
| 1.7598        | 5.0   | 945  | 1.7456          | 0.7107             | 0.6922   |
| 1.7259        | 6.0   | 1134 | 1.7409          | 0.7257             | 0.7172   |
| 1.7265        | 7.0   | 1323 | 1.7509          | 0.7120             | 0.6975   |
| 1.7143        | 8.0   | 1512 | 1.7444          | 0.7207             | 0.7112   |
| 1.7146        | 9.0   | 1701 | 1.7460          | 0.7219             | 0.7116   |


### Framework versions

- Transformers 5.18.0
- Pytorch 2.11.0+cu130
- Datasets 4.8.5
- Tokenizers 0.23.2
