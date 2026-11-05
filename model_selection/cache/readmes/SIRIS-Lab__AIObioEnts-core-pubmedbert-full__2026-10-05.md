---
library_name: transformers
tags:
- ner
- biomedicine
license: mit
base_model:
- microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract-fulltext
pipeline_tag: token-classification
---

# AIObioEnts: All-in-one biomedical entities

Biomedical named-entity recognition following the all-in-one NER (AIONER) scheme introduced by [Luo *et al.*](https://doi.org/10.1093/bioinformatics/btad310). This is a straightforward Hugging-Face-compatible implementation without using a decoding head for ease of integration with other pipelines.

**For full details, see the [main GitHub repository](https://github.com/sirisacademic/AIObioEnts/)**

## Core biomedical entities

We have followed the original original AIONER training pipeline based on the BioRED dataset along with additional BioRED-compatible datasets:
- Gene: GNormPlus, NLM-Gene, DrugProt
- Disease: BC5CDR, NCBI Disease
- Chemical: BC5CDR, NLM-Chem, DrugProt
- Species: Species-800, Linnaeus
- Variant: tmVar
- Cell line: BioID

using three pre-trained language models as a base. This model corresponds to the implementation based on [BiomedBERT-base pre-trained on both abstracts from PubMed and full-texts articles from PubMedCentral](https://huggingface.co/microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract-fulltext)


**F1 scores**

The F1 scores of the current implementation on the BioRED test set are shown below:

|               | **BiomedBERT-base abstract+fulltext** |
| ------------- | :-----------------------------------: |
| **Cell line** |                 96.91                 |
| **Chemical**  |                 92.02                 |
| **Disease**   |                 88.64                 |
| **Gene**      |                 94.41                 |
| **Species**   |                 97.59                 |
| **Variant**   |                 89.58                 |
|  |  |  |  |
| **Overall**   |               92.44              |


## Usage

The model can be directly used from HuggingFace in a NER pipeline. However, we note that:
- The model was trained on sentence-level data, and it works best when the input is split
- Each sentence to tag must be surrounded by the flag corresponding to the entity type one wishes to identify (any of the 6 individual entities or "ALL"), as in: `<entity_type>sentence</entity_type>`
- Since additional `'O'` labels are used in the AIONER scheme, the outputs should be postprocessed before aggregating the tags

We provide helper functions to tag individual texts in the [main repository](https://github.com/sirisacademic/AIObioEnts/)

````python
from tagging_fn import process_one_text
from transformers import pipeline

pipe = pipeline('ner', model='SIRIS-Lab/AIObioEnts-core-pubmedbert-full', aggregation_strategy='none', device=0)

process_one_text(text_to_tag, pipeline=pipe, entity_type='ALL')
````

## References

[[1] Ling Luo, Chih-Hsuan Wei, Po-Ting Lai, Robert Leaman, Qingyu Chen, and Zhiyong Lu. "AIONER: All-in-one scheme-based biomedical named entity recognition using deep learning." Bioinformatics, Volume 39, Issue 5, May 2023, btad310.](https://doi.org/10.1093/bioinformatics/btad310)