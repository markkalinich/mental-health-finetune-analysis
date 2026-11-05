---
library_name: transformers
license: apache-2.0
base_model: answerdotai/ModernBERT-base
tags:
- trackio
- trackio:https://huggingface.co/spaces/jefftherover/huggingface-static-6af8a8
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: pii-layout-synth-v9
  results: []
---
<a href="https://huggingface.co/spaces/jefftherover/huggingface-static-6af8a8" target="_blank"><img src="https://raw.githubusercontent.com/gradio-app/trackio/refs/heads/main/trackio/assets/badge.png" alt="Visualize in Trackio" title="Visualize in Trackio" style="height: 40px;"/></a>
<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# pii-layout-synth-v9

This model is a fine-tuned version of [answerdotai/ModernBERT-base](https://huggingface.co/answerdotai/ModernBERT-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0049
- Precision: 0.9896
- Recall: 0.9929
- F1: 0.9912
- Accuracy: 0.9985

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
- lr_scheduler_warmup_steps: 200
- num_epochs: 5
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch  | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:------:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.0463        | 0.2455 | 500  | 0.0209          | 0.9469    | 0.9744 | 0.9605 | 0.9938   |
| 0.0246        | 0.4909 | 1000 | 0.0105          | 0.9749    | 0.9848 | 0.9798 | 0.9967   |
| 0.0191        | 0.7364 | 1500 | 0.0087          | 0.9817    | 0.9913 | 0.9865 | 0.9974   |
| 0.0144        | 0.9818 | 2000 | 0.0077          | 0.9785    | 0.9846 | 0.9815 | 0.9973   |
| 0.0093        | 1.2273 | 2500 | 0.0055          | 0.9878    | 0.9922 | 0.9900 | 0.9982   |
| 0.0090        | 1.4728 | 3000 | 0.0056          | 0.9875    | 0.9926 | 0.9900 | 0.9981   |
| 0.0080        | 1.7182 | 3500 | 0.0059          | 0.9870    | 0.9925 | 0.9897 | 0.9981   |
| 0.0089        | 1.9637 | 4000 | 0.0051          | 0.9890    | 0.9944 | 0.9917 | 0.9984   |
| 0.0045        | 2.2091 | 4500 | 0.0063          | 0.9844    | 0.9906 | 0.9875 | 0.9980   |
| 0.0062        | 2.4546 | 5000 | 0.0073          | 0.9870    | 0.9897 | 0.9884 | 0.9980   |
| 0.0035        | 2.7000 | 5500 | 0.0049          | 0.9896    | 0.9929 | 0.9912 | 0.9985   |


### Framework versions

- Transformers 5.12.1
- Pytorch 2.12.1+cu130
- Datasets 5.0.0
- Tokenizers 0.22.2
