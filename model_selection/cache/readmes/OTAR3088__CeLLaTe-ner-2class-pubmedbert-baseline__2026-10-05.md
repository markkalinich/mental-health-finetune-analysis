---
library_name: transformers
language:
- en
license: apache-2.0
base_model: microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract-fulltext
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: CeLLaTe-ner-pubmedbert-baseline
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# CeLLaTe-ner-pubmedbert-baseline

This model is a fine-tuned version of [microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract-fulltext](https://huggingface.co/microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract-fulltext) on the OTAR3088/CeLLaTe_V3.2_contracted_ent_IOB dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0640
- Precision: 0.7746
- Recall: 0.7254
- F1: 0.7492
- Accuracy: 0.9839

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
- seed: 3407
- gradient_accumulation_steps: 2
- total_train_batch_size: 32
- optimizer: Use OptimizerNames.ADAMW_TORCH with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.01
- num_epochs: 20
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.2418        | 1.0   | 263  | 0.0612          | 0.6099    | 0.7212 | 0.6609 | 0.9794   |
| 0.0403        | 2.0   | 526  | 0.0520          | 0.7575    | 0.7224 | 0.7395 | 0.9834   |
| 0.0258        | 3.0   | 789  | 0.0613          | 0.7419    | 0.7401 | 0.7410 | 0.9829   |
| 0.0196        | 4.0   | 1052 | 0.0644          | 0.7746    | 0.7254 | 0.7492 | 0.9839   |
| 0.0145        | 5.0   | 1315 | 0.0683          | 0.7746    | 0.7047 | 0.7380 | 0.9831   |
| 0.011         | 6.0   | 1578 | 0.0768          | 0.7628    | 0.7084 | 0.7346 | 0.9831   |
| 0.0086        | 7.0   | 1841 | 0.0732          | 0.7468    | 0.7450 | 0.7459 | 0.9838   |


### Framework versions

- Transformers 4.48.2
- Pytorch 2.4.1+cu121
- Datasets 3.0.2
- Tokenizers 0.21.0
