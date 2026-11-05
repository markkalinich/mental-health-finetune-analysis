---
license: cc-by-nc-4.0
base_model: mental/mental-roberta-base
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: mental-roberta-base-finetuned-depression
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# mental-roberta-base-finetuned-depression

This model is a fine-tuned version of [mental/mental-roberta-base](https://huggingface.co/mental/mental-roberta-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6567
- Precision: 0.8863
- Recall: 0.9168
- F1: 0.8996
- Accuracy: 0.9115

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
- num_epochs: 20

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 1.0   | 469  | 0.3852          | 0.7878    | 0.8253 | 0.7958 | 0.8667   |
| 0.5249        | 2.0   | 938  | 0.4720          | 0.8778    | 0.8722 | 0.8662 | 0.8913   |
| 0.2598        | 3.0   | 1407 | 0.5459          | 0.8975    | 0.8791 | 0.8865 | 0.8977   |
| 0.1624        | 4.0   | 1876 | 0.5022          | 0.9004    | 0.8979 | 0.8976 | 0.9072   |
| 0.1036        | 5.0   | 2345 | 0.6257          | 0.8910    | 0.8968 | 0.8931 | 0.9009   |
| 0.0668        | 6.0   | 2814 | 0.6531          | 0.9145    | 0.8927 | 0.9026 | 0.9104   |
| 0.0539        | 7.0   | 3283 | 0.6209          | 0.8552    | 0.9115 | 0.8802 | 0.8945   |
| 0.057         | 8.0   | 3752 | 0.6567          | 0.8863    | 0.9168 | 0.8996 | 0.9115   |
| 0.0523        | 9.0   | 4221 | 0.7184          | 0.9067    | 0.8984 | 0.8993 | 0.9083   |
| 0.0354        | 10.0  | 4690 | 0.7112          | 0.8874    | 0.9014 | 0.8914 | 0.9072   |
| 0.0268        | 11.0  | 5159 | 0.7168          | 0.8996    | 0.9012 | 0.8979 | 0.9083   |
| 0.0297        | 12.0  | 5628 | 0.7499          | 0.8667    | 0.9096 | 0.8847 | 0.9030   |
| 0.0242        | 13.0  | 6097 | 0.7554          | 0.8946    | 0.9014 | 0.8955 | 0.9072   |
| 0.0238        | 14.0  | 6566 | 0.7990          | 0.8909    | 0.9014 | 0.8934 | 0.9072   |
| 0.0178        | 15.0  | 7035 | 0.8298          | 0.8965    | 0.8933 | 0.8925 | 0.9051   |
| 0.0226        | 16.0  | 7504 | 0.8428          | 0.9099    | 0.8890 | 0.8973 | 0.9062   |
| 0.0226        | 17.0  | 7973 | 0.8490          | 0.8742    | 0.8983 | 0.8816 | 0.9041   |
| 0.0183        | 18.0  | 8442 | 0.8148          | 0.8940    | 0.8965 | 0.8930 | 0.9072   |
| 0.0188        | 19.0  | 8911 | 0.8146          | 0.8927    | 0.8960 | 0.8921 | 0.9062   |
| 0.015         | 20.0  | 9380 | 0.8216          | 0.8927    | 0.8960 | 0.8921 | 0.9062   |


### Framework versions

- Transformers 4.41.2
- Pytorch 2.3.0+cu121
- Datasets 2.20.0
- Tokenizers 0.19.1
