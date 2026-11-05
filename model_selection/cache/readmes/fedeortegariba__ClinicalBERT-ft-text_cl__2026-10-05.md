---
library_name: transformers
base_model: medicalai/ClinicalBERT
tags:
- generated_from_trainer
metrics:
- accuracy
- recall
- precision
- f1
model-index:
- name: ClinicalBERT-ft-text_cl
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# ClinicalBERT-ft-text_cl

This model is a fine-tuned version of [medicalai/ClinicalBERT](https://huggingface.co/medicalai/ClinicalBERT) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.0173
- Accuracy: 0.8880
- Recall: 0.9412
- Precision: 0.8766
- F1: 0.9078

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
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 30

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | Recall | Precision | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:------:|:---------:|:------:|
| No log        | 1.0   | 231  | 0.3258          | 0.8658   | 0.9552 | 0.8383    | 0.8929 |
| No log        | 2.0   | 462  | 0.4387          | 0.8664   | 0.9711 | 0.8298    | 0.8949 |
| 0.2029        | 3.0   | 693  | 0.4922          | 0.8786   | 0.9771 | 0.8413    | 0.9041 |
| 0.2029        | 4.0   | 924  | 0.6135          | 0.8874   | 0.9582 | 0.8643    | 0.9088 |
| 0.0562        | 5.0   | 1155 | 0.6957          | 0.8821   | 0.9592 | 0.8568    | 0.9051 |
| 0.0562        | 6.0   | 1386 | 0.8482          | 0.8734   | 0.9612 | 0.8443    | 0.8989 |
| 0.0169        | 7.0   | 1617 | 0.6741          | 0.9008   | 0.9542 | 0.8854    | 0.9185 |
| 0.0169        | 8.0   | 1848 | 0.8648          | 0.8641   | 0.9631 | 0.8315    | 0.8925 |
| 0.0132        | 9.0   | 2079 | 0.7180          | 0.8967   | 0.9313 | 0.8965    | 0.9135 |
| 0.0132        | 10.0  | 2310 | 0.8567          | 0.8891   | 0.9552 | 0.8687    | 0.9099 |
| 0.0044        | 11.0  | 2541 | 0.7808          | 0.9002   | 0.9293 | 0.9032    | 0.9161 |
| 0.0044        | 12.0  | 2772 | 1.0333          | 0.8629   | 0.9671 | 0.8278    | 0.8921 |
| 0.0033        | 13.0  | 3003 | 0.9561          | 0.8839   | 0.9552 | 0.8616    | 0.9060 |
| 0.0033        | 14.0  | 3234 | 0.8847          | 0.8897   | 0.9522 | 0.8715    | 0.9100 |
| 0.0033        | 15.0  | 3465 | 1.2981          | 0.8471   | 0.9831 | 0.8011    | 0.8828 |
| 0.0028        | 16.0  | 3696 | 1.0164          | 0.8722   | 0.9542 | 0.8470    | 0.8974 |
| 0.0028        | 17.0  | 3927 | 0.8194          | 0.8915   | 0.9512 | 0.8745    | 0.9113 |
| 0.0114        | 18.0  | 4158 | 0.8303          | 0.9014   | 0.9502 | 0.8891    | 0.9186 |
| 0.0114        | 19.0  | 4389 | 0.9197          | 0.8874   | 0.9562 | 0.8656    | 0.9087 |
| 0.0029        | 20.0  | 4620 | 1.0221          | 0.8845   | 0.9592 | 0.8598    | 0.9068 |
| 0.0029        | 21.0  | 4851 | 0.9183          | 0.8926   | 0.9363 | 0.8868    | 0.9109 |
| 0.0026        | 22.0  | 5082 | 1.0870          | 0.8816   | 0.9572 | 0.8573    | 0.9045 |
| 0.0026        | 23.0  | 5313 | 1.0594          | 0.8856   | 0.9542 | 0.8646    | 0.9072 |
| 0.0025        | 24.0  | 5544 | 0.9493          | 0.8973   | 0.9353 | 0.8943    | 0.9143 |
| 0.0025        | 25.0  | 5775 | 0.9936          | 0.8880   | 0.9502 | 0.8704    | 0.9086 |
| 0.0026        | 26.0  | 6006 | 1.0409          | 0.8886   | 0.9552 | 0.8679    | 0.9094 |
| 0.0026        | 27.0  | 6237 | 1.0020          | 0.8874   | 0.9452 | 0.8730    | 0.9077 |
| 0.0026        | 28.0  | 6468 | 1.0178          | 0.8868   | 0.9412 | 0.875     | 0.9069 |
| 0.0016        | 29.0  | 6699 | 1.0101          | 0.8868   | 0.9392 | 0.8764    | 0.9067 |
| 0.0016        | 30.0  | 6930 | 1.0173          | 0.8880   | 0.9412 | 0.8766    | 0.9078 |


### Framework versions

- Transformers 4.51.3
- Pytorch 2.6.0+cu124
- Tokenizers 0.21.1
