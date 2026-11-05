---
library_name: transformers
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: medical-ner-roberta
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# medical-ner-roberta

This model was trained from scratch on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1293
- Precision: 0.9306
- Recall: 0.9431
- F1: 0.9368
- Accuracy: 0.9792

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
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- optimizer: Use adamw_torch with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: cosine
- num_epochs: 20

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 1.0   | 90   | 0.6883          | 0.4376    | 0.4556 | 0.4464 | 0.7834   |
| No log        | 2.0   | 180  | 0.4971          | 0.5779    | 0.6286 | 0.6022 | 0.8343   |
| No log        | 3.0   | 270  | 0.4184          | 0.5892    | 0.7451 | 0.6581 | 0.8569   |
| No log        | 4.0   | 360  | 0.3410          | 0.6474    | 0.8062 | 0.7182 | 0.8893   |
| No log        | 5.0   | 450  | 0.2515          | 0.7554    | 0.8181 | 0.7855 | 0.9270   |
| 0.5383        | 6.0   | 540  | 0.2256          | 0.7738    | 0.8577 | 0.8136 | 0.9338   |
| 0.5383        | 7.0   | 630  | 0.1782          | 0.8270    | 0.8824 | 0.8538 | 0.9488   |
| 0.5383        | 8.0   | 720  | 0.1734          | 0.8271    | 0.8977 | 0.8610 | 0.9554   |
| 0.5383        | 9.0   | 810  | 0.1474          | 0.8702    | 0.9123 | 0.8908 | 0.9661   |
| 0.5383        | 10.0  | 900  | 0.1476          | 0.8806    | 0.9216 | 0.9006 | 0.9685   |
| 0.5383        | 11.0  | 990  | 0.1404          | 0.8913    | 0.9304 | 0.9105 | 0.9722   |
| 0.0733        | 12.0  | 1080 | 0.1354          | 0.9085    | 0.9273 | 0.9178 | 0.9741   |
| 0.0733        | 13.0  | 1170 | 0.1332          | 0.9112    | 0.9266 | 0.9188 | 0.9739   |
| 0.0733        | 14.0  | 1260 | 0.1337          | 0.9072    | 0.9396 | 0.9231 | 0.9755   |
| 0.0733        | 15.0  | 1350 | 0.1332          | 0.9283    | 0.9362 | 0.9322 | 0.9776   |
| 0.0733        | 16.0  | 1440 | 0.1293          | 0.9321    | 0.9389 | 0.9355 | 0.9783   |
| 0.0236        | 17.0  | 1530 | 0.1307          | 0.9253    | 0.9431 | 0.9341 | 0.9786   |
| 0.0236        | 18.0  | 1620 | 0.1293          | 0.9278    | 0.9439 | 0.9358 | 0.9788   |
| 0.0236        | 19.0  | 1710 | 0.1294          | 0.9306    | 0.9431 | 0.9368 | 0.9792   |
| 0.0236        | 20.0  | 1800 | 0.1293          | 0.9306    | 0.9431 | 0.9368 | 0.9792   |


### Framework versions

- Transformers 4.46.2
- Pytorch 2.5.1+cu121
- Datasets 3.1.0
- Tokenizers 0.20.3
