---
license: llama3
base_model: tsavage68/MedQA_L3_1000steps_1e6rate_SFT
tags:
- trl
- dpo
- generated_from_trainer
model-index:
- name: MedQA_L3_1000steps_1e7rate_01beta_CSFTDPO
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# MedQA_L3_1000steps_1e7rate_01beta_CSFTDPO

This model is a fine-tuned version of [tsavage68/MedQA_L3_1000steps_1e6rate_SFT](https://huggingface.co/tsavage68/MedQA_L3_1000steps_1e6rate_SFT) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6556
- Rewards/chosen: 0.3104
- Rewards/rejected: 0.2288
- Rewards/accuracies: 0.7187
- Rewards/margins: 0.0816
- Logps/rejected: -31.5670
- Logps/chosen: -28.2248
- Logits/rejected: -0.7354
- Logits/chosen: -0.7346

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
| 0.6932        | 0.0489 | 50   | 0.6927          | -0.0017        | -0.0025          | 0.5297             | 0.0008          | -33.8801       | -31.3453     | -0.7320         | -0.7313       |
| 0.691         | 0.0977 | 100  | 0.6894          | 0.0852         | 0.0776           | 0.6505             | 0.0076          | -33.0791       | -30.4769     | -0.7328         | -0.7321       |
| 0.6779        | 0.1466 | 150  | 0.6824          | 0.1496         | 0.1271           | 0.6791             | 0.0225          | -32.5836       | -29.8325     | -0.7314         | -0.7307       |
| 0.6695        | 0.1954 | 200  | 0.6773          | 0.0689         | 0.0354           | 0.6945             | 0.0335          | -33.5008       | -30.6395     | -0.7313         | -0.7306       |
| 0.6792        | 0.2443 | 250  | 0.6730          | 0.1279         | 0.0855           | 0.7231             | 0.0424          | -32.9998       | -30.0495     | -0.7313         | -0.7306       |
| 0.6641        | 0.2931 | 300  | 0.6678          | 0.1588         | 0.1052           | 0.7297             | 0.0536          | -32.8025       | -29.7403     | -0.7323         | -0.7315       |
| 0.665         | 0.3420 | 350  | 0.6652          | 0.2014         | 0.1419           | 0.7187             | 0.0595          | -32.4354       | -29.3144     | -0.7344         | -0.7336       |
| 0.6504        | 0.3908 | 400  | 0.6621          | 0.2655         | 0.1993           | 0.7363             | 0.0662          | -31.8619       | -28.6732     | -0.7340         | -0.7332       |
| 0.6533        | 0.4397 | 450  | 0.6607          | 0.2838         | 0.2142           | 0.7319             | 0.0697          | -31.7132       | -28.4903     | -0.7347         | -0.7339       |
| 0.66          | 0.4885 | 500  | 0.6588          | 0.3223         | 0.2481           | 0.7187             | 0.0742          | -31.3734       | -28.1056     | -0.7350         | -0.7342       |
| 0.6373        | 0.5374 | 550  | 0.6578          | 0.3176         | 0.2410           | 0.7143             | 0.0766          | -31.4445       | -28.1521     | -0.7355         | -0.7347       |
| 0.6608        | 0.5862 | 600  | 0.6566          | 0.3164         | 0.2373           | 0.7187             | 0.0792          | -31.4823       | -28.1640     | -0.7357         | -0.7349       |
| 0.6457        | 0.6351 | 650  | 0.6560          | 0.3040         | 0.2233           | 0.7187             | 0.0807          | -31.6215       | -28.2882     | -0.7350         | -0.7342       |
| 0.657         | 0.6839 | 700  | 0.6554          | 0.3088         | 0.2267           | 0.7165             | 0.0820          | -31.5874       | -28.2407     | -0.7349         | -0.7341       |
| 0.6597        | 0.7328 | 750  | 0.6560          | 0.3104         | 0.2296           | 0.7187             | 0.0808          | -31.5590       | -28.2246     | -0.7355         | -0.7346       |
| 0.6642        | 0.7816 | 800  | 0.6553          | 0.3115         | 0.2291           | 0.7209             | 0.0824          | -31.5639       | -28.2138     | -0.7353         | -0.7345       |
| 0.673         | 0.8305 | 850  | 0.6555          | 0.3114         | 0.2296           | 0.7231             | 0.0818          | -31.5592       | -28.2146     | -0.7352         | -0.7344       |
| 0.6659        | 0.8793 | 900  | 0.6556          | 0.3142         | 0.2324           | 0.7143             | 0.0818          | -31.5308       | -28.1868     | -0.7357         | -0.7349       |
| 0.6533        | 0.9282 | 950  | 0.6556          | 0.3104         | 0.2288           | 0.7187             | 0.0816          | -31.5668       | -28.2246     | -0.7354         | -0.7346       |
| 0.6255        | 0.9770 | 1000 | 0.6556          | 0.3104         | 0.2288           | 0.7187             | 0.0816          | -31.5670       | -28.2248     | -0.7354         | -0.7346       |


### Framework versions

- Transformers 4.41.1
- Pytorch 2.0.0+cu117
- Datasets 2.19.1
- Tokenizers 0.19.1
