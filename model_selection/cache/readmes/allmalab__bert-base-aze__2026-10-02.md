---
license: mit
tags:
- generated_from_trainer
base_model: google-bert/bert-base-uncased
model-index:
- name: bert-base-aze
  results: []
---
# aLLMA-Base
**Note:** This model is not a fine-tuned version of BERT, we have simply used the same architecture.

### Citation
If you use the dataset, please cite the following paper:
```bib
@inproceedings{isbarov-etal-2024-open,
    title = "Open foundation models for {A}zerbaijani language",
    author = "Isbarov, Jafar  and
      Huseynova, Kavsar  and
      Mammadov, Elvin  and
      Hajili, Mammad  and
      Ataman, Duygu",
    editor = {Ataman, Duygu  and
      Derin, Mehmet Oguz  and
      Ivanova, Sardana  and
      K{\"o}ksal, Abdullatif  and
      S{\"a}lev{\"a}, Jonne  and
      Zeyrek, Deniz},
    booktitle = "Proceedings of the First Workshop on Natural Language Processing for Turkic Languages (SIGTURK 2024)",
    month = aug,
    year = "2024",
    address = "Bangkok, Thailand and Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2024.sigturk-1.2",
    pages = "18--28",
    abstract = "The emergence of multilingual large language models has enabled the development of language understanding and generation systems in Azerbaijani. However, most of the production-grade systems rely on cloud solutions, such as GPT-4. While there have been several attempts to develop open foundation models for Azerbaijani, these works have not found their way into common use due to a lack of systemic benchmarking. This paper encompasses several lines of work that promote open-source foundation models for Azerbaijani. We introduce (1) a large text corpus for Azerbaijani, (2) a family of encoder-only language models trained on this dataset, (3) labeled datasets for evaluating these models, and (4) extensive evaluation that covers all major open-source models with Azerbaijani support.",
}
```
https://arxiv.org/abs/2407.02337
### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 22
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 88
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: cosine
- lr_scheduler_warmup_steps: 10000
- num_epochs: 10
- mixed_precision_training: Native AMP


### Framework versions

- Transformers 4.37.1
- Pytorch 2.1.2+cu121
- Datasets 2.16.1
- Tokenizers 0.15.1
