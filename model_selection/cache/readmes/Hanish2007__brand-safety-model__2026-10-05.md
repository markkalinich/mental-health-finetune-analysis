---
library_name: transformers
license: apache-2.0
base_model: distilbert/distilbert-base-uncased
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: brand-safety-model
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# brand-safety-model

This model is a fine-tuned version of [distilbert/distilbert-base-uncased](https://huggingface.co/distilbert/distilbert-base-uncased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4779
- Accuracy: 0.8657

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
- train_batch_size: 64
- eval_batch_size: 64
- seed: 42
- optimizer: Use adamw_torch with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 15

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 1.581         | 1.0   | 112  | 1.4547          | 0.6798   |
| 0.9156        | 2.0   | 224  | 0.8586          | 0.7904   |
| 0.6402        | 3.0   | 336  | 0.6679          | 0.8292   |
| 0.5405        | 4.0   | 448  | 0.5595          | 0.8551   |
| 0.4553        | 5.0   | 560  | 0.5183          | 0.8534   |
| 0.3509        | 6.0   | 672  | 0.4825          | 0.8629   |
| 0.316         | 7.0   | 784  | 0.4786          | 0.8584   |
| 0.2506        | 8.0   | 896  | 0.4710          | 0.8618   |
| 0.2049        | 9.0   | 1008 | 0.4912          | 0.8567   |
| 0.1416        | 10.0  | 1120 | 0.4881          | 0.8567   |
| 0.1572        | 11.0  | 1232 | 0.4779          | 0.8657   |
| 0.1407        | 12.0  | 1344 | 0.4886          | 0.8596   |
| 0.132         | 13.0  | 1456 | 0.4933          | 0.8618   |
| 0.1319        | 14.0  | 1568 | 0.4807          | 0.8635   |
| 0.1277        | 15.0  | 1680 | 0.4846          | 0.8618   |


### Framework versions

- Transformers 4.46.3
- Pytorch 2.4.0
- Datasets 2.20.0
- Tokenizers 0.20.3
