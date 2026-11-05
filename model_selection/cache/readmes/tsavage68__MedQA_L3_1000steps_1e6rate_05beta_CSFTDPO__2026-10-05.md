---
license: llama3
base_model: tsavage68/MedQA_L3_1000steps_1e6rate_SFT
tags:
- trl
- dpo
- generated_from_trainer
model-index:
- name: MedQA_L3_1000steps_1e6rate_03beta_CSFTDPO
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# MedQA_L3_1000steps_1e6rate_03beta_CSFTDPO

This model is a fine-tuned version of [tsavage68/MedQA_L3_1000steps_1e6rate_SFT](https://huggingface.co/tsavage68/MedQA_L3_1000steps_1e6rate_SFT) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5473
- Rewards/chosen: 5.1238
- Rewards/rejected: 0.9227
- Rewards/accuracies: 0.8198
- Rewards/margins: 4.2011
- Logps/rejected: -32.0093
- Logps/chosen: -21.0808
- Logits/rejected: -1.0586
- Logits/chosen: -1.0567

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
| 0.6909        | 0.0489 | 50   | 0.6059          | -0.4307        | -0.6542          | 0.7538             | 0.2235          | -35.1631       | -32.1898     | -0.7254         | -0.7246       |
| 0.4343        | 0.0977 | 100  | 0.7202          | 6.9486         | 5.2431           | 0.6989             | 1.7054          | -23.3686       | -17.4314     | -0.7816         | -0.7804       |
| 0.7011        | 0.1466 | 150  | 0.6146          | 3.7158         | 2.0629           | 0.7407             | 1.6528          | -29.7289       | -23.8970     | -0.8414         | -0.8404       |
| 0.3318        | 0.1954 | 200  | 0.7133          | 3.7895         | 1.2854           | 0.7385             | 2.5041          | -31.2840       | -23.7495     | -0.8346         | -0.8329       |
| 0.4681        | 0.2443 | 250  | 0.5702          | 4.4998         | 2.1458           | 0.7758             | 2.3541          | -29.5633       | -22.3288     | -0.8127         | -0.8116       |
| 0.4446        | 0.2931 | 300  | 0.5104          | 4.3384         | 1.4734           | 0.8022             | 2.8651          | -30.9081       | -22.6517     | -0.9419         | -0.9402       |
| 0.6618        | 0.3420 | 350  | 0.5375          | 4.1100         | 1.1267           | 0.7912             | 2.9833          | -31.6015       | -23.1084     | -1.0095         | -1.0077       |
| 0.6507        | 0.3908 | 400  | 0.4901          | 4.9193         | 1.9906           | 0.8088             | 2.9288          | -29.8737       | -21.4898     | -1.0601         | -1.0586       |
| 0.6922        | 0.4397 | 450  | 0.5171          | 4.9828         | 1.7479           | 0.8088             | 3.2350          | -30.3591       | -21.3628     | -1.0672         | -1.0656       |
| 1.0069        | 0.4885 | 500  | 0.5208          | 5.1851         | 1.8633           | 0.8154             | 3.3218          | -30.1282       | -20.9583     | -1.0738         | -1.0722       |
| 0.3449        | 0.5374 | 550  | 0.5287          | 4.7906         | 1.3304           | 0.8022             | 3.4602          | -31.1941       | -21.7474     | -1.0809         | -1.0794       |
| 0.5353        | 0.5862 | 600  | 0.5222          | 4.7907         | 1.0268           | 0.8242             | 3.7639          | -31.8012       | -21.7471     | -1.0774         | -1.0757       |
| 0.5161        | 0.6351 | 650  | 0.5463          | 5.2594         | 1.2353           | 0.8176             | 4.0241          | -31.3842       | -20.8097     | -1.0613         | -1.0595       |
| 0.3686        | 0.6839 | 700  | 0.5430          | 5.0821         | 0.9881           | 0.8154             | 4.0939          | -31.8786       | -21.1644     | -1.0604         | -1.0585       |
| 0.4533        | 0.7328 | 750  | 0.5497          | 5.2255         | 1.0741           | 0.8286             | 4.1513          | -31.7065       | -20.8775     | -1.0601         | -1.0582       |
| 0.4364        | 0.7816 | 800  | 0.5480          | 5.1239         | 0.9444           | 0.8198             | 4.1795          | -31.9660       | -21.0807     | -1.0600         | -1.0581       |
| 0.6738        | 0.8305 | 850  | 0.5512          | 5.1510         | 0.9491           | 0.8198             | 4.2019          | -31.9565       | -21.0265     | -1.0594         | -1.0575       |
| 0.7741        | 0.8793 | 900  | 0.5493          | 5.1296         | 0.9313           | 0.8220             | 4.1983          | -31.9922       | -21.0693     | -1.0588         | -1.0569       |
| 0.4633        | 0.9282 | 950  | 0.5498          | 5.1295         | 0.9317           | 0.8220             | 4.1978          | -31.9914       | -21.0696     | -1.0587         | -1.0568       |
| 0.1659        | 0.9770 | 1000 | 0.5473          | 5.1238         | 0.9227           | 0.8198             | 4.2011          | -32.0093       | -21.0808     | -1.0586         | -1.0567       |


### Framework versions

- Transformers 4.41.1
- Pytorch 2.0.0+cu117
- Datasets 2.19.1
- Tokenizers 0.19.1
