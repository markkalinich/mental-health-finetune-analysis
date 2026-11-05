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
- name: CeLLaTe-tapt-pubmedbert-tokenizer-adapted-wwmask
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# CeLLaTe-tapt-pubmedbert-tokenizer-adapted-wwmask

This model is a fine-tuned version of [microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract-fulltext](https://huggingface.co/microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract-fulltext) on the Mardiyyah/TAPT_CeLLaTe2.0 dataset.
It achieves the following results on the evaluation set:
- Loss: 1.2144
- Accuracy: 0.7569
- Perplexity: 3.3682

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 3e-05
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
| 1.4325        | 1.0   | 14   | 1.2906          | 0.7533   | 3.6351     |
| 1.4038        | 2.0   | 28   | 1.2569          | 0.7560   | 3.5146     |
| 1.3795        | 3.0   | 42   | 1.2207          | 0.7535   | 3.3895     |
| 1.3515        | 4.0   | 56   | 1.1725          | 0.7632   | 3.2301     |
| 1.3173        | 5.0   | 70   | 1.1807          | 0.7625   | 3.2565     |
| 1.271         | 6.0   | 84   | 1.1901          | 0.7561   | 3.2874     |
| 1.2655        | 7.0   | 98   | 1.1605          | 0.7615   | 3.1915     |
| 1.2681        | 8.0   | 112  | 1.1396          | 0.7630   | 3.1255     |
| 1.2362        | 9.0   | 126  | 1.1118          | 0.7709   | 3.0397     |
| 1.2196        | 10.0  | 140  | 1.1419          | 0.7619   | 3.1328     |
| 1.2191        | 11.0  | 154  | 1.1508          | 0.7569   | 3.1606     |
| 1.1892        | 12.0  | 168  | 1.1398          | 0.7642   | 3.1263     |
| 1.1819        | 13.0  | 182  | 1.1509          | 0.7616   | 3.1612     |
| 1.1469        | 14.0  | 196  | 1.1664          | 0.7601   | 3.2103     |


### Framework versions

- Transformers 4.48.2
- Pytorch 2.4.1+cu121
- Datasets 3.0.2
- Tokenizers 0.21.0
