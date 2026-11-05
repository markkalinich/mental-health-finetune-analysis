---
library_name: transformers
license: apache-2.0
base_model: answerdotai/ModernBERT-base
tags:
- trackio
- trackio:https://huggingface.co/spaces/jefftherover/huggingface-static-31b720
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: modernbert-pii-mapped-v12
  results: []
---
<a href="https://huggingface.co/spaces/jefftherover/huggingface-static-31b720" target="_blank"><img src="https://raw.githubusercontent.com/gradio-app/trackio/refs/heads/main/trackio/assets/badge.png" alt="Visualize in Trackio" title="Visualize in Trackio" style="height: 40px;"/></a>
<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# modernbert-pii-mapped-v12

This model is a fine-tuned version of [answerdotai/ModernBERT-base](https://huggingface.co/answerdotai/ModernBERT-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0077
- Precision: 0.9787
- Recall: 0.9909
- F1: 0.9848
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
| 0.0656        | 0.3591 | 500  | 0.0333          | 0.8816    | 0.9458 | 0.9125 | 0.9910   |
| 0.0408        | 0.7181 | 1000 | 0.0189          | 0.9444    | 0.9723 | 0.9582 | 0.9949   |
| 0.0156        | 1.0768 | 1500 | 0.0099          | 0.9639    | 0.9865 | 0.9751 | 0.9969   |
| 0.0136        | 1.4359 | 2000 | 0.0104          | 0.9695    | 0.9935 | 0.9814 | 0.9972   |
| 0.0163        | 1.7950 | 2500 | 0.0094          | 0.9617    | 0.9769 | 0.9692 | 0.9969   |
| 0.0061        | 2.1537 | 3000 | 0.0080          | 0.9728    | 0.9917 | 0.9822 | 0.9978   |
| 0.0080        | 2.5127 | 3500 | 0.0069          | 0.9757    | 0.9935 | 0.9845 | 0.9980   |
| 0.0075        | 2.8718 | 4000 | 0.0076          | 0.9778    | 0.9917 | 0.9847 | 0.9981   |
| 0.0023        | 3.2305 | 4500 | 0.0078          | 0.9778    | 0.9929 | 0.9853 | 0.9981   |
| 0.0020        | 3.5896 | 5000 | 0.0076          | 0.9783    | 0.9916 | 0.9849 | 0.9980   |
| 0.0017        | 3.9487 | 5500 | 0.0073          | 0.9766    | 0.9890 | 0.9828 | 0.9981   |
| 0.0005        | 4.3074 | 6000 | 0.0078          | 0.9792    | 0.9925 | 0.9858 | 0.9982   |
| 0.0006        | 4.6664 | 6500 | 0.0076          | 0.9787    | 0.9906 | 0.9846 | 0.9982   |
| 0.0007        | 5.0    | 6965 | 0.0077          | 0.9787    | 0.9909 | 0.9848 | 0.9982   |


### Framework versions

- Transformers 5.9.0
- Pytorch 2.12.0+cu130
- Datasets 4.8.5
- Tokenizers 0.22.2
