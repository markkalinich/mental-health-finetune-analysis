---
library_name: transformers
language:
- en
license: apache-2.0
base_model: Mardiyyah/CeLLaTe-tapt-pubmedbert-tokenizer-adapted-wwmask-combinedData
tags:
- generated_from_trainer
metrics:
- precision
- recall
- accuracy
model-index:
- name: CeLLaTe-ner-2class-reinitllrd-tapt-pubmedbert-tokenizer-adapted-combData-gazetteers-lr_3.36e5
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# CeLLaTe-ner-2class-reinitllrd-tapt-pubmedbert-tokenizer-adapted-combData-gazetteers-lr_3.36e5

This model is a fine-tuned version of [Mardiyyah/CeLLaTe-tapt-pubmedbert-tokenizer-adapted-wwmask-combinedData](https://huggingface.co/Mardiyyah/CeLLaTe-tapt-pubmedbert-tokenizer-adapted-wwmask-combinedData) on the OTAR3088/CeLLaTe-ner-2class-iob_final dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1191
- Precision: 0.7710
- Recall: 0.7715
- Micro F1: 0.7713
- Weighted F1: 0.7716
- Macro F1: 0.7796
- Accuracy: 0.9840

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 3.3553919637731326e-05
- train_batch_size: 32
- eval_batch_size: 16
- seed: 17
- gradient_accumulation_steps: 2
- total_train_batch_size: 64
- optimizer: Use OptimizerNames.ADAMW_TORCH with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: cosine
- lr_scheduler_warmup_ratio: 0.01
- num_epochs: 20
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | Micro F1 | Weighted F1 | Macro F1 | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:--------:|:-----------:|:--------:|:--------:|
| 0.1691        | 1.0   | 526  | 0.0682          | 0.5931    | 0.7486 | 0.6619   | 0.6628      | 0.6760   | 0.9754   |
| 0.0159        | 2.0   | 1052 | 0.0743          | 0.7810    | 0.7204 | 0.7495   | 0.7497      | 0.7593   | 0.9834   |
| 0.0078        | 3.0   | 1578 | 0.0803          | 0.7541    | 0.7523 | 0.7532   | 0.7532      | 0.7593   | 0.9834   |
| 0.0042        | 4.0   | 2104 | 0.1010          | 0.6814    | 0.7974 | 0.7348   | 0.7374      | 0.7548   | 0.9805   |
| 0.0029        | 5.0   | 2630 | 0.0922          | 0.7690    | 0.7589 | 0.7639   | 0.7641      | 0.7681   | 0.9844   |
| 0.0023        | 6.0   | 3156 | 0.1128          | 0.7829    | 0.7330 | 0.7571   | 0.7570      | 0.7669   | 0.9833   |
| 0.0017        | 7.0   | 3682 | 0.1158          | 0.8085    | 0.7288 | 0.7666   | 0.7667      | 0.7750   | 0.9836   |
| 0.0013        | 8.0   | 4208 | 0.1334          | 0.8062    | 0.7156 | 0.7582   | 0.7575      | 0.7695   | 0.9825   |
| 0.0012        | 9.0   | 4734 | 0.1144          | 0.7839    | 0.7589 | 0.7712   | 0.7713      | 0.7774   | 0.9839   |
| 0.001         | 10.0  | 5260 | 0.1145          | 0.7751    | 0.7565 | 0.7657   | 0.7657      | 0.7740   | 0.9844   |
| 0.0008        | 11.0  | 5786 | 0.1205          | 0.7857    | 0.7541 | 0.7696   | 0.7696      | 0.7776   | 0.9843   |
| 0.0006        | 12.0  | 6312 | 0.1188          | 0.7706    | 0.7715 | 0.7710   | 0.7714      | 0.7794   | 0.9840   |
| 0.0005        | 13.0  | 6838 | 0.1269          | 0.7808    | 0.7474 | 0.7637   | 0.7638      | 0.7731   | 0.9837   |
| 0.0005        | 14.0  | 7364 | 0.1324          | 0.7712    | 0.7601 | 0.7656   | 0.7659      | 0.7741   | 0.9834   |
| 0.0004        | 15.0  | 7890 | 0.1304          | 0.7889    | 0.7529 | 0.7705   | 0.7705      | 0.7787   | 0.9842   |


### Framework versions

- Transformers 4.48.2
- Pytorch 2.4.1+cu121
- Datasets 3.0.2
- Tokenizers 0.21.0
