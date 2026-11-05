---
library_name: transformers
license: apache-2.0
base_model: d4data/biomedical-ner-all
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: ner-biomedical-maccrobat2018
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# ner-biomedical-maccrobat2018

This model is a fine-tuned version of [d4data/biomedical-ner-all](https://huggingface.co/d4data/biomedical-ner-all) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6342
- Accuracy: 0.7903

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0001
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Use adamw_torch with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 20

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 2.5437        | 1.0   | 10   | 1.6009          | 0.3671   |
| 1.3262        | 2.0   | 20   | 0.9660          | 0.6254   |
| 0.8675        | 3.0   | 30   | 0.7436          | 0.7145   |
| 0.6199        | 4.0   | 40   | 0.6544          | 0.7385   |
| 0.4707        | 5.0   | 50   | 0.6131          | 0.7660   |
| 0.3735        | 6.0   | 60   | 0.6027          | 0.7709   |
| 0.3049        | 7.0   | 70   | 0.6056          | 0.7786   |
| 0.2507        | 8.0   | 80   | 0.5992          | 0.7792   |
| 0.2144        | 9.0   | 90   | 0.6115          | 0.7780   |
| 0.1801        | 10.0  | 100  | 0.6062          | 0.7863   |
| 0.1539        | 11.0  | 110  | 0.6101          | 0.7854   |
| 0.1372        | 12.0  | 120  | 0.6157          | 0.7892   |
| 0.1234        | 13.0  | 130  | 0.6269          | 0.7896   |
| 0.1119        | 14.0  | 140  | 0.6285          | 0.7881   |
| 0.1025        | 15.0  | 150  | 0.6364          | 0.7879   |
| 0.0945        | 16.0  | 160  | 0.6326          | 0.7896   |
| 0.09          | 17.0  | 170  | 0.6297          | 0.7916   |
| 0.0861        | 18.0  | 180  | 0.6318          | 0.7908   |
| 0.083         | 19.0  | 190  | 0.6317          | 0.7901   |
| 0.0817        | 20.0  | 200  | 0.6342          | 0.7903   |


### Framework versions

- Transformers 4.47.1
- Pytorch 2.5.1+cu121
- Datasets 3.2.0
- Tokenizers 0.21.0
