---
license: apache-2.0
base_model: distilbert-base-uncased
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
- name: BioMedical_NER-maccrobat-distilbert
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

# BioMedical_NER-maccrobat-distilbert

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on [maccrobat2018_2020](https://huggingface.co/datasets/ktgiahieu/maccrobat2018_2020) dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3418
- Precision: 0.8858
- Recall: 0.9578
- F1: 0.9204
- Accuracy: 0.9541

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
- num_epochs: 70

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 1.0   | 45   | 1.8297          | 0.0       | 0.0    | 0.0    | 0.6197   |
| No log        | 2.0   | 90   | 1.5738          | 0.2713    | 0.0490 | 0.0830 | 0.6324   |
| No log        | 3.0   | 135  | 1.3283          | 0.3165    | 0.2269 | 0.2644 | 0.6654   |
| No log        | 4.0   | 180  | 1.1738          | 0.3634    | 0.3538 | 0.3585 | 0.6915   |
| No log        | 5.0   | 225  | 1.1003          | 0.4080    | 0.5041 | 0.4510 | 0.7074   |
| No log        | 6.0   | 270  | 1.0484          | 0.4339    | 0.5727 | 0.4937 | 0.7193   |
| No log        | 7.0   | 315  | 0.9841          | 0.4685    | 0.6209 | 0.5340 | 0.7434   |
| No log        | 8.0   | 360  | 0.8765          | 0.5286    | 0.6369 | 0.5777 | 0.7712   |
| No log        | 9.0   | 405  | 0.8037          | 0.5638    | 0.6635 | 0.6096 | 0.7922   |
| No log        | 10.0  | 450  | 0.7924          | 0.5572    | 0.7013 | 0.6210 | 0.8008   |
| No log        | 11.0  | 495  | 0.7403          | 0.5732    | 0.7228 | 0.6394 | 0.8143   |
| 1.0716        | 12.0  | 540  | 0.6235          | 0.6636    | 0.7083 | 0.6852 | 0.8457   |
| 1.0716        | 13.0  | 585  | 0.6182          | 0.6418    | 0.7448 | 0.6895 | 0.8487   |
| 1.0716        | 14.0  | 630  | 0.6498          | 0.6312    | 0.7724 | 0.6947 | 0.8456   |
| 1.0716        | 15.0  | 675  | 0.5830          | 0.6638    | 0.7874 | 0.7204 | 0.8650   |
| 1.0716        | 16.0  | 720  | 0.5199          | 0.6992    | 0.7954 | 0.7442 | 0.8804   |
| 1.0716        | 17.0  | 765  | 0.5470          | 0.7129    | 0.8119 | 0.7592 | 0.8836   |
| 1.0716        | 18.0  | 810  | 0.5065          | 0.7269    | 0.8318 | 0.7758 | 0.8920   |
| 1.0716        | 19.0  | 855  | 0.4645          | 0.7521    | 0.8353 | 0.7916 | 0.9018   |
| 1.0716        | 20.0  | 900  | 0.5204          | 0.7240    | 0.8501 | 0.7820 | 0.8915   |
| 1.0716        | 21.0  | 945  | 0.4383          | 0.7660    | 0.8495 | 0.8056 | 0.9078   |
| 1.0716        | 22.0  | 990  | 0.4345          | 0.7659    | 0.8662 | 0.8130 | 0.9127   |
| 0.2987        | 23.0  | 1035 | 0.4492          | 0.7675    | 0.8733 | 0.8170 | 0.9118   |
| 0.2987        | 24.0  | 1080 | 0.4654          | 0.7691    | 0.8805 | 0.8211 | 0.9101   |
| 0.2987        | 25.0  | 1125 | 0.4186          | 0.7995    | 0.8778 | 0.8368 | 0.9216   |
| 0.2987        | 26.0  | 1170 | 0.3898          | 0.8131    | 0.8871 | 0.8485 | 0.9269   |
| 0.2987        | 27.0  | 1215 | 0.4057          | 0.8041    | 0.8928 | 0.8461 | 0.9256   |
| 0.2987        | 28.0  | 1260 | 0.3916          | 0.8156    | 0.8938 | 0.8529 | 0.9290   |
| 0.2987        | 29.0  | 1305 | 0.3771          | 0.8250    | 0.8989 | 0.8604 | 0.9317   |
| 0.2987        | 30.0  | 1350 | 0.3690          | 0.8253    | 0.8997 | 0.8609 | 0.9337   |
| 0.2987        | 31.0  | 1395 | 0.3716          | 0.8320    | 0.9084 | 0.8685 | 0.9357   |
| 0.2987        | 32.0  | 1440 | 0.3764          | 0.8278    | 0.9115 | 0.8677 | 0.9349   |
| 0.2987        | 33.0  | 1485 | 0.3549          | 0.8389    | 0.9113 | 0.8736 | 0.9376   |
| 0.1133        | 34.0  | 1530 | 0.3715          | 0.8368    | 0.9160 | 0.8746 | 0.9372   |
| 0.1133        | 35.0  | 1575 | 0.3621          | 0.8452    | 0.9208 | 0.8814 | 0.9401   |
| 0.1133        | 36.0  | 1620 | 0.3533          | 0.8489    | 0.9248 | 0.8852 | 0.9420   |
| 0.1133        | 37.0  | 1665 | 0.3471          | 0.8540    | 0.9259 | 0.8885 | 0.9427   |
| 0.1133        | 38.0  | 1710 | 0.3492          | 0.8504    | 0.9263 | 0.8867 | 0.9423   |
| 0.1133        | 39.0  | 1755 | 0.3570          | 0.8572    | 0.9327 | 0.8933 | 0.9441   |
| 0.1133        | 40.0  | 1800 | 0.3647          | 0.8535    | 0.9348 | 0.8923 | 0.9436   |
| 0.1133        | 41.0  | 1845 | 0.3500          | 0.8656    | 0.9381 | 0.9004 | 0.9466   |
| 0.1133        | 42.0  | 1890 | 0.3570          | 0.8594    | 0.9405 | 0.8981 | 0.9452   |
| 0.1133        | 43.0  | 1935 | 0.3545          | 0.8695    | 0.9436 | 0.9050 | 0.9480   |
| 0.1133        | 44.0  | 1980 | 0.3578          | 0.8660    | 0.9415 | 0.9022 | 0.9467   |
| 0.0575        | 45.0  | 2025 | 0.3384          | 0.8723    | 0.9419 | 0.9058 | 0.9498   |
| 0.0575        | 46.0  | 2070 | 0.3450          | 0.8755    | 0.9472 | 0.9100 | 0.9502   |
| 0.0575        | 47.0  | 2115 | 0.3468          | 0.8736    | 0.9495 | 0.9100 | 0.9500   |
| 0.0575        | 48.0  | 2160 | 0.3488          | 0.8706    | 0.9502 | 0.9087 | 0.9505   |
| 0.0575        | 49.0  | 2205 | 0.3480          | 0.8738    | 0.9517 | 0.9111 | 0.9506   |
| 0.0575        | 50.0  | 2250 | 0.3474          | 0.8725    | 0.9504 | 0.9098 | 0.9501   |
| 0.0575        | 51.0  | 2295 | 0.3463          | 0.8711    | 0.9498 | 0.9087 | 0.9499   |
| 0.0575        | 52.0  | 2340 | 0.3328          | 0.8782    | 0.9525 | 0.9138 | 0.9518   |
| 0.0575        | 53.0  | 2385 | 0.3550          | 0.8738    | 0.9527 | 0.9115 | 0.9508   |
| 0.0575        | 54.0  | 2430 | 0.3351          | 0.8777    | 0.9525 | 0.9135 | 0.9526   |
| 0.0575        | 55.0  | 2475 | 0.3438          | 0.8781    | 0.9548 | 0.9148 | 0.9521   |
| 0.0364        | 56.0  | 2520 | 0.3452          | 0.8797    | 0.9540 | 0.9153 | 0.9521   |
| 0.0364        | 57.0  | 2565 | 0.3496          | 0.8810    | 0.9561 | 0.9170 | 0.9523   |
| 0.0364        | 58.0  | 2610 | 0.3472          | 0.8802    | 0.9557 | 0.9164 | 0.9525   |
| 0.0364        | 59.0  | 2655 | 0.3476          | 0.8813    | 0.9559 | 0.9171 | 0.9530   |
| 0.0364        | 60.0  | 2700 | 0.3413          | 0.8839    | 0.9563 | 0.9187 | 0.9536   |
| 0.0364        | 61.0  | 2745 | 0.3395          | 0.8839    | 0.9563 | 0.9187 | 0.9538   |
| 0.0364        | 62.0  | 2790 | 0.3417          | 0.8843    | 0.9580 | 0.9196 | 0.9537   |
| 0.0364        | 63.0  | 2835 | 0.3397          | 0.8846    | 0.9563 | 0.9191 | 0.9536   |
| 0.0364        | 64.0  | 2880 | 0.3428          | 0.8839    | 0.9576 | 0.9192 | 0.9534   |
| 0.0364        | 65.0  | 2925 | 0.3411          | 0.8847    | 0.9576 | 0.9197 | 0.9539   |
| 0.0364        | 66.0  | 2970 | 0.3442          | 0.8849    | 0.9574 | 0.9197 | 0.9538   |
| 0.028         | 67.0  | 3015 | 0.3444          | 0.8844    | 0.9578 | 0.9196 | 0.9538   |
| 0.028         | 68.0  | 3060 | 0.3437          | 0.8857    | 0.9584 | 0.9206 | 0.9541   |
| 0.028         | 69.0  | 3105 | 0.3411          | 0.8857    | 0.9582 | 0.9205 | 0.9540   |
| 0.028         | 70.0  | 3150 | 0.3418          | 0.8858    | 0.9578 | 0.9204 | 0.9541   |


### Framework versions

- Transformers 4.32.1
- Pytorch 2.0.1+cu118
- Datasets 2.14.4
- Tokenizers 0.13.3
