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
- name: CeLLaTe-tapt-pubmedbert-tokenizer-original-baseline-combinedData
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# CeLLaTe-tapt-pubmedbert-tokenizer-original-baseline-combinedData

This model is a fine-tuned version of [microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract-fulltext](https://huggingface.co/microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract-fulltext) on the Mardiyyah/Combined_TAPT_dataset dataset.
It achieves the following results on the evaluation set:
- Loss: 0.9904
- Accuracy: 0.7745
- Perplexity: 2.6923

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
| 1.1406        | 1.0   | 28   | 1.0306          | 0.7735   | 2.8028     |
| 1.1214        | 2.0   | 56   | 0.9953          | 0.7771   | 2.7055     |
| 1.1017        | 3.0   | 84   | 0.9777          | 0.7752   | 2.6582     |
| 1.0798        | 4.0   | 112  | 0.9868          | 0.7746   | 2.6826     |
| 1.0642        | 5.0   | 140  | 0.9592          | 0.7816   | 2.6096     |
| 1.0604        | 6.0   | 168  | 0.9888          | 0.7742   | 2.6880     |
| 1.0397        | 7.0   | 196  | 0.9889          | 0.7761   | 2.6884     |
| 1.039         | 8.0   | 224  | 0.9815          | 0.7780   | 2.6683     |
| 1.0295        | 9.0   | 252  | 0.9945          | 0.7729   | 2.7035     |
| 1.0088        | 10.0  | 280  | 0.9534          | 0.7820   | 2.5945     |
| 1.0021        | 11.0  | 308  | 0.9779          | 0.7746   | 2.6590     |
| 0.9926        | 12.0  | 336  | 0.9840          | 0.7751   | 2.6750     |
| 0.9761        | 13.0  | 364  | 0.9873          | 0.7769   | 2.6840     |
| 0.9724        | 14.0  | 392  | 0.9602          | 0.7809   | 2.6121     |
| 0.9665        | 15.0  | 420  | 0.9978          | 0.7726   | 2.7123     |


### Framework versions

- Transformers 4.48.2
- Pytorch 2.4.1+cu121
- Datasets 3.0.2
- Tokenizers 0.21.0
