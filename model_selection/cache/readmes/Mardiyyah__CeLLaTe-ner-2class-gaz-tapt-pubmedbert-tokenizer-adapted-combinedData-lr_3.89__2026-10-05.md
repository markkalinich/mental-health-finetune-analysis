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
- name: CeLLaTe-ner-2class-tapt-pubmedbert-tokenizer-adapted-combinedData-lr_3.89
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# CeLLaTe-ner-2class-tapt-pubmedbert-tokenizer-adapted-combinedData-lr_3.89

This model is a fine-tuned version of [Mardiyyah/CeLLaTe-tapt-pubmedbert-tokenizer-adapted-wwmask-combinedData](https://huggingface.co/Mardiyyah/CeLLaTe-tapt-pubmedbert-tokenizer-adapted-wwmask-combinedData) on the OTAR3088/CeLLaTe-ner-2class-iob_final dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1149
- Precision: 0.7696
- Recall: 0.7853
- Micro F1: 0.7774
- Weighted F1: 0.7778
- Macro F1: 0.7857
- Accuracy: 0.9841

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 3.88548620843886e-05
- train_batch_size: 16
- eval_batch_size: 16
- seed: 3407
- gradient_accumulation_steps: 2
- total_train_batch_size: 32
- optimizer: Use OptimizerNames.ADAMW_TORCH with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.03
- num_epochs: 20
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | Micro F1 | Weighted F1 | Macro F1 | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:--------:|:-----------:|:--------:|:--------:|
| 0.1396        | 1.0   | 1052 | 0.0622          | 0.7545    | 0.7372 | 0.7457   | 0.7463      | 0.7586   | 0.9827   |
| 0.0132        | 2.0   | 2104 | 0.0786          | 0.6921    | 0.7679 | 0.7281   | 0.7286      | 0.7434   | 0.9810   |
| 0.0055        | 3.0   | 3156 | 0.0972          | 0.7227    | 0.7709 | 0.7460   | 0.7465      | 0.7590   | 0.9823   |
| 0.0034        | 4.0   | 4208 | 0.1046          | 0.7710    | 0.7673 | 0.7691   | 0.7693      | 0.7763   | 0.9836   |
| 0.0023        | 5.0   | 5260 | 0.1081          | 0.7828    | 0.7432 | 0.7625   | 0.7623      | 0.7710   | 0.9831   |
| 0.0019        | 6.0   | 6312 | 0.1153          | 0.7696    | 0.7853 | 0.7774   | 0.7778      | 0.7857   | 0.9841   |
| 0.0014        | 7.0   | 7364 | 0.1118          | 0.7570    | 0.7980 | 0.7769   | 0.7773      | 0.7846   | 0.9842   |
| 0.0015        | 8.0   | 8416 | 0.1111          | 0.7441    | 0.7799 | 0.7616   | 0.7617      | 0.7664   | 0.9826   |
| 0.0011        | 9.0   | 9468 | 0.1344          | 0.7805    | 0.7571 | 0.7686   | 0.7684      | 0.7740   | 0.9835   |


### Framework versions

- Transformers 4.48.2
- Pytorch 2.4.1+cu121
- Datasets 3.0.2
- Tokenizers 0.21.0
