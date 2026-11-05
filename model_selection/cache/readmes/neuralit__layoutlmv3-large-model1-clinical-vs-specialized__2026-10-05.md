---
library_name: transformers
license: cc-by-nc-sa-4.0
base_model: microsoft/layoutlmv3-large
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: layoutlmv3-large-model1-clinical-vs-specialized
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# layoutlmv3-large-model1-clinical-vs-specialized

This model is a fine-tuned version of [microsoft/layoutlmv3-large](https://huggingface.co/microsoft/layoutlmv3-large) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1348
- Accuracy: 0.9771
- Macro Precision: 0.9771
- Macro Recall: 0.9771
- Macro F1: 0.9771
- Weighted F1: 0.9771
- Precision Specialized Diagnostics Procedures: 0.9776
- Recall Specialized Diagnostics Procedures: 0.9766
- F1 Specialized Diagnostics Procedures: 0.9771
- Precision Clinical Evaluation Progress: 0.9766
- Recall Clinical Evaluation Progress: 0.9776
- F1 Clinical Evaluation Progress: 0.9771

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

| Training Loss | Epoch  | Step | Validation Loss | Accuracy | Macro Precision | Macro Recall | Macro F1 | Weighted F1 | Precision Specialized Diagnostics Procedures | Recall Specialized Diagnostics Procedures | F1 Specialized Diagnostics Procedures | Precision Clinical Evaluation Progress | Recall Clinical Evaluation Progress | F1 Clinical Evaluation Progress |
|:-------------:|:------:|:----:|:---------------:|:--------:|:---------------:|:------------:|:--------:|:-----------:|:--------------------------------------------:|:-----------------------------------------:|:-------------------------------------:|:--------------------------------------:|:-----------------------------------:|:-------------------------------:|
| 0.1797        | 0.2426 | 500  | 0.6136          | 0.8732   | 0.8942          | 0.8732       | 0.8715   | 0.8715      | 0.8033                                       | 0.9885                                    | 0.8863                                | 0.9851                                 | 0.7579                              | 0.8567                          |
| 0.1666        | 0.4851 | 1000 | 0.2275          | 0.9558   | 0.9568          | 0.9558       | 0.9558   | 0.9558      | 0.9354                                       | 0.9793                                    | 0.9568                                | 0.9783                                 | 0.9324                              | 0.9548                          |
| 0.1152        | 0.7277 | 1500 | 0.1561          | 0.9681   | 0.9683          | 0.9681       | 0.9681   | 0.9681      | 0.9772                                       | 0.9586                                    | 0.9678                                | 0.9593                                 | 0.9776                              | 0.9684                          |
| 0.1771        | 0.9703 | 2000 | 0.1491          | 0.9643   | 0.9645          | 0.9643       | 0.9643   | 0.9643      | 0.9733                                       | 0.9547                                    | 0.9639                                | 0.9556                                 | 0.9738                              | 0.9646                          |
| 0.1685        | 1.2125 | 2500 | 0.1408          | 0.9719   | 0.9719          | 0.9719       | 0.9719   | 0.9719      | 0.9722                                       | 0.9716                                    | 0.9719                                | 0.9717                                 | 0.9722                              | 0.9719                          |
| 0.1446        | 1.4551 | 3000 | 0.1437          | 0.9725   | 0.9725          | 0.9725       | 0.9725   | 0.9725      | 0.9702                                       | 0.9749                                    | 0.9725                                | 0.9748                                 | 0.9700                              | 0.9724                          |
| 0.1136        | 1.6976 | 3500 | 0.1414          | 0.9711   | 0.9712          | 0.9711       | 0.9711   | 0.9711      | 0.9768                                       | 0.9651                                    | 0.9709                                | 0.9655                                 | 0.9771                              | 0.9713                          |
| 0.0852        | 1.9402 | 4000 | 0.1387          | 0.9733   | 0.9734          | 0.9733       | 0.9733   | 0.9733      | 0.9806                                       | 0.9656                                    | 0.9731                                | 0.9662                                 | 0.9809                              | 0.9735                          |
| 0.0429        | 2.1824 | 4500 | 0.1323          | 0.9768   | 0.9768          | 0.9768       | 0.9768   | 0.9768      | 0.9787                                       | 0.9749                                    | 0.9768                                | 0.9750                                 | 0.9787                              | 0.9769                          |
| 0.0717        | 2.4250 | 5000 | 0.1373          | 0.9766   | 0.9766          | 0.9766       | 0.9766   | 0.9766      | 0.975                                        | 0.9782                                    | 0.9766                                | 0.9781                                 | 0.9749                              | 0.9765                          |
| 0.0784        | 2.6676 | 5500 | 0.1257          | 0.9785   | 0.9785          | 0.9785       | 0.9785   | 0.9785      | 0.9787                                       | 0.9782                                    | 0.9785                                | 0.9782                                 | 0.9787                              | 0.9785                          |
| 0.1109        | 2.9101 | 6000 | 0.1348          | 0.9771   | 0.9771          | 0.9771       | 0.9771   | 0.9771      | 0.9776                                       | 0.9766                                    | 0.9771                                | 0.9766                                 | 0.9776                              | 0.9771                          |


### Framework versions

- Transformers 4.57.6
- Pytorch 2.10.0+cu128
- Tokenizers 0.22.2
