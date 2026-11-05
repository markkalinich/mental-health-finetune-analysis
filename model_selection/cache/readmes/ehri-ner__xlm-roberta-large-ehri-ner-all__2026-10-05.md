---
license: eupl-1.1
datasets:
- ehri-ner/ehri-ner-all
language:
- cs
- de
- en
- fr
- hu
- nl
- pl
- sk
- yi
metrics:
- name: f1
  type: f1
  value: 81.5
pipeline_tag: token-classification
tags:
- Holocaust
- EHRI
base_model: FacebookAI/xlm-roberta-large
---
# Model Card for ehri-ner/xlm-roberta-large-ehri-ner-all

<!-- Provide a quick summary of what the model is/does. -->

The European Holocaust Research Infrastructure (EHRI) aims to support Holocaust research by making information
about dispersed Holocaust material accessible and interconnected through its services. Creating a tool capable of
detecting named entities in texts such as Holocaust testimonies or archival descriptions would make it easier to
link more material with relevant identifiers in domain-specific controlled vocabularies, semantically enriching it, and
making it more discoverable. The xlm-roberta-large-ehri-ner-all model finetunes XLM-RoBERTa (XLM-R) for Holocaust-related Named Entity Recognition (NER)
using the EHRI-NER dataset, a multilingual dataset (Czech, German, English, French, Hungarian, Dutch, Polish, Slovak, Yiddish) for NER in Holocaust-related texts.
The EHRI-NER dataset is built by aggregating all the annotated documents in the EHRI Online Editions and converting them to a
format suitable for training NER models. The results of our experiments show that despite our relatively small
dataset, in a multilingual experiment setup, the overall F1 score achieved by XLM-R fine-tuned on multilingual annotations
is 81.5%.


### Model Description

<!-- Provide a longer summary of what this model is. -->


- **Developed by:** Dermentzi, M. & Scheithauer, H.
- **Funded by:** European Commission call H2020-INFRAIA-2018–2020. Grant agreement ID 871111. DOI 10.3030/871111.
- **Language(s) (NLP):** The model was fine-tuned on cs, de, en, fr, hu, nl, pl, sk, yi data but it may work for more languages due to the use of a multilingual base model (XLM-R) with cross-lingual transfer capabilities.
- **License:** EUPL-1.2
- **Finetuned from model:** FacebookAI/xlm-roberta-large

<!-- ### Model Sources [optional]

<!-- Provide the basic links for the model.

- **Repository:** [More Information Needed]
- **Paper [optional]:** [More Information Needed]
-->

## Uses

<!-- Address questions around how the model is intended to be used, including the foreseeable users of the model and those affected by the model. -->
This model was developed for research purposes in the context of the EHRI-3 project. Specifically, the aim was to determine 
whether a single model can be trained to recognize entities across different document types and languages in Holocaust-related texts. 
The results of our experiments show that despite our relatively small dataset, in a multilingual experiment setup, the overall F1 score achieved by 
XLM-R fine-tuned on multilingual Holocaust-related annotations is 81.5%. We argue that this score is sufficiently high to consider the next steps 
towards deploying this model, i.e., receiving more feedback from the EHRI community. Once we have a stable model that EHRI stakeholders are 
satisfied with, this model and its potential successors are intended to be used as part of an EHRI editorial pipeline whereby, 
upon inputting some text into a tool that supports our model, potential named entities within the text will be automatically pre-annotated 
in a way that helps our intended users (i.e., researchers and professional archivists) detect them faster and link them to their associated controlled vocabulary entities from the 
custom EHRI controlled vocabularies and authority sets. This has the potential to facilitate metadata enrichment of descriptions 
in the EHRI Portal and enhance their discoverability. It would also make it easier for EHRI to develop new Online Editions and 
unlock new ways for archivists and researchers within the EHRI network to organize, 
analyze, and present their materials and research data in ways that would otherwise require a lot of manual work.

## Limitations

<!-- This section is meant to convey both technical and sociotechnical limitations. -->
The dataset used to fine-tune this model stems from a series of manually annotated
digital scholarly editions, the EHRI Online Editions. The original purpose
of these editions was not to provide a dataset
for training NER models, although we argue that they nevertheless
constitute a high-quality resource that is
suitable to be used in this way. However, users should still be mindful that 
our dataset repurposes a resource that was not built for purpose. 

The fine-tuned model occasionally misclassifies entities
as non-entity tokens, I-GHETTO being the most
confused entity. The fine-tuned model occasionally
encounters challenges in extracting multi-tokens
entities, such as I-CAMP, I-LOC, and I-ORG, which
are sometimes confused with the beginning of an
entity. Moreover, it tends to misclassify B-GHETTO
and B-CAMP as B-LOC, which is not surprising
given that they are semantically close.

This model was envisioned to work as part of EHRI-related editorial and publishing pipelines and may not be suitable for 
the purposes of other users/organizations.

### Recommendations

For more information, we encourage potential users to read the paper accompanying this model:
Dermentzi, M., & Scheithauer, H. (2024, May). Repurposing Holocaust-Related Digital Scholarly Editions to Develop Multilingual Domain-Specific Named Entity Recognition Tools. LREC-COLING 2024 - Joint International Conference on Computational Linguistics, Language Resources and Evaluation. HTRes@LREC-COLING 2024, Torino, Italy. https://hal.science/hal-04547222

## Citation

**BibTeX:**
@inproceedings{dermentzi_repurposing_2024,
	address = {Torino, Italy},
	title = {Repurposing {Holocaust}-{Related} {Digital} {Scholarly} {Editions} to {Develop} {Multilingual} {Domain}-{Specific} {Named} {Entity} {Recognition} {Tools}},
	url = {https://hal.science/hal-04547222},
	abstract = {The European Holocaust Research Infrastructure (EHRI) aims to support Holocaust research by making information about dispersed Holocaust material accessible and interconnected through its services. Creating a tool capable of detecting named entities in texts such as Holocaust testimonies or archival descriptions would make it easier to link more material with relevant identifiers in domain-specific controlled vocabularies, semantically enriching it, and making it more discoverable. With this paper, we release EHRI-NER, a multilingual dataset (Czech, German, English, French, Hungarian, Dutch, Polish, Slovak, Yiddish) for Named Entity Recognition (NER) in Holocaust-related texts. EHRI-NER is built by aggregating all the annotated documents in the EHRI Online Editions and converting them to a format suitable for training NER models. We leverage this dataset to fine-tune the multilingual Transformer-based language model XLM-RoBERTa (XLM-R) to determine whether a single model can be trained to recognize entities across different document types and languages. The results of our experiments show that despite our relatively small dataset, in a multilingual experiment setup, the overall F1 score achieved by XLM-R fine-tuned on multilingual annotations is 81.5{\textbackslash}\%. We argue that this score is sufficiently high to consider the next steps towards deploying this model.},
	urldate = {2024-04-29},
	booktitle = {{LREC}-{COLING} 2024 - {Joint} {International} {Conference} on {Computational} {Linguistics}, {Language} {Resources} and {Evaluation}},
	publisher = {ELRA Language Resources Association (ELRA); International Committee on Computational Linguistics (ICCL)},
	author = {Dermentzi, Maria and Scheithauer, Hugo},
	month = may,
	year = {2024},
	keywords = {Digital Editions, Holocaust Testimonies, Multilingual, Named Entity Recognition, Transfer Learning, Transformers},
}

**APA:**
Dermentzi, M., & Scheithauer, H. (2024, May). Repurposing Holocaust-Related Digital Scholarly Editions to Develop Multilingual Domain-Specific Named Entity Recognition Tools. LREC-COLING 2024 - Joint International Conference on Computational Linguistics, Language Resources and Evaluation. HTRes@LREC-COLING 2024, Torino, Italy. https://hal.science/hal-04547222