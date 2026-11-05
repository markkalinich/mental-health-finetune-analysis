---
language:
- fr
license: mit
library_name: transformers
tags:
- biomedical
- clinical
- life sciences
- neuron
datasets:
- rntc/biomed-fr
pipeline_tag: fill-mask
widget:
- text: Les médicaments <mask> typiques sont largement utilisés dans le traitement
    de première intention des patients schizophrènes.
---

<a href=https://camembert-bio-model.fr/>
  <img width="300px" src="./camembert-bio-logo.png">
</a>

# CamemBERT-bio : a Tasty French Language Model Better for your Health

CamemBERT-bio is a state-of-the-art french biomedical language model built using continual-pretraining from [camembert-base](https://huggingface.co/camembert-base). 
It was trained on a french public biomedical corpus of 413M words containing scientific documents, drug leaflets and clinical cases extrated from theses and articles.
It shows 2.54 points of F1 score improvement on average on 5 different biomedical named entity recognition tasks compared to [camembert-base](https://huggingface.co/camembert-base).

## Absract

Clinical data in hospitals are increasingly accessible for research through clinical data warehouses, however these documents are unstructured. It is therefore necessary to extract information from medical
reports to conduct clinical studies. Transfer learning with BERT-like models such as CamemBERT
has allowed major advances, especially for named entity recognition. However, these models are
trained for plain language and are less efficient on biomedical data. This is why we propose a new
french public biomedical dataset on which we have continued the pre-training of CamemBERT. Thus,
we introduce a first version of CamemBERT-bio, a specialized public model for the french biomedical
domain that shows 2.54 points of F1 score improvement on average on different biomedical named
entity recognition tasks.

- **Developed by:** [Rian Touchent](https://rian-t.github.io), [Eric Villemonte de La Clergerie](http://pauillac.inria.fr/~clerger/)
- **Logo by:** [Alix Chagué](https://alix-tz.github.io)
- **License:** MIT

<!-- ### Model Sources [optional] -->

<!-- Provide the basic links for the model. -->

<!-- - **Website:** camembert-bio-model.fr -->
<!-- - **Paper [optional]:** [More Information Needed] -->
<!-- - **Demo [optional]:** [More Information Needed] -->


## Training Details

### Training Data

<!-- This should link to a Data Card, perhaps with a short stub of information on what the training data is all about as well as documentation related to data pre-processing or additional filtering. -->

| **Corpus** | **Details**                                                        | **Size** |
|------------|--------------------------------------------------------------------|------------|
| ISTEX      | diverse scientific literature indexed on ISTEX  | 276 M      |
| CLEAR      | drug leaflets                                           | 73 M       |
| E3C        | various documents from journals, drug leaflets, and clinical cases | 64 M       |
| Total      |                                                                    | 413 M      |


### Training Procedure 

<!-- This relates heavily to the Technical Specifications. Content here should link to that section when it is relevant to the training procedure. -->

We used continual-pretraining from [camembert-base](https://huggingface.co/camembert-base). 
We trained the model using the Masked Language Modeling (MLM) objective with Whole Word Masking for 50k steps during 39 hours
with 2 Tesla V100.

## Evaluation

<!-- This section describes the evaluation protocols and provides the results. -->

### Fine-tuning

For fine-tuning, we utilized Optuna to select the hyperparameters. 
The learning rate was set to 5e-5, with a warmup ratio of 0.224 and a batch size of 16. 
The fine-tuning process was carried out for 2000 steps. 
For prediction, a simple linear layer was added on top of the model. 
Notably, none of the CamemBERT layers were frozen during the fine-tuning process.

### Scoring

To evaluate the performance of the model, we used the seqeval tool in strict mode with the IOB2 scheme. 
For each evaluation, the best fine-tuned model on the validation set was selected to calculate the final score on the test set. 
To ensure reliability, we averaged over 10 evaluations with different seeds.

### Results 

| Style        | Dataset | Score | CamemBERT         | CamemBERT-bio         |
| :----------- | :------ | :---- | :---------------: | :-------------------: |
| Clinical     | CAS1    | F1    | 70\.50 ~~±~~ 1.75 | **73\.03 ~~±~~ 1.29** |
|              |         | P     | 70\.12 ~~±~~ 1.93 | **71\.71 ~~±~~ 1.61**     |
|              |         | R     | 70\.89 ~~±~~ 1.78 | **74\.42 ~~±~~ 1.49** |
|              | CAS2    | F1    | 79\.02 ~~±~~ 0.92 | **81\.66 ~~±~~ 0.59** |
|              |         | P     | 77\.3 ~~±~~ 1.36  | **80\.96 ~~±~~ 0.91** |
|              |         | R     | 80\.83 ~~±~~ 0.96 | **82\.37 ~~±~~ 0.69** |
|              | E3C     | F1    | 67\.63 ~~±~~ 1.45 | **69\.85 ~~±~~ 1.58** |
|              |         | P     | 78\.19 ~~±~~ 0.72 | **79\.11 ~~±~~ 0.42** |
|              |         | R     | 59\.61 ~~±~~ 2.25 | **62\.56 ~~±~~ 2.50** |
| Drug leaflets      | EMEA    | F1    | 74\.14 ~~±~~ 1.95 | **76\.71 ~~±~~ 1.50** |
|              |         | P     | 74\.62 ~~±~~ 1.97 | **76\.92 ~~±~~ 1.96** |
|              |         | R     | 73\.68 ~~±~~ 2.22 | **76\.52 ~~±~~ 1.62** |
| Scientific | MEDLINE | F1    | 65\.73 ~~±~~ 0.40 | **68\.47 ~~±~~ 0.54** |
|              |         | P     | 64\.94 ~~±~~ 0.82 | **67\.77 ~~±~~ 0.88** |
|              |         | R     | 66\.56 ~~±~~ 0.56 | **69\.21 ~~±~~ 1.32** |


## Environmental Impact estimation

<!-- Total emissions (in grams of CO2eq) and additional considerations, such as electricity usage, go here. Edit the suggested text below accordingly -->

- **Hardware Type:** 2 x Tesla V100
- **Hours used:** 39 hours
- **Provider:** INRIA clusters
- **Compute Region:** Paris, France
- **Carbon Emitted:** 0.84 kg CO2 eq.

<!-- ## Citation [optional] -->

<!-- If there is a paper or blog post introducing the model, the APA and Bibtex information for that should go in this section. -->

<!-- **BibTeX:** -->

## Citation information

```bibtex

@inproceedings{touchent-de-la-clergerie-2024-camembert-bio,
    title = "{C}amem{BERT}-bio: Leveraging Continual Pre-training for Cost-Effective Models on {F}rench Biomedical Data",
    author = "Touchent, Rian  and
      de la Clergerie, {\'E}ric",
    editor = "Calzolari, Nicoletta  and
      Kan, Min-Yen  and
      Hoste, Veronique  and
      Lenci, Alessandro  and
      Sakti, Sakriani  and
      Xue, Nianwen",
    booktitle = "Proceedings of the 2024 Joint International Conference on Computational Linguistics, Language Resources and Evaluation (LREC-COLING 2024)",
    month = may,
    year = "2024",
    address = "Torino, Italia",
    publisher = "ELRA and ICCL",
    url = "https://aclanthology.org/2024.lrec-main.241",
    pages = "2692--2701",
    abstract = "Clinical data in hospitals are increasingly accessible for research through clinical data warehouses. However these documents are unstructured and it is therefore necessary to extract information from medical reports to conduct clinical studies. Transfer learning with BERT-like models such as CamemBERT has allowed major advances for French, especially for named entity recognition. However, these models are trained for plain language and are less efficient on biomedical data. Addressing this gap, we introduce CamemBERT-bio, a dedicated French biomedical model derived from a new public French biomedical dataset. Through continual pre-training of the original CamemBERT, CamemBERT-bio achieves an improvement of 2.54 points of F1-score on average across various biomedical named entity recognition tasks, reinforcing the potential of continual pre-training as an equally proficient yet less computationally intensive alternative to training from scratch. Additionally, we highlight the importance of using a standard evaluation protocol that provides a clear view of the current state-of-the-art for French biomedical models.",
}


@inproceedings{touchent:hal-04130187,
  TITLE = {{CamemBERT-bio : Un mod{\`e}le de langue fran{\c c}ais savoureux et meilleur pour la sant{\'e}}},
  AUTHOR = {Touchent, Rian and Romary, Laurent and De La Clergerie, Eric},
  URL = {https://hal.science/hal-04130187},
  BOOKTITLE = {{18e  Conf{\'e}rence en Recherche d'Information et Applications \\ 16e Rencontres Jeunes Chercheurs en RI \\ 30e Conf{\'e}rence sur le Traitement Automatique des Langues Naturelles \\ 25e Rencontre des {\'E}tudiants Chercheurs en Informatique pour le Traitement Automatique des Langues}},
  ADDRESS = {Paris, France},
  EDITOR = {Servan, Christophe and Vilnat, Anne},
  PUBLISHER = {{ATALA}},
  PAGES = {323-334},
  YEAR = {2023},
  KEYWORDS = {comptes rendus m{\'e}dicaux ; TAL clinique ; CamemBERT ; extraction d'information ; biom{\'e}dical ; reconnaissance d'entit{\'e}s nomm{\'e}es},
  HAL_ID = {hal-04130187},
  HAL_VERSION = {v1},
}
```

<!-- [More Information Needed] -->

<!-- **APA:** -->

<!-- [More Information Needed] -->