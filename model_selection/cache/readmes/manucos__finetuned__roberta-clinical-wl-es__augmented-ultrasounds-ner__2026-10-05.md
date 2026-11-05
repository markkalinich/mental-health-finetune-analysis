---
license: apache-2.0
base_model: manucos/finetuned__roberta-clinical-wl-es__augmented-ultrasounds
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: finetuned__roberta-clinical-wl-es__augmented-ultrasounds-ner
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# finetuned__roberta-clinical-wl-es__augmented-ultrasounds-ner

This model is a fine-tuned version of [manucos/finetuned__roberta-clinical-wl-es__augmented-ultrasounds](https://huggingface.co/manucos/finetuned__roberta-clinical-wl-es__augmented-ultrasounds) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3995
- Precision: 0.7932
- Recall: 0.8775
- F1: 0.8333
- Accuracy: 0.9231

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
- num_epochs: 30

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 1.0   | 22   | 1.2788          | 0.5687    | 0.2763 | 0.3719 | 0.6256   |
| No log        | 2.0   | 44   | 0.6691          | 0.6975    | 0.7470 | 0.7214 | 0.8576   |
| No log        | 3.0   | 66   | 0.4416          | 0.7649    | 0.8168 | 0.7900 | 0.9051   |
| No log        | 4.0   | 88   | 0.3715          | 0.7350    | 0.8279 | 0.7787 | 0.9115   |
| No log        | 5.0   | 110  | 0.3398          | 0.7658    | 0.8441 | 0.8031 | 0.9221   |
| No log        | 6.0   | 132  | 0.3320          | 0.7808    | 0.8472 | 0.8126 | 0.9216   |
| No log        | 7.0   | 154  | 0.3306          | 0.7844    | 0.8431 | 0.8127 | 0.9199   |
| No log        | 8.0   | 176  | 0.3321          | 0.7778    | 0.8502 | 0.8124 | 0.9199   |
| No log        | 9.0   | 198  | 0.3398          | 0.7845    | 0.8512 | 0.8165 | 0.9196   |
| No log        | 10.0  | 220  | 0.3445          | 0.7731    | 0.8553 | 0.8121 | 0.9197   |
| No log        | 11.0  | 242  | 0.3560          | 0.7804    | 0.8522 | 0.8147 | 0.9196   |
| No log        | 12.0  | 264  | 0.3516          | 0.7904    | 0.8664 | 0.8267 | 0.9214   |
| No log        | 13.0  | 286  | 0.3553          | 0.7923    | 0.8725 | 0.8304 | 0.9228   |
| No log        | 14.0  | 308  | 0.3644          | 0.7896    | 0.8775 | 0.8313 | 0.9223   |
| No log        | 15.0  | 330  | 0.3706          | 0.7927    | 0.8745 | 0.8316 | 0.9214   |
| No log        | 16.0  | 352  | 0.3763          | 0.7921    | 0.8755 | 0.8317 | 0.9228   |
| No log        | 17.0  | 374  | 0.3811          | 0.7869    | 0.8745 | 0.8284 | 0.9228   |
| No log        | 18.0  | 396  | 0.3772          | 0.7830    | 0.8765 | 0.8271 | 0.9238   |
| No log        | 19.0  | 418  | 0.3888          | 0.7829    | 0.8796 | 0.8284 | 0.9218   |
| No log        | 20.0  | 440  | 0.3878          | 0.7900    | 0.8755 | 0.8305 | 0.9208   |
| No log        | 21.0  | 462  | 0.3916          | 0.7853    | 0.8775 | 0.8289 | 0.9221   |
| No log        | 22.0  | 484  | 0.3884          | 0.7938    | 0.8806 | 0.8349 | 0.9231   |
| 0.2377        | 23.0  | 506  | 0.3926          | 0.7921    | 0.8715 | 0.8299 | 0.9219   |
| 0.2377        | 24.0  | 528  | 0.3951          | 0.7956    | 0.8785 | 0.8350 | 0.9239   |
| 0.2377        | 25.0  | 550  | 0.3941          | 0.7920    | 0.8785 | 0.8330 | 0.9229   |
| 0.2377        | 26.0  | 572  | 0.3970          | 0.7934    | 0.8785 | 0.8338 | 0.9236   |
| 0.2377        | 27.0  | 594  | 0.3979          | 0.7965    | 0.8796 | 0.8360 | 0.9241   |
| 0.2377        | 28.0  | 616  | 0.3999          | 0.7949    | 0.8785 | 0.8346 | 0.9236   |
| 0.2377        | 29.0  | 638  | 0.4001          | 0.7925    | 0.8775 | 0.8329 | 0.9233   |
| 0.2377        | 30.0  | 660  | 0.3995          | 0.7932    | 0.8775 | 0.8333 | 0.9231   |


### Framework versions

- Transformers 4.40.0
- Pytorch 2.2.1+cu121
- Datasets 2.19.0
- Tokenizers 0.19.1
