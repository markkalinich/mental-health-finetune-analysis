---
language: en
tags:
- exbert
license: mit
---

## MSR BiomedELECTRA-base (abstracts only)

<div style="border: 2px solid orange; border-radius:10px; padding:0px 10px; width: fit-content;">

* This model was previously named **"PubMedELECTRA (abstracts)"**.
* You can either adopt the new model name "microsoft/BiomedNLP-BiomedELECTRA-base-uncased-abstract" or update your `transformers` library to version 4.22+ if you need to refer to the old name.

</div>

Pretraining large neural language models, such as BERT and ELECTRA, has led to impressive gains on many natural language processing (NLP) tasks. However, most pretraining efforts focus on general domain corpora, such as newswire and Web. A prevailing assumption is that even domain-specific pretraining can benefit by starting from general-domain language models. [Recent work](https://arxiv.org/abs/2007.15779) shows that for domains with abundant unlabeled text, such as biomedicine, pretraining language models from scratch results in substantial gains over continual pretraining of general-domain language models. [Followup work](https://arxiv.org/abs/2112.07869) explores alternate pretraining strategies and the impact of these on performance on the BLURB benchmark. 

This BiomedELECTRA is pretrained from scratch using _abstracts_ from [PubMed](https://pubmed.ncbi.nlm.nih.gov/).

## Citation

If you find BiomedELECTRA useful in your research, please cite the following paper:

```latex
@misc{https://doi.org/10.48550/arxiv.2112.07869,
  doi = {10.48550/ARXIV.2112.07869},
  url = {https://arxiv.org/abs/2112.07869},
  author = {Tinn, Robert and Cheng, Hao and Gu, Yu and Usuyama, Naoto and Liu, Xiaodong and Naumann, Tristan and Gao, Jianfeng and Poon, Hoifung},
  keywords = {Computation and Language (cs.CL), Machine Learning (cs.LG), FOS: Computer and information sciences, FOS: Computer and information sciences},
  title = {Fine-Tuning Large Neural Language Models for Biomedical Natural Language Processing},
  publisher = {arXiv},
  year = {2021},
  copyright = {arXiv.org perpetual, non-exclusive license}
}
```
