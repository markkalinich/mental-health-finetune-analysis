---
library_name: transformers
language:
- en
license: apache-2.0
base_model: Mardiyyah/CeLLaTe-tapt-pubmedbert-tokenizer-original-baseline
tags:
- generated_from_trainer
metrics:
- precision
- recall
- accuracy
model-index:
- name: CeLLaTe-ner-3class-pubmedbert-tapt-original-tokenizer-v1
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# CeLLaTe-ner-3class-pubmedbert-tapt-original-tokenizer-v1

This model is a fine-tuned version of [Mardiyyah/CeLLaTe-tapt-pubmedbert-tokenizer-original-baseline](https://huggingface.co/Mardiyyah/CeLLaTe-tapt-pubmedbert-tokenizer-original-baseline) on the OTAR3088/CeLLaTe-ner-3class-iob_final dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0899
- Precision: 0.7839
- Recall: 0.7423
- Micro F1: 0.7626
- Weighted F1: 0.7621
- Macro F1: 0.7588
- Accuracy: 0.9828

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

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | Micro F1 | Weighted F1 | Macro F1 | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:--------:|:-----------:|:--------:|:--------:|
| 0.3682        | 1.0   | 263  | 0.0833          | 0.5170    | 0.6419 | 0.5727   | 0.5659      | 0.5480   | 0.9746   |
| 0.0569        | 2.0   | 526  | 0.0682          | 0.7733    | 0.6783 | 0.7227   | 0.7221      | 0.7218   | 0.9807   |
| 0.0354        | 3.0   | 789  | 0.0681          | 0.7189    | 0.7470 | 0.7327   | 0.7322      | 0.7311   | 0.9809   |
| 0.0253        | 4.0   | 1052 | 0.0758          | 0.7570    | 0.7199 | 0.7380   | 0.7375      | 0.7354   | 0.9817   |
| 0.019         | 5.0   | 1315 | 0.0727          | 0.7431    | 0.7303 | 0.7367   | 0.7374      | 0.7352   | 0.9815   |
| 0.0148        | 6.0   | 1578 | 0.0837          | 0.7431    | 0.7335 | 0.7383   | 0.7379      | 0.7359   | 0.9816   |
| 0.0114        | 7.0   | 1841 | 0.0856          | 0.7428    | 0.7548 | 0.7488   | 0.7487      | 0.7471   | 0.9819   |
| 0.01          | 8.0   | 2104 | 0.0875          | 0.7378    | 0.7486 | 0.7432   | 0.7445      | 0.7436   | 0.9822   |
| 0.0086        | 9.0   | 2367 | 0.0905          | 0.7839    | 0.7423 | 0.7626   | 0.7621      | 0.7588   | 0.9828   |
| 0.0073        | 10.0  | 2630 | 0.0979          | 0.7744    | 0.7382 | 0.7559   | 0.7544      | 0.7514   | 0.9825   |
| 0.006         | 11.0  | 2893 | 0.0982          | 0.7658    | 0.7454 | 0.7555   | 0.7549      | 0.7514   | 0.9824   |
| 0.0051        | 12.0  | 3156 | 0.1007          | 0.7633    | 0.7569 | 0.7601   | 0.7599      | 0.7568   | 0.9826   |
| 0.0045        | 13.0  | 3419 | 0.1035          | 0.7505    | 0.7533 | 0.7519   | 0.7513      | 0.7494   | 0.9820   |
| 0.004         | 14.0  | 3682 | 0.1105          | 0.7730    | 0.7392 | 0.7557   | 0.7549      | 0.7514   | 0.9823   |


### Framework versions

- Transformers 4.48.2
- Pytorch 2.4.1+cu121
- Datasets 3.0.2
- Tokenizers 0.21.0
