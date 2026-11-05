---
license: apache-2.0
base_model: BSC-LT/roberta-base-biomedical-clinical-es
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: roberta-base-biomedical-clinical-es-ner
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# roberta-base-biomedical-clinical-es-ner

This model is a fine-tuned version of [BSC-LT/roberta-base-biomedical-clinical-es](https://huggingface.co/BSC-LT/roberta-base-biomedical-clinical-es) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3813
- Precision: 0.8687
- Recall: 0.8919
- F1: 0.8801
- Accuracy: 0.9374

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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 15

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 1.0   | 280  | 0.3201          | 0.7961    | 0.8385 | 0.8167 | 0.9130   |
| 0.5051        | 2.0   | 560  | 0.2833          | 0.8245    | 0.8770 | 0.8500 | 0.9282   |
| 0.5051        | 3.0   | 840  | 0.2717          | 0.8459    | 0.8622 | 0.8540 | 0.9262   |
| 0.1434        | 4.0   | 1120 | 0.2782          | 0.8477    | 0.8904 | 0.8685 | 0.9324   |
| 0.1434        | 5.0   | 1400 | 0.3119          | 0.8525    | 0.8993 | 0.8753 | 0.9355   |
| 0.0804        | 6.0   | 1680 | 0.3146          | 0.8639    | 0.8933 | 0.8784 | 0.9366   |
| 0.0804        | 7.0   | 1960 | 0.3211          | 0.8637    | 0.8919 | 0.8776 | 0.9346   |
| 0.0475        | 8.0   | 2240 | 0.3523          | 0.8707    | 0.8978 | 0.8840 | 0.9372   |
| 0.0347        | 9.0   | 2520 | 0.3651          | 0.8434    | 0.8859 | 0.8642 | 0.9335   |
| 0.0347        | 10.0  | 2800 | 0.3663          | 0.8706    | 0.8874 | 0.8789 | 0.9360   |
| 0.0241        | 11.0  | 3080 | 0.3756          | 0.8680    | 0.8963 | 0.8819 | 0.9372   |
| 0.0241        | 12.0  | 3360 | 0.3692          | 0.86      | 0.8919 | 0.8756 | 0.9369   |
| 0.0201        | 13.0  | 3640 | 0.3782          | 0.8631    | 0.8874 | 0.8751 | 0.9360   |
| 0.0201        | 14.0  | 3920 | 0.3820          | 0.8698    | 0.8904 | 0.8799 | 0.9374   |
| 0.0172        | 15.0  | 4200 | 0.3813          | 0.8687    | 0.8919 | 0.8801 | 0.9374   |


### Framework versions

- Transformers 4.41.1
- Pytorch 2.3.0+cu121
- Datasets 2.19.1
- Tokenizers 0.19.1
