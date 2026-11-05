---
library_name: transformers
license: apache-2.0
base_model: OpenMed/OpenMed-PII-SuperClinical-Small-44M-v1
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: OpenMed-PII-Small-finetuned-v1
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# OpenMed-PII-Small-finetuned-v1

This model is a fine-tuned version of [OpenMed/OpenMed-PII-SuperClinical-Small-44M-v1](https://huggingface.co/OpenMed/OpenMed-PII-SuperClinical-Small-44M-v1) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0157
- Precision: 0.9624
- Recall: 0.9732
- F1: 0.9678
- Accuracy: 0.9956

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 3e-05
- train_batch_size: 32
- eval_batch_size: 64
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 200
- num_epochs: 3
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch  | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:------:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.0331        | 0.1632 | 500  | 0.0247          | 0.9439    | 0.9623 | 0.9531 | 0.9934   |
| 0.0235        | 0.3265 | 1000 | 0.0209          | 0.9517    | 0.9650 | 0.9583 | 0.9944   |
| 0.0244        | 0.4897 | 1500 | 0.0205          | 0.9517    | 0.9648 | 0.9582 | 0.9943   |
| 0.0274        | 0.6530 | 2000 | 0.0198          | 0.9503    | 0.9635 | 0.9568 | 0.9944   |
| 0.0208        | 0.8162 | 2500 | 0.0185          | 0.9548    | 0.9676 | 0.9611 | 0.9949   |
| 0.0211        | 0.9794 | 3000 | 0.0180          | 0.9593    | 0.9655 | 0.9624 | 0.9951   |
| 0.0169        | 1.1427 | 3500 | 0.0207          | 0.9468    | 0.9684 | 0.9575 | 0.9940   |
| 0.0189        | 1.3059 | 4000 | 0.0189          | 0.9508    | 0.9726 | 0.9616 | 0.9946   |
| 0.0174        | 1.4691 | 4500 | 0.0175          | 0.9557    | 0.9702 | 0.9629 | 0.9950   |
| 0.0161        | 1.6324 | 5000 | 0.0182          | 0.9521    | 0.9737 | 0.9628 | 0.9948   |
| 0.0181        | 1.7956 | 5500 | 0.0174          | 0.9566    | 0.9740 | 0.9652 | 0.9952   |
| 0.0158        | 1.9589 | 6000 | 0.0167          | 0.9594    | 0.9709 | 0.9651 | 0.9952   |
| 0.0130        | 2.1221 | 6500 | 0.0161          | 0.9609    | 0.9723 | 0.9666 | 0.9954   |
| 0.0148        | 2.2853 | 7000 | 0.0174          | 0.9593    | 0.9732 | 0.9662 | 0.9951   |
| 0.0150        | 2.4486 | 7500 | 0.0178          | 0.9583    | 0.9733 | 0.9657 | 0.9950   |
| 0.0144        | 2.6118 | 8000 | 0.0161          | 0.9609    | 0.9738 | 0.9673 | 0.9955   |
| 0.0149        | 2.7751 | 8500 | 0.0160          | 0.9600    | 0.9744 | 0.9671 | 0.9955   |
| 0.0124        | 2.9383 | 9000 | 0.0157          | 0.9624    | 0.9732 | 0.9678 | 0.9956   |
| 0.0126        | 3.0    | 9189 | 0.0157          | 0.9614    | 0.9732 | 0.9673 | 0.9956   |


### Framework versions

- Transformers 5.7.0
- Pytorch 2.5.1+cu121
- Datasets 4.8.5
- Tokenizers 0.22.2
