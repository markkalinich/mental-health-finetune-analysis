---
library_name: transformers
language:
- en
license: apache-2.0
base_model: Mardiyyah/CeLLaTe-tapt-pubmedbert-tokenizer-adapted-wwmask
tags:
- generated_from_trainer
metrics:
- precision
- recall
- accuracy
model-index:
- name: CeLLaTe-ner-3class-pubmedbert-tapt-tokenizer-adapted-wwmask-lr_4.029
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# CeLLaTe-ner-3class-pubmedbert-tapt-tokenizer-adapted-wwmask-lr_4.029

This model is a fine-tuned version of [Mardiyyah/CeLLaTe-tapt-pubmedbert-tokenizer-adapted-wwmask](https://huggingface.co/Mardiyyah/CeLLaTe-tapt-pubmedbert-tokenizer-adapted-wwmask) on the OTAR3088/CeLLaTe-ner-3class-iob_final dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1014
- Precision: 0.7826
- Recall: 0.7424
- Micro F1: 0.7620
- Weighted F1: 0.7622
- Macro F1: 0.7607
- Accuracy: 0.9824

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 4.029773209271021e-05
- train_batch_size: 32
- eval_batch_size: 32
- seed: 10472999
- gradient_accumulation_steps: 2
- total_train_batch_size: 64
- optimizer: Use OptimizerNames.ADAMW_TORCH with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.06
- num_epochs: 20
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | Micro F1 | Weighted F1 | Macro F1 | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:--------:|:-----------:|:--------:|:--------:|
| 0.8266        | 1.0   | 132  | 0.1413          | 0.2311    | 0.2099 | 0.2200   | 0.1443      | 0.1089   | 0.9518   |
| 0.0885        | 2.0   | 264  | 0.0782          | 0.7548    | 0.6003 | 0.6688   | 0.6615      | 0.6566   | 0.9784   |
| 0.0379        | 3.0   | 396  | 0.0664          | 0.7237    | 0.7204 | 0.7220   | 0.7240      | 0.7256   | 0.9808   |
| 0.0255        | 4.0   | 528  | 0.0736          | 0.7046    | 0.7342 | 0.7191   | 0.7185      | 0.7190   | 0.9804   |
| 0.0205        | 5.0   | 660  | 0.0779          | 0.7810    | 0.7245 | 0.7517   | 0.7487      | 0.7432   | 0.9824   |
| 0.0134        | 6.0   | 792  | 0.0843          | 0.7753    | 0.7009 | 0.7362   | 0.7362      | 0.7332   | 0.9816   |
| 0.0103        | 7.0   | 924  | 0.0807          | 0.7650    | 0.7465 | 0.7556   | 0.7558      | 0.7539   | 0.9831   |
| 0.0081        | 8.0   | 1056 | 0.0876          | 0.7516    | 0.7404 | 0.7459   | 0.7461      | 0.7445   | 0.9812   |
| 0.0065        | 9.0   | 1188 | 0.0993          | 0.7690    | 0.7260 | 0.7469   | 0.7467      | 0.7461   | 0.9813   |
| 0.0056        | 10.0  | 1320 | 0.0912          | 0.7485    | 0.7450 | 0.7467   | 0.7471      | 0.7474   | 0.9817   |
| 0.0049        | 11.0  | 1452 | 0.1002          | 0.7826    | 0.7424 | 0.7620   | 0.7622      | 0.7607   | 0.9824   |
| 0.0046        | 12.0  | 1584 | 0.1069          | 0.7910    | 0.7342 | 0.7616   | 0.7617      | 0.7604   | 0.9827   |
| 0.0034        | 13.0  | 1716 | 0.0993          | 0.7575    | 0.7563 | 0.7569   | 0.7573      | 0.7574   | 0.9824   |
| 0.003         | 14.0  | 1848 | 0.1136          | 0.7919    | 0.7281 | 0.7586   | 0.7577      | 0.7570   | 0.9826   |
| 0.0026        | 15.0  | 1980 | 0.1111          | 0.7954    | 0.7281 | 0.7602   | 0.7597      | 0.7584   | 0.9829   |
| 0.0024        | 16.0  | 2112 | 0.1069          | 0.7770    | 0.7455 | 0.7609   | 0.7607      | 0.7593   | 0.9828   |


### Framework versions

- Transformers 4.48.2
- Pytorch 2.4.1+cu121
- Datasets 3.0.2
- Tokenizers 0.21.0
