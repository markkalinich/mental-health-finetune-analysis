---
license: mit
pipeline_tag: sentence-similarity
tags:
- sentence-similarity
- sentence-transformers
- medical
model_name: PubMedBERT-base-uncased-sts-combined
---
# PubMedBERT-base-uncased-sts-combined 

This repo contains a fine-tuned version of PubMedBERT to generate semantic textual similarity pairs, primarily for use in the `sts-select` feature selection package detailed [here](https://github.com/bcwarner/sts-select). 
Details about the model and vocabulary can be in the paper [here](https://huggingface.co/papers/2308.09892).

## Citation

If you use this model for STS-based feature selection, please cite the following paper:

```
@misc{warner2023utilizing,
      title={Utilizing Semantic Textual Similarity for Clinical Survey Data Feature Selection}, 
      author={Benjamin C. Warner and Ziqi Xu and Simon Haroutounian and Thomas Kannampallil and Chenyang Lu},
      year={2023},
      eprint={2308.09892},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}

```
Additionally, the original model and fine-tuning papers should be cited as follows:
```
@article{Gu_Tinn_Cheng_Lucas_Usuyama_Liu_Naumann_Gao_Poon_2021, title={Domain-specific language model pretraining for biomedical natural language processing}, volume={3}, number={1}, journal={ACM Transactions on Computing for Healthcare (HEALTH)}, publisher={ACM New York, NY}, author={Gu, Yu and Tinn, Robert and Cheng, Hao and Lucas, Michael and Usuyama, Naoto and Liu, Xiaodong and Naumann, Tristan and Gao, Jianfeng and Poon, Hoifung}, year={2021}, pages={1–23} }

@inproceedings{Cer_Diab_Agirre_Lopez-Gazpio_Specia_2017, address={Vancouver, Canada}, title={SemEval-2017 Task 1: Semantic Textual Similarity Multilingual and Crosslingual Focused Evaluation}, url={https://aclanthology.org/S17-2001}, DOI={10.18653/v1/S17-2001}, booktitle={Proceedings of the 11th International Workshop on Semantic Evaluation (SemEval-2017)}, publisher={Association for Computational Linguistics}, author={Cer, Daniel and Diab, Mona and Agirre, Eneko and Lopez-Gazpio, Iñigo and Specia, Lucia}, year={2017}, month=aug, pages={1–14} }
@article{Chiu_Pyysalo_Vulić_Korhonen_2018, title={Bio-SimVerb and Bio-SimLex: wide-coverage evaluation sets of word similarity in biomedicine}, volume={19}, number={1}, journal={BMC bioinformatics}, publisher={BioMed Central}, author={Chiu, Billy and Pyysalo, Sampo and Vulić, Ivan and Korhonen, Anna}, year={2018}, pages={1–13} }
@inproceedings{May_2021, title={Machine translated multilingual STS benchmark dataset.}, url={https://github.com/PhilipMay/stsb-multi-mt}, author={May, Philip}, year={2021} }
@article{Pedersen_Pakhomov_Patwardhan_Chute_2007, title={Measures of semantic similarity and relatedness in the biomedical domain}, volume={40}, number={3}, journal={Journal of biomedical informatics}, publisher={Elsevier}, author={Pedersen, Ted and Pakhomov, Serguei VS and Patwardhan, Siddharth and Chute, Christopher G}, year={2007}, pages={288–299} }
```
