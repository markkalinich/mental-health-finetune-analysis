---
license: cc-by-nc-4.0
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: EriBERTa-clinical-trials-umls-7sgs
  results: []
widget:
- text: "Criterios de inclusión: 18 a 65 años; necrosis avascular de cadera; sintomática de menos de 6 meses; capaz de otorgar consentimiento informado.\n
Criterios de exclusión: embarazo, lactancia, mujer fértil sin métodos anticonceptivos adecuados; tratamiento activo con bifosfonatos; infección por VIH, hepatitis B o hepatitis C; historia de neoplasia en cualquier organo."
- text: "Recuperación de daño hepático relacionado con nutrición parenteral con ácidos omega-3 en adultos críticos: ensayo clínico aleatorizado."
- text: "Título público: Análisis del dolor tras inyección intramuscular de penicilina con agujas de mayor calibre y anestésico local, frente a aguja tradicional sin anestésico en pacientes con sífilis"

---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# EriBERTa-clinical-trials-umls-7sgs

This medical named entity recognition model detects 7 types of semantic groups from the [Unified Medical Language System (UMLS)](https://www.nlm.nih.gov/research/umls/index.html) ([Bodenreider 2004](https://academic.oup.com/nar/article/32/suppl_1/D267/2505235)):
- ANAT: body parts and anatomy (e.g. *garganta*, 'throat')
- CHEM: chemical entities and pharmacological substances (e.g. *aspirina*,'aspirin')
- DEVI: medical devices (e.g. *catéter*, 'catheter')
- DISO: pathologic conditions (e.g. *dolor*, 'pain')
- LIVB: living beings (e.g. *paciente*, 'patient')
- PHYS: physiological processes (e.g. *respiración*, 'breathing')
- PROC: diagnostic and therapeutic procedures, laboratory analyses and medical research activities (e.g. *cirugía*, 'surgery')

The model achieves the following results on the test set (when trained with the training and development set; results are averaged over 5 evaluation rounds):
- Precision: 0.881 (±0.005)
- Recall: 0.896 (±0.002)
- F1: 0.889 (±0.003)
- Accuracy: 0.959 (±0.001)


## Model description

This model adapts the pre-trained model [EriBERTa-base](https://huggingface.co/HiTZ/EriBERTa-base), presented in [De la Iglesia et al. (2023)](https://arxiv.org/abs/2306.07373). 
It is fine-tuned to conduct medical named entity recognition on Spanish texts about clinical trials. 
The model is fine-tuned on the [CT-EBM-ES corpus (Campillos-Llanos et al. 2021)](https://bmcmedinformdecismak.biomedcentral.com/articles/10.1186/s12911-021-01395-z) vs 2.

If you use this model, please, cite as follows:

```
@article{campillosetal2024,
        title = {Hybrid tool for semantic annotation and concept extraction of medical texts in Spanish},
        author = {Campillos-Llanos, Leonardo and Valverde-Mateos, Ana and Capllonch-Carri{\'o}n, Adri{\'a}n},
        journal = {BMC Bioinformatics},
        year={2024},
        publisher={BioMed Central}
}
```

## Intended uses & limitations

**Disclosure**: *This model is under development and needs to be improved. It should not be used for medical decision making without human assistance and supervision*

This model is intended for a generalist purpose, and may have bias and/or any other undesirable distortions.

Third parties who deploy or provide systems and/or services using any of these models (or using systems based on these models) should note that it is their responsibility to mitigate the risks arising from their use. Third parties, in any event, need to comply with applicable regulations, including regulations concerning the use of artificial intelligence.

The owner or creator of the models will in no event be liable for any results arising from the use made by third parties of these models.

**Descargo de responsabilidad**: *Esta herramienta se encuentra en desarrollo y no debe ser empleada para la toma de decisiones médicas*

La finalidad de este modelo es generalista, y se advierte que puede tener sesgos y/u otro tipo de distorsiones indeseables.

Terceras partes que desplieguen o proporcionen sistemas y/o servicios usando alguno de estos modelos (o utilizando sistemas basados en estos modelos) han tener presente que es su responsabilidad abordar y minimizar los riesgos derivados de su uso. Las terceras partes, en cualquier circunstancia, deben cumplir con la normativa aplicable, incluyendo la normativa que concierne al uso de la inteligencia artificial.

El propietario o creador de los modelos de ningún modo será responsable de los resultados derivados del uso que las terceras partes hagan de estos modelos.


## Training and evaluation data

The data used for fine-tuning are the [Clinical Trials for Evidence-Based-Medicine in Spanish corpus](http://www.lllf.uam.es/ESP/nlpdata/wp2/) vs 2.
It is a collection of 1200 texts about clinical trials studies and clinical trials announcements:
- 500 abstracts from journals published under a Creative Commons license, e.g. available in PubMed or the Scientific Electronic Library Online (SciELO)
- 700 clinical trials announcements published in the European Clinical Trials Register and Repositorio Español de Estudios Clínicos

If you use the CT-EBM-ES resource, please, cite as follows:

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
- seed: we used different seeds for 5 evaluation rounds, and uploaded the model with the best results
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: average 15.50 epochs (±4.12); trained with early stopping if no improvement after 5 epochs (early stopping patience: 5)


### Training results (test set; average and standard deviation of 5 rounds with different seeds)

|   Precision    |     Recall     |       F1       |    Accuracy    |
|:--------------:|:--------------:|:--------------:|:--------------:|
| 0.881 (±0.005) | 0.896 (±0.002) | 0.889 (±0.003) | 0.959 (±0.001) |



### Framework versions

- Transformers 4.17.0
- Pytorch 1.10.2+cu113
- Datasets 1.18.4
- Tokenizers 0.11.6
