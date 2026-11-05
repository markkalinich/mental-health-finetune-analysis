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
- name: CeLLaTe-tapt-pubmedbert-tokenizer-adapted_v2_lr-1e5
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# CeLLaTe-tapt-pubmedbert-tokenizer-adapted_v2_lr-1e5

This model is a fine-tuned version of [microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract-fulltext](https://huggingface.co/microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract-fulltext) on the Mardiyyah/TAPT_CeLLaTe2.0 dataset.
It achieves the following results on the evaluation set:
- Loss: 1.1540
- Accuracy: 0.7656
- Perplexity: 3.1710

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-05
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
| 1.3604        | 1.0   | 14   | 1.2099          | 0.7589   | 3.3532     |
| 1.379         | 2.0   | 28   | 1.2093          | 0.7611   | 3.3510     |
| 1.3573        | 3.0   | 42   | 1.2053          | 0.7575   | 3.3377     |
| 1.3451        | 4.0   | 56   | 1.2265          | 0.7551   | 3.4092     |
| 1.3249        | 5.0   | 70   | 1.2203          | 0.7572   | 3.3881     |
| 1.3186        | 6.0   | 84   | 1.2113          | 0.7549   | 3.3579     |
| 1.3065        | 7.0   | 98   | 1.1578          | 0.7646   | 3.1829     |
| 1.3073        | 8.0   | 112  | 1.2125          | 0.7521   | 3.3620     |
| 1.2854        | 9.0   | 126  | 1.1526          | 0.7605   | 3.1665     |
| 1.2812        | 10.0  | 140  | 1.1805          | 0.7573   | 3.2559     |
| 1.2996        | 11.0  | 154  | 1.1601          | 0.7548   | 3.1903     |
| 1.2608        | 12.0  | 168  | 1.1775          | 0.7599   | 3.2463     |
| 1.2642        | 13.0  | 182  | 1.2410          | 0.7528   | 3.4592     |
| 1.2615        | 14.0  | 196  | 1.1971          | 0.7567   | 3.3107     |


### Framework versions

- Transformers 4.48.2
- Pytorch 2.4.1+cu121
- Datasets 3.0.2
- Tokenizers 0.21.0
