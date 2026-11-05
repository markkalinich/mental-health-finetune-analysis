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
- name: CeLLaTe-ner-2class-tapt-pubmedbert-tokenizer-adapted-spanmask
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# CeLLaTe-ner-2class-tapt-pubmedbert-tokenizer-adapted-spanmask

This model is a fine-tuned version of [Mardiyyah/CeLLaTe-tapt-pubmedbert-tokenizer-adapted-spanmask](https://huggingface.co/Mardiyyah/CeLLaTe-tapt-pubmedbert-tokenizer-adapted-spanmask) on the OTAR3088/CeLLaTe-ner-2class-iob_final dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0853
- Precision: 0.7758
- Recall: 0.7426
- Micro F1: 0.7588
- Weighted F1: 0.7592
- Macro F1: 0.7706
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

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | Micro F1 | Weighted F1 | Macro F1 | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:--------:|:-----------:|:--------:|:--------:|
| 0.2522        | 1.0   | 263  | 0.0588          | 0.6756    | 0.6813 | 0.6784   | 0.6794      | 0.6963   | 0.9817   |
| 0.044         | 2.0   | 526  | 0.0560          | 0.7373    | 0.6903 | 0.7130   | 0.7136      | 0.7277   | 0.9824   |
| 0.0266        | 3.0   | 789  | 0.0596          | 0.7102    | 0.7162 | 0.7132   | 0.7144      | 0.7353   | 0.9825   |
| 0.0196        | 4.0   | 1052 | 0.0616          | 0.7427    | 0.7378 | 0.7403   | 0.7408      | 0.7530   | 0.9837   |
| 0.0144        | 5.0   | 1315 | 0.0740          | 0.7917    | 0.6969 | 0.7413   | 0.7413      | 0.7457   | 0.9831   |
| 0.0114        | 6.0   | 1578 | 0.0658          | 0.7691    | 0.7312 | 0.7497   | 0.7498      | 0.7558   | 0.9840   |
| 0.0087        | 7.0   | 1841 | 0.0781          | 0.7421    | 0.7372 | 0.7397   | 0.7398      | 0.7431   | 0.9832   |
| 0.0066        | 8.0   | 2104 | 0.0800          | 0.7926    | 0.7168 | 0.7528   | 0.7527      | 0.7623   | 0.9839   |
| 0.006         | 9.0   | 2367 | 0.0815          | 0.7570    | 0.7438 | 0.7504   | 0.7509      | 0.7636   | 0.9836   |
| 0.0049        | 10.0  | 2630 | 0.0846          | 0.7758    | 0.7426 | 0.7588   | 0.7592      | 0.7706   | 0.9839   |
| 0.0037        | 11.0  | 2893 | 0.0902          | 0.7643    | 0.7408 | 0.7524   | 0.7527      | 0.7628   | 0.9838   |
| 0.0037        | 12.0  | 3156 | 0.0904          | 0.7734    | 0.7492 | 0.7611   | 0.7616      | 0.7694   | 0.9845   |
| 0.0029        | 13.0  | 3419 | 0.0970          | 0.7756    | 0.7420 | 0.7585   | 0.7584      | 0.7658   | 0.9841   |
| 0.0026        | 14.0  | 3682 | 0.0915          | 0.7639    | 0.7529 | 0.7583   | 0.7587      | 0.7672   | 0.9846   |
| 0.0024        | 15.0  | 3945 | 0.0964          | 0.7638    | 0.7505 | 0.7571   | 0.7575      | 0.7684   | 0.9845   |


### Framework versions

- Transformers 4.48.2
- Pytorch 2.4.1+cu121
- Datasets 3.0.2
- Tokenizers 0.21.0
