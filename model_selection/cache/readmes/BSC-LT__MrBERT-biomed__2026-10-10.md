---
language:
- es
- en
tags: 
  - fill-mask
  - masked-lm
  - long-context
  - modernbert
base_model: BSC-LT/MrBERT
license: apache-2.0
library_name: transformers
---
# MrBERT-biomed Model Card

MrBERT-biomed is a new foundational multilingual biomedical model built on the [ModernBERT](https://huggingface.co/answerdotai/ModernBERT-base/tree/main) architecture. The model is obtained via domain adaptation from [MrBERT](https://huggingface.co/BSC-LT/MrBERT), initializing all weights from MrBERT-es and further training on a domain-specific biomedical corpus comprising 24.13B tokens for 2 epochs. The training data is predominantly English (84.7%), followed by Spanish (14.8%), with smaller portions of German (0.18%), Italian (0.11%), French (0.11%), and minor traces of Portuguese and Russian.

## Technical Description

Technical details of the MrBERT-biomed model.

| Description          | Value         |
|-------------------------|:--------------|
| Model Parameters        | 308M          |
| Tokenizer Type          | SPM           |
| Vocabulary size         | 25600         |
| Precision               | bfloat16      |
| Context length          | 8192          |


Training Hyperparemeters

| Hyperparameter                | Value                             |
|-------------------------      |:--------------                    |
| Pretraining  Objective        | Masked Language Modeling          |
| Learning Rate                 | 2E-03                             |
| Learning Rate Scheduler       | Cosine                            |
| Warmup                        | 2,400,000,000 tokens              |
| Optimizer                     | decoupled_stableadamw             |
| Optimizer Hyperparameters     | AdamW (β1=0.9,β2=0.98,ε =1e-06 )  |
| Weight Decay                  | 1E-05                             |
| Global Batch Size             | 512                               |
| Dropout                       | 1E-01                             |
| Activation Function           | GeLU                              |


## How to use

```python
>>> from transformers import pipeline
>>> from pprint import pprint

>>> unmasker = pipeline('fill-mask', model='BSC-LT/MrBERT-biomed')

>>> pprint(unmasker("El uso prolongado de<mask>puede causar toxicidad hepática.",top_k=3))
[{'score': 0.19885338842868805,
  'sequence': 'El uso prolongado de esteroides puede causar toxicidad '
              'hepática.',
  'token': 215060,
  'token_str': 'esteroides'},
 {'score': 0.03336358070373535,
  'sequence': 'El uso prolongado de insulina puede causar toxicidad hepática.',
  'token': 131044,
  'token_str': 'insulina'},
 {'score': 0.022234393283724785,
  'sequence': 'El uso prolongado de drogas puede causar toxicidad hepática.',
  'token': 99191,
  'token_str': 'drogas'}]
>>> pprint(unmasker("Prolonged use of<mask>can cause hepatotoxicity.", top_k=3))
[{'score': 0.10918917506933212,
  'sequence': 'Prolonged use of steroids can cause hepatotoxicity.',
  'token': 232800,
  'token_str': 'steroids'},
 {'score': 0.08295559883117676,
  'sequence': 'Prolonged use of drugs can cause hepatotoxicity.',
  'token': 101507,
  'token_str': 'drugs'},
 {'score': 0.049813270568847656,
  'sequence': 'Prolonged use of alcohol can cause hepatotoxicity.',
  'token': 52167,
  'token_str': 'alcohol'}]
```

## EVALUATION: Retrieval

In addition to the MrBERT family, the following base foundation models were considered:
 
| Multilingual Foundational Model | Number of Parameters | Vocab Size | Description |
|---------------------------------|----------------------|------------|-------------|
| [mmBERT](https://huggingface.co/jhu-clsp/mmBERT-base)                | 308M                | 250K       |   Multilingual ModernBERT pre-trained with staged language learning.          | 
| [mGTE](https://huggingface.co/Alibaba-NLP/gte-multilingual-base)                | 306M                | 250K       |   Multilingual encoder also adapted for retrieval tasks.          | 
| [Clinical ModernBERT](https://huggingface.co/Simonlee711/Clinical_ModernBERT) | 137M | 50K | Pre-trained model on biomedical data using ModernBERT architecture | 
| [BioClinical-ModernBERT](https://huggingface.co/thomas-sounack/BioClinical-ModernBERT-base) | 150M | 50K | Domain adaptation from ModernBERT to bioclinical data | 

The benchmarks used for comparison are:
- **MTEB:** We select a subset of MTEB that evaluates legal tasks in English.
- **Absatnitas:**  An internally designed task for evaluating Spanish-language retrieval performance on biomedical abstracts.
- **NER:** 3 Spanish Named-Entity Recognition datasets.


| **Task Name**                             | **Task Type** | **mmBERT (308M)** | **MrBERT (308M)** | **MrBERT-es (150M)** | **BioClinical-MdnBERT (150M)** | **Clinical MdnBERT (137M)** | **MrBERT-biomed (308M)** |
|-----------------------------------------------|--------------------|------------------------|------------------------|---------------------------|-------------------------------------|----------------------------------|-------------------------------|
| bsc-bio-distemist-ner (ES) | NER | <u>78.00</u> | 77.84 | **78.07** | 75.45 | 70.22 | 77.93 |
| cantemist (ES)                                | NER                | **78.03**         | 68.73                  | <u>73.40</u>               | 66.68                               | 30.91                            | 70.78                         |
| pharmaconer (ES)                              | NER                | <u>89.66</u>            | 88.58                  | 88.97                     | 87.66                               | 81.69                            | **89.92**                |
| AbSanitas (ES)                                | Retrieval          | 34.68                  | 34.16                  | **53.49**            | 30.41                               | 18.08                            | <u>51.01</u>                   |
| r2med (EN)                                    | Retrieval          | **10.87**         | <u>10.15</u>            | 8.65                      | 9.97                                | 5.91                             | 9.76                          |
| SciDocs (EN)                                  | Retrieval          | <u>10.00</u>            | 9.75                   | 9.90                      | 9.33                                | 3.64                             | **10.05**                |
| SciFact (EN)                                  | Retrieval          | **32.35**         | 31.08                  | 31.46                     | <u>32.07</u>                         | 20.34                            | 30.25                         |
| TREC-COVID (EN)                               | Retrieval          | 30.77                  | **49.53**         | 37.51                     | 46.08                               | 23.88                            | <u>48.76</u>                   |
| Average (EN)                                  | All Tasks          | 21.00                  | **25.13**         | 21.88                     | 24.36                               | 13.44                            | <u>24.71</u>                   |
| Average (EN + ES)                             | All Tasks          | 45.55                  | 46.23                  | <u>47.68</u>               | 44.71                               | 31.83                            | **48.56**                |


## Additional information

### Author
The Language Technologies Lab from Barcelona Supercomputing Center.

### Contact
For further information, please send an email to <langtech@bsc.es>.

### Copyright
Copyright(c) 2026 by Language Technologies Lab, Barcelona Supercomputing Center.

### Funding

This work has been supported and funded by the Ministerio para la Transformación Digital y de la Función Pública and the Plan de Recuperación, Transformación y Resiliencia – funded by the EU through NextGenerationEU, within the framework of the Modelos del Lenguaje project, as well as by the European Union – NextGenerationEU. Views and opinions expressed are however those of the author(s) only and do not necessarily reflect those of the European Union or European Commission. Neither the European Union nor the European Commission can be held responsible for them.

### Acknowledgements


This project has benefited from the contributions of numerous teams and institutions through data contributions.

In Catalonia, many institutions have been involved in the project. Our thanks to Òmnium Cultural, Parlament de Catalunya, Institut d'Estudis Aranesos, Racó Català, Vilaweb, ACN, Nació Digital, El món and Aquí Berguedà.

At national level, we are especially grateful to our ILENIA project partners: CENID, HiTZ and CiTIUS for their participation. We also extend our genuine gratitude to the Spanish Senate and Congress, Fundación Dialnet, Fundación Elcano, the "Instituto de Ingenieria del Conocimiento" and the ‘Instituto Universitario de Sistemas Inteligentes y Aplicaciones Numéricas en Ingeniería (SIANI)’ of the University of Las Palmas de Gran Canaria.

At the international level, we thank the Welsh government, DFKI, Occiglot project, especially Malte Ostendorff, and The Common Crawl Foundation, especially Pedro Ortiz, for their collaboration.

Their valuable efforts have been instrumental in the development of this work.

### Disclaimer
Be aware that the model may contain biases or other unintended distortions. 
When third parties deploy systems or provide services based on this model, or use the model themselves, 
they bear the responsibility for mitigating any associated risks and ensuring compliance with applicable regulations, 
including those governing the use of Artificial Intelligence.

The Barcelona Supercomputing Center, as the owner and creator of the model, shall not be held liable for any outcomes resulting from third-party use.

### Citation

```
@article{tamayo2026mrbert,
  title={MrBERT: Modern Multilingual Encoders via Vocabulary, Domain, and Dimensional Adaptation},
  author={Tamayo, Daniel and Lacunza, I{\~n}aki and Rivera-Hidalgo, Paula and Da Dalt, Severino and Aula-Blasco, Javier and Gonzalez-Agirre, Aitor and Villegas, Marta},
  journal={arXiv preprint arXiv:2602.21379},
  year={2026}
}
```

### License
[Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0)