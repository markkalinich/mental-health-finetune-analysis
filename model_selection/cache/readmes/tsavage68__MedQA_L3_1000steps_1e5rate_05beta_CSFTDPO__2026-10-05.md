---
license: llama3
base_model: tsavage68/MedQA_L3_1000steps_1e6rate_SFT
tags:
- trl
- dpo
- generated_from_trainer
model-index:
- name: MedQA_L3_1000steps_1e5rate_05beta_CSFTDPO
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# MedQA_L3_1000steps_1e5rate_05beta_CSFTDPO

This model is a fine-tuned version of [tsavage68/MedQA_L3_1000steps_1e6rate_SFT](https://huggingface.co/tsavage68/MedQA_L3_1000steps_1e6rate_SFT) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 2.7867
- Rewards/chosen: -10.2874
- Rewards/rejected: -9.4675
- Rewards/accuracies: 0.4330
- Rewards/margins: -0.8198
- Logps/rejected: -52.7899
- Logps/chosen: -51.9033
- Logits/rejected: -0.3129
- Logits/chosen: -0.3128

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
| 0.9373        | 0.0489 | 50   | 1.5325          | 0.6891         | -0.1945          | 0.5912             | 0.8836          | -34.2439       | -29.9504     | -1.1200         | -1.1197       |
| 3.7169        | 0.0977 | 100  | 3.7845          | -9.7504        | -8.8431          | 0.4527             | -0.9074         | -51.5409       | -50.8294     | -0.6137         | -0.6138       |
| 5.2014        | 0.1466 | 150  | 5.2600          | -22.3993       | -21.8605         | 0.4681             | -0.5389         | -77.5758       | -76.1272     | -1.3215         | -1.3217       |
| 5.4743        | 0.1954 | 200  | 3.9034          | -7.1491        | -6.2277          | 0.4176             | -0.9214         | -46.3103       | -45.6268     | -0.6483         | -0.6486       |
| 3.0731        | 0.2443 | 250  | 4.1865          | -11.6364       | -10.1791         | 0.4198             | -1.4572         | -54.2131       | -54.6012     | -0.7051         | -0.7056       |
| 5.7952        | 0.2931 | 300  | 3.6683          | -9.2381        | -7.9895          | 0.4264             | -1.2486         | -49.8338       | -49.8046     | -0.4055         | -0.4058       |
| 3.8474        | 0.3420 | 350  | 3.4898          | -12.7687       | -11.9414         | 0.4132             | -0.8274         | -57.7376       | -56.8660     | -0.8625         | -0.8625       |
| 5.5721        | 0.3908 | 400  | 3.4194          | -13.5468       | -12.3658         | 0.4044             | -1.1810         | -58.5864       | -58.4221     | -0.8921         | -0.8922       |
| 6.0929        | 0.4397 | 450  | 3.4518          | -12.5599       | -11.2787         | 0.4132             | -1.2812         | -56.4122       | -56.4483     | -0.6596         | -0.6596       |
| 5.4036        | 0.4885 | 500  | 3.4349          | -13.3250       | -12.3700         | 0.4264             | -0.9550         | -58.5948       | -57.9785     | -0.4398         | -0.4397       |
| 4.2614        | 0.5374 | 550  | 3.4447          | -13.2741       | -12.0523         | 0.4132             | -1.2218         | -57.9595       | -57.8767     | -0.2318         | -0.2318       |
| 5.0683        | 0.5862 | 600  | 3.6325          | -10.9169       | -9.7136          | 0.4242             | -1.2033         | -53.2821       | -53.1624     | 0.0024          | 0.0023        |
| 2.8041        | 0.6351 | 650  | 3.3753          | -13.7510       | -12.4756         | 0.4110             | -1.2754         | -58.8060       | -58.8306     | -0.4253         | -0.4254       |
| 2.852         | 0.6839 | 700  | 3.2123          | -11.3782       | -10.1837         | 0.4132             | -1.1945         | -54.2221       | -54.0849     | -0.3353         | -0.3353       |
| 3.1506        | 0.7328 | 750  | 2.9861          | -10.9246       | -9.9019          | 0.4198             | -1.0227         | -53.6587       | -53.1778     | -0.3577         | -0.3577       |
| 2.9206        | 0.7816 | 800  | 2.8476          | -10.3118       | -9.4465          | 0.4264             | -0.8653         | -52.7479       | -51.9522     | -0.2881         | -0.2880       |
| 3.6047        | 0.8305 | 850  | 2.8115          | -10.1979       | -9.3565          | 0.4308             | -0.8414         | -52.5679       | -51.7243     | -0.3016         | -0.3015       |
| 2.4799        | 0.8793 | 900  | 2.7874          | -10.3005       | -9.4828          | 0.4308             | -0.8177         | -52.8204       | -51.9295     | -0.3147         | -0.3146       |
| 2.8467        | 0.9282 | 950  | 2.7864          | -10.2878       | -9.4711          | 0.4330             | -0.8167         | -52.7969       | -51.9040     | -0.3132         | -0.3130       |
| 2.2638        | 0.9770 | 1000 | 2.7867          | -10.2874       | -9.4675          | 0.4330             | -0.8198         | -52.7899       | -51.9033     | -0.3129         | -0.3128       |


### Framework versions

- Transformers 4.41.1
- Pytorch 2.0.0+cu117
- Datasets 2.19.1
- Tokenizers 0.19.1
