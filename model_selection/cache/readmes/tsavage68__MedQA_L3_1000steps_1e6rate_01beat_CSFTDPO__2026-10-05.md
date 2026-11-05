---
license: llama3
base_model: meta-llama/Meta-Llama-3-8B-Instruct
tags:
- trl
- dpo
- generated_from_trainer
model-index:
- name: MedQA_L3_1000steps_1e6rate_01beat_CSFTDPO
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# MedQA_L3_1000steps_1e6rate_01beat_CSFTDPO

This model is a fine-tuned version of [meta-llama/Meta-Llama-3-8B-Instruct](https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4018
- Rewards/chosen: -1.1456
- Rewards/rejected: -2.9172
- Rewards/accuracies: 0.7912
- Rewards/margins: 1.7716
- Logps/rejected: -50.4889
- Logps/chosen: -29.6790
- Logits/rejected: -1.3967
- Logits/chosen: -1.3936

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
| 0.695         | 0.0489 | 50   | 0.6713          | 0.0342         | -0.0142          | 0.6615             | 0.0484          | -21.4583       | -17.8807     | -0.9400         | -0.9395       |
| 0.6187        | 0.0977 | 100  | 0.5915          | -0.1174        | -0.4200          | 0.7121             | 0.3027          | -25.5168       | -19.3963     | -1.0412         | -1.0403       |
| 0.5652        | 0.1466 | 150  | 0.5103          | -0.6250        | -1.3027          | 0.7495             | 0.6777          | -34.3433       | -24.4723     | -1.1124         | -1.1110       |
| 0.4549        | 0.1954 | 200  | 0.5152          | -1.3616        | -2.3988          | 0.7231             | 1.0372          | -45.3043       | -31.8385     | -1.2048         | -1.2020       |
| 0.4875        | 0.2443 | 250  | 0.4642          | -0.6443        | -1.7506          | 0.7648             | 1.1063          | -38.8228       | -24.6654     | -1.1785         | -1.1765       |
| 0.4433        | 0.2931 | 300  | 0.4453          | -0.8917        | -2.2308          | 0.8044             | 1.3391          | -43.6244       | -27.1394     | -1.2423         | -1.2401       |
| 0.5036        | 0.3420 | 350  | 0.4581          | -0.7568        | -2.0680          | 0.7692             | 1.3112          | -41.9963       | -25.7907     | -1.2182         | -1.2158       |
| 0.6285        | 0.3908 | 400  | 0.4703          | -0.6136        | -1.9063          | 0.7604             | 1.2927          | -40.3798       | -24.3588     | -1.2386         | -1.2361       |
| 0.5726        | 0.4397 | 450  | 0.4732          | -0.4602        | -1.5238          | 0.7692             | 1.0636          | -36.5545       | -22.8248     | -1.2652         | -1.2626       |
| 0.5198        | 0.4885 | 500  | 0.4280          | -0.9825        | -2.4466          | 0.8066             | 1.4641          | -45.7828       | -28.0480     | -1.3426         | -1.3399       |
| 0.3963        | 0.5374 | 550  | 0.4236          | -0.9424        | -2.3856          | 0.8022             | 1.4432          | -45.1725       | -27.6467     | -1.3514         | -1.3488       |
| 0.3233        | 0.5862 | 600  | 0.4127          | -0.9551        | -2.5770          | 0.8000             | 1.6219          | -47.0868       | -27.7738     | -1.3761         | -1.3733       |
| 0.3955        | 0.6351 | 650  | 0.4236          | -0.9988        | -2.7155          | 0.7846             | 1.7167          | -48.4714       | -28.2110     | -1.3837         | -1.3806       |
| 0.3121        | 0.6839 | 700  | 0.4109          | -1.0837        | -2.8282          | 0.7868             | 1.7445          | -49.5986       | -29.0595     | -1.3902         | -1.3871       |
| 0.4809        | 0.7328 | 750  | 0.4060          | -1.1344        | -2.8863          | 0.7846             | 1.7519          | -50.1796       | -29.5667     | -1.3954         | -1.3923       |
| 0.4075        | 0.7816 | 800  | 0.4013          | -1.1649        | -2.9284          | 0.7868             | 1.7635          | -50.6008       | -29.8717     | -1.3971         | -1.3939       |
| 0.584         | 0.8305 | 850  | 0.4014          | -1.1482        | -2.9188          | 0.7890             | 1.7706          | -50.5041       | -29.7042     | -1.3971         | -1.3939       |
| 0.5942        | 0.8793 | 900  | 0.4042          | -1.1517        | -2.9160          | 0.7846             | 1.7643          | -50.4761       | -29.7394     | -1.3965         | -1.3934       |
| 0.3169        | 0.9282 | 950  | 0.4040          | -1.1507        | -2.9162          | 0.7934             | 1.7655          | -50.4786       | -29.7294     | -1.3965         | -1.3934       |
| 0.2727        | 0.9770 | 1000 | 0.4018          | -1.1456        | -2.9172          | 0.7912             | 1.7716          | -50.4889       | -29.6790     | -1.3967         | -1.3936       |


### Framework versions

- Transformers 4.41.0
- Pytorch 2.0.0+cu117
- Datasets 2.19.1
- Tokenizers 0.19.1
