---
language:
- en
license: apache-2.0
tags:
- dialogue-summarization
datasets:
- samsum
model_index:
- name: hybrid_utt-clusterrank_bart-base_samsum_sum
  results:
  - task:
      name: Summarization
      type: summarization
base_model: facebook/bart-base
---

## Paper

## [Domain Adapted Abstractive Summarization of Dialogue using Transfer Learning](https://dl.acm.org/doi/10.1145/3508546.3508640)
Authors: *Rohit Sroch*

## Abstract

Recently, the abstractive dialogue summarization task has been gaining a lot of attention from researchers. Also, unlike news articles and documents with well-structured text, dialogue differs in the sense that it often comes from two or more interlocutors, exchanging information with each other and having an inherent hierarchical structure based on the sequence of utterances by different speakers. This paper proposes a simple but effective hybrid approach that consists of two modules and uses transfer learning by leveraging pretrained language models (PLMs) to generate an abstractive summary. The first module highlights important utterances, capturing the utterance level relationship by adapting an auto-encoding model like BERT based on the unsupervised or supervised method. And then, the second module generates a concise abstractive summary by adapting encoder-decoder models like T5, BART, and PEGASUS. Experiment results on benchmark datasets show that our approach achieves a state-of-the-art performance by adapting to dialogue scenarios and can also be helpful in low-resource settings for domain adaptation.

*Rohit Sroch. 2021. Domain Adapted Abstractive Summarization of Dialogue using Transfer Learning. In 2021 4th International Conference on Algorithms, Computing and Artificial Intelligence (ACAI'21). Association for Computing Machinery, New York, NY, USA, Article 94, 1–6. https://doi.org/10.1145/3508546.3508640*

# hybrid_utt-clusterrank_bart-base_samsum_sum

This model is a fine-tuned version of [facebook/bart-base](https://huggingface.co/facebook/bart-base) on SAMSum dataset for dialogue summarization task.

## Model description

More information needed

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-5
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 10.0
- label_smoothing_factor: 0.1

### Results on Test Set

- predict_gen_len           =      23.9048 
- predict_rouge1             =    **47.355** 
- predict_rouge2             =    **22.4593** 
- predict_rougeL             =    **38.694** 
- predict_rougeLsum          =    **42.98** 
- predict_samples            =       819 
- predict_samples_per_second =       9.279 
- predict_steps_per_second   =       2.322


### Framework versions

- Transformers>=4.8.0
- Pytorch>=1.6.0
- Datasets>=1.10.2
- Tokenizers>=0.10.3

If you use this model, please cite the following paper:

```
@inproceedings{10.1145/3508546.3508640,
    author = {Sroch, Rohit},
    title = {Domain Adapted Abstractive Summarization of Dialogue Using Transfer Learning},
    year = {2021},
    isbn = {9781450385053},
    publisher = {Association for Computing Machinery},
    address = {New York, NY, USA},
    url = {https://doi.org/10.1145/3508546.3508640},
    doi = {10.1145/3508546.3508640},
    articleno = {94},
    numpages = {6},
    keywords = {encoder-decoder, T5, abstractive summary, PEGASUS, BART, dialogue summarization, PLMs, BERT},
    location = {Sanya, China},
    series = {ACAI'21}
} 
```