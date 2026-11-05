---
license: llama3
base_model: tsavage68/MedQA_L3_1000steps_1e6rate_SFT
tags:
- trl
- dpo
- generated_from_trainer
model-index:
- name: MedQA_L3_1000steps_1e7rate_05beta_CSFTDPO
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# MedQA_L3_1000steps_1e7rate_05beta_CSFTDPO

This model is a fine-tuned version of [tsavage68/MedQA_L3_1000steps_1e6rate_SFT](https://huggingface.co/tsavage68/MedQA_L3_1000steps_1e6rate_SFT) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5679
- Rewards/chosen: 0.9256
- Rewards/rejected: 0.5812
- Rewards/accuracies: 0.7407
- Rewards/margins: 0.3444
- Logps/rejected: -32.6925
- Logps/chosen: -29.4774
- Logits/rejected: -0.7357
- Logits/chosen: -0.7349

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-07
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
| 0.6857        | 0.0489 | 50   | 0.6947          | -0.0249        | -0.0232          | 0.4879             | -0.0018         | -33.9011       | -31.3784     | -0.7318         | -0.7312       |
| 0.6799        | 0.0977 | 100  | 0.6734          | 0.3881         | 0.3450           | 0.6681             | 0.0432          | -33.1649       | -30.5522     | -0.7330         | -0.7323       |
| 0.6275        | 0.1466 | 150  | 0.6484          | 0.5732         | 0.4639           | 0.6813             | 0.1093          | -32.9271       | -30.1822     | -0.7310         | -0.7303       |
| 0.5934        | 0.1954 | 200  | 0.6321          | 0.1707         | 0.0172           | 0.6989             | 0.1535          | -33.8203       | -30.9871     | -0.7310         | -0.7303       |
| 0.6358        | 0.2443 | 250  | 0.6181          | 0.4355         | 0.2501           | 0.7253             | 0.1854          | -33.3546       | -30.4574     | -0.7315         | -0.7308       |
| 0.5727        | 0.2931 | 300  | 0.6007          | 0.5633         | 0.3322           | 0.7429             | 0.2311          | -33.1904       | -30.2020     | -0.7321         | -0.7314       |
| 0.5786        | 0.3420 | 350  | 0.5923          | 0.7025         | 0.4439           | 0.7407             | 0.2586          | -32.9670       | -29.9235     | -0.7343         | -0.7335       |
| 0.545         | 0.3908 | 400  | 0.5830          | 0.9347         | 0.6493           | 0.7385             | 0.2854          | -32.5562       | -29.4591     | -0.7336         | -0.7328       |
| 0.5497        | 0.4397 | 450  | 0.5795          | 0.9735         | 0.6722           | 0.7385             | 0.3014          | -32.5105       | -29.3814     | -0.7346         | -0.7338       |
| 0.5857        | 0.4885 | 500  | 0.5781          | 1.0925         | 0.7817           | 0.7407             | 0.3108          | -32.2914       | -29.1435     | -0.7356         | -0.7348       |
| 0.5168        | 0.5374 | 550  | 0.5714          | 1.0244         | 0.6925           | 0.7385             | 0.3319          | -32.4698       | -29.2796     | -0.7358         | -0.7350       |
| 0.567         | 0.5862 | 600  | 0.5699          | 0.9715         | 0.6353           | 0.7407             | 0.3362          | -32.5842       | -29.3855     | -0.7356         | -0.7349       |
| 0.5375        | 0.6351 | 650  | 0.5689          | 0.9102         | 0.5695           | 0.7429             | 0.3407          | -32.7158       | -29.5081     | -0.7357         | -0.7349       |
| 0.5541        | 0.6839 | 700  | 0.5698          | 0.9277         | 0.5885           | 0.7385             | 0.3391          | -32.6778       | -29.4732     | -0.7359         | -0.7351       |
| 0.5824        | 0.7328 | 750  | 0.5693          | 0.9133         | 0.5709           | 0.7516             | 0.3424          | -32.7129       | -29.5019     | -0.7358         | -0.7350       |
| 0.5769        | 0.7816 | 800  | 0.5684          | 0.9103         | 0.5658           | 0.7429             | 0.3444          | -32.7232       | -29.5080     | -0.7354         | -0.7346       |
| 0.6223        | 0.8305 | 850  | 0.5678          | 0.9317         | 0.5868           | 0.7473             | 0.3449          | -32.6812       | -29.4651     | -0.7360         | -0.7352       |
| 0.5968        | 0.8793 | 900  | 0.5687          | 0.9231         | 0.5807           | 0.7385             | 0.3424          | -32.6935       | -29.4824     | -0.7361         | -0.7353       |
| 0.5673        | 0.9282 | 950  | 0.5678          | 0.9259         | 0.5813           | 0.7407             | 0.3446          | -32.6921       | -29.4767     | -0.7357         | -0.7349       |
| 0.4742        | 0.9770 | 1000 | 0.5679          | 0.9256         | 0.5812           | 0.7407             | 0.3444          | -32.6925       | -29.4774     | -0.7357         | -0.7349       |


### Framework versions

- Transformers 4.41.1
- Pytorch 2.0.0+cu117
- Datasets 2.19.1
- Tokenizers 0.19.1
