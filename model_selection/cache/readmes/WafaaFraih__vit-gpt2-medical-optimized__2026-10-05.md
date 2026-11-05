---
library_name: transformers
license: apache-2.0
base_model: nlpconnect/vit-gpt2-image-captioning
tags:
- generated_from_trainer
metrics:
- bleu
model-index:
- name: vit-gpt2-medical-optimized
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# vit-gpt2-medical-optimized

This model is a fine-tuned version of [nlpconnect/vit-gpt2-image-captioning](https://huggingface.co/nlpconnect/vit-gpt2-image-captioning) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 5.0098
- Bleu: 0.9833

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
- train_batch_size: 2
- eval_batch_size: 2
- seed: 42
- gradient_accumulation_steps: 8
- total_train_batch_size: 16
- optimizer: Use OptimizerNames.ADAMW_8BIT with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 100
- num_epochs: 3
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch  | Step | Validation Loss | Bleu   |
|:-------------:|:------:|:----:|:---------------:|:------:|
| 5.4924        | 0.9412 | 250  | 5.3911          | 0.0    |
| 5.1009        | 1.8809 | 500  | 5.0913          | 3.9891 |
| 4.7911        | 2.8207 | 750  | 5.0098          | 0.9833 |


### Framework versions

- Transformers 4.56.0
- Pytorch 2.8.0+cu126
- Datasets 4.0.0
- Tokenizers 0.22.0
