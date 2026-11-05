---
library_name: transformers
license: apache-2.0
base_model: PlanTL-GOB-ES/bsc-bio-ehr-es
tags:
- token-classification
- generated_from_trainer
datasets:
- Rodrigo1771/symptemist-75-ner
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: output
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: Rodrigo1771/symptemist-75-ner
      type: Rodrigo1771/symptemist-75-ner
      config: SympTEMIST NER
      split: validation
      args: SympTEMIST NER
    metrics:
    - name: Precision
      type: precision
      value: 0.6896
    - name: Recall
      type: recall
      value: 0.7077175697865353
    - name: F1
      type: f1
      value: 0.6985413290113451
    - name: Accuracy
      type: accuracy
      value: 0.9496936058263018
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# output

This model is a fine-tuned version of [PlanTL-GOB-ES/bsc-bio-ehr-es](https://huggingface.co/PlanTL-GOB-ES/bsc-bio-ehr-es) on the Rodrigo1771/symptemist-75-ner dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3089
- Precision: 0.6896
- Recall: 0.7077
- F1: 0.6985
- Accuracy: 0.9497

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
- train_batch_size: 32
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 64
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10.0

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 1.0   | 248  | 0.1649          | 0.5942    | 0.6820 | 0.6351 | 0.9478   |
| No log        | 2.0   | 496  | 0.1815          | 0.6558    | 0.6705 | 0.6631 | 0.9476   |
| 0.134         | 3.0   | 744  | 0.2111          | 0.6651    | 0.6979 | 0.6811 | 0.9492   |
| 0.134         | 4.0   | 992  | 0.2523          | 0.6692    | 0.7121 | 0.6900 | 0.9488   |
| 0.026         | 5.0   | 1240 | 0.2771          | 0.6584    | 0.7132 | 0.6847 | 0.9491   |
| 0.026         | 6.0   | 1488 | 0.2968          | 0.6668    | 0.7165 | 0.6908 | 0.9486   |
| 0.0084        | 7.0   | 1736 | 0.3089          | 0.6896    | 0.7077 | 0.6985 | 0.9497   |
| 0.0084        | 8.0   | 1984 | 0.3188          | 0.6825    | 0.7072 | 0.6946 | 0.9499   |
| 0.0042        | 9.0   | 2232 | 0.3296          | 0.6809    | 0.7159 | 0.6980 | 0.9495   |
| 0.0042        | 10.0  | 2480 | 0.3328          | 0.6814    | 0.7165 | 0.6985 | 0.9499   |


### Framework versions

- Transformers 4.44.2
- Pytorch 2.4.0+cu121
- Datasets 2.21.0
- Tokenizers 0.19.1
