---
library_name: transformers
license: apache-2.0
base_model: Falconsai/medical_summarization
tags:
- generated_from_trainer
metrics:
- rouge
model-index:
- name: Fine-Tuned-clinical-Summarization
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Fine-Tuned-clinical-Summarization

This model is a fine-tuned version of [Falconsai/medical_summarization](https://huggingface.co/Falconsai/medical_summarization) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 5.1563
- Rouge1: 0.044
- Rouge2: 0.0041
- Rougel: 0.0338
- Rougelsum: 0.0337
- Generated Length: 19.0

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
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Use adamw_torch with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 3
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Rouge1 | Rouge2 | Rougel | Rougelsum | Generated Length |
|:-------------:|:-----:|:----:|:---------------:|:------:|:------:|:------:|:---------:|:----------------:|
| No log        | 1.0   | 2    | 5.2591          | 0.044  | 0.0041 | 0.0338 | 0.0337    | 19.0             |
| No log        | 2.0   | 4    | 5.1865          | 0.044  | 0.0041 | 0.0338 | 0.0337    | 19.0             |
| No log        | 3.0   | 6    | 5.1563          | 0.044  | 0.0041 | 0.0338 | 0.0337    | 19.0             |


### Framework versions

- Transformers 4.46.2
- Pytorch 2.5.1+cu121
- Datasets 3.1.0
- Tokenizers 0.20.3
