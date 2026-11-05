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
- name: CeLLaTe-ner-2class-tapt-pubmedbert-reinitllrd-tokenizer-adapted-combinedData-lr_3.215
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# CeLLaTe-ner-2class-tapt-pubmedbert-reinitllrd-tokenizer-adapted-combinedData-lr_3.215

This model is a fine-tuned version of [Mardiyyah/CeLLaTe-tapt-pubmedbert-tokenizer-adapted-wwmask-combinedData](https://huggingface.co/Mardiyyah/CeLLaTe-tapt-pubmedbert-tokenizer-adapted-wwmask-combinedData) on the OTAR3088/CeLLaTe-ner-2class-iob_final dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1216
- Precision: 0.7861
- Recall: 0.7601
- Micro F1: 0.7729
- Weighted F1: 0.7731
- Macro F1: 0.7810
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
- learning_rate: 3.215e-05
- train_batch_size: 32
- eval_batch_size: 32
- seed: 3407
- gradient_accumulation_steps: 2
- total_train_batch_size: 64
- optimizer: Use OptimizerNames.ADAMW_TORCH with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.01
- num_epochs: 20
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | Micro F1 | Weighted F1 | Macro F1 | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:--------:|:-----------:|:--------:|:--------:|
| 0.1395        | 1.0   | 526  | 0.0609          | 0.7306    | 0.7468 | 0.7386   | 0.7388      | 0.7494   | 0.9829   |
| 0.0152        | 2.0   | 1052 | 0.0764          | 0.7473    | 0.7468 | 0.7471   | 0.7474      | 0.7607   | 0.9825   |
| 0.0072        | 3.0   | 1578 | 0.0989          | 0.7922    | 0.6831 | 0.7336   | 0.7334      | 0.7403   | 0.9825   |
| 0.0041        | 4.0   | 2104 | 0.0834          | 0.7472    | 0.7661 | 0.7565   | 0.7573      | 0.7684   | 0.9832   |
| 0.0027        | 5.0   | 2630 | 0.1005          | 0.7572    | 0.7595 | 0.7583   | 0.7588      | 0.7681   | 0.9828   |
| 0.0019        | 6.0   | 3156 | 0.1007          | 0.7334    | 0.7727 | 0.7526   | 0.7538      | 0.7659   | 0.9828   |
| 0.0015        | 7.0   | 3682 | 0.1114          | 0.8016    | 0.7360 | 0.7674   | 0.7674      | 0.7748   | 0.9841   |
| 0.0012        | 8.0   | 4208 | 0.1120          | 0.775     | 0.7643 | 0.7696   | 0.7698      | 0.7767   | 0.9837   |
| 0.0013        | 9.0   | 4734 | 0.1137          | 0.7363    | 0.7757 | 0.7555   | 0.7560      | 0.7662   | 0.9826   |
| 0.0012        | 10.0  | 5260 | 0.1213          | 0.7764    | 0.7685 | 0.7724   | 0.7728      | 0.7802   | 0.9840   |
| 0.0008        | 11.0  | 5786 | 0.1213          | 0.7861    | 0.7601 | 0.7729   | 0.7731      | 0.7810   | 0.9839   |
| 0.0007        | 12.0  | 6312 | 0.1268          | 0.7780    | 0.7565 | 0.7671   | 0.7671      | 0.7738   | 0.9838   |
| 0.0007        | 13.0  | 6838 | 0.1243          | 0.7806    | 0.7661 | 0.7733   | 0.7734      | 0.7798   | 0.9836   |
| 0.0005        | 14.0  | 7364 | 0.1237          | 0.7673    | 0.7673 | 0.7673   | 0.7676      | 0.7768   | 0.9835   |


### Framework versions

- Transformers 4.48.2
- Pytorch 2.4.1+cu121
- Datasets 3.0.2
- Tokenizers 0.21.0
