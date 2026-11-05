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
- name: CeLLaTe-tapt-pubmedbert-tokenizer-adapted-spanmask
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# CeLLaTe-tapt-pubmedbert-tokenizer-adapted-spanmask

This model is a fine-tuned version of [microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract-fulltext](https://huggingface.co/microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract-fulltext) on the Mardiyyah/TAPT_CeLLaTe2.0 dataset.
It achieves the following results on the evaluation set:
- Loss: 2.3029
- Accuracy: 0.5761
- Perplexity: 10.0034

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
| 3.0089        | 1.0   | 14   | 2.6409          | 0.5507   | 14.0253    |
| 2.7347        | 2.0   | 28   | 2.4055          | 0.5698   | 11.0835    |
| 2.6256        | 3.0   | 42   | 2.4142          | 0.5723   | 11.1810    |
| 2.5855        | 4.0   | 56   | 2.3657          | 0.5720   | 10.6515    |
| 2.5716        | 5.0   | 70   | 2.3596          | 0.5713   | 10.5871    |
| 2.5212        | 6.0   | 84   | 2.3339          | 0.5698   | 10.3177    |
| 2.4673        | 7.0   | 98   | 2.3420          | 0.5751   | 10.4017    |
| 2.4827        | 8.0   | 112  | 2.2801          | 0.5824   | 9.7779     |
| 2.4762        | 9.0   | 126  | 2.2619          | 0.5839   | 9.6009     |
| 2.457         | 10.0  | 140  | 2.2566          | 0.5845   | 9.5509     |
| 2.4403        | 11.0  | 154  | 2.3328          | 0.5761   | 10.3072    |
| 2.3889        | 12.0  | 168  | 2.2309          | 0.5902   | 9.3085     |
| 2.3968        | 13.0  | 182  | 2.2488          | 0.5802   | 9.4764     |
| 2.3618        | 14.0  | 196  | 2.2365          | 0.5814   | 9.3607     |
| 2.3805        | 15.0  | 210  | 2.2719          | 0.5776   | 9.6975     |
| 2.348         | 16.0  | 224  | 2.3000          | 0.5791   | 9.9740     |
| 2.3436        | 17.0  | 238  | 2.2701          | 0.5824   | 9.6807     |


### Framework versions

- Transformers 4.48.2
- Pytorch 2.4.1+cu121
- Datasets 3.0.2
- Tokenizers 0.21.0
