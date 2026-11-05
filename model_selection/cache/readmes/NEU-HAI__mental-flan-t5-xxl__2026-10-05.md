---
license: apache-2.0
language:
- en
tags:
- mental
- mental health
- large language model
- flan-t5
---
# Model Card for mental-flan-t5-xxl

<!-- Provide a quick summary of what the model is/does. -->

This is a fine-tuned large language model for mental health prediction via online text data.


## Model Details

### Model Description

We fine-tune a FLAN-T5-XXL model with 4 high-quality text (6 tasks in total) datasets for the mental health prediction scenario: Dreaddit, DepSeverity, SDCNL, and CCRS-Suicide.
We have a separate model, fine-tuned on Alpaca, namely Mental-Alpaca, shared [here](https://huggingface.co/NEU-HAI/mental-alpaca) 

- **Developed by:** Northeastern University Human-Centered AI Lab
- **Model type:** Sequence-to-sequence Text-generation 
- **Language(s) (NLP):** English
- **License:** Apache 2.0 License
- **Finetuned from model :** [FLAN-T5-XXL](https://huggingface.co/google/flan-t5-xxl)

### Model Sources

<!-- Provide the basic links for the model. -->

- **Repository:** https://github.com/neuhai/Mental-LLM
- **Paper:** https://arxiv.org/abs/2307.14385


## Uses

<!-- Address questions around how the model is intended to be used, including the foreseeable users of the model and those affected by the model. -->

### Direct Use

The model is intended to be used for research purposes only in English.
The model has been fine-tuned for mental health prediction via online text data. Detailed information about the fine-tuning process and prompts can be found in our [paper](https://arxiv.org/abs/2307.14385).
The use of this model should also comply with the restrictions from [FLAN-T5-XXL](https://huggingface.co/google/flan-t5-xxl)


### Out-of-Scope Use

The out-of-scope use of this model should comply with [FLAN-T5-XXL](https://huggingface.co/google/flan-t5-xxl).

## Bias, Risks, and Limitations

<!-- This section is meant to convey both technical and sociotechnical limitations. -->

The Bias, Risks, and Limitations of this model should also comply with [FLAN-T5-XXL](https://huggingface.co/google/flan-t5-xxl).


## How to Get Started with the Model

Use the code below to get started with the model.

```
from transformers import T5ForConditionalGeneration, T5Tokenizer

tokenizer = T5ForConditionalGeneration.from_pretrained("NEU-HAI/mental-flan-t5-xxl")
mdoel =  T5Tokenizer.from_pretrained("NEU-HAI/mental-flan-t5-xxl")
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