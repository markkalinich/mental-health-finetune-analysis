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
# MrBERT-es Model Card

MrBERT-es is a new foundational bilingual language model for Spanish and English built on the [ModernBERT](https://huggingface.co/answerdotai/ModernBERT-base/tree/main) architecture. It uses vocabulary adaptation from [MrBERT](https://huggingface.co/BSC-LT/MrBERT), a method that initializes all weights from MrBERT while applying a specialized treatment to the embedding matrix. This treatment carefully handles the differences between the two tokenizers. 

Following initialization, the model is continually pretrained on a bilingual corpus of 615 billion tokens, evenly balanced between English and Spanish. 

## Technical Description

Technical details of the MrBERT-es model.


| Description          | Value         |
|-------------------------|:--------------|
| Model Parameters        | 150M          |
| Tokenizer Type          | SPM           |
| Vocabulary size         | 51200         |
| Precision               | bfloat16      |
| Context length          | 8192          |


Training Hyperparemeters

| Hyperparameter                | Value                             |
|-------------------------      |:--------------                    |
| Pretraining  Objective        | Masked Language Modeling          |
| Learning Rate                 | 4E-04                             |
| Learning Rate Scheduler       | WSD                               |
| Warmup                        | 3,000,000,000 tokens              |
| Optimizer                     | decoupled_stableadamw             |
| Optimizer Hyperparameters     | AdamW (β1=0.9,β2=0.98,ε =1e-06 )  |
| Weight Decay                  | 1E-05                             |
| Global Batch Size             | 480                               |
| Dropout                       | 1E-01                             |
| Activation Function           | GeLU                              |


## How to use

```python
>>> from transformers import pipeline
>>> from pprint import pprint

>>> unmasker = pipeline('fill-mask', model='BSC-LT/MrBERT-es')

>>> pprint(unmasker("Me encanta la<mask>de Barcelona.",top_k=3))
[{'score': 0.2312059849500656,
  'sequence': 'Me encanta la ciudad de Barcelona.',
  'token': 2634,
  'token_str': 'ciudad'},
 {'score': 0.0812854915857315,
  'sequence': 'Me encanta la gente de Barcelona.',
  'token': 4475,
  'token_str': 'gente'},
 {'score': 0.07678654044866562,
  'sequence': 'Me encanta la gastronomía de Barcelona.',
  'token': 18096,
  'token_str': 'gastronomía'}]
>>> pprint(unmasker("La ciencia engloba disciplinas como la<mask>y las matemáticas.",top_k=3))
[{'score': 0.8801143765449524,
  'sequence': 'La ciencia engloba disciplinas como la física y las '
              'matemáticas.',
  'token': 9204,
  'token_str': 'física'},
 {'score': 0.07342680543661118,
  'sequence': 'La ciencia engloba disciplinas como la biología y las '
              'matemáticas.',
  'token': 40678,
  'token_str': 'biología'},
 {'score': 0.02307266741991043,
  'sequence': 'La ciencia engloba disciplinas como la química y las '
              'matemáticas.',
  'token': 25047,
  'token_str': 'química'}]
>>> pprint(unmasker("Since I can't conquer the world yet, I'll just hide my weights under your<mask>and wait patiently.", top_k=3))
[{'score': 0.12437283992767334,
  'sequence': "Since I can't conquer the world yet, I'll just hide my weights "
              'under your pillow and wait patiently.',
  'token': 40389,
  'token_str': 'pillow'},
 {'score': 0.09473687410354614,
  'sequence': "Since I can't conquer the world yet, I'll just hide my weights "
              'under your arm and wait patiently.',
  'token': 6198,
  'token_str': 'arm'},
 {'score': 0.08770021051168442,
  'sequence': "Since I can't conquer the world yet, I'll just hide my weights "
              'under your feet and wait patiently.',
  'token': 6985,
  'token_str': 'feet'}]
```

Which is equivalent to the following torch script:

```python
from transformers import AutoTokenizer, AutoModelForMaskedLM
import torch

model = AutoModelForMaskedLM.from_pretrained("BSC-LT/MrBERT-es")
tokenizer = AutoTokenizer.from_pretrained("BSC-LT/MrBERT-es")

# The index of "<mask>" token is -3 given that the -1 position is the EOS token "</s>" and -2 the position of the "." token.
outputs = model(**tokenizer("La capital de España es<mask>.", return_tensors="pt")).logits
predicted_token = tokenizer.decode(torch.argmax(outputs[0,-3,:]))

print(f"The prediction is \"{predicted_token}\"." ) # The prediction is "Madrid"
```

### EVALUATION: EvalES Benchmark

Model performance in Spanish Language is assessed using the EvalES benchmark. The [EvalES benchmark](https://benchmark.plantl.bsc.es/datasets.html) consists of 7 tasks: Named Entity Recognition and Classification (CoNLL-NERC), Part-of-Speech Tagging (UD-POS), Text Classification (MLDoc), Paraphrase Identification (PAWS-X), Semantic Textual Similarity (STS), Question Answering (SQAC), and Textual Entailment (XNLI). This benchmark evaluates the model's capabilities in the Spanish language.

In addition to the MrBERT family, the following base foundation models were considered:
 
| Multilingual Foundational Model | Number of Parameters | Vocab Size | Description |
|---------------------------------|----------------------|------------|-------------|
| [xlm-roberta-base](https://huggingface.co/FacebookAI/xlm-roberta-base)                | 279M                | 250K       |   Foundational RoBERTa model pretrained with CommonCrawl data containing 100 languages.          | 
| [mRoBERTa](https://huggingface.co/BSC-LT/mRoBERTa)                       | 283M                | 256K       |     RoBERTa base model pretrained with 35 European languages and a larger vocabulary size.         |
| [mmBERT](https://huggingface.co/jhu-clsp/mmBERT-base)                | 308M                | 250K       |   Multilingual ModernBERT pre-trained with staged language learning.          | 
| [mGTE](https://huggingface.co/Alibaba-NLP/gte-multilingual-base)                | 306M                | 250K       |   Multilingual encoder also adapted for retrieval tasks.          | 


| tasks        |   xlm-roberta-base (278M) | mRoBERTa (283M)   | mmBERT (308M)   | mGTE (306M)   | MrBERT (308M)   | MrBERT-es (150M)   |
|--------------|---------------------------|-------------------|-----------------|-------------------------|-----------------|--------------------|
| pos (f1)     |                     99.01 | 99.03             | **99.09**       | 98.92                   | 99.06           | <u>99.08</u>       |
| ner (f1)     |                     86.91 | **87.77**         | 87.01           | 86.96                   | 87.42           | <u>87.77</u>       |
| sts (person) |                     80.88 | 79.69             | 82.88           | <u>84.52</u>            | 84.18           | **85.23**          |
| tc - paws-x (acc)     |                     90.35 | 91.30             | <u>91.35</u>    | 89.70                   | 91.25           | **91.90**          |
| tc - mldoc (acc)    |                     47.67 | 91.28             | 95.10           | **96.13**               | 95.28           | <u>95.55</u>       |
| tc - massivenew (acc)    |                     21.89 | 86.45             | 86.79           | <u>87.19</u>            | **87.46**       | 87.05              |
| qa (f1)      |                     74.48 | 77.03             | 79.79           | 76.78                   | <u>81.96</u>    | **82.19**          |
| Average      |                     71.60  | 87.51             | 88.86           | 88.60                   | <u>89.52</u>    | **89.83**          |

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