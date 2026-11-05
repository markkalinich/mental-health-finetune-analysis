---
license: llama3
base_model: tsavage68/MedQA_L3_1000steps_1e6rate_SFT
tags:
- trl
- dpo
- generated_from_trainer
model-index:
- name: MedQA_L3_1000steps_1e6rate_01beta_CSFTDPO
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# MedQA_L3_1000steps_1e6rate_01beta_CSFTDPO

This model is a fine-tuned version of [tsavage68/MedQA_L3_1000steps_1e6rate_SFT](https://huggingface.co/tsavage68/MedQA_L3_1000steps_1e6rate_SFT) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4143
- Rewards/chosen: -0.2461
- Rewards/rejected: -2.6298
- Rewards/accuracies: 0.8088
- Rewards/margins: 2.3838
- Logps/rejected: -60.1531
- Logps/chosen: -33.7891
- Logits/rejected: -1.3940
- Logits/chosen: -1.3910

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
| 0.6869        | 0.0489 | 50   | 0.6696          | -0.2211        | -0.2710          | 0.7253             | 0.0498          | -36.5645       | -33.5400     | -0.7298         | -0.7290       |
| 0.4779        | 0.0977 | 100  | 0.5887          | 1.4526         | 1.0417           | 0.6945             | 0.4109          | -23.4374       | -16.8024     | -0.8047         | -0.8036       |
| 0.5752        | 0.1466 | 150  | 0.4975          | 0.5331         | -0.2997          | 0.7473             | 0.8328          | -36.8518       | -25.9976     | -0.8723         | -0.8705       |
| 0.4157        | 0.1954 | 200  | 0.5087          | -0.0815        | -1.0065          | 0.7538             | 0.9250          | -43.9199       | -32.1434     | -0.9039         | -0.9019       |
| 0.4271        | 0.2443 | 250  | 0.4619          | 0.5202         | -0.5333          | 0.7648             | 1.0535          | -39.1874       | -26.1265     | -0.9341         | -0.9319       |
| 0.3162        | 0.2931 | 300  | 0.4272          | 0.2052         | -1.3157          | 0.8110             | 1.5209          | -47.0122       | -29.2765     | -1.0303         | -1.0281       |
| 0.3868        | 0.3420 | 350  | 0.4366          | 0.0191         | -1.4354          | 0.7868             | 1.4545          | -48.2090       | -31.1376     | -1.1172         | -1.1146       |
| 0.4267        | 0.3908 | 400  | 0.4253          | 0.8142         | -0.6501          | 0.8044             | 1.4642          | -40.3556       | -23.1869     | -1.2091         | -1.2069       |
| 0.4816        | 0.4397 | 450  | 0.4235          | 0.7057         | -0.6954          | 0.7978             | 1.4011          | -40.8093       | -24.2719     | -1.2618         | -1.2590       |
| 0.5777        | 0.4885 | 500  | 0.4147          | 0.5199         | -1.2061          | 0.8088             | 1.7260          | -45.9158       | -26.1293     | -1.3148         | -1.3119       |
| 0.3051        | 0.5374 | 550  | 0.4133          | 0.2933         | -1.3715          | 0.8022             | 1.6647          | -47.5694       | -28.3956     | -1.3646         | -1.3616       |
| 0.5378        | 0.5862 | 600  | 0.4219          | -0.4403        | -2.6925          | 0.8088             | 2.2522          | -60.7803       | -35.7319     | -1.3525         | -1.3496       |
| 0.359         | 0.6351 | 650  | 0.4122          | -0.0585        | -2.2242          | 0.8132             | 2.1656          | -56.0965       | -31.9139     | -1.3793         | -1.3763       |
| 0.4137        | 0.6839 | 700  | 0.4019          | 0.0561         | -2.0220          | 0.8066             | 2.0781          | -54.0746       | -30.7675     | -1.3921         | -1.3890       |
| 0.3899        | 0.7328 | 750  | 0.4093          | -0.1488        | -2.4231          | 0.8110             | 2.2743          | -58.0863       | -32.8165     | -1.3920         | -1.3890       |
| 0.3645        | 0.7816 | 800  | 0.4095          | -0.2104        | -2.5505          | 0.8132             | 2.3401          | -59.3594       | -33.4322     | -1.3965         | -1.3935       |
| 0.4993        | 0.8305 | 850  | 0.4157          | -0.2412        | -2.6172          | 0.8088             | 2.3760          | -60.0272       | -33.7410     | -1.3947         | -1.3918       |
| 0.6907        | 0.8793 | 900  | 0.4164          | -0.2462        | -2.6292          | 0.8110             | 2.3829          | -60.1466       | -33.7908     | -1.3944         | -1.3914       |
| 0.3846        | 0.9282 | 950  | 0.4140          | -0.2447        | -2.6315          | 0.8110             | 2.3868          | -60.1702       | -33.7755     | -1.3939         | -1.3909       |
| 0.3404        | 0.9770 | 1000 | 0.4143          | -0.2461        | -2.6298          | 0.8088             | 2.3838          | -60.1531       | -33.7891     | -1.3940         | -1.3910       |


### Framework versions

- Transformers 4.41.1
- Pytorch 2.0.0+cu117
- Datasets 2.19.1
- Tokenizers 0.19.1
