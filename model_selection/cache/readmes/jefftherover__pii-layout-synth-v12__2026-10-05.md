---
library_name: transformers
license: apache-2.0
base_model: answerdotai/ModernBERT-base
tags:
- trackio
- trackio:https://huggingface.co/spaces/jefftherover/huggingface-static-34560d
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: pii-layout-synth-v12
  results: []
---
<a href="https://huggingface.co/spaces/jefftherover/huggingface-static-34560d" target="_blank"><img src="https://raw.githubusercontent.com/gradio-app/trackio/refs/heads/main/trackio/assets/badge.png" alt="Visualize in Trackio" title="Visualize in Trackio" style="height: 40px;"/></a>
<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# pii-layout-synth-v12

This model is a fine-tuned version of [answerdotai/ModernBERT-base](https://huggingface.co/answerdotai/ModernBERT-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0041
- Precision: 0.9926
- Recall: 0.9954
- F1: 0.9940
- Accuracy: 0.9988

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
| 0.0340        | 0.1863 | 500  | 0.0140          | 0.9722    | 0.9818 | 0.9770 | 0.9960   |
| 0.0238        | 0.3726 | 1000 | 0.0104          | 0.9820    | 0.9888 | 0.9854 | 0.9970   |
| 0.0138        | 0.5589 | 1500 | 0.0077          | 0.9852    | 0.9919 | 0.9885 | 0.9977   |
| 0.0126        | 0.7452 | 2000 | 0.0063          | 0.9873    | 0.9910 | 0.9891 | 0.9980   |
| 0.0143        | 0.9314 | 2500 | 0.0049          | 0.9914    | 0.9954 | 0.9934 | 0.9986   |
| 0.0058        | 1.1177 | 3000 | 0.0042          | 0.9920    | 0.9959 | 0.9939 | 0.9988   |
| 0.0073        | 1.3040 | 3500 | 0.0064          | 0.9891    | 0.9933 | 0.9912 | 0.9981   |
| 0.0081        | 1.4903 | 4000 | 0.0068          | 0.9891    | 0.9917 | 0.9904 | 0.9981   |
| 0.0058        | 1.6766 | 4500 | 0.0037          | 0.9932    | 0.9965 | 0.9949 | 0.9989   |
| 0.0075        | 1.8629 | 5000 | 0.0040          | 0.9918    | 0.9957 | 0.9938 | 0.9988   |
| 0.0030        | 2.0492 | 5500 | 0.0033          | 0.9935    | 0.9952 | 0.9944 | 0.9990   |
| 0.0033        | 2.2355 | 6000 | 0.0041          | 0.9926    | 0.9954 | 0.9940 | 0.9988   |


### Framework versions

- Transformers 5.12.1
- Pytorch 2.12.1+cu130
- Datasets 5.0.0
- Tokenizers 0.22.2
