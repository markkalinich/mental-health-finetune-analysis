---
library_name: transformers
license: apache-2.0
base_model: PlanTL-GOB-ES/bsc-bio-ehr-es
tags:
- token-classification
- generated_from_trainer
datasets:
- Rodrigo1771/combined-train-drugtemist-dev-85-ner
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
      name: Rodrigo1771/combined-train-drugtemist-dev-85-ner
      type: Rodrigo1771/combined-train-drugtemist-dev-85-ner
      config: CombinedTrainDrugTEMISTDevNER
      split: validation
      args: CombinedTrainDrugTEMISTDevNER
    metrics:
    - name: Precision
      type: precision
      value: 0.09400470929179497
    - name: Recall
      type: recall
      value: 0.9540441176470589
    - name: F1
      type: f1
      value: 0.17114591920857378
    - name: Accuracy
      type: accuracy
      value: 0.7890274211487498
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# output

This model is a fine-tuned version of [PlanTL-GOB-ES/bsc-bio-ehr-es](https://huggingface.co/PlanTL-GOB-ES/bsc-bio-ehr-es) on the Rodrigo1771/combined-train-drugtemist-dev-85-ner dataset.
It achieves the following results on the evaluation set:
- Loss: 1.1806
- Precision: 0.0940
- Recall: 0.9540
- F1: 0.1711
- Accuracy: 0.7890

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
| 0.3191        | 1.0   | 541  | 0.8151          | 0.0825    | 0.9605 | 0.1520 | 0.7763   |
| 0.1619        | 2.0   | 1082 | 0.8332          | 0.0922    | 0.9458 | 0.168  | 0.7901   |
| 0.11          | 3.0   | 1623 | 1.1094          | 0.0899    | 0.9494 | 0.1643 | 0.7738   |
| 0.0764        | 4.0   | 2164 | 1.1206          | 0.0885    | 0.9449 | 0.1618 | 0.7740   |
| 0.0567        | 5.0   | 2705 | 1.1806          | 0.0940    | 0.9540 | 0.1711 | 0.7890   |
| 0.0428        | 6.0   | 3246 | 1.3138          | 0.0901    | 0.9458 | 0.1645 | 0.7827   |
| 0.0332        | 7.0   | 3787 | 1.4009          | 0.0922    | 0.9384 | 0.1679 | 0.7874   |
| 0.0257        | 8.0   | 4328 | 1.5611          | 0.0904    | 0.9412 | 0.1650 | 0.7791   |
| 0.022         | 9.0   | 4869 | 1.5934          | 0.0921    | 0.9467 | 0.1679 | 0.7835   |
| 0.0181        | 10.0  | 5410 | 1.6103          | 0.0922    | 0.9439 | 0.1680 | 0.7863   |


### Framework versions

- Transformers 4.44.2
- Pytorch 2.4.0+cu121
- Datasets 2.21.0
- Tokenizers 0.19.1
