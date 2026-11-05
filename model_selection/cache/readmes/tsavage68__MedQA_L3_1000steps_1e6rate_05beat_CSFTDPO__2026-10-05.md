---
license: llama3
base_model: meta-llama/Meta-Llama-3-8B-Instruct
tags:
- trl
- dpo
- generated_from_trainer
model-index:
- name: MedQA_L3_1000steps_1e6rate_05beat_CSFTDPO
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# MedQA_L3_1000steps_1e6rate_05beat_CSFTDPO

This model is a fine-tuned version of [meta-llama/Meta-Llama-3-8B-Instruct](https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5717
- Rewards/chosen: -1.8210
- Rewards/rejected: -5.7186
- Rewards/accuracies: 0.8066
- Rewards/margins: 3.8976
- Logps/rejected: -32.7538
- Logps/chosen: -21.8647
- Logits/rejected: -1.0151
- Logits/chosen: -1.0132

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-06
- train_batch_size: 2
- eval_batch_size: 1
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 4
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: cosine
- lr_scheduler_warmup_steps: 100
- training_steps: 1000

### Training results

| Training Loss | Epoch  | Step | Validation Loss | Rewards/chosen | Rewards/rejected | Rewards/accuracies | Rewards/margins | Logps/rejected | Logps/chosen | Logits/rejected | Logits/chosen |
|:-------------:|:------:|:----:|:---------------:|:--------------:|:----------------:|:------------------:|:---------------:|:--------------:|:------------:|:---------------:|:-------------:|
| 0.7075        | 0.0489 | 50   | 0.6367          | 0.2363         | 0.0705           | 0.6571             | 0.1658          | -21.1755       | -17.7501     | -0.9379         | -0.9373       |
| 0.6451        | 0.0977 | 100  | 0.6114          | -0.8886        | -1.7629          | 0.6923             | 0.8743          | -24.8423       | -19.9998     | -0.9999         | -0.9992       |
| 0.7409        | 0.1466 | 150  | 0.6018          | -1.9813        | -3.3881          | 0.7297             | 1.4068          | -28.0927       | -22.1852     | -0.9814         | -0.9805       |
| 0.4181        | 0.1954 | 200  | 0.5971          | -1.4742        | -3.0996          | 0.7341             | 1.6254          | -27.5157       | -21.1711     | -0.9791         | -0.9778       |
| 0.7476        | 0.2443 | 250  | 0.5735          | -1.5098        | -3.3523          | 0.7648             | 1.8425          | -28.0212       | -21.2423     | -0.9317         | -0.9303       |
| 0.5351        | 0.2931 | 300  | 0.7384          | -1.9600        | -4.7179          | 0.7538             | 2.7579          | -30.7524       | -22.1427     | -0.9715         | -0.9699       |
| 0.3789        | 0.3420 | 350  | 0.6165          | -2.8286        | -5.5771          | 0.7846             | 2.7485          | -32.4706       | -23.8798     | -0.9876         | -0.9860       |
| 0.6639        | 0.3908 | 400  | 0.5874          | -1.6246        | -4.5259          | 0.7912             | 2.9013          | -30.3683       | -21.4718     | -1.0086         | -1.0070       |
| 1.046         | 0.4397 | 450  | 0.5833          | -1.4867        | -4.5791          | 0.8044             | 3.0924          | -30.4748       | -21.1961     | -0.9772         | -0.9753       |
| 1.1477        | 0.4885 | 500  | 0.5726          | -1.9020        | -4.7805          | 0.8022             | 2.8785          | -30.8775       | -22.0266     | -0.9644         | -0.9628       |
| 0.2869        | 0.5374 | 550  | 0.5733          | -1.9387        | -5.0557          | 0.8000             | 3.1170          | -31.4279       | -22.1000     | -0.9901         | -0.9887       |
| 0.3924        | 0.5862 | 600  | 0.5336          | -1.1994        | -4.6601          | 0.8066             | 3.4607          | -30.6367       | -20.6214     | -0.9897         | -0.9880       |
| 0.5685        | 0.6351 | 650  | 0.5600          | -0.6431        | -4.3081          | 0.8000             | 3.6650          | -29.9327       | -19.5088     | -1.0020         | -1.0002       |
| 0.5743        | 0.6839 | 700  | 0.5739          | -1.5294        | -5.3059          | 0.8000             | 3.7764          | -31.9282       | -21.2815     | -1.0088         | -1.0069       |
| 0.5395        | 0.7328 | 750  | 0.5778          | -1.6200        | -5.4658          | 0.8088             | 3.8459          | -32.2482       | -21.4626     | -1.0136         | -1.0117       |
| 0.3395        | 0.7816 | 800  | 0.5754          | -1.8314        | -5.7044          | 0.8000             | 3.8730          | -32.7253       | -21.8854     | -1.0148         | -1.0130       |
| 0.6214        | 0.8305 | 850  | 0.5752          | -1.8114        | -5.6937          | 0.8000             | 3.8823          | -32.7039       | -21.8454     | -1.0152         | -1.0133       |
| 0.9719        | 0.8793 | 900  | 0.5707          | -1.8135        | -5.7132          | 0.8066             | 3.8997          | -32.7430       | -21.8497     | -1.0147         | -1.0128       |
| 0.3164        | 0.9282 | 950  | 0.5710          | -1.8198        | -5.7127          | 0.8000             | 3.8929          | -32.7420       | -21.8623     | -1.0148         | -1.0129       |
| 0.1257        | 0.9770 | 1000 | 0.5717          | -1.8210        | -5.7186          | 0.8066             | 3.8976          | -32.7538       | -21.8647     | -1.0151         | -1.0132       |


### Framework versions

- Transformers 4.41.0
- Pytorch 2.0.0+cu117
- Datasets 2.19.1
- Tokenizers 0.19.1
