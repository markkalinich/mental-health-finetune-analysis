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
- accuracy
model-index:
- name: CeLLaTe-ner-2class-pubmedbert-baseline-with-gazetteers
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# CeLLaTe-ner-2class-pubmedbert-baseline-with-gazetteers

This model is a fine-tuned version of [microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract-fulltext](https://huggingface.co/microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract-fulltext) on the OTAR3088/CeLLaTe-ner-2class-iob_final dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1114
- Precision: 0.7806
- Recall: 0.7706
- Micro F1: 0.7756
- Weighted F1: 0.7757
- Macro F1: 0.7841
- Accuracy: 0.9849

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

| Training Loss | Epoch | Step  | Validation Loss | Precision | Recall | Micro F1 | Weighted F1 | Macro F1 | Accuracy |
|:-------------:|:-----:|:-----:|:---------------:|:---------:|:------:|:--------:|:-----------:|:--------:|:--------:|
| 0.1195        | 1.0   | 1052  | 0.0575          | 0.7415    | 0.7596 | 0.7505   | 0.7510      | 0.7605   | 0.9834   |
| 0.014         | 2.0   | 2104  | 0.0780          | 0.7921    | 0.7346 | 0.7623   | 0.7624      | 0.7703   | 0.9837   |
| 0.0061        | 3.0   | 3156  | 0.0862          | 0.7709    | 0.7370 | 0.7536   | 0.7535      | 0.7570   | 0.9836   |
| 0.0036        | 4.0   | 4208  | 0.0906          | 0.7855    | 0.7419 | 0.7631   | 0.7635      | 0.7712   | 0.9848   |
| 0.0023        | 5.0   | 5260  | 0.1029          | 0.7616    | 0.7505 | 0.7560   | 0.7561      | 0.7661   | 0.9835   |
| 0.0018        | 6.0   | 6312  | 0.1057          | 0.7565    | 0.7334 | 0.7447   | 0.7445      | 0.7374   | 0.9833   |
| 0.0013        | 7.0   | 7364  | 0.1107          | 0.7806    | 0.7706 | 0.7756   | 0.7757      | 0.7841   | 0.9849   |
| 0.0012        | 8.0   | 8416  | 0.1190          | 0.7478    | 0.7871 | 0.7669   | 0.7677      | 0.7783   | 0.9836   |
| 0.0009        | 9.0   | 9468  | 0.1196          | 0.7837    | 0.7492 | 0.7661   | 0.7661      | 0.7743   | 0.9841   |
| 0.0009        | 10.0  | 10520 | 0.1227          | 0.7746    | 0.7547 | 0.7645   | 0.7650      | 0.7761   | 0.9842   |
| 0.0007        | 11.0  | 11572 | 0.1317          | 0.7892    | 0.7492 | 0.7687   | 0.7690      | 0.7773   | 0.9844   |
| 0.0007        | 12.0  | 12624 | 0.1369          | 0.7735    | 0.7480 | 0.7605   | 0.7603      | 0.7700   | 0.9837   |


### Framework versions

- Transformers 4.48.2
- Pytorch 2.4.1+cu121
- Datasets 3.0.2
- Tokenizers 0.21.0
