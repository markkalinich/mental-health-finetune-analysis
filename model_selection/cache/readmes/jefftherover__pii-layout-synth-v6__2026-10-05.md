---
library_name: transformers
license: apache-2.0
base_model: answerdotai/ModernBERT-base
tags:
- trackio
- trackio:https://huggingface.co/spaces/jefftherover/huggingface-static-6aebf9
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: pii-layout-synth-v6
  results: []
---
<a href="https://huggingface.co/spaces/jefftherover/huggingface-static-6aebf9" target="_blank"><img src="https://raw.githubusercontent.com/gradio-app/trackio/refs/heads/main/trackio/assets/badge.png" alt="Visualize in Trackio" title="Visualize in Trackio" style="height: 40px;"/></a>
<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# pii-layout-synth-v6

This model is a fine-tuned version of [answerdotai/ModernBERT-base](https://huggingface.co/answerdotai/ModernBERT-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0064
- Precision: 0.9880
- Recall: 0.9919
- F1: 0.9899
- Accuracy: 0.9984

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
- train_batch_size: 16
- eval_batch_size: 32
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 32
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: cosine_with_restarts
- lr_scheduler_warmup_steps: 0.1
- num_epochs: 5
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch  | Step  | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:------:|:-----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.1387        | 0.2455 | 500   | 0.0547          | 0.8950    | 0.9223 | 0.9084 | 0.9860   |
| 0.0737        | 0.4909 | 1000  | 0.0306          | 0.9442    | 0.9608 | 0.9524 | 0.9921   |
| 0.0380        | 0.7364 | 1500  | 0.0192          | 0.9606    | 0.9756 | 0.9681 | 0.9944   |
| 0.0324        | 0.9818 | 2000  | 0.0126          | 0.9698    | 0.9797 | 0.9747 | 0.9962   |
| 0.0160        | 1.2273 | 2500  | 0.0109          | 0.9756    | 0.9842 | 0.9799 | 0.9966   |
| 0.0168        | 1.4728 | 3000  | 0.0106          | 0.9770    | 0.9840 | 0.9805 | 0.9967   |
| 0.0161        | 1.7182 | 3500  | 0.0095          | 0.9767    | 0.9854 | 0.9811 | 0.9969   |
| 0.0126        | 1.9637 | 4000  | 0.0098          | 0.9783    | 0.9865 | 0.9824 | 0.9972   |
| 0.0078        | 2.2091 | 4500  | 0.0080          | 0.9829    | 0.9857 | 0.9843 | 0.9973   |
| 0.0085        | 2.4546 | 5000  | 0.0072          | 0.9831    | 0.9900 | 0.9865 | 0.9978   |
| 0.0062        | 2.7000 | 5500  | 0.0066          | 0.9846    | 0.9886 | 0.9866 | 0.9978   |
| 0.0050        | 2.9455 | 6000  | 0.0063          | 0.9840    | 0.9905 | 0.9872 | 0.9980   |
| 0.0038        | 3.1910 | 6500  | 0.0070          | 0.9859    | 0.9911 | 0.9885 | 0.9980   |
| 0.0026        | 3.4364 | 7000  | 0.0059          | 0.9866    | 0.9910 | 0.9888 | 0.9982   |
| 0.0043        | 3.6819 | 7500  | 0.0063          | 0.9859    | 0.9905 | 0.9882 | 0.9981   |
| 0.0022        | 3.9273 | 8000  | 0.0059          | 0.9881    | 0.9918 | 0.9899 | 0.9983   |
| 0.0011        | 4.1728 | 8500  | 0.0060          | 0.9875    | 0.9911 | 0.9893 | 0.9983   |
| 0.0009        | 4.4183 | 9000  | 0.0063          | 0.9881    | 0.9922 | 0.9901 | 0.9984   |
| 0.0007        | 4.6637 | 9500  | 0.0064          | 0.9881    | 0.9921 | 0.9901 | 0.9984   |
| 0.0008        | 4.9092 | 10000 | 0.0064          | 0.9880    | 0.9919 | 0.9900 | 0.9984   |
| 0.0007        | 5.0    | 10185 | 0.0064          | 0.9880    | 0.9919 | 0.9899 | 0.9984   |


### Framework versions

- Transformers 5.12.1
- Pytorch 2.12.0+cu130
- Datasets 5.0.0
- Tokenizers 0.22.2
