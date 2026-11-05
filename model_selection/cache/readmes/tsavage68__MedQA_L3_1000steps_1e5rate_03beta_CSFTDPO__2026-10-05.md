---
license: llama3
base_model: tsavage68/MedQA_L3_1000steps_1e6rate_SFT
tags:
- trl
- dpo
- generated_from_trainer
model-index:
- name: MedQA_L3_1000steps_1e5rate_03beta_CSFTDPO
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# MedQA_L3_1000steps_1e5rate_03beta_CSFTDPO

This model is a fine-tuned version of [tsavage68/MedQA_L3_1000steps_1e6rate_SFT](https://huggingface.co/tsavage68/MedQA_L3_1000steps_1e6rate_SFT) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.8199
- Rewards/chosen: -5.6953
- Rewards/rejected: -5.2697
- Rewards/accuracies: 0.4571
- Rewards/margins: -0.4255
- Logps/rejected: -51.4207
- Logps/chosen: -50.3128
- Logits/rejected: -1.1748
- Logits/chosen: -1.1747

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-05
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
| 0.6976        | 0.0489 | 50   | 1.6003          | -6.0871        | -6.7321          | 0.5626             | 0.6450          | -56.2952       | -51.6189     | -0.8478         | -0.8474       |
| 2.0492        | 0.0977 | 100  | 1.5171          | -2.8937        | -2.7957          | 0.4791             | -0.0979         | -43.1739       | -40.9741     | -0.7086         | -0.7085       |
| 3.2675        | 0.1466 | 150  | 2.4839          | -9.5405        | -8.8952          | 0.4264             | -0.6452         | -63.5056       | -63.1301     | -0.6090         | -0.6092       |
| 2.5387        | 0.1954 | 200  | 2.8407          | -10.8845       | -10.2333         | 0.4220             | -0.6513         | -67.9657       | -67.6103     | -2.0451         | -2.0454       |
| 3.5954        | 0.2443 | 250  | 5.2964          | -26.2267       | -26.1016         | 0.4725             | -0.1251         | -120.8603      | -118.7509    | -2.7907         | -2.7903       |
| 5.2171        | 0.2931 | 300  | 3.1156          | -11.9636       | -11.4341         | 0.4549             | -0.5294         | -71.9686       | -71.2070     | -1.4795         | -1.4797       |
| 2.6671        | 0.3420 | 350  | 2.8765          | -8.6508        | -8.1258          | 0.4220             | -0.5250         | -60.9407       | -60.1644     | -0.9503         | -0.9502       |
| 3.7894        | 0.3908 | 400  | 2.8694          | -9.8779        | -9.1060          | 0.4242             | -0.7720         | -64.2081       | -64.2550     | -1.0926         | -1.0927       |
| 4.4115        | 0.4397 | 450  | 2.6152          | -9.1581        | -8.5492          | 0.4176             | -0.6089         | -62.3523       | -61.8555     | -1.3932         | -1.3933       |
| 3.6882        | 0.4885 | 500  | 2.5995          | -10.0842       | -9.5563          | 0.4352             | -0.5279         | -65.7092       | -64.9425     | -1.3920         | -1.3918       |
| 4.7478        | 0.5374 | 550  | 3.1439          | -13.8538       | -13.2693         | 0.4264             | -0.5845         | -78.0858       | -77.5078     | -1.4673         | -1.4673       |
| 3.6453        | 0.5862 | 600  | 2.5501          | -10.1562       | -9.6020          | 0.4154             | -0.5542         | -65.8615       | -65.1824     | -1.8008         | -1.8006       |
| 1.9093        | 0.6351 | 650  | 2.0900          | -7.1034        | -6.4496          | 0.4352             | -0.6537         | -55.3536       | -55.0064     | -1.5307         | -1.5306       |
| 1.978         | 0.6839 | 700  | 1.9643          | -5.1638        | -4.6928          | 0.4593             | -0.4710         | -49.4976       | -48.5413     | -1.2420         | -1.2419       |
| 2.6252        | 0.7328 | 750  | 1.8926          | -6.6759        | -6.1506          | 0.4396             | -0.5254         | -54.3567       | -53.5815     | -1.3560         | -1.3560       |
| 2.0384        | 0.7816 | 800  | 1.8552          | -6.4512        | -5.9923          | 0.4374             | -0.4588         | -53.8292       | -52.8324     | -1.2189         | -1.2188       |
| 2.3167        | 0.8305 | 850  | 1.8255          | -5.8191        | -5.3851          | 0.4549             | -0.4341         | -51.8050       | -50.7256     | -1.1902         | -1.1901       |
| 2.1526        | 0.8793 | 900  | 1.8196          | -5.7219        | -5.2966          | 0.4549             | -0.4252         | -51.5102       | -50.4014     | -1.1751         | -1.1750       |
| 2.0182        | 0.9282 | 950  | 1.8220          | -5.6982        | -5.2706          | 0.4593             | -0.4276         | -51.4235       | -50.3224     | -1.1750         | -1.1749       |
| 1.3984        | 0.9770 | 1000 | 1.8199          | -5.6953        | -5.2697          | 0.4571             | -0.4255         | -51.4207       | -50.3128     | -1.1748         | -1.1747       |


### Framework versions

- Transformers 4.41.1
- Pytorch 2.0.0+cu117
- Datasets 2.19.1
- Tokenizers 0.19.1
