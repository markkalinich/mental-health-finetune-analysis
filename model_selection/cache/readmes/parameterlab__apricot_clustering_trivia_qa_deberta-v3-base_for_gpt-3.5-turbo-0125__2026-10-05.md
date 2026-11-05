---
license: mit
base_model: microsoft/deberta-v3-base
tags:
- generated_from_trainer
- calibration
- uncertainty
model-index:
- name: apricot_clustering_trivia_qa_deberta-v3-base_for_gpt-3.5-turbo-0125
  results: []
datasets:
- mandarjoshi/trivia_qa
library_name: transformers
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# apricot_clustering_trivia_qa_deberta-v3-base_for_gpt-3.5-turbo-0125

This model is fine-tuned for black-box LLM calibration as part of the 🍑 Apricot paper ["Calibrating Large Language Models Using Their Generations Only"](https://arxiv.org/abs/2403.05973) (ACL 2024).

## Model description

This model is a fine-tuned version of [microsoft/deberta-v3-base](https://huggingface.co/microsoft/deberta-v3-base) to predict the calibration score for the gpt-3.5-turbo-0125 model on the questions from the trivia_qa dataset. It uses the clustering type of calibration target score.

## Intended uses & limitations

More information needed


## Training procedure

### Training hyperparameters

This model was trained with the code available on the [parameterlab/apricot GitHub repository](https://github.com/parameterlab/apricot) using the following command:
```shell
python3 run_regression_experiment.py --model-identifier lmsys/vicuna-7b-v1.5 --dataset-name trivia_qa --device cuda:0 --num-training-steps 600 --num-in-context-samples 10 --data-dir $data_dir --model-save-dir $model_save_dir --result-dir $result_dir --lr 0.00003369 --weight-decay 0.008936 --model-save-dir models --push-to-hub
```

### Framework versions

- Transformers 4.32.0
- Pytorch 2.0.0+cu117
- Datasets 2.14.6
- Tokenizers 0.13.3


## Citation
If you find 🍑 Apricot models useful for your work, please cite our paper:
``` latex
@inproceedings{ulmer-etal-2024-calibrating,
    title = "Calibrating Large Language Models Using Their Generations Only",
    author = "Ulmer, Dennis  and
      Gubri, Martin  and
      Lee, Hwaran  and
      Yun, Sangdoo  and
      Oh, Seong",
    editor = "Ku, Lun-Wei  and
      Martins, Andre  and
      Srikumar, Vivek",
    booktitle = "Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)",
    month = aug,
    year = "2024",
    address = "Bangkok, Thailand",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2024.acl-long.824",
    doi = "10.18653/v1/2024.acl-long.824",
    pages = "15440--15459",
    abstract = "As large language models (LLMs) are increasingly deployed in user-facing applications, building trust and maintaining safety by accurately quantifying a model{'}s confidence in its prediction becomes even more important. However, finding effective ways to calibrate LLMs{---}especially when the only interface to the models is their generated text{---}remains a challenge. We propose APRICOT (Auxiliary prediction of confidence targets): A method to set confidence targets and train an additional model that predicts an LLM{'}s confidence based on its textual input and output alone. This approach has several advantages: It is conceptually simple, does not require access to the target model beyond its output, does not interfere with the language generation, and has a multitude of potential usages, for instance by verbalizing the predicted confidence or using it to re-prompting the LLM to accurately reflecting its uncertainty. We show how our approach performs competitively in terms of calibration error for white-box and black-box LLMs on closed-book question-answering to detect incorrect LLM answers.",
}
```