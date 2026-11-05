---
library_name: transformers
license: cc-by-nc-sa-4.0
base_model: microsoft/layoutlmv3-large
tags:
- layoutlmv3
- document-classification
- medical-documents
- model2b
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: layoutlmv3-large-model2b-radiology-lab-operative
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# layoutlmv3-large-model2b-radiology-lab-operative

This model is a fine-tuned version of [microsoft/layoutlmv3-large](https://huggingface.co/microsoft/layoutlmv3-large) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1427
- Accuracy: 0.9689
- Macro Precision: 0.9680
- Macro Recall: 0.9696
- Macro F1: 0.9688
- Weighted F1: 0.9689
- Precision Radiology Report: 0.9752
- Recall Radiology Report: 0.9689
- F1 Radiology Report: 0.9720
- Precision Lab Report: 0.9589
- Recall Lab Report: 0.9668
- F1 Lab Report: 0.9628
- Precision Operative Report: 0.9699
- Recall Operative Report: 0.9732
- F1 Operative Report: 0.9715

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 1
- eval_batch_size: 1
- seed: 42
- gradient_accumulation_steps: 16
- total_train_batch_size: 16
- optimizer: Use OptimizerNames.ADAFACTOR and the args are:
No additional optimizer arguments
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 3.0

### Training results

| Training Loss | Epoch  | Step | Validation Loss | Accuracy | Macro Precision | Macro Recall | Macro F1 | Weighted F1 | Precision Radiology Report | Recall Radiology Report | F1 Radiology Report | Precision Lab Report | Recall Lab Report | F1 Lab Report | Precision Operative Report | Recall Operative Report | F1 Operative Report |
|:-------------:|:------:|:----:|:---------------:|:--------:|:---------------:|:------------:|:--------:|:-----------:|:--------------------------:|:-----------------------:|:-------------------:|:--------------------:|:-----------------:|:-------------:|:--------------------------:|:-----------------------:|:-------------------:|
| 0.2022        | 0.4851 | 500  | 0.1871          | 0.9618   | 0.9581          | 0.9599       | 0.9589   | 0.9619      | 0.975                      | 0.9614                  | 0.9682              | 0.9465               | 0.9685            | 0.9574        | 0.9529                     | 0.9497                  | 0.9513              |
| 0.0799        | 0.9703 | 1000 | 0.1950          | 0.9618   | 0.9538          | 0.9639       | 0.9586   | 0.9619      | 0.9813                     | 0.9550                  | 0.9680              | 0.9481               | 0.9701            | 0.9590        | 0.9320                     | 0.9664                  | 0.9489              |
| 0.0367        | 1.4551 | 1500 | 0.2264          | 0.9635   | 0.9604          | 0.9645       | 0.9624   | 0.9635      | 0.9792                     | 0.9603                  | 0.9697              | 0.9418               | 0.9668            | 0.9542        | 0.96                       | 0.9664                  | 0.9632              |
| 0.0602        | 1.9402 | 2000 | 0.1863          | 0.9640   | 0.9620          | 0.9634       | 0.9626   | 0.9641      | 0.9751                     | 0.9636                  | 0.9693              | 0.9480               | 0.9668            | 0.9573        | 0.9630                     | 0.9597                  | 0.9613              |
| 0.0604        | 2.4250 | 2500 | 0.1429          | 0.9689   | 0.9680          | 0.9696       | 0.9688   | 0.9689      | 0.9752                     | 0.9689                  | 0.9720              | 0.9589               | 0.9668            | 0.9628        | 0.9699                     | 0.9732                  | 0.9715              |
| 0.0447        | 2.9101 | 3000 | 0.1817          | 0.9673   | 0.9673          | 0.9673       | 0.9672   | 0.9673      | 0.9772                     | 0.9636                  | 0.9703              | 0.9484               | 0.9751            | 0.9616        | 0.9762                     | 0.9631                  | 0.9696              |


### Framework versions

- Transformers 4.57.6
- Pytorch 2.10.0+cu128
- Tokenizers 0.22.2
