---
license: apache-2.0
base_model: bert-base-uncased
tags:
- generated_from_trainer
datasets:
- ktgiahieu/maccrobat2018_2020
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: BioMedical_NER-maccrobat-bert
  results: []
widget:
- text: "CASE: A 28-year-old previously healthy man presented with a 6-week history of palpitations.
The symptoms occurred during rest, 2–3 times per week, lasted up to 30 minutes at a time and were associated with dyspnea.
Except for a grade 2/6 holosystolic tricuspid regurgitation murmur (best heard at the left sternal border with inspiratory accentuation), physical examination yielded unremarkable findings."
  example_title: "example 1"
- text: "A 63-year-old woman with no known cardiac history presented with a sudden onset of dyspnea requiring intubation and ventilatory support out of hospital.
She denied preceding symptoms of chest discomfort, palpitations, syncope or infection.
The patient was afebrile and normotensive, with a sinus tachycardia of 140 beats/min."
  example_title: "example 2"
- text: "A 48 year-old female presented with vaginal bleeding and abnormal Pap smears.
Upon diagnosis of invasive non-keratinizing SCC of the cervix, she underwent a radical hysterectomy with salpingo-oophorectomy which demonstrated positive spread to the pelvic lymph nodes and the parametrium.
Pathological examination revealed that the tumour also extensively involved the lower uterine segment."
  example_title: "example 3"
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# BioMedical_NER-maccrobat-bert

This model is a fine-tuned version of [bert-base-uncased](https://huggingface.co/bert-base-uncased) on [maccrobat2018_2020](https://huggingface.co/datasets/ktgiahieu/maccrobat2018_2020) dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3418
- Precision: 0.8668
- Recall: 0.9491
- F1: 0.9061
- Accuracy: 0.9501

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 50

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 1.0   | 45   | 1.7363          | 0.4262    | 0.0055 | 0.0108 | 0.6274   |
| No log        | 2.0   | 90   | 1.3805          | 0.3534    | 0.2073 | 0.2613 | 0.6565   |
| No log        | 3.0   | 135  | 1.1713          | 0.4026    | 0.3673 | 0.3841 | 0.6908   |
| No log        | 4.0   | 180  | 1.0551          | 0.4392    | 0.5309 | 0.4807 | 0.7149   |
| No log        | 5.0   | 225  | 0.9591          | 0.4893    | 0.6012 | 0.5395 | 0.7496   |
| No log        | 6.0   | 270  | 0.8656          | 0.5156    | 0.6483 | 0.5744 | 0.7722   |
| No log        | 7.0   | 315  | 0.8613          | 0.5124    | 0.6871 | 0.5870 | 0.7716   |
| No log        | 8.0   | 360  | 0.7524          | 0.5699    | 0.7114 | 0.6329 | 0.8110   |
| No log        | 9.0   | 405  | 0.6966          | 0.5884    | 0.7374 | 0.6545 | 0.8265   |
| No log        | 10.0  | 450  | 0.6564          | 0.6147    | 0.7678 | 0.6827 | 0.8373   |
| No log        | 11.0  | 495  | 0.5950          | 0.6484    | 0.7826 | 0.7092 | 0.8563   |
| 0.9321        | 12.0  | 540  | 0.6083          | 0.6578    | 0.8001 | 0.7220 | 0.8587   |
| 0.9321        | 13.0  | 585  | 0.5821          | 0.6682    | 0.8206 | 0.7366 | 0.8688   |
| 0.9321        | 14.0  | 630  | 0.5578          | 0.6787    | 0.8324 | 0.7477 | 0.8744   |
| 0.9321        | 15.0  | 675  | 0.4819          | 0.7338    | 0.8484 | 0.7870 | 0.8974   |
| 0.9321        | 16.0  | 720  | 0.4775          | 0.7461    | 0.8573 | 0.7978 | 0.9020   |
| 0.9321        | 17.0  | 765  | 0.4786          | 0.7395    | 0.8600 | 0.7952 | 0.9020   |
| 0.9321        | 18.0  | 810  | 0.4481          | 0.7647    | 0.8740 | 0.8157 | 0.9102   |
| 0.9321        | 19.0  | 855  | 0.4597          | 0.7638    | 0.8799 | 0.8177 | 0.9108   |
| 0.9321        | 20.0  | 900  | 0.4551          | 0.7617    | 0.8835 | 0.8181 | 0.9096   |
| 0.9321        | 21.0  | 945  | 0.4365          | 0.7698    | 0.8873 | 0.8244 | 0.9142   |
| 0.9321        | 22.0  | 990  | 0.3993          | 0.7986    | 0.8957 | 0.8444 | 0.9247   |
| 0.2115        | 23.0  | 1035 | 0.4162          | 0.7950    | 0.9014 | 0.8449 | 0.9234   |
| 0.2115        | 24.0  | 1080 | 0.4188          | 0.8007    | 0.9042 | 0.8493 | 0.9248   |
| 0.2115        | 25.0  | 1125 | 0.3996          | 0.8105    | 0.9103 | 0.8575 | 0.9291   |
| 0.2115        | 26.0  | 1170 | 0.3775          | 0.8226    | 0.9134 | 0.8657 | 0.9333   |
| 0.2115        | 27.0  | 1215 | 0.3656          | 0.8297    | 0.9187 | 0.8720 | 0.9364   |
| 0.2115        | 28.0  | 1260 | 0.3744          | 0.8323    | 0.9217 | 0.8747 | 0.9371   |
| 0.2115        | 29.0  | 1305 | 0.3763          | 0.8296    | 0.9229 | 0.8738 | 0.9364   |
| 0.2115        | 30.0  | 1350 | 0.3506          | 0.8454    | 0.9272 | 0.8844 | 0.9414   |
| 0.2115        | 31.0  | 1395 | 0.3602          | 0.8441    | 0.9301 | 0.8850 | 0.9413   |
| 0.2115        | 32.0  | 1440 | 0.3617          | 0.8359    | 0.9303 | 0.8806 | 0.9400   |
| 0.2115        | 33.0  | 1485 | 0.3737          | 0.8352    | 0.9310 | 0.8805 | 0.9388   |
| 0.0818        | 34.0  | 1530 | 0.3541          | 0.8477    | 0.9352 | 0.8893 | 0.9438   |
| 0.0818        | 35.0  | 1575 | 0.3553          | 0.8487    | 0.9377 | 0.8910 | 0.9439   |
| 0.0818        | 36.0  | 1620 | 0.3583          | 0.8476    | 0.9367 | 0.8899 | 0.9438   |
| 0.0818        | 37.0  | 1665 | 0.3318          | 0.8642    | 0.9400 | 0.9005 | 0.9484   |
| 0.0818        | 38.0  | 1710 | 0.3449          | 0.8598    | 0.9409 | 0.8985 | 0.9471   |
| 0.0818        | 39.0  | 1755 | 0.3466          | 0.8591    | 0.9419 | 0.8986 | 0.9468   |
| 0.0818        | 40.0  | 1800 | 0.3494          | 0.8591    | 0.9426 | 0.8989 | 0.9473   |
| 0.0818        | 41.0  | 1845 | 0.3494          | 0.8591    | 0.9451 | 0.9001 | 0.9475   |
| 0.0818        | 42.0  | 1890 | 0.3545          | 0.8588    | 0.9462 | 0.9004 | 0.9477   |
| 0.0818        | 43.0  | 1935 | 0.3569          | 0.8599    | 0.9460 | 0.9009 | 0.9470   |
| 0.0818        | 44.0  | 1980 | 0.3465          | 0.8645    | 0.9468 | 0.9038 | 0.9492   |
| 0.0469        | 45.0  | 2025 | 0.3424          | 0.8663    | 0.9489 | 0.9057 | 0.9498   |
| 0.0469        | 46.0  | 2070 | 0.3460          | 0.8643    | 0.9481 | 0.9043 | 0.9490   |
| 0.0469        | 47.0  | 2115 | 0.3445          | 0.8658    | 0.9483 | 0.9052 | 0.9496   |
| 0.0469        | 48.0  | 2160 | 0.3387          | 0.8701    | 0.9500 | 0.9083 | 0.9508   |
| 0.0469        | 49.0  | 2205 | 0.3432          | 0.8671    | 0.9491 | 0.9063 | 0.9501   |
| 0.0469        | 50.0  | 2250 | 0.3418          | 0.8668    | 0.9491 | 0.9061 | 0.9501   |


### Framework versions

- Transformers 4.32.1
- Pytorch 2.0.1+cu118
- Datasets 2.14.4
- Tokenizers 0.13.3
