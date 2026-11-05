---
license: apache-2.0
language:
- bs
- hr
- sr
- sl
- sk
- cs
- en
tags:
- sentiment-analysis
- text-regression
- text-classification
- sentiment-regression
- sentiment-classification
- parliament
inference: false
datasets:
- classla/ParlaSent
---


# Multilingual parliament sentiment regression model XLM-R-ParlaSent

This model is based on [xlm-r-parla](https://huggingface.co/classla/xlm-r-parla), an XLM-R-large model additionally pre-trained on parliamentary proceedings. The model was fine-tuned on the [ParlaSent dataset](http://hdl.handle.net/11356/1868), a manually annotated selection of sentences of parliamentary proceedings from Bosnia and Herzegovina, Croatia, Czechia, Serbia, Slovakia, Slovenia, and the United Kingdom.

Both the additionally pre-trained model, as well as [the training dataset](http://hdl.handle.net/11356/1868) are results of the [ParlaMint project](https://www.clarin.eu/parlamint). The details on the models and the dataset are described in our [paper](https://arxiv.org/abs/2309.09783):

```latex
@article{
 Mochtak_Rupnik_Ljubešić_2023,
 title={The ParlaSent multilingual training dataset for sentiment identification in parliamentary proceedings},
 rights={All rights reserved},
 url={http://arxiv.org/abs/2309.09783},
 abstractNote={Sentiments inherently drive politics. How we receive and process information plays an essential role in political decision-making, shaping our judgment with strategic consequences both on the level of legislators and the masses. If sentiment plays such an important role in politics, how can we study and measure it systematically? The paper presents a new dataset of sentiment-annotated sentences, which are used in a series of experiments focused on training a robust sentiment classiﬁer for parliamentary proceedings. The paper also introduces the ﬁrst domain-speciﬁc LLM for political science applications additionally pre-trained on 1.72 billion domain-speciﬁc words from proceedings of 27 European parliaments. We present experiments demonstrating how the additional pre-training of LLM on parliamentary data can signiﬁcantly improve the model downstream performance on the domain-speciﬁc tasks, in our case, sentiment detection in parliamentary proceedings. We further show that multilingual models perform very well on unseen languages and that additional data from other languages signiﬁcantly improves the target parliament’s results. The paper makes an important contribution to multiple domains of social sciences and bridges them with computer science and computational linguistics. Lastly, it sets up a more robust approach to sentiment analysis of political texts in general, which allows scholars to study political sentiment from a comparative perspective using standardized tools and techniques.},
 note={arXiv:2309.09783 [cs]},
 number={arXiv:2309.09783},
 publisher={arXiv},
 author={Mochtak, Michal and Rupnik, Peter and Ljubešić, Nikola},
 year={2023},
 month={Sep},
 language={en}
}
```

The model itself can be cited as
```latex
@misc{parlasent-model,
	author       = { Rupnik, Peter and  Ljubešić, Nikola and  Mochtak, Michal },
	title        = { xlm-r-parlasent (Revision a04de02) },
	year         = 2023,
	url          = { https://huggingface.co/classla/xlm-r-parlasent },
	doi          = { 10.57967/hf/6718 },
	publisher    = { Hugging Face }
}
```
## Annotation schema

The discrete labels, present in the [ParlaSent dataset](http://hdl.handle.net/11356/1868), were mapped to integers as follows:

```
  "Negative": 0.0,
  "M_Negative": 1.0,
  "N_Neutral": 2.0,
  "P_Neutral": 3.0,
  "M_Positive": 4.0,
  "Positive": 5.0,
```
The model was then fine-tuned on numeric labels and set up as a regressor.

### Translating regression results back to original categories

Should you wish to translate numerical outputs back into the original labels, you might find this snippet useful:

```python

num_output = 0.12
def get_original_6_category_label(x: float) -> str:
    import numpy as np
    label_mapping = {
        0: 'Negative',
        1: 'Mixed Negative',
        2: 'Neutral Negative',
        3: 'Neutral Positive',
        4: 'Mixed Positive',
        5: 'Positive'
    }
    return label_mapping[
      int(np.clip(np.round(x), 0, 5))
      ]
get_original_6_category_label(num_output)
# Output: "Negative"
```

In addition, it is possible to condense the labels even further into three categories. In this case we would post-process the numerical output as:

```python
num_output = 0.12
def get_3_category_label(x: float) -> str:
    import numpy as np
    three_category_mapper = {
        0: 'Negative',
        1: 'Neutral',
        2: 'Positive',
    }
    return three_category_mapper[
      int(np.clip(np.round(x), 0, 5) // 2)
      ]
get_3_category_label(num_output)
# Output: "Negative"
```

## Finetuning procedure

The fine-tuning procedure is described in the paper, cited above. Presumed optimal hyperparameters used are
```
  num_train_epochs=4,
  train_batch_size=32,
  learning_rate=8e-6,
  regression=True
```

## Results

Results reported were obtained from 5 fine-tuning runs.

test dataset | R^2 | MAE
--- | --- | ---
BCS | 0.6146 ± 0.0104 | 0.7050 ± 0.0089
EN | 0.6722 ± 0.0100 | 0.6755 ± 0.0076

## Usage Example

With `simpletransformers==0.64.3`.
```python
from simpletransformers.classification import ClassificationModel, ClassificationArgs
import torch
model_args = ClassificationArgs(
        regression=True,
    )
model = ClassificationModel(model_type="xlmroberta", model_name="classla/xlm-r-parlasent",use_cuda=torch.cuda.is_available(), num_labels=1,args=model_args)
model.predict(["I fully disagree with this argument.", 
               "The ministers are entering the chamber.",
               "Things can always be improved in the future.",
               "These are great news."])
```

Output:
```python
(
  array([0.11633301, 3.63671875, 4.203125, 5.30859375]),
  array([0.11633301, 3.63671875, 4.203125, 5.30859375])
)
```
## Large scale use

[Bojan](https://huggingface.co/Bojan) tested the example above on a large dataset. He reports execution time can be improved by a factor of five with the use of `transformers` as follows:

```python

from transformers import AutoModelForSequenceClassification, TextClassificationPipeline, AutoTokenizer,                                                                                               AutoConfig

MODEL = "classla/xlm-r-parlasent"
tokenizer = AutoTokenizer.from_pretrained(MODEL)
config = AutoConfig.from_pretrained(MODEL)
model = AutoModelForSequenceClassification.from_pretrained(MODEL)

pipe = TextClassificationPipeline(model=model, tokenizer=tokenizer, return_all_scores=True,
                                      task='sentiment_analysis', device=0, function_to_apply="none")
pipe([
    "I fully disagree with this argument.", 
    "The ministers are entering the chamber.",
    "Things can always be improved in the future.",
    "These are great news."
])
```