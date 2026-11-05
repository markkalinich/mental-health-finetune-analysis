---
license: apache-2.0
base_model: manucos/finetuned__roberta-base-biomedical-clinical-es__59k-ultrasounds
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: test-finetuned__roberta-base-biomedical-clinical-es__59k-ultrasounds-ner
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# test-finetuned__roberta-base-biomedical-clinical-es__59k-ultrasounds-ner

This model is a fine-tuned version of [manucos/finetuned__roberta-base-biomedical-clinical-es__59k-ultrasounds](https://huggingface.co/manucos/finetuned__roberta-base-biomedical-clinical-es__59k-ultrasounds) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3097
- Precision: 0.8060
- Recall: 0.8917
- F1: 0.8467
- Accuracy: 0.9300

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
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 1.0   | 206  | 0.2915          | 0.7439    | 0.8350 | 0.7868 | 0.9096   |
| No log        | 2.0   | 412  | 0.2505          | 0.7779    | 0.8613 | 0.8175 | 0.9215   |
| 0.4211        | 3.0   | 618  | 0.2737          | 0.7647    | 0.8553 | 0.8075 | 0.9179   |
| 0.4211        | 4.0   | 824  | 0.2784          | 0.7879    | 0.8796 | 0.8312 | 0.9239   |
| 0.1009        | 5.0   | 1030 | 0.2779          | 0.7885    | 0.8866 | 0.8347 | 0.9282   |
| 0.1009        | 6.0   | 1236 | 0.2979          | 0.8037    | 0.8866 | 0.8431 | 0.9276   |
| 0.1009        | 7.0   | 1442 | 0.3058          | 0.7903    | 0.8887 | 0.8366 | 0.9273   |
| 0.0525        | 8.0   | 1648 | 0.3010          | 0.8057    | 0.8856 | 0.8438 | 0.9269   |
| 0.0525        | 9.0   | 1854 | 0.3090          | 0.8137    | 0.8927 | 0.8514 | 0.9307   |
| 0.0316        | 10.0  | 2060 | 0.3097          | 0.8060    | 0.8917 | 0.8467 | 0.9300   |


### Framework versions

- Transformers 4.40.0
- Pytorch 2.2.1+cu121
- Datasets 2.19.0
- Tokenizers 0.19.1
