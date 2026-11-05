---
library_name: transformers
license: cc-by-sa-4.0
base_model: nlpaueb/legal-bert-base-uncased
tags:
- generated_from_trainer
metrics:
- accuracy
- f1
model-index:
- name: legal-bert-base-uncased-finetuned-medmcqa-2024-11-25-T15-39-29
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# legal-bert-base-uncased-finetuned-medmcqa-2024-11-25-T15-39-29

This model is a fine-tuned version of [nlpaueb/legal-bert-base-uncased](https://huggingface.co/nlpaueb/legal-bert-base-uncased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.3852
- Accuracy: 0.3810
- F1: 0.4126

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
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- gradient_accumulation_steps: 8
- total_train_batch_size: 32
- optimizer: Use adamw_torch with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 1
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch  | Step | Validation Loss | Accuracy | F1     |
|:-------------:|:------:|:----:|:---------------:|:--------:|:------:|
| 1.3984        | 0.9978 | 57   | 1.3852          | 0.3810   | 0.4126 |


### Framework versions

- Transformers 4.46.2
- Pytorch 2.5.1+cu121
- Datasets 3.1.0
- Tokenizers 0.20.3
