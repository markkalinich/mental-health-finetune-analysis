---
library_name: transformers
license: apache-2.0
base_model: jefftherover/modernbert-pii-ner
tags:
- trackio
- trackio:https://huggingface.co/spaces/jefftherover/huggingface-static-a94390
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: modernbert-pii-mapped
  results: []
---
<a href="https://huggingface.co/spaces/jefftherover/huggingface-static-a94390" target="_blank"><img src="https://raw.githubusercontent.com/gradio-app/trackio/refs/heads/main/trackio/assets/badge.png" alt="Visualize in Trackio" title="Visualize in Trackio" style="height: 40px;"/></a>
<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# modernbert-pii-mapped

This model is a fine-tuned version of [jefftherover/modernbert-pii-ner](https://huggingface.co/jefftherover/modernbert-pii-ner) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0104
- Precision: 0.9793
- Recall: 0.9893
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
- learning_rate: 3e-05
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
| 0.0085        | 0.4087 | 500  | 0.0079          | 0.9700    | 0.9833 | 0.9766 | 0.9977   |
| 0.0055        | 0.8173 | 1000 | 0.0070          | 0.9770    | 0.9879 | 0.9824 | 0.9982   |
| 0.0045        | 1.2256 | 1500 | 0.0085          | 0.9722    | 0.9819 | 0.9770 | 0.9979   |
| 0.0037        | 1.6342 | 2000 | 0.0079          | 0.9749    | 0.9884 | 0.9816 | 0.9980   |
| 0.0022        | 2.0425 | 2500 | 0.0079          | 0.9775    | 0.9891 | 0.9833 | 0.9981   |
| 0.0012        | 2.4512 | 3000 | 0.0093          | 0.9745    | 0.9879 | 0.9812 | 0.9980   |
| 0.0011        | 2.8598 | 3500 | 0.0086          | 0.9778    | 0.9914 | 0.9846 | 0.9982   |
| 0.0002        | 3.2681 | 4000 | 0.0094          | 0.9814    | 0.9892 | 0.9853 | 0.9984   |
| 0.0001        | 3.6767 | 4500 | 0.0104          | 0.9796    | 0.9897 | 0.9846 | 0.9983   |
| 0.0000        | 4.0850 | 5000 | 0.0103          | 0.9793    | 0.9898 | 0.9845 | 0.9983   |
| 0.0000        | 4.4937 | 5500 | 0.0104          | 0.9793    | 0.9893 | 0.9843 | 0.9983   |


### Framework versions

- Transformers 5.8.0
- Pytorch 2.11.0+cu130
- Datasets 4.8.5
- Tokenizers 0.22.2
