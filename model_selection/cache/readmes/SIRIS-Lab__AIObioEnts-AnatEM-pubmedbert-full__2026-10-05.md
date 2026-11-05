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

## Anatomical biomedical entities

We have followed the original AIONER training pipeline based on the BioRED dataset along with additional BioRED-compatible datasets for set of core entities (Gene, Disease, Chemical, Species, Variant, Cell line), which we have fine-tuned using a modified version of the latest release of the [AnatEM](https://nactem.ac.uk/anatomytagger/#AnatEM) corpus, and a subset of entities that are of interest to us: *cell*, *cell component*, *tissue*, *muti-tissue structure*, and *organ*, along with the newly-introduced *cancer*. This model corresponds to the implementation based on [BiomedBERT-base pre-trained on both abstracts from PubMed and full-texts articles from PubMedCentral](https://huggingface.co/microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract-fulltext)

**F1 scores**

The F1 scores on the test set of this modified dataset are shown below:

|                            | **BiomedBERT-base abstract+fulltext** |
| -------------------------- | :-----------------------------------: |
| **Cell**                   |                 87.76                 |
| **Cell component**         |                 81.74                 |
| **Tissue**                 |                 72.26                 |
| **Cancer**                 |                 89.29                 |
| **Organ**                  |                 84.18                 |
| **Multi-tissue structure** |                 72.65                 |
|  |  |  |  |
| **Overall**                |               84.22               |

## Usage

The model can be directly used from HuggingFace in a NER pipeline. However, we note that:
- The model was trained on sentence-level data, and it works best when the input is split
- Each sentence to tag must be surrounded by the flag corresponding to the entity type one wishes to identify, as in: `<entity_type>sentence</entity_type>`. In the case of this fine-tuned model, the entity type should be `'ALL'`.
- Since additional `'O'` labels are used in the AIONER scheme, the outputs should be postprocessed before aggregating the tags

We provide helper functions to tag individual texts in the [main repository](https://github.com/sirisacademic/AIObioEnts/)

````python
from tagging_fn import process_one_text
from transformers import pipeline
pipe = pipeline('ner', model='SIRIS-Lab/AIObioEnts-AnatEM-pubmedbert-full', aggregation_strategy='none', device=0)
process_one_text(text_to_tag, pipeline=pipe, entity_type='ALL')
````

## References

[[1] Ling Luo, Chih-Hsuan Wei, Po-Ting Lai, Robert Leaman, Qingyu Chen, and Zhiyong Lu. "AIONER: All-in-one scheme-based biomedical named entity recognition using deep learning." Bioinformatics, Volume 39, Issue 5, May 2023, btad310.](https://doi.org/10.1093/bioinformatics/btad310)
