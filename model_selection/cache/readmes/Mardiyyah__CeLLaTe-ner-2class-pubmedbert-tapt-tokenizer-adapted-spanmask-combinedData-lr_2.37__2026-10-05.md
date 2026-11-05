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
- name: CeLLaTe-ner-2class-pubmedbert-tapt-tokenizer-adapted-spanmask-lr_2.37
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# CeLLaTe-ner-2class-pubmedbert-tapt-tokenizer-adapted-spanmask-lr_2.37

This model is a fine-tuned version of [Mardiyyah/CeLLaTe-tapt-pubmedbert-tokenizer-adapted-spanmask](https://huggingface.co/Mardiyyah/CeLLaTe-tapt-pubmedbert-tokenizer-adapted-spanmask) on the OTAR3088/CeLLaTe-ner-2class-iob_final dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0854
- Precision: 0.7459
- Recall: 0.7643
- Micro F1: 0.7550
- Weighted F1: 0.7554
- Macro F1: 0.7691
- Accuracy: 0.9837

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2.3706685643807145e-05
- train_batch_size: 32
- eval_batch_size: 16
- seed: 10472999
- gradient_accumulation_steps: 2
- total_train_batch_size: 64
- optimizer: Use OptimizerNames.ADAMW_TORCH with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: cosine
- lr_scheduler_warmup_ratio: 0.05
- num_epochs: 20
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | Micro F1 | Weighted F1 | Macro F1 | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:--------:|:-----------:|:--------:|:--------:|
| 0.6564        | 1.0   | 132  | 0.1156          | 0.2252    | 0.2038 | 0.2140   | 0.1787      | 0.1265   | 0.9545   |
| 0.0783        | 2.0   | 264  | 0.0548          | 0.7026    | 0.7017 | 0.7022   | 0.7028      | 0.7232   | 0.9820   |
| 0.0362        | 3.0   | 396  | 0.0590          | 0.7170    | 0.6933 | 0.7050   | 0.7056      | 0.7227   | 0.9820   |
| 0.0258        | 4.0   | 528  | 0.0644          | 0.7311    | 0.7162 | 0.7236   | 0.7242      | 0.7366   | 0.9827   |
| 0.0191        | 5.0   | 660  | 0.0626          | 0.7341    | 0.7270 | 0.7305   | 0.7308      | 0.7402   | 0.9834   |
| 0.0152        | 6.0   | 792  | 0.0681          | 0.7593    | 0.7150 | 0.7365   | 0.7367      | 0.7458   | 0.9831   |
| 0.0118        | 7.0   | 924  | 0.0709          | 0.7411    | 0.7486 | 0.7448   | 0.7451      | 0.7533   | 0.9835   |
| 0.0092        | 8.0   | 1056 | 0.0790          | 0.7654    | 0.7162 | 0.7400   | 0.7403      | 0.7518   | 0.9833   |
| 0.0074        | 9.0   | 1188 | 0.0743          | 0.7520    | 0.7384 | 0.7451   | 0.7452      | 0.7536   | 0.9840   |
| 0.0062        | 10.0  | 1320 | 0.0801          | 0.7458    | 0.7252 | 0.7354   | 0.7360      | 0.7501   | 0.9834   |
| 0.0053        | 11.0  | 1452 | 0.0843          | 0.7564    | 0.7450 | 0.7507   | 0.7509      | 0.7617   | 0.9842   |
| 0.0045        | 12.0  | 1584 | 0.0844          | 0.7452    | 0.7511 | 0.7481   | 0.7488      | 0.7618   | 0.9835   |
| 0.0038        | 13.0  | 1716 | 0.0859          | 0.7459    | 0.7643 | 0.7550   | 0.7554      | 0.7691   | 0.9837   |
| 0.0037        | 14.0  | 1848 | 0.0914          | 0.7714    | 0.7306 | 0.7505   | 0.7506      | 0.7621   | 0.9837   |
| 0.0032        | 15.0  | 1980 | 0.0891          | 0.7531    | 0.7354 | 0.7441   | 0.7448      | 0.7594   | 0.9837   |
| 0.003         | 16.0  | 2112 | 0.0925          | 0.7601    | 0.7336 | 0.7466   | 0.7470      | 0.7584   | 0.9837   |
| 0.0028        | 17.0  | 2244 | 0.0917          | 0.7465    | 0.7420 | 0.7443   | 0.7447      | 0.7567   | 0.9839   |
| 0.0028        | 18.0  | 2376 | 0.0928          | 0.7560    | 0.7378 | 0.7468   | 0.7472      | 0.7596   | 0.9837   |


### Framework versions

- Transformers 4.48.2
- Pytorch 2.4.1+cu121
- Datasets 3.0.2
- Tokenizers 0.21.0
