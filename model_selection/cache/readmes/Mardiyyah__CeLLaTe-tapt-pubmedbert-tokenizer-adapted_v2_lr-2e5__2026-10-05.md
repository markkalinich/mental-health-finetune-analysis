---
library_name: transformers
language:
- en
license: apache-2.0
base_model: microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract-fulltext
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: CeLLaTe-tapt-pubmedbert-tokenizer-adapted_v2_lr-2e5
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# CeLLaTe-tapt-pubmedbert-tokenizer-adapted_v2_lr-2e5

This model is a fine-tuned version of [microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract-fulltext](https://huggingface.co/microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract-fulltext) on the Mardiyyah/TAPT_CeLLaTe2.0 dataset.
It achieves the following results on the evaluation set:
- Loss: 1.1498
- Accuracy: 0.7645
- Perplexity: 3.1576

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
- train_batch_size: 32
- eval_batch_size: 32
- seed: 3407
- gradient_accumulation_steps: 2
- total_train_batch_size: 64
- optimizer: Use OptimizerNames.ADAMW_TORCH with betas=(0.9,0.999) and epsilon=1e-06 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.06
- num_epochs: 100
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | Perplexity |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:----------:|
| 1.3593        | 1.0   | 14   | 1.2054          | 0.7589   | 3.3382     |
| 1.3738        | 2.0   | 28   | 1.2002          | 0.7611   | 3.3209     |
| 1.3468        | 3.0   | 42   | 1.1980          | 0.7585   | 3.3135     |
| 1.3319        | 4.0   | 56   | 1.2181          | 0.7557   | 3.3808     |
| 1.3085        | 5.0   | 70   | 1.2109          | 0.7581   | 3.3565     |
| 1.2994        | 6.0   | 84   | 1.2024          | 0.7545   | 3.3279     |
| 1.2836        | 7.0   | 98   | 1.1483          | 0.7640   | 3.1530     |
| 1.2806        | 8.0   | 112  | 1.2058          | 0.7517   | 3.3393     |
| 1.254         | 9.0   | 126  | 1.1481          | 0.7611   | 3.1522     |
| 1.247         | 10.0  | 140  | 1.1739          | 0.7567   | 3.2345     |
| 1.2627        | 11.0  | 154  | 1.1571          | 0.7559   | 3.1807     |
| 1.2227        | 12.0  | 168  | 1.1721          | 0.7587   | 3.2287     |
| 1.2235        | 13.0  | 182  | 1.2401          | 0.7522   | 3.4560     |
| 1.2163        | 14.0  | 196  | 1.1925          | 0.7567   | 3.2953     |


### Framework versions

- Transformers 4.48.2
- Pytorch 2.4.1+cu121
- Datasets 3.0.2
- Tokenizers 0.21.0
