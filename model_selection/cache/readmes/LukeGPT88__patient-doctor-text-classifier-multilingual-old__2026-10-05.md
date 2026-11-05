---
license: apache-2.0
base_model: lxyuan/distilbert-base-multilingual-cased-sentiments-student
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: distilbert-base-cased-finetuned-patient-doctor-text-classifier-eng-multilingual
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-cased-finetuned-patient-doctor-text-classifier-eng-multilingual

This model is a fine-tuned version of [lxyuan/distilbert-base-multilingual-cased-sentiments-student](https://huggingface.co/lxyuan/distilbert-base-multilingual-cased-sentiments-student) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0988
- Accuracy: 0.9851

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
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Accuracy |
|:-------------:|:-----:|:-----:|:---------------:|:--------:|
| 0.1049        | 1.0   | 1547  | 0.0713          | 0.9819   |
| 0.0442        | 2.0   | 3094  | 0.0751          | 0.9833   |
| 0.0307        | 3.0   | 4641  | 0.0699          | 0.9856   |
| 0.0231        | 4.0   | 6188  | 0.0889          | 0.9844   |
| 0.0188        | 5.0   | 7735  | 0.0898          | 0.9852   |
| 0.0169        | 6.0   | 9282  | 0.0974          | 0.9831   |
| 0.0138        | 7.0   | 10829 | 0.0954          | 0.9852   |
| 0.0124        | 8.0   | 12376 | 0.0986          | 0.9845   |
| 0.0108        | 9.0   | 13923 | 0.0959          | 0.9846   |
| 0.0095        | 10.0  | 15470 | 0.0988          | 0.9851   |


### Framework versions

- Transformers 4.38.1
- Pytorch 2.1.2
- Datasets 2.1.0
- Tokenizers 0.15.2
