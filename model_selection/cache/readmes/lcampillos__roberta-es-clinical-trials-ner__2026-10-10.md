---
license: cc-by-nc-4.0
tags:
- generated_from_trainer
language: 
- es
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: roberta-es-clinical-trials-ner
  results: []
widget:
- text: "El ensayo clínico con vacunas promete buenos resultados para la infección por SARS-CoV-2."
- text: "El paciente toma aspirina para el dolor de cabeza y porque la garganta también le duele mucho."
- text: "El mejor tratamiento actual contra la COVID es la vacunación."
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# roberta-es-clinical-trials-ner

This medical named entity recognition model detects 4 types of semantic groups from the Unified Medical Language System (UMLS) (Bodenreider 2004):
- ANAT: body parts and anatomy (e.g. *garganta*, 'throat')
- CHEM: chemical entities and pharmacological substances (e.g. *aspirina*,'aspirin')
- DISO: pathologic conditions (e.g. *dolor*, 'pain')
- PROC: diagnostic and therapeutic procedures, laboratory analyses and medical research activities (e.g. *cirugía*, 'surgery')

The model achieves the following results on the evaluation set:
- Loss: 0.1580
- Precision: 0.8495
- Recall: 0.8806
- F1: 0.8647
- Accuracy: 0.9583

## Model description

This model adapts the pre-trained model [bsc-bio-ehr-es](https://huggingface.co/PlanTL-GOB-ES/bsc-bio-ehr-es), presented in [Pio Carriño et al. (2022)](https://aclanthology.org/2022.bionlp-1.19/). 
It is fine-tuned to conduct medical named entity recognition on Spanish texts about clinical trials. 
The model is fine-tuned on the [CT-EBM-SP corpus (Campillos-Llanos et al. 2021)](https://bmcmedinformdecismak.biomedcentral.com/articles/10.1186/s12911-021-01395-z).

## Intended uses & limitations

**Disclosure**: *This model is under development and needs to be improved. It should not be used for medical decision making without human assistance and supervision*

This model is intended for a generalist purpose, and may have bias and/or any other undesirable distortions.

Third parties who deploy or provide systems and/or services using any of these models (or using systems based on these models) should note that it is their responsibility to mitigate the risks arising from their use. Third parties, in any event, need to comply with applicable regulations, including regulations concerning the use of artificial intelligence.

The owner or creator of the models (CSIC – Consejo Superior de Investigaciones Científicas) will in no event be liable for any results arising from the use made by third parties of these models.

**Descargo de responsabilidad**: *Esta herramienta se encuentra en desarrollo y no debe ser empleada para la toma de decisiones médicas*

La finalidad de este modelo es generalista, y se advierte que puede tener sesgos y/u otro tipo de distorsiones indeseables.

Terceras partes que desplieguen o proporcionen sistemas y/o servicios usando alguno de estos modelos (o utilizando sistemas basados en estos modelos) han tener presente que es su responsabilidad abordar y minimizar los riesgos derivados de su uso. Las terceras partes, en cualquier circunstancia, deben cumplir con la normativa aplicable, incluyendo la normativa que concierne al uso de la inteligencia artificial.

El propietario o creador de los modelos (CSIC – Consejo Superior de Investigaciones Científicas) de ningún modo será responsable de los resultados derivados del uso que las terceras partes hagan de estos modelos.


## Training and evaluation data

The data used for fine-tuning is the [Clinical Trials for Evidence-Based-Medicine in Spanish corpus](http://www.lllf.uam.es/ESP/nlpdata/wp2/).

It is a collection of 1200 texts about clinical trials studies and clinical trials announcements:
- 500 abstracts from journals published under a Creative Commons license, e.g. available in PubMed or the Scientific Electronic Library Online (SciELO)
- 700 clinical trials announcements published in the European Clinical Trials Register and Repositorio Español de Estudios Clínicos

If you use this resource, please, cite as follows:

```
@article{campillosetal-midm2021,
        title = {A clinical trials corpus annotated with UMLS© entities to enhance the access to Evidence-Based Medicine},
        author = {Campillos-Llanos, Leonardo and Valverde-Mateos, Ana and Capllonch-Carri{\'o}n, Adri{\'a}n and Moreno-Sandoval, Antonio},
        journal = {BMC Medical Informatics and Decision Making},
        volume={21},
        number={1},
        pages={1--19},
        year={2021},
        publisher={BioMed Central}
}
```

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 4

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.0771        | 1.0   | 785  | 0.1274          | 0.8449    | 0.8797 | 0.8619 | 0.9608   |
| 0.0415        | 2.0   | 1570 | 0.1356          | 0.8569    | 0.8856 | 0.8710 | 0.9528   |
| 0.0262        | 3.0   | 2355 | 0.1562          | 0.8619    | 0.8798 | 0.8707 | 0.9526   |
| 0.0186        | 4.0   | 3140 | 0.1582          | 0.8609    | 0.8846 | 0.8726 | 0.9527   |

**Results per class (test set)**

| Class | Precision | Recall | F1     |  Support |
|:-----:|:---------:|:------:|:------:|:--------:|
| ANAT  | 0.7069    | 0.6518 | 0.6783 |    359   |
| CHEM  | 0.9162    | 0.9228 | 0.9195 |   2929   |
| DISO  | 0.8805    | 0.8918 | 0.8861 |   3042   |
| PROC  | 0.8198    | 0.8720 | 0.8450 |   3954   |

### Framework versions

- Transformers 4.17.0
- Pytorch 1.10.2+cu113
- Datasets 1.18.4
- Tokenizers 0.11.6

## Environmental Impact

Carbon emissions are estimated with the [Machine Learning Impact calculator](https://mlco2.github.io/impact/#compute) by [Lacoste et al. (2019)](https://arxiv.org/abs/1910.09700). The carbon impact is estimated by specifying the hardware, runtime, cloud provider, and compute region.

- Hardware Type: 1 GPU 24 GB RTX 3090
- Time used: 4' (0.07 hours) 
- Compute Region: Spain, Europe 
- Carbon Emitted (Power consumption x Time x Carbon produced based on location of power grid): 0.01 kg eq. CO2
(Carbon offset: 0)

## Funding

This model was created with the annotated dataset from the [NLPMedTerm project](http://www.lllf.uam.es/ESP/nlpmedterm_en.html), funded by  InterTalentum UAM, Marie Skłodowska-Curie COFUND grant (2019-2021) (H2020 program, contract number 713366) and by the Computational Linguistics Chair from the Knowledge Engineering Institute (IIC-UAM).

We thank the [Computational Linguistics Laboratory (LLI)](http://www.lllf.uam.es) at the Autonomous Universidad of Madrid (Universidad Autónoma de Madrid) for the computational facilities we used to fine-tune the model.

# License

Attribution-NonCommercial 4.0 International (CC BY 4.0)

