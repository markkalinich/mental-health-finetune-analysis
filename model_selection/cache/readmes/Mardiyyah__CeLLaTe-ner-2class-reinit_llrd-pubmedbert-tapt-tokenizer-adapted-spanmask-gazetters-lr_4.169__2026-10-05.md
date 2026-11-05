---
library_name: transformers
language:
- en
license: apache-2.0
base_model: Mardiyyah/CeLLaTe-tapt-pubmedbert-tokenizer-adapted-spanmask
tags:
- generated_from_trainer
metrics:
- precision
- recall
- accuracy
model-index:
- name: CeLLaTe-ner-2class-reinit_llrd-pubmedbert-tapt-tokenizer-adapted-spanmask-gazetters-lr_4.169
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# CeLLaTe-ner-2class-reinit_llrd-pubmedbert-tapt-tokenizer-adapted-spanmask-gazetters-lr_4.169

This model is a fine-tuned version of [Mardiyyah/CeLLaTe-tapt-pubmedbert-tokenizer-adapted-spanmask](https://huggingface.co/Mardiyyah/CeLLaTe-tapt-pubmedbert-tokenizer-adapted-spanmask) on the OTAR3088/CeLLaTe-ner-2class-iob_final dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1085
- Precision: 0.8014
- Recall: 0.7787
- Micro F1: 0.7899
- Weighted F1: 0.7900
- Macro F1: 0.7958
- Accuracy: 0.9855

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 4.1695990556e-05
- train_batch_size: 16
- eval_batch_size: 16
- seed: 2026
- gradient_accumulation_steps: 2
- total_train_batch_size: 32
- optimizer: Use OptimizerNames.ADAMW_TORCH with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: cosine
- lr_scheduler_warmup_ratio: 0.03
- num_epochs: 20
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Precision | Recall | Micro F1 | Weighted F1 | Macro F1 | Accuracy |
|:-------------:|:-----:|:-----:|:---------------:|:---------:|:------:|:--------:|:-----------:|:--------:|:--------:|
| 0.156         | 1.0   | 1052  | 0.0645          | 0.7314    | 0.7468 | 0.7391   | 0.7399      | 0.7520   | 0.9832   |
| 0.0137        | 2.0   | 2104  | 0.0780          | 0.8041    | 0.7132 | 0.7559   | 0.7559      | 0.7666   | 0.9838   |
| 0.006         | 3.0   | 3156  | 0.0818          | 0.7424    | 0.7679 | 0.7550   | 0.7553      | 0.7650   | 0.9826   |
| 0.0038        | 4.0   | 4208  | 0.0947          | 0.7485    | 0.7697 | 0.7590   | 0.7592      | 0.7684   | 0.9830   |
| 0.0027        | 5.0   | 5260  | 0.1075          | 0.7372    | 0.7775 | 0.7568   | 0.7573      | 0.7670   | 0.9826   |
| 0.0021        | 6.0   | 6312  | 0.1112          | 0.7202    | 0.7956 | 0.756    | 0.7564      | 0.7630   | 0.9823   |
| 0.0019        | 7.0   | 7364  | 0.1120          | 0.7606    | 0.7354 | 0.7478   | 0.7478      | 0.7513   | 0.9828   |
| 0.0013        | 8.0   | 8416  | 0.1093          | 0.8014    | 0.7787 | 0.7899   | 0.7900      | 0.7958   | 0.9855   |
| 0.0015        | 9.0   | 9468  | 0.1177          | 0.8046    | 0.7577 | 0.7804   | 0.7805      | 0.7865   | 0.9848   |
| 0.0009        | 10.0  | 10520 | 0.1174          | 0.7576    | 0.7781 | 0.7677   | 0.7679      | 0.7729   | 0.9835   |
| 0.0008        | 11.0  | 11572 | 0.1164          | 0.7782    | 0.7745 | 0.7764   | 0.7768      | 0.7843   | 0.9844   |
| 0.0007        | 12.0  | 12624 | 0.1481          | 0.7200    | 0.7962 | 0.7561   | 0.7570      | 0.7660   | 0.9819   |
| 0.0006        | 13.0  | 13676 | 0.1353          | 0.7865    | 0.7865 | 0.7865   | 0.7866      | 0.7906   | 0.9843   |


### Framework versions

- Transformers 4.48.2
- Pytorch 2.4.1+cu121
- Datasets 3.0.2
- Tokenizers 0.21.0
