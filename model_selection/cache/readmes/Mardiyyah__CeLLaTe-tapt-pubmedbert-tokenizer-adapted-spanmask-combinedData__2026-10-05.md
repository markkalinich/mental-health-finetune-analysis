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
- name: CeLLaTe-tapt-pubmedbert-tokenizer-adapted-spanmask-combinedData
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# CeLLaTe-tapt-pubmedbert-tokenizer-adapted-spanmask-combinedData

This model is a fine-tuned version of [microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract-fulltext](https://huggingface.co/microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract-fulltext) on the Mardiyyah/Combined_TAPT_dataset dataset.
It achieves the following results on the evaluation set:
- Loss: 2.2865
- Accuracy: 0.5769
- Perplexity: 9.8401

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
| 2.9396        | 1.0   | 28   | 2.5275          | 0.5599   | 12.5225    |
| 2.6425        | 2.0   | 56   | 2.4571          | 0.5677   | 11.6704    |
| 2.5762        | 3.0   | 84   | 2.3612          | 0.5702   | 10.6040    |
| 2.5444        | 4.0   | 112  | 2.3182          | 0.5815   | 10.1570    |
| 2.533         | 5.0   | 140  | 2.3575          | 0.5703   | 10.5645    |
| 2.4781        | 6.0   | 168  | 2.3388          | 0.5754   | 10.3687    |
| 2.4447        | 7.0   | 196  | 2.3351          | 0.5748   | 10.3308    |
| 2.4447        | 8.0   | 224  | 2.3080          | 0.5757   | 10.0540    |
| 2.4373        | 9.0   | 252  | 2.2718          | 0.5796   | 9.6969     |
| 2.4251        | 10.0  | 280  | 2.2967          | 0.5795   | 9.9413     |
| 2.4202        | 11.0  | 308  | 2.2407          | 0.5858   | 9.4003     |
| 2.3904        | 12.0  | 336  | 2.2537          | 0.5825   | 9.5226     |
| 2.3781        | 13.0  | 364  | 2.3002          | 0.5770   | 9.9764     |
| 2.3732        | 14.0  | 392  | 2.2511          | 0.5872   | 9.4982     |
| 2.3337        | 15.0  | 420  | 2.2408          | 0.5854   | 9.4009     |
| 2.3321        | 16.0  | 448  | 2.2484          | 0.5810   | 9.4722     |


### Framework versions

- Transformers 4.48.2
- Pytorch 2.4.1+cu121
- Datasets 3.0.2
- Tokenizers 0.21.0
