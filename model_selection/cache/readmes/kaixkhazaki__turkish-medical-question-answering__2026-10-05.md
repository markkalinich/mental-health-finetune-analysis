---
library_name: transformers
license: mit
base_model: dbmdz/bert-base-turkish-cased
tags:
- generated_from_trainer
- turkish
- med
metrics:
- f1
- exact_match
model-index:
- name: turkish-medical-question-answering
  results: []
datasets:
- incidelen/MedTurkQuAD
language:
- tr
pipeline_tag: question-answering
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# turkish-medical-question-answering

## Model description

This model is a fine-tuned version of [dbmdz/bert-base-turkish-cased](https://huggingface.co/dbmdz/bert-base-turkish-cased) optimized for medical domain question answering in Turkish. 
It uses a BERT-based architecture with additional dropout regularization to prevent overfitting and is specifically trained to extract answers from medical text contexts.


It achieves the following results on the test evaluation set:
- Loss: 1.2814
- Exact Match: 52.7881
- F1: 76.1437

Validation Metrics
 - eval_loss': 1.2329986095428467
 - eval_exact_match': 56.52724968314322
 - eval_f1': 76.17448254104453

Test Metrics
 - eval_loss: 1.2814178466796875
 - eval_exact_match: 52.78810408921933
 - eval_f1: 76.14367323441282

## Usage
```python
# Use a pipeline as a high-level helper
from transformers import pipeline

pipe = pipeline("question-answering", model="kaixkhazaki/turkish-question-answering")


# Example 
## Define the context

context = """
Kalça kırığından şüphe duyulan hastalarda öncelikle standart grafiler çekilmelidir. Bunlar ön arka pelvis grafisi ve etkilenen kalçanın ön arka ve yan grafileridir. 
Özellikle deplase olmayan kırıklarda sağlam taraf ile patolojik tarafın mukayese edilmesi önemlidir. Kırık kalçanın filmi, alt ekstremite hafif traksiyonda iken nötral pozisyonda, 
patella ışın düzlemine dikey halde çekilir. Trokanter majörün en az 10 cm distaline kadar görülmesi faydalı olacaktır. Ayrıca sağlam tarafın görülmesi ile osteoporoz ve hastanın 
normal boyun-cisim açısının tayininde önemlidir. Lateral radyografi posteriorda kırığın stabilitesini ve deplasman miktarını belirlemek için gereklidir. Lateral grafi çekimi acil 
olmamakla birlikte kırığın daha doğru değerlendirilmesi açısından önemlidir. Eğer hasta grafi masasında iken çekilemiyor ise, traksiyon masasına alındığında görülebilir. 
Nadiren de olsa tanı için tomografi çekilmesi gerekli olabilir. Bunun yanında kalça kırığı şüphesi yüksek olan, ancak direk grafide kırık tanısı konulamayan hastalara MR çekilerek 
tanı rahatlıkla konulabilir. Yine röntgende görünmeyen ancak kırık şüphesi yüksek olan hastalara 48-72 saat içerisinde yapılan sintigrafilerde duyarlılık % 100'dür.
"""

# Define the question
question = "Lateral radyografi hangi durumlar için gereklidir?"

pipe(question=question, context=context)
>>
{'score': 0.7423108220100403,
 'start': 595,
 'end': 662,
 'answer': 'posteriorda kırığın stabilitesini ve deplasman miktarını belirlemek'}

#Example

## Define the context
context = """
Kalça kırığından şüphe duyulan hastalarda öncelikle standart grafiler çekilmelidir. Bunlar ön arka pelvis grafisi ve etkilenen kalçanın ön arka ve yan grafileridir. 
Özellikle deplase olmayan kırıklarda sağlam taraf ile patolojik tarafın mukayese edilmesi önemlidir. Kırık kalçanın filmi, alt ekstremite hafif traksiyonda iken nötral pozisyonda, 
patella ışın düzlemine dikey halde çekilir. Trokanter majörün en az 10 cm distaline kadar görülmesi faydalı olacaktır. Ayrıca sağlam tarafın görülmesi ile osteoporoz ve hastanın 
normal boyun-cisim açısının tayininde önemlidir. Lateral radyografi posteriorda kırığın stabilitesini ve deplasman miktarını belirlemek için gereklidir. Lateral grafi çekimi acil 
olmamakla birlikte kırığın daha doğru değerlendirilmesi açısından önemlidir. Eğer hasta grafi masasında iken çekilemiyor ise, traksiyon masasına alındığında görülebilir. 
Nadiren de olsa tanı için tomografi çekilmesi gerekli olabilir. Bunun yanında kalça kırığı şüphesi yüksek olan, ancak direk grafide kırık tanısı konulamayan hastalara MR çekilerek 
tanı rahatlıkla konulabilir. Yine röntgende görünmeyen ancak kırık şüphesi yüksek olan hastalara 48-72 saat içerisinde yapılan sintigrafilerde duyarlılık % 100'dür.
"""

# Define the question
question = "Trokanter majörün kaç cm distaline kadar görülmesi faydalıdır?"

pipe(question=question, context=context)

>>
{'score': 0.8581815361976624,
'start': 416,
'end': 418,
'answer': '10'}

```



## Intended Uses, Bias, Risks, and Limitations

**Intended Uses**
* Medical question answering in Turkish
* Information extraction from Turkish medical texts
* Supporting medical professionals and researchers in finding specific information in medical documents

**Limitations**
* This model **should not** be used as a substitute for professional medical advice
* The model may reflect biases present in the medical training data
* Performance may vary across different medical specialties and terminology
* The model is not suitable for answering complex medical questions requiring reasoning or synthesis of information
* The model is specifically trained for the medical domain and may not perform well on general domain questions
* Performance may vary on highly technical medical terminology not present in the training data
* The model is limited to extractive QA (finding answers that are directly present in the text)

## Training Details


**Training Hyperparameters**
* Base Model: dbmdz/bert-base-turkish-cased
* Batch Size: 16
* Learning Rate: 1e-5
* Number of Epochs: 10
* Weight Decay: 0.02
* Warmup Steps: 1000
* Learning Rate Scheduler: Cosine
* Gradient Clipping: 1.0
* Training Precision: BF16
* Optimizer: AdamW

**Model Architecture Modifications**
* Hidden Dropout Probability: 0.2
* Attention Probability Dropout: 0.2


## Training and evaluation data

The model was trained on the Turkish Medical Question Answering dataset. 
```bibtex
@INPROCEEDINGS{10711128,
  author={İncidelen, Mert and Aydoğan, Murat},
  booktitle={2024 8th International Artificial Intelligence and Data Processing Symposium (IDAP)}, 
  title={Developing Question-Answering Models in Low-Resource Languages: A Case Study on Turkish Medical Texts Using Transformer-Based Approaches}, 
  year={2024},
  volume={},
  number={},
  pages={1-4},
  keywords={Training;Adaptation models;Natural languages;Focusing;Encyclopedias;Transformers;Data models;Internet;Online services;Text processing;Natural Language Processing;Medical Domain;BERTurk;Question-Answering},
  doi={10.1109/IDAP64064.2024.10711128}}
```
## Training procedure

**Preprocessing**
* Maximum Sequence Length: 384
* Stride: 128
* Question and context pairs are tokenized using BertTokenizerFast

**Evaluation Strategy**
* Evaluation performed every 50 steps
* Best model saved based on F1 score
* Metrics as Exact Match and F1 Score



### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-05
- train_batch_size: 16
- eval_batch_size: 64
- seed: 42
- optimizer: Use adamw_torch with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: cosine
- lr_scheduler_warmup_steps: 1000
- num_epochs: 10



### Training results

| Training Loss | Epoch  | Step | Validation Loss | Exact Match | F1      |
|:-------------:|:------:|:----:|:---------------:|:-----------:|:-------:|
| 5.9507        | 0.1166 | 50   | 5.9381          | 0.0         | 6.0684  |
| 5.8385        | 0.2331 | 100  | 5.7914          | 0.0         | 6.4166  |
| 5.6579        | 0.3497 | 150  | 5.5785          | 0.0         | 6.1711  |
| 5.3863        | 0.4662 | 200  | 5.3045          | 0.2012      | 6.2450  |
| 5.0968        | 0.5828 | 250  | 4.9885          | 0.5976      | 7.6302  |
| 4.7795        | 0.6993 | 300  | 4.6415          | 1.0941      | 8.9163  |
| 4.4223        | 0.8159 | 350  | 4.2947          | 1.6293      | 9.4547  |
| 4.1392        | 0.9324 | 400  | 3.9772          | 4.6748      | 14.3025 |
| 3.8572        | 1.0490 | 450  | 3.4575          | 12.5448     | 27.5850 |
| 3.3154        | 1.1655 | 500  | 2.5605          | 28.7234     | 51.4219 |
| 2.8303        | 1.2821 | 550  | 2.2085          | 35.0144     | 57.9319 |
| 2.5985        | 1.3986 | 600  | 2.0545          | 38.8122     | 61.8230 |
| 2.3931        | 1.5152 | 650  | 1.9646          | 38.8283     | 62.3091 |
| 2.3749        | 1.6317 | 700  | 1.8911          | 42.2311     | 64.3891 |
| 2.3268        | 1.7483 | 750  | 1.8363          | 42.9521     | 65.1745 |
| 2.1324        | 1.8648 | 800  | 1.7683          | 43.2540     | 66.5840 |
| 2.1652        | 1.9814 | 850  | 1.6980          | 45.5979     | 67.6440 |
| 1.9279        | 2.0979 | 900  | 1.6432          | 46.4935     | 68.1335 |
| 1.9351        | 2.2145 | 950  | 1.6031          | 46.7866     | 68.4213 |
| 1.8488        | 2.3310 | 1000 | 1.5765          | 48.7047     | 70.2017 |
| 1.8967        | 2.4476 | 1050 | 1.5462          | 47.9791     | 69.8952 |
| 1.7476        | 2.5641 | 1100 | 1.5040          | 49.2903     | 71.0521 |
| 1.7635        | 2.6807 | 1150 | 1.5197          | 49.2188     | 70.7629 |
| 1.7595        | 2.7972 | 1200 | 1.4790          | 49.8724     | 70.5285 |
| 1.7699        | 2.9138 | 1250 | 1.4283          | 52.5707     | 72.8425 |
| 1.7792        | 3.0303 | 1300 | 1.4246          | 50.5762     | 72.0336 |
| 1.5396        | 3.1469 | 1350 | 1.4117          | 52.6248     | 72.8936 |
| 1.5112        | 3.2634 | 1400 | 1.3938          | 53.1888     | 73.1075 |
| 1.5936        | 3.3800 | 1450 | 1.3805          | 53.8953     | 73.4629 |
| 1.4775        | 3.4965 | 1500 | 1.3522          | 53.5443     | 72.8847 |
| 1.3998        | 3.6131 | 1550 | 1.3730          | 52.9262     | 72.7934 |
| 1.4743        | 3.7296 | 1600 | 1.3593          | 53.2319     | 73.0427 |
| 1.572         | 3.8462 | 1650 | 1.3748          | 53.7484     | 73.1917 |
| 1.5321        | 3.9627 | 1700 | 1.3096          | 54.2929     | 72.9719 |
| 1.2849        | 4.0793 | 1750 | 1.3057          | 54.1823     | 73.5710 |
| 1.4073        | 4.1958 | 1800 | 1.2768          | 55.1072     | 73.9657 |
| 1.2894        | 4.3124 | 1850 | 1.3707          | 54.0984     | 73.5854 |
| 1.2771        | 4.4289 | 1900 | 1.3068          | 54.9686     | 74.2854 |
| 1.2683        | 4.5455 | 1950 | 1.2683          | 55.6818     | 74.6788 |
| 1.3432        | 4.6620 | 2000 | 1.2704          | 55.3866     | 74.1082 |
| 1.3052        | 4.7786 | 2050 | 1.2826          | 54.5570     | 73.9376 |
| 1.3458        | 4.8951 | 2100 | 1.2436          | 54.4304     | 74.1391 |
| 1.1832        | 5.0117 | 2150 | 1.2914          | 55.8081     | 74.5105 |
| 1.1964        | 5.1282 | 2200 | 1.2332          | 56.8182     | 75.6849 |
| 1.1179        | 5.2448 | 2250 | 1.2661          | 55.5273     | 74.5969 |
| 1.1602        | 5.3613 | 2300 | 1.2717          | 56.0203     | 75.5936 |
| 1.1314        | 5.4779 | 2350 | 1.2784          | 55.5133     | 75.2080 |
| 1.2153        | 5.5944 | 2400 | 1.2401          | 56.3682     | 75.6323 |
| 1.1613        | 5.7110 | 2450 | 1.2470          | 55.8081     | 75.5565 |
| 1.0839        | 5.8275 | 2500 | 1.2555          | 56.2108     | 75.3284 |
| 1.1208        | 5.9441 | 2550 | 1.2151          | 56.0606     | 75.3103 |
| 1.1018        | 6.0606 | 2600 | 1.2407          | 56.2814     | 75.4373 |
| 1.004         | 6.1772 | 2650 | 1.2561          | 56.1869     | 75.1453 |
| 1.0081        | 6.2937 | 2700 | 1.2708          | 56.3843     | 75.1235 |
| 1.0503        | 6.4103 | 2750 | 1.2398          | 56.4780     | 75.2607 |
| 1.1078        | 6.5268 | 2800 | 1.2424          | 56.1558     | 75.4293 |
| 1.0516        | 6.6434 | 2850 | 1.2425          | 57.0342     | 76.0343 |
| 1.0919        | 6.7599 | 2900 | 1.2361          | 56.5107     | 75.1984 |
| 1.0834        | 6.8765 | 2950 | 1.2307          | 56.6158     | 75.4564 |
| 1.0308        | 6.9930 | 3000 | 1.2331          | 55.9236     | 75.7649 |
| 0.9756        | 7.1096 | 3050 | 1.2354          | 56.9250     | 76.0355 |
| 0.9279        | 7.2261 | 3100 | 1.2538          | 56.4168     | 75.7899 |
| 0.9655        | 7.3427 | 3150 | 1.2458          | 56.4885     | 76.0547 |
| 0.9776        | 7.4592 | 3200 | 1.2351          | 57.0701     | 76.0798 |
| 0.925         | 7.5758 | 3250 | 1.2309          | 56.6158     | 75.7755 |
| 1.0088        | 7.6923 | 3300 | 1.2403          | 56.2897     | 75.7209 |
| 1.0534        | 7.8089 | 3350 | 1.2426          | 55.1592     | 75.2877 |
| 1.0021        | 7.9254 | 3400 | 1.2364          | 55.9645     | 75.4818 |
| 0.9248        | 8.0420 | 3450 | 1.2420          | 55.5838     | 75.7577 |
| 0.9077        | 8.1585 | 3500 | 1.2389          | 56.0051     | 75.6164 |
| 0.9882        | 8.2751 | 3550 | 1.2259          | 55.8228     | 75.5104 |
| 0.9151        | 8.3916 | 3600 | 1.2330          | 56.5272     | 76.1745 |
| 0.9682        | 8.5082 | 3650 | 1.2406          | 56.6372     | 75.9005 |
| 1.0271        | 8.6247 | 3700 | 1.2343          | 56.4557     | 75.7307 |
| 0.9019        | 8.7413 | 3750 | 1.2343          | 56.3291     | 75.8930 |
| 0.8673        | 8.8578 | 3800 | 1.2379          | 56.2183     | 75.9115 |
| 0.91          | 8.9744 | 3850 | 1.2421          | 56.0759     | 75.8580 |
| 0.8888        | 9.0909 | 3900 | 1.2399          | 56.2183     | 76.0760 |
| 0.874         | 9.2075 | 3950 | 1.2438          | 56.0203     | 75.8630 |
| 0.9676        | 9.3240 | 4000 | 1.2445          | 56.2738     | 76.0027 |
| 0.9712        | 9.4406 | 4050 | 1.2413          | 56.1470     | 76.0020 |
| 0.8792        | 9.5571 | 4100 | 1.2416          | 56.1470     | 75.9679 |
| 0.9358        | 9.6737 | 4150 | 1.2406          | 56.4005     | 75.9939 |
| 0.8496        | 9.7902 | 4200 | 1.2411          | 56.4005     | 76.0539 |
| 0.9618        | 9.9068 | 4250 | 1.2412          | 56.2738     | 76.0405 |


### Framework versions

- Transformers 4.48.0.dev0
- Pytorch 2.4.1+cu121
- Datasets 3.1.0
- Tokenizers 0.21.0



## Citation

```bibtex
@misc{turkish-medical-question-answering,
  author = {Fatih Demirci},
  title = {Turkish Medical Question Answering Model},
  year = {2024},
  publisher = {HuggingFace},
  journal = {HuggingFace Model Hub}
  howpublished = {\url{https://huggingface.co/kaixkhazaki/turkish-medical-question-answering}}
}

```