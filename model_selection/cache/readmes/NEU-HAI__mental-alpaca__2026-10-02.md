---
license: cc-by-nc-4.0
language:
- en
tags:
- mental
- mental health
- large language model
- alpaca
---
# Model Card for mental-alpaca

<!-- Provide a quick summary of what the model is/does. -->

This is a fine-tuned large language model for mental health prediction via online text data.

## Model Details

### Model Description

<!-- Provide a longer summary of what this model is. -->

We fine-tune an Alpaca model with 4 high-quality text (6 tasks in total) datasets for the mental health prediction scenario: Dreaddit, DepSeverity, SDCNL, and CCRS-Suicide.
We have a separate model, fine-tuned on FLAN-T5-XXL, namely Mental-FLAN-T5, shared [here](https://huggingface.co/NEU-HAI/mental-flan-t5-xxl) 


- **Developed by:** Northeastern University Human-Centered AI Lab
- **Model type:** Sequence-to-sequence Text-generation
- **Language(s) (NLP):** English
- **License:** cc-by-nc-4.0 
- **Finetuned from model:** https://github.com/tatsu-lab/stanford_alpaca

### Model Sources [optional]

<!-- Provide the basic links for the model. -->

- **Repository:** https://github.com/neuhai/Mental-LLM
- **Paper:** https://arxiv.org/abs/2307.14385

## Uses

<!-- Address questions around how the model is intended to be used, including the foreseeable users of the model and those affected by the model. -->

### Direct Use

<!-- This section is for the model use without fine-tuning or plugging into a larger ecosystem/app. -->

The model is intended to be used for research purposes only in English.
The model has been fine-tuned for mental health prediction via online text data. Detailed information about the fine-tuning process and prompts can be found in our [paper](https://arxiv.org/abs/2307.14385).
The use of this model should also comply with the restrictions from [stanford_alpaca project](https://github.com/tatsu-lab/stanford_alpaca) and [Llama-2-7b](https://huggingface.co/meta-llama/Llama-2-7b).



### Out-of-Scope Use

<!-- This section addresses misuse, malicious use, and uses that the model will not work well for. -->

The out-of-scope use of this model should comply with [stanford_alpaca project](https://github.com/tatsu-lab/stanford_alpaca) and [Llama-2-7b](https://huggingface.co/meta-llama/Llama-2-7b).


## Bias, Risks, and Limitations

The Bias, Risks, and Limitations of this model should also comply with [stanford_alpaca project](https://github.com/tatsu-lab/stanford_alpaca) and [Llama-2-7b](https://huggingface.co/meta-llama/Llama-2-7b).


## How to Get Started with the Model

Use the code below to get started with the model.

```
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("NEU-HAI/Llama-2-7b-alpaca-cleaned")
model = AutoModelForCausalLM.from_pretrained("NEU-HAI/Llama-2-7b-alpaca-cleaned")
```

## Training Details and Evaluation


Detailed information about our work can be found in our [paper](https://arxiv.org/abs/2307.14385).

## Citation

```
@article{xu2023leveraging,
  title={Mental-LLM: Leveraging large language models for mental health prediction via online text data},
  author={Xu, Xuhai and Yao, Bingshen and Dong, Yuanzhe and Gabriel, Saadia and Yu, Hong and Ghassemi, Marzyeh and Hendler, James and Dey, Anind K and Wang, Dakuo},
  journal={arXiv preprint arXiv:2307.14385},
  year={2023}
}
```
