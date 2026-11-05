---
library_name: transformers
license: cc-by-sa-4.0
base_model: ZycckZ/Zk1-QA-VN-test
tags:
- generated_from_trainer
model-index:
- name: Zk1-QA-VN-test2
  results: []
datasets:
- taidng/UIT-ViQuAD2.0
language:
- vi
pipeline_tag: question-answering
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Zk1-QA-VN-test2 (ZycckZ/Simple_VieQA)

This model is a fine-tuned version of [ZycckZ/Zk1-QA-VN-test](https://huggingface.co/ZycckZ/Zk1-QA-VN-test) and [taidng/UIT-ViQuAD2](https://huggingface.co/datasets/taidng/UIT-ViQuAD2.0) dataset.

It achieves the following results on the evaluation set:
- Loss: 1.8800
- Exact Match (EM): 70.07
- F1 Score: 82.34

## Model description

This model now much better than the model before ([ZycckZ/Zk1-QA-VN-test](https://huggingface.co/ZycckZ/Zk1-QA-VN-test)). 

## Intended uses & limitations

- Create a simple chatbot QA 🤗
- Just for Vietnamese QA system

## Training and evaluation data

Training:
- taidng/UIT-ViQuAD2.0 - "train"
- taidng/UIT-ViQuAD2.0 - "validation"
- taidng/UIT-ViQuAD2.0 - "test"

Evaluation:
- taidng/UIT-ViQuAD2.0 - "validation"

## Training procedure

Based on Question Answering HuggingFace 🤗

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step  | Validation Loss |
|:-------------:|:-----:|:-----:|:---------------:|
| 1.171         | 1.0   | 2226  | 1.0648          |
| 0.8499        | 2.0   | 4452  | 1.1054          |
| 0.5862        | 3.0   | 6678  | 1.2583          |
| 0.4082        | 4.0   | 8904  | 1.5642          |
| 0.2835        | 5.0   | 11130 | 1.8800          |


### Framework versions

- Transformers 4.52.2
- Pytorch 2.6.0+cu124
- Datasets 2.14.4
- Tokenizers 0.21.1