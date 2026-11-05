---
license: llama3
base_model: tsavage68/MedQA_L3_1000steps_1e6rate_SFT
tags:
- trl
- dpo
- generated_from_trainer
model-index:
- name: MedQA_L3_1000steps_1e5rate_01beta_CSFTDPO
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# MedQA_L3_1000steps_1e5rate_01beta_CSFTDPO

This model is a fine-tuned version of [tsavage68/MedQA_L3_1000steps_1e6rate_SFT](https://huggingface.co/tsavage68/MedQA_L3_1000steps_1e6rate_SFT) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.9802
- Rewards/chosen: -1.8607
- Rewards/rejected: -1.7391
- Rewards/accuracies: 0.4505
- Rewards/margins: -0.1215
- Logps/rejected: -51.2462
- Logps/chosen: -49.9353
- Logits/rejected: -0.2251
- Logits/chosen: -0.2248

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
| 0.671         | 0.0489 | 50   | 1.6433          | -6.4141        | -6.3515          | 0.4747             | -0.0626         | -97.3700       | -95.4696     | -0.6453         | -0.6453       |
| 1.0504        | 0.0977 | 100  | 0.8270          | -1.6657        | -1.8409          | 0.5385             | 0.1752          | -52.2642       | -47.9860     | -1.0550         | -1.0545       |
| 1.4654        | 0.1466 | 150  | 0.9969          | -1.4406        | -1.2778          | 0.4264             | -0.1627         | -46.6333       | -45.7340     | -0.2863         | -0.2860       |
| 1.2453        | 0.1954 | 200  | 1.6314          | -5.7863        | -5.5157          | 0.4462             | -0.2706         | -89.0113       | -89.1912     | 1.2703          | 1.2702        |
| 1.0999        | 0.2443 | 250  | 1.0650          | -2.0798        | -1.9143          | 0.4549             | -0.1655         | -52.9977       | -52.1260     | -0.3259         | -0.3258       |
| 1.6167        | 0.2931 | 300  | 1.0970          | -2.8882        | -2.6210          | 0.4374             | -0.2672         | -60.0648       | -60.2105     | -0.5895         | -0.5898       |
| 1.251         | 0.3420 | 350  | 1.0338          | -1.6529        | -1.4770          | 0.4374             | -0.1759         | -48.6251       | -47.8575     | -0.1797         | -0.1796       |
| 1.3582        | 0.3908 | 400  | 1.0344          | -2.2844        | -2.1347          | 0.4505             | -0.1498         | -55.2016       | -54.1729     | -0.3671         | -0.3669       |
| 1.3581        | 0.4397 | 450  | 1.0581          | -2.2666        | -2.0185          | 0.4286             | -0.2481         | -54.0398       | -53.9945     | -0.4232         | -0.4233       |
| 1.398         | 0.4885 | 500  | 1.0994          | -3.1646        | -2.9353          | 0.4110             | -0.2293         | -63.2075       | -62.9742     | -0.6033         | -0.6033       |
| 1.2895        | 0.5374 | 550  | 1.0714          | -2.3198        | -2.0945          | 0.4352             | -0.2252         | -54.8002       | -54.5263     | -0.2667         | -0.2665       |
| 1.2884        | 0.5862 | 600  | 1.3491          | -5.2367        | -5.0465          | 0.4264             | -0.1902         | -84.3200       | -83.6955     | -0.5133         | -0.5133       |
| 0.9758        | 0.6351 | 650  | 1.0323          | -1.9192        | -1.7312          | 0.4396             | -0.1880         | -51.1668       | -50.5202     | -0.2364         | -0.2363       |
| 0.9671        | 0.6839 | 700  | 1.0307          | -1.8280        | -1.6474          | 0.4484             | -0.1806         | -50.3290       | -49.6088     | -0.2707         | -0.2706       |
| 1.1016        | 0.7328 | 750  | 1.0113          | -1.9758        | -1.8284          | 0.4374             | -0.1474         | -52.1388       | -51.0861     | -0.2470         | -0.2469       |
| 1.0075        | 0.7816 | 800  | 0.9896          | -2.0327        | -1.9017          | 0.4462             | -0.1310         | -52.8716       | -51.6551     | -0.2568         | -0.2566       |
| 1.3333        | 0.8305 | 850  | 0.9832          | -1.8654        | -1.7449          | 0.4484             | -0.1205         | -51.3041       | -49.9827     | -0.2344         | -0.2341       |
| 1.0175        | 0.8793 | 900  | 0.9806          | -1.8682        | -1.7465          | 0.4527             | -0.1217         | -51.3197       | -50.0107     | -0.2269         | -0.2267       |
| 1.1061        | 0.9282 | 950  | 0.9806          | -1.8612        | -1.7388          | 0.4462             | -0.1224         | -51.2424       | -49.9402     | -0.2250         | -0.2248       |
| 0.8508        | 0.9770 | 1000 | 0.9802          | -1.8607        | -1.7391          | 0.4505             | -0.1215         | -51.2462       | -49.9353     | -0.2251         | -0.2248       |


### Framework versions

- Transformers 4.41.1
- Pytorch 2.0.0+cu117
- Datasets 2.19.1
- Tokenizers 0.19.1
