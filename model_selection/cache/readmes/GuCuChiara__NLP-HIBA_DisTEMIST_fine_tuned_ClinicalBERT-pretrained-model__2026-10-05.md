---
license: mit
base_model: emilyalsentzer/Bio_ClinicalBERT
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: NLP-HIBA_DisTEMIST_fine_tuned_ClinicalBERT-pretrained-model
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# NLP-HIBA_DisTEMIST_fine_tuned_ClinicalBERT-pretrained-model

This model is a fine-tuned version of [emilyalsentzer/Bio_ClinicalBERT](https://huggingface.co/emilyalsentzer/Bio_ClinicalBERT) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2557
- Precision: 0.4943
- Recall: 0.5046
- F1: 0.4994
- Accuracy: 0.9407

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 12

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 1.0   | 71   | 0.2423          | 0.1951    | 0.1433 | 0.1653 | 0.9109   |
| No log        | 2.0   | 142  | 0.2177          | 0.2905    | 0.3474 | 0.3164 | 0.9138   |
| No log        | 3.0   | 213  | 0.1822          | 0.3912    | 0.3701 | 0.3804 | 0.9325   |
| No log        | 4.0   | 284  | 0.1845          | 0.3839    | 0.4367 | 0.4086 | 0.9298   |
| No log        | 5.0   | 355  | 0.2033          | 0.4533    | 0.4271 | 0.4398 | 0.9367   |
| No log        | 6.0   | 426  | 0.2005          | 0.4535    | 0.4736 | 0.4633 | 0.9365   |
| No log        | 7.0   | 497  | 0.2297          | 0.4352    | 0.5155 | 0.4720 | 0.9321   |
| 0.1436        | 8.0   | 568  | 0.2236          | 0.4854    | 0.4656 | 0.4753 | 0.9395   |
| 0.1436        | 9.0   | 639  | 0.2335          | 0.4935    | 0.5101 | 0.5016 | 0.9397   |
| 0.1436        | 10.0  | 710  | 0.2413          | 0.4829    | 0.5075 | 0.4949 | 0.9405   |
| 0.1436        | 11.0  | 781  | 0.2557          | 0.4849    | 0.5239 | 0.5036 | 0.9383   |
| 0.1436        | 12.0  | 852  | 0.2557          | 0.4943    | 0.5046 | 0.4994 | 0.9407   |


### Framework versions

- Transformers 4.35.1
- Pytorch 2.1.0+cu118
- Datasets 2.14.6
- Tokenizers 0.14.1
