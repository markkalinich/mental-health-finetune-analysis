---
library_name: transformers
license: mit
base_model: pyannote/segmentation-3.0
tags:
- speaker-diarization
- speaker-segmentation
- generated_from_trainer
datasets:
- abar-uwc/medical-segmentation-dataset_v2
model-index:
- name: medical_segmentation_v2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# medical_segmentation_v2

This model is a fine-tuned version of [pyannote/segmentation-3.0](https://huggingface.co/pyannote/segmentation-3.0) on the abar-uwc/medical-segmentation-dataset_v2 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0143
- Model Preparation Time: 0.004
- Der: 0.0033
- False Alarm: 0.0014
- Missed Detection: 0.0017
- Confusion: 0.0002

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.001
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Use adamw_torch with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: cosine
- num_epochs: 10.0

### Training results

| Training Loss | Epoch | Step | Validation Loss | Model Preparation Time | Der    | False Alarm | Missed Detection | Confusion |
|:-------------:|:-----:|:----:|:---------------:|:----------------------:|:------:|:-----------:|:----------------:|:---------:|
| 0.0153        | 1.0   | 202  | 0.0290          | 0.004                  | 0.0067 | 0.0028      | 0.0027           | 0.0012    |
| 0.0116        | 2.0   | 404  | 0.0192          | 0.004                  | 0.0045 | 0.0020      | 0.0021           | 0.0004    |
| 0.0102        | 3.0   | 606  | 0.0162          | 0.004                  | 0.0037 | 0.0016      | 0.0020           | 0.0002    |
| 0.0086        | 4.0   | 808  | 0.0165          | 0.004                  | 0.0042 | 0.0021      | 0.0019           | 0.0002    |
| 0.0089        | 5.0   | 1010 | 0.0156          | 0.004                  | 0.0040 | 0.0018      | 0.0020           | 0.0002    |
| 0.0059        | 6.0   | 1212 | 0.0145          | 0.004                  | 0.0035 | 0.0016      | 0.0017           | 0.0002    |
| 0.0055        | 7.0   | 1414 | 0.0147          | 0.004                  | 0.0035 | 0.0016      | 0.0017           | 0.0002    |
| 0.0069        | 8.0   | 1616 | 0.0142          | 0.004                  | 0.0033 | 0.0015      | 0.0017           | 0.0001    |
| 0.0067        | 9.0   | 1818 | 0.0142          | 0.004                  | 0.0032 | 0.0014      | 0.0017           | 0.0001    |
| 0.0063        | 10.0  | 2020 | 0.0143          | 0.004                  | 0.0033 | 0.0014      | 0.0017           | 0.0002    |


### Framework versions

- Transformers 4.49.0
- Pytorch 2.7.0+cu126
- Datasets 3.5.0
- Tokenizers 0.21.0
