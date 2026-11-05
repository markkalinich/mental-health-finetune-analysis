---
library_name: transformers
license: apache-2.0
base_model: answerdotai/ModernBERT-base
tags:
- trackio
- trackio:https://huggingface.co/spaces/jefftherover/huggingface-static-33daf5
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: pii-layout-synth-v2
  results: []
---
<a href="https://huggingface.co/spaces/jefftherover/huggingface-static-33daf5" target="_blank"><img src="https://raw.githubusercontent.com/gradio-app/trackio/refs/heads/main/trackio/assets/badge.png" alt="Visualize in Trackio" title="Visualize in Trackio" style="height: 40px;"/></a>
<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# pii-layout-synth-v2

This model is a fine-tuned version of [answerdotai/ModernBERT-base](https://huggingface.co/answerdotai/ModernBERT-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0055
- Precision: 0.9870
- Recall: 0.9911
- F1: 0.9890
- Accuracy: 0.9982

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
| 0.0806        | 0.2489 | 500  | 0.0406          | 0.8933    | 0.9476 | 0.9196 | 0.9878   |
| 0.0344        | 0.4978 | 1000 | 0.0187          | 0.9575    | 0.9744 | 0.9659 | 0.9945   |
| 0.0197        | 0.7466 | 1500 | 0.0093          | 0.9792    | 0.9882 | 0.9837 | 0.9972   |
| 0.0154        | 0.9955 | 2000 | 0.0113          | 0.9750    | 0.9874 | 0.9812 | 0.9965   |
| 0.0125        | 1.2444 | 2500 | 0.0071          | 0.9831    | 0.9887 | 0.9859 | 0.9977   |
| 0.0104        | 1.4933 | 3000 | 0.0068          | 0.9841    | 0.9910 | 0.9875 | 0.9979   |
| 0.0108        | 1.7422 | 3500 | 0.0065          | 0.9849    | 0.9907 | 0.9878 | 0.9979   |
| 0.0124        | 1.9910 | 4000 | 0.0058          | 0.9863    | 0.9923 | 0.9893 | 0.9981   |
| 0.0050        | 2.2399 | 4500 | 0.0055          | 0.9879    | 0.9920 | 0.9900 | 0.9983   |
| 0.0047        | 2.4888 | 5000 | 0.0055          | 0.9872    | 0.9926 | 0.9899 | 0.9983   |
| 0.0050        | 2.7377 | 5500 | 0.0058          | 0.9865    | 0.9926 | 0.9895 | 0.9982   |
| 0.0062        | 2.9866 | 6000 | 0.0055          | 0.9870    | 0.9911 | 0.9890 | 0.9982   |


### Framework versions

- Transformers 5.11.0
- Pytorch 2.12.0+cu130
- Datasets 5.0.0
- Tokenizers 0.22.2
