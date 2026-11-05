---
library_name: transformers
license: apache-2.0
base_model: answerdotai/ModernBERT-base
tags:
- trackio
- trackio:https://huggingface.co/spaces/jefftherover/huggingface-static-b842a7
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: pii-layout-synth-v1
  results: []
---
<a href="https://huggingface.co/spaces/jefftherover/huggingface-static-b842a7" target="_blank"><img src="https://raw.githubusercontent.com/gradio-app/trackio/refs/heads/main/trackio/assets/badge.png" alt="Visualize in Trackio" title="Visualize in Trackio" style="height: 40px;"/></a>
<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# pii-layout-synth-v1

This model is a fine-tuned version of [answerdotai/ModernBERT-base](https://huggingface.co/answerdotai/ModernBERT-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0040
- Precision: 0.9934
- Recall: 0.9956
- F1: 0.9945
- Accuracy: 0.9991

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
| 0.0666        | 0.2386 | 500  | 0.0279          | 0.9352    | 0.9544 | 0.9447 | 0.9922   |
| 0.0305        | 0.4772 | 1000 | 0.0174          | 0.9665    | 0.9808 | 0.9736 | 0.9955   |
| 0.0172        | 0.7158 | 1500 | 0.0101          | 0.9743    | 0.9825 | 0.9784 | 0.9970   |
| 0.0197        | 0.9544 | 2000 | 0.0056          | 0.9856    | 0.9908 | 0.9882 | 0.9984   |
| 0.0064        | 1.1928 | 2500 | 0.0057          | 0.9880    | 0.9916 | 0.9898 | 0.9985   |
| 0.0080        | 1.4314 | 3000 | 0.0049          | 0.9879    | 0.9928 | 0.9903 | 0.9986   |
| 0.0076        | 1.6700 | 3500 | 0.0050          | 0.9878    | 0.9899 | 0.9888 | 0.9985   |
| 0.0078        | 1.9086 | 4000 | 0.0042          | 0.9916    | 0.9943 | 0.9930 | 0.9989   |
| 0.0035        | 2.1470 | 4500 | 0.0038          | 0.9913    | 0.9941 | 0.9927 | 0.9989   |
| 0.0031        | 2.3856 | 5000 | 0.0038          | 0.9911    | 0.9938 | 0.9924 | 0.9989   |
| 0.0026        | 2.6242 | 5500 | 0.0037          | 0.9921    | 0.9948 | 0.9935 | 0.9990   |
| 0.0021        | 2.8628 | 6000 | 0.0042          | 0.9920    | 0.9949 | 0.9934 | 0.9989   |
| 0.0011        | 3.1012 | 6500 | 0.0037          | 0.9927    | 0.9951 | 0.9939 | 0.9991   |
| 0.0012        | 3.3398 | 7000 | 0.0040          | 0.9927    | 0.9950 | 0.9938 | 0.9991   |
| 0.0009        | 3.5784 | 7500 | 0.0039          | 0.9930    | 0.9952 | 0.9941 | 0.9991   |
| 0.0009        | 3.8170 | 8000 | 0.0038          | 0.9936    | 0.9959 | 0.9948 | 0.9991   |
| 0.0003        | 4.0554 | 8500 | 0.0039          | 0.9935    | 0.9955 | 0.9945 | 0.9991   |
| 0.0003        | 4.2940 | 9000 | 0.0040          | 0.9934    | 0.9955 | 0.9945 | 0.9991   |
| 0.0001        | 4.5326 | 9500 | 0.0040          | 0.9934    | 0.9956 | 0.9945 | 0.9991   |


### Framework versions

- Transformers 5.10.2
- Pytorch 2.12.0+cu130
- Datasets 5.0.0
- Tokenizers 0.22.2
