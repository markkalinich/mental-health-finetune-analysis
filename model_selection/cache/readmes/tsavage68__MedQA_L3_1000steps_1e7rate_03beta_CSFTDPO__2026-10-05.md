---
license: llama3
base_model: tsavage68/MedQA_L3_1000steps_1e6rate_SFT
tags:
- trl
- dpo
- generated_from_trainer
model-index:
- name: MedQA_L3_1000steps_1e7rate_03beta_CSFTDPO
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# MedQA_L3_1000steps_1e7rate_03beta_CSFTDPO

This model is a fine-tuned version of [tsavage68/MedQA_L3_1000steps_1e6rate_SFT](https://huggingface.co/tsavage68/MedQA_L3_1000steps_1e6rate_SFT) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6020
- Rewards/chosen: 0.7087
- Rewards/rejected: 0.4830
- Rewards/accuracies: 0.7341
- Rewards/margins: 0.2257
- Logps/rejected: -32.2447
- Logps/chosen: -28.9661
- Logits/rejected: -0.7358
- Logits/chosen: -0.7350

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
| 0.6925        | 0.0489 | 50   | 0.6930          | -0.0016        | -0.0023          | 0.5011             | 0.0007          | -33.8624       | -31.3338     | -0.7320         | -0.7314       |
| 0.6841        | 0.0977 | 100  | 0.6807          | 0.2459         | 0.2195           | 0.6549             | 0.0264          | -33.1233       | -30.5088     | -0.7330         | -0.7323       |
| 0.6562        | 0.1466 | 150  | 0.6641          | 0.3800         | 0.3137           | 0.6791             | 0.0663          | -32.8092       | -30.0619     | -0.7310         | -0.7303       |
| 0.6334        | 0.1954 | 200  | 0.6509          | 0.1334         | 0.0355           | 0.7165             | 0.0979          | -33.7366       | -30.8837     | -0.7311         | -0.7304       |
| 0.6544        | 0.2443 | 250  | 0.6415          | 0.2943         | 0.1754           | 0.7209             | 0.1189          | -33.2701       | -30.3474     | -0.7311         | -0.7303       |
| 0.6145        | 0.2931 | 300  | 0.6304          | 0.3548         | 0.2099           | 0.7385             | 0.1448          | -33.1550       | -30.1459     | -0.7317         | -0.7310       |
| 0.6171        | 0.3420 | 350  | 0.6223          | 0.4756         | 0.3093           | 0.7341             | 0.1663          | -32.8238       | -29.7432     | -0.7336         | -0.7328       |
| 0.5911        | 0.3908 | 400  | 0.6181          | 0.6387         | 0.4602           | 0.7121             | 0.1785          | -32.3208       | -29.1996     | -0.7334         | -0.7327       |
| 0.5942        | 0.4397 | 450  | 0.6129          | 0.6839         | 0.4904           | 0.7253             | 0.1935          | -32.2203       | -29.0489     | -0.7347         | -0.7339       |
| 0.6096        | 0.4885 | 500  | 0.6090          | 0.7785         | 0.5741           | 0.7297             | 0.2044          | -31.9411       | -28.7335     | -0.7351         | -0.7343       |
| 0.5671        | 0.5374 | 550  | 0.6068          | 0.7522         | 0.5395           | 0.7275             | 0.2127          | -32.0566       | -28.8212     | -0.7355         | -0.7347       |
| 0.6066        | 0.5862 | 600  | 0.6061          | 0.7215         | 0.5067           | 0.7209             | 0.2147          | -32.1657       | -28.9236     | -0.7356         | -0.7348       |
| 0.5816        | 0.6351 | 650  | 0.6046          | 0.6882         | 0.4692           | 0.7231             | 0.2191          | -32.2910       | -29.0344     | -0.7356         | -0.7348       |
| 0.5968        | 0.6839 | 700  | 0.6030          | 0.6956         | 0.4723           | 0.7451             | 0.2233          | -32.2804       | -29.0097     | -0.7352         | -0.7344       |
| 0.6132        | 0.7328 | 750  | 0.6042          | 0.7103         | 0.4891           | 0.7297             | 0.2212          | -32.2246       | -28.9608     | -0.7354         | -0.7346       |
| 0.6133        | 0.7816 | 800  | 0.6021          | 0.6956         | 0.4697           | 0.7407             | 0.2258          | -32.2890       | -29.0099     | -0.7358         | -0.7350       |
| 0.6397        | 0.8305 | 850  | 0.6029          | 0.7027         | 0.4791           | 0.7341             | 0.2236          | -32.2579       | -28.9862     | -0.7354         | -0.7346       |
| 0.6273        | 0.8793 | 900  | 0.6030          | 0.7126         | 0.4896           | 0.7341             | 0.2230          | -32.2229       | -28.9533     | -0.7356         | -0.7348       |
| 0.5996        | 0.9282 | 950  | 0.6019          | 0.7087         | 0.4830           | 0.7341             | 0.2257          | -32.2447       | -28.9661     | -0.7358         | -0.7350       |
| 0.5319        | 0.9770 | 1000 | 0.6020          | 0.7087         | 0.4830           | 0.7341             | 0.2257          | -32.2447       | -28.9661     | -0.7358         | -0.7350       |


### Framework versions

- Transformers 4.41.1
- Pytorch 2.0.0+cu117
- Datasets 2.19.1
- Tokenizers 0.19.1
