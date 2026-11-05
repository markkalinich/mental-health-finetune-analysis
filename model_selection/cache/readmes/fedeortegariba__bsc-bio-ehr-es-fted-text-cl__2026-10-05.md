---
library_name: transformers
license: apache-2.0
base_model: PlanTL-GOB-ES/bsc-bio-ehr-es
tags:
- generated_from_trainer
metrics:
- accuracy
- recall
- precision
- f1
model-index:
- name: bsc-bio-ehr-es-fted-text-cl
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bsc-bio-ehr-es-fted-text-cl

This model is a fine-tuned version of [PlanTL-GOB-ES/bsc-bio-ehr-es](https://huggingface.co/PlanTL-GOB-ES/bsc-bio-ehr-es) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.7020
- Accuracy: 0.9218
- Recall: 0.9313
- Precision: 0.935
- F1: 0.9331

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
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 30

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | Recall | Precision | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:------:|:---------:|:------:|
| No log        | 1.0   | 231  | 0.2719          | 0.9072   | 0.9263 | 0.9163    | 0.9212 |
| No log        | 2.0   | 462  | 0.3650          | 0.9067   | 0.9452 | 0.9004    | 0.9223 |
| 0.1526        | 3.0   | 693  | 0.4611          | 0.9137   | 0.9462 | 0.9100    | 0.9277 |
| 0.1526        | 4.0   | 924  | 0.4861          | 0.9271   | 0.9412 | 0.9347    | 0.9380 |
| 0.025         | 5.0   | 1155 | 0.5708          | 0.9154   | 0.9432 | 0.9150    | 0.9289 |
| 0.025         | 6.0   | 1386 | 0.6532          | 0.9090   | 0.9512 | 0.8992    | 0.9245 |
| 0.0064        | 7.0   | 1617 | 0.6813          | 0.9084   | 0.9482 | 0.9007    | 0.9238 |
| 0.0064        | 8.0   | 1848 | 0.6611          | 0.9131   | 0.9532 | 0.9037    | 0.9278 |
| 0.0043        | 9.0   | 2079 | 0.5888          | 0.9224   | 0.9313 | 0.9359    | 0.9336 |
| 0.0043        | 10.0  | 2310 | 0.9218          | 0.8804   | 0.9641 | 0.8514    | 0.9043 |
| 0.0049        | 11.0  | 2541 | 0.6622          | 0.9078   | 0.9432 | 0.9036    | 0.9230 |
| 0.0049        | 12.0  | 2772 | 0.6939          | 0.9172   | 0.9462 | 0.9152    | 0.9305 |
| 0.003         | 13.0  | 3003 | 0.7052          | 0.9096   | 0.9532 | 0.8986    | 0.9251 |
| 0.003         | 14.0  | 3234 | 0.9217          | 0.8926   | 0.9661 | 0.8661    | 0.9134 |
| 0.003         | 15.0  | 3465 | 0.7322          | 0.9055   | 0.9402 | 0.9025    | 0.9210 |
| 0.0049        | 16.0  | 3696 | 0.6537          | 0.9183   | 0.9283 | 0.932     | 0.9301 |
| 0.0049        | 17.0  | 3927 | 0.7311          | 0.9119   | 0.9472 | 0.9066    | 0.9264 |
| 0.0031        | 18.0  | 4158 | 0.7479          | 0.9125   | 0.9452 | 0.9090    | 0.9268 |
| 0.0031        | 19.0  | 4389 | 0.7028          | 0.9137   | 0.9412 | 0.9139    | 0.9274 |
| 0.0013        | 20.0  | 4620 | 0.7262          | 0.9096   | 0.9412 | 0.9078    | 0.9242 |
| 0.0013        | 21.0  | 4851 | 0.6785          | 0.9125   | 0.9273 | 0.9236    | 0.9254 |
| 0.0015        | 22.0  | 5082 | 0.7053          | 0.9148   | 0.9333 | 0.9222    | 0.9277 |
| 0.0015        | 23.0  | 5313 | 0.6688          | 0.9207   | 0.9193 | 0.9438    | 0.9314 |
| 0.0013        | 24.0  | 5544 | 0.7291          | 0.9125   | 0.9363 | 0.9162    | 0.9261 |
| 0.0013        | 25.0  | 5775 | 0.7323          | 0.9107   | 0.9363 | 0.9135    | 0.9247 |
| 0.0016        | 26.0  | 6006 | 0.7450          | 0.9096   | 0.9373 | 0.9109    | 0.9239 |
| 0.0016        | 27.0  | 6237 | 0.7436          | 0.9102   | 0.9363 | 0.9126    | 0.9243 |
| 0.0016        | 28.0  | 6468 | 0.7080          | 0.9218   | 0.9313 | 0.935     | 0.9331 |
| 0.001         | 29.0  | 6699 | 0.7077          | 0.9218   | 0.9313 | 0.935     | 0.9331 |
| 0.001         | 30.0  | 6930 | 0.7020          | 0.9218   | 0.9313 | 0.935     | 0.9331 |


### Framework versions

- Transformers 4.51.3
- Pytorch 2.6.0+cu124
- Datasets 3.5.0
- Tokenizers 0.21.1
