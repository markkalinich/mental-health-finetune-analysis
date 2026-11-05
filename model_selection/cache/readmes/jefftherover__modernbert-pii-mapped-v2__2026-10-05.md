---
library_name: transformers
license: apache-2.0
base_model: answerdotai/ModernBERT-base
tags:
- trackio
- trackio:https://huggingface.co/spaces/jefftherover/huggingface-static-c5ac60
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: modernbert-pii-mapped-v2
  results: []
---
<a href="https://huggingface.co/spaces/jefftherover/huggingface-static-c5ac60" target="_blank"><img src="https://raw.githubusercontent.com/gradio-app/trackio/refs/heads/main/trackio/assets/badge.png" alt="Visualize in Trackio" title="Visualize in Trackio" style="height: 40px;"/></a>
<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# modernbert-pii-mapped-v2

This model is a fine-tuned version of [answerdotai/ModernBERT-base](https://huggingface.co/answerdotai/ModernBERT-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0073
- Precision: 0.9800
- Recall: 0.9887
- F1: 0.9843
- Accuracy: 0.9983

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

| Training Loss | Epoch  | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:------:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.0521        | 0.4087 | 500  | 0.0201          | 0.9174    | 0.9504 | 0.9336 | 0.9941   |
| 0.0206        | 0.8173 | 1000 | 0.0109          | 0.9437    | 0.9740 | 0.9586 | 0.9965   |
| 0.0175        | 1.2256 | 1500 | 0.0097          | 0.9625    | 0.9739 | 0.9682 | 0.9972   |
| 0.0117        | 1.6342 | 2000 | 0.0082          | 0.9650    | 0.9848 | 0.9748 | 0.9975   |
| 0.0083        | 2.0425 | 2500 | 0.0067          | 0.9690    | 0.9903 | 0.9795 | 0.9977   |
| 0.0065        | 2.4512 | 3000 | 0.0071          | 0.9697    | 0.9910 | 0.9802 | 0.9977   |
| 0.0062        | 2.8598 | 3500 | 0.0060          | 0.9806    | 0.9888 | 0.9847 | 0.9983   |
| 0.0030        | 3.2681 | 4000 | 0.0062          | 0.9807    | 0.9898 | 0.9853 | 0.9984   |
| 0.0024        | 3.6767 | 4500 | 0.0068          | 0.9794    | 0.9890 | 0.9842 | 0.9983   |
| 0.0008        | 4.0850 | 5000 | 0.0070          | 0.9801    | 0.9895 | 0.9848 | 0.9983   |
| 0.0006        | 4.4937 | 5500 | 0.0073          | 0.9800    | 0.9887 | 0.9843 | 0.9983   |


### Framework versions

- Transformers 5.8.0
- Pytorch 2.11.0+cu130
- Datasets 4.8.5
- Tokenizers 0.22.2
