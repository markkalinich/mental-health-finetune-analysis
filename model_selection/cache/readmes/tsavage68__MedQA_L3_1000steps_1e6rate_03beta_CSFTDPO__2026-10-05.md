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
- Loss: 0.4310
- Rewards/chosen: 2.8905
- Rewards/rejected: 0.0317
- Rewards/accuracies: 0.8264
- Rewards/margins: 2.8588
- Logps/rejected: -33.7491
- Logps/chosen: -21.6935
- Logits/rejected: -1.0851
- Logits/chosen: -1.0825

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
| 0.685         | 0.0489 | 50   | 0.6334          | -0.7936        | -0.9359          | 0.7363             | 0.1423          | -36.9746       | -33.9739     | -0.7278         | -0.7271       |
| 0.4052        | 0.0977 | 100  | 0.6106          | 3.7995         | 2.4858           | 0.6945             | 1.3137          | -25.5688       | -18.6634     | -0.7922         | -0.7909       |
| 0.6321        | 0.1466 | 150  | 0.5384          | 2.8483         | 1.6055           | 0.7538             | 1.2428          | -28.5030       | -21.8341     | -0.8459         | -0.8447       |
| 0.3156        | 0.1954 | 200  | 0.5868          | 2.1271         | 0.4376           | 0.7407             | 1.6895          | -32.3962       | -24.2382     | -0.8621         | -0.8602       |
| 0.3344        | 0.2443 | 250  | 0.4933          | 2.5832         | 0.3834           | 0.7824             | 2.1997          | -32.5767       | -22.7179     | -0.8632         | -0.8616       |
| 0.4058        | 0.2931 | 300  | 0.4765          | 2.1119         | -0.2236          | 0.8000             | 2.3354          | -34.6000       | -24.2889     | -0.9125         | -0.9102       |
| 0.5311        | 0.3420 | 350  | 0.4711          | 3.6592         | 1.7891           | 0.7978             | 1.8701          | -27.8913       | -19.1312     | -0.9957         | -0.9939       |
| 0.479         | 0.3908 | 400  | 0.4337          | 3.0010         | 0.8751           | 0.7824             | 2.1260          | -30.9380       | -21.3251     | -1.0345         | -1.0327       |
| 0.573         | 0.4397 | 450  | 0.4394          | 2.5507         | 0.4211           | 0.8022             | 2.1296          | -32.4512       | -22.8262     | -1.0418         | -1.0398       |
| 0.6634        | 0.4885 | 500  | 0.4321          | 3.2654         | 0.8717           | 0.8132             | 2.3938          | -30.9492       | -20.4437     | -1.0854         | -1.0833       |
| 0.3697        | 0.5374 | 550  | 0.4301          | 2.6205         | 0.1723           | 0.8154             | 2.4482          | -33.2805       | -22.5936     | -1.0958         | -1.0937       |
| 0.3885        | 0.5862 | 600  | 0.4183          | 2.6945         | 0.1151           | 0.8308             | 2.5794          | -33.4712       | -22.3469     | -1.0962         | -1.0938       |
| 0.3881        | 0.6351 | 650  | 0.4274          | 2.9139         | 0.1880           | 0.8176             | 2.7259          | -33.2283       | -21.6156     | -1.0865         | -1.0841       |
| 0.3716        | 0.6839 | 700  | 0.4210          | 2.5828         | -0.1081          | 0.8198             | 2.6908          | -34.2150       | -22.7192     | -1.0921         | -1.0896       |
| 0.3551        | 0.7328 | 750  | 0.4259          | 2.8154         | 0.0217           | 0.8286             | 2.7936          | -33.7823       | -21.9439     | -1.0879         | -1.0854       |
| 0.3479        | 0.7816 | 800  | 0.4277          | 2.8533         | 0.0183           | 0.8286             | 2.8350          | -33.7940       | -21.8176     | -1.0873         | -1.0848       |
| 0.5329        | 0.8305 | 850  | 0.4294          | 2.8955         | 0.0400           | 0.8264             | 2.8556          | -33.7217       | -21.6767     | -1.0854         | -1.0829       |
| 0.5049        | 0.8793 | 900  | 0.4309          | 2.8795         | 0.0259           | 0.8242             | 2.8536          | -33.7685       | -21.7303     | -1.0849         | -1.0824       |
| 0.3206        | 0.9282 | 950  | 0.4285          | 2.8888         | 0.0248           | 0.8220             | 2.8640          | -33.7722       | -21.6991     | -1.0845         | -1.0820       |
| 0.2356        | 0.9770 | 1000 | 0.4310          | 2.8905         | 0.0317           | 0.8264             | 2.8588          | -33.7491       | -21.6935     | -1.0851         | -1.0825       |


### Framework versions

- Transformers 4.41.1
- Pytorch 2.0.0+cu117
- Datasets 2.19.1
- Tokenizers 0.19.1
