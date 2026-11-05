---
license: bigscience-bloom-rail-1.0
language:
- fr
- en
pipeline_tag: text-classification
base_model:
- cmarkea/bloomz-3b-sft-chat
---


Bloomz-3b-guardrail
---------------------

We introduce the Bloomz-3b-guardrail model, which is a fine-tuning of the [Bloomz-3b-sft-chat](https://huggingface.co/cmarkea/bloomz-3b-sft-chat) model. This model is designed to detect the toxicity of a text in five modes:

* Obscene: Content that is offensive, indecent, or morally inappropriate, especially in relation to social norms or standards of decency.
* Sexual explicit: Content that presents explicit sexual aspects in a clear and detailed manner.
* Identity attack: Content that aims to attack, denigrate, or harass someone based on their identity, especially related to characteristics such as race, gender, sexual orientation, religion, ethnic origin, or other personal aspects.
* Insult: Offensive, disrespectful, or hurtful content used to attack or denigrate a person.
* Threat: Content that presents a direct threat to an individual.

This kind of modeling can be ideal for monitoring and controlling the output of generative models, as well as measuring the generated degree of toxicity.

Training
--------

The training dataset consists of 500k examples of comments in English and 500k comments in French (translated by Google Translate), each annotated with a probablity toxicity severity. The dataset used is provided by [Jigsaw](https://jigsaw.google.com/approach/) as part of a Kaggle competition : [Jigsaw Unintended Bias in Toxicity Classification](https://www.kaggle.com/competitions/jigsaw-unintended-bias-in-toxicity-classification/data). As the score represents the probability of a toxicity mode, an optimization goal of cross-entropy type has been chosen:
$$loss=l_{\mathrm{obscene}}+l_{\mathrm{sexual\_explicit}}+l_{\mathrm{identity\_attack}}+l_{\mathrm{insult}}+l_{\mathrm{threat}}$$
with
$$l_i=\frac{-1}{\vert\mathcal{O}\vert}\sum_{o\in\mathcal{O}}\mathrm{score}_{i,o}\log(\sigma(\mathrm{logit}_{i,o}))+(\mathrm{score}_{i,o}-1)\log(1-\sigma(\mathrm{logit}_{i,o}))$$
Where sigma is the sigmoid function and O represents the set of learning observations.

Benchmark
---------

Pearson's inter-correlation was chosen as a measure. Pearson's inter-correlation is a measure ranging from -1 to 1, where 0 represents no correlation, -1 represents perfect negative correlation, and 1 represents perfect positive correlation. The goal is to quantitatively measure the correlation between the model's scores and the scores assigned by judges for 730 comments not seen during training.

| Model                                                                         | Language | Obsecene (x100)         | Sexual explicit (x100)        | Identity attack (x100)        | Insult (x100)        | Threat (x100)        | Mean |
|------------------------------------------------------------------------------:|:---------|:-----------------------:|:-----------------------------:|:-----------------------------:|:--------------------:|:--------------------:|:----:|
| [Bloomz-560m-guardrail](https://huggingface.co/cmarkea/bloomz-560m-guardrail) | French   | 64                      | 74                            | 72                            | 70                   | 58                   | 68   |
| [Bloomz-560m-guardrail](https://huggingface.co/cmarkea/bloomz-560m-guardrail) | English  | 63                      | 63                            | 62                            | 70                   | 51                   | 62   |
| [Bloomz-3b-guardrail](https://huggingface.co/cmarkea/bloomz-3b-guardrail)     | French   | 71                      | 82                            | 84                            | 77                   | 77                   | 78   |
| [Bloomz-3b-guardrail](https://huggingface.co/cmarkea/bloomz-3b-guardrail)     | English  | 74                      | 76                            | 79                            | 76                   | 79                   | 77   |

With a correlation of approximately 65 for the 560m model and approximately 80 for the 3b model, the output is highly correlated with the judges' scores.


Opting for the maximum of different modes results in a score extremely close to the target toxicity of the original dataset, with a correlation of 0.976 and a mean absolute error of 0.013&plusmn;0.04. Therefore, this approach serves as a robust approximation for evaluating the overall performance of the model, transcending rare toxicity modes. Taking a toxicity threshold &ge; 0.5 to create the target, we have 240 positive cases out of 730 observations. Consequently, we will determine the Precision-Recall AUC, ROC AUC, accuracy, and the F1-score.

| Model                                                                         | Language | PR AUC (%)    | ROC AUC (%)       | Accuracy (%)       | F1-score (%)    |
|------------------------------------------------------------------------------:|:---------|:-------------:|:-----------------:|:------------------:|:---------------:|
| [Bloomz-560m-guardrail](https://huggingface.co/cmarkea/bloomz-560m-guardrail) | French   | 77            | 85                | 78                 | 60              |
| [Bloomz-560m-guardrail](https://huggingface.co/cmarkea/bloomz-560m-guardrail) | English  | 77            | 84                | 79                 | 62              |
| [Bloomz-3b-guardrail](https://huggingface.co/cmarkea/bloomz-3b-guardrail)     | French   | 82            | 89                | 84                 | 72              |
| [Bloomz-3b-guardrail](https://huggingface.co/cmarkea/bloomz-3b-guardrail)     | English  | 80            | 88                | 82                 | 70              |

How to Use Bloomz-3b-guardrail
--------------------------------

The following example utilizes the API Pipeline of the Transformers library.

```python
from transformers import pipeline

guardrail = pipeline("text-classification", "cmarkea/bloomz-3b-guardrail")

list_text: List[str] = [...]
result = guardrail(
    list_text,
    return_all_scores=True, # Crucial for assessing all modalities of toxicity!
    function_to_apply='sigmoid' # To ensure obtaining a score between 0 and 1!
)
```

Citation
--------

```bibtex
@online{DeBloomzGuard,
  AUTHOR = {Cyrile Delestre},
  ORGANIZATION = {Cr{\'e}dit Mutuel Ark{\'e}a},
  URL = {https://huggingface.co/cmarkea/bloomz-3b-guardrail},
  YEAR = {2023},
  KEYWORDS = {NLP ; Transformers ; LLM ; Bloomz},
}
```