---
language: 
  - es
tags:
  - biomedical
  - clinical
  - EHR
  - spanish
  - symptoms
license: cc-by-4.0
metrics:
- precision
- recall
- f1
base_model:
- PlanTL-GOB-ES/bsc-bio-ehr-es

model-index:
- name: BSC-NLP4BIA/bsc-bio-ehr-es-carmen-symptemist
  results:
    
    - task:
        type: token-classification
      dataset:
        name: CARMEN-I-symptoms
        type: CARMEN-I-symptoms
      metrics:
        - name: precision (micro)
          type: precision
          value: 0.743
        - name: recall (micro)
          type: recall
          value: 0.764
        - name: f1 (micro)
          type: f1
          value: 0.753
widget:
  - text: El diagnóstico definitivo de nuestro paciente fue de un Adenocarcinoma de pulmón cT2a cN3 cM1a Estadio IV (por una única lesión pulmonar contralateral) PD-L1 90%, EGFR negativo, ALK negativo y ROS-1 negativo.
  - text: Durante el ingreso se realiza una TC, observándose un nódulo pulmonar en el LII y una masa renal derecha indeterminada. Se realiza punción biopsia del nódulo pulmonar, con hallazgos altamente sospechosos de carcinoma.
  - text: Trombosis paraneoplásica con sospecha de hepatocarcinoma por imagen, sobre hígado cirrótico, en paciente con índice Child-Pugh B.

---


# bsc-bio-ehr-es-carmen-symptemist

## Table of contents
<details>
<summary>Click to expand</summary>

- [Model description](#model-description)
- [How to use](#how-to-use)
- [Limitations and bias](#limitations-and-bias)
- [Additional information](#additional-information)
  - [Authors](#authors)
  - [Contact information](#contact-information)
  - [Funding](#funding)
  - [Citing information](#citing-information)
  - [Disclaimer](#disclaimer)
  
</details>

## Model description
Model trained on the symptoms and signs mentions of [CARMEN-I](https://zenodo.org/records/10171540) and [SympTEMIST](https://doi.org/10.5281/zenodo.10635215).

## How to use

⚠ We recommend pre-tokenizing the input text into words instead of providing it directly to the model, as this is how the model was trained. Otherwise, the results and performance might get affected.

A usage example can be found [here](https://github.com/nlp4bia-bsc/hugging-face-pipeline/blob/main/simple_inference.py).

## Limitations and bias
At the time of submission, no measures have been taken to estimate the bias embedded in the model. However, we are well aware that our models may be biased since the corpora have been collected using crawling techniques on multiple web sources. We intend to conduct research in these areas in the future, and if completed, this model card will be updated. 


## Additional information

### Authors
NLP4BIA team at the Barcelona Supercomputing Center (nlp4bia@bsc.es).

### Contact information
jan.rodriguez [at] bsc.es

### Funding

This project was partially funded by the Spanish Plan for the Advancement of Language Technology (Plan TL) in collaboration with the Barcelona Supercomputing Center (BSC) and the Hospital Clinic de Barcelona (HCB). On the BSC's side, we acknowledge additional funding by the Spanish National AI4ProfHealth project (PID2020-119266RA-I00 MICIU/AEI/10.13039/501100011033) and EU Horizon projects (AI4HF 101080430 and DataTools4Heart 101057849). On the HCB's side, the project was also supported by the Instituto de Salud Carlos III (ISCIII).

### Citing information

Please cite the following works:

```bibtex

@article{LimaLopez2025,
  author       = {Salvador Lima-López and Eulàlia Farré-Maduell and Luis Gasco and Jan Rodríguez-Miret and Santiago Frid and Xavier Pastor and Xavier Borrat and Martin Krallinger},
  title        = {A textual dataset of de-identified health records in Spanish and Catalan for medical entity recognition and anonymization},
  journal      = {Scientific Data},
  volume       = {12},
  pages        = {Article 1088},
  year         = {2025},
  publisher    = {Nature Publishing Group},
  doi          = {10.1038/s41597-025-05320-1},
  url          = {https://www.nature.com/articles/s41597-025-05320-1}
}

@misc{carmen_physionet,
  author = {Farre Maduell, Eulalia and Lima-Lopez, Salvador and Frid, Santiago Andres and Conesa, Artur and Asensio, Elisa and Lopez-Rueda, Antonio and Arino, Helena and Calvo, Elena and Bertran, Maria Jesús and Marcos, Maria Angeles and Nofre Maiz, Montserrat and Tañá Velasco, Laura and Marti, Antonia and Farreres, Ricardo and Pastor, Xavier and Borrat Frigola, Xavier and Krallinger, Martin},
  title = {{CARMEN-I: A resource of anonymized electronic health records in Spanish and Catalan for training and testing NLP tools (version 1.0.1)}},
  year = {2024},
  publisher = {PhysioNet},
  url = {https://doi.org/10.13026/x7ed-9r91}
},

@inproceedings{symptemist,
  author = {Lima-L{\'o}pez, Salvador and Farr{\'e}-Maduell, Eul{\`a}lia and Gasco-S{\'a}nchez, Luis and Rodr{\'i}guez-Miret, Jan and Krallinger, Martin},
  title = {{Overview of SympTEMIST at BioCreative VIII: Corpus, Guidelines and Evaluation of Systems for the Detection and Normalization of Symptoms, Signs and Findings from Text}},
  booktitle = {Proceedings of the BioCreative VIII Challenge and Workshop: Curation and Evaluation in the era of Generative Models},
  year = 2023
}

@article{physionet,
  author = {Ary L. Goldberger  and Luis A. N. Amaral  and Leon Glass  and Jeffrey M. Hausdorff  and Plamen Ch. Ivanov  and Roger G. Mark  and Joseph E. Mietus  and George B. Moody  and Chung-Kang Peng  and H. Eugene Stanley },
  title = {PhysioBank, PhysioToolkit, and PhysioNet  },
  journal = {Circulation},
  volume = {101},
  number = {23},
  pages = {e215-e220},
  year = {2000},
  doi = {10.1161/01.CIR.101.23.e215},
  URL = {https://www.ahajournals.org/doi/abs/10.1161/01.CIR.101.23.e215}
}
```

### Disclaimer

The models published in this repository are intended for a generalist purpose and are available to third parties. These models may have bias and/or any other undesirable distortions.

When third parties deploy or provide systems and/or services to other parties using any of these models (or using systems based on these models) or become users of the models, they should note that it is their responsibility to mitigate the risks arising from their use and, in any event, to comply with applicable regulations, including regulations regarding the use of artificial intelligence.

---
Los modelos publicados en este repositorio tienen una finalidad generalista y están a disposición de terceros. Estos modelos pueden tener sesgos y/u otro tipo de distorsiones indeseables.

Cuando terceros desplieguen o proporcionen sistemas y/o servicios a otras partes usando alguno de estos modelos (o utilizando sistemas basados en estos modelos) o se conviertan en usuarios de los modelos, deben tener en cuenta que es su responsabilidad mitigar los riesgos derivados de su uso y, en todo caso, cumplir con la normativa aplicable, incluyendo la normativa en materia de uso de inteligencia artificial.
