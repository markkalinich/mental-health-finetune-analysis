---
license: mit
language:
- en
- de
- es
- fr
- pt
metrics:
- accuracy
base_model:
- microsoft/mdeberta-v3-base
pipeline_tag: text-classification
tags:
- formal or informal classification
- sentiment-analysis
widget:
- text: Bitte geh einkaufen.
- text: Können Sie mir spontan dabei helfen?
- text: Als nächstes kommen 4g Champignons und 500g Mehl dazu.
library_name: transformers
---


# formality-classifier-mdeberta-v3-base

This model can classify texts based on their formality. It classifies inputs into one of the three classes `["formal", "informal", "neutral"]`, with neutral pertaining to texts which do not have a clear formality, such as passive statements etc.


In selecting and generating training data, a focus was put on languages that actually have a type of formal address etc., including French, German, Italian, Portuguese and Spanish.
Some samples from [osyvokon/pavlick-formality-scores](https://huggingface.co/datasets/osyvokon/pavlick-formality-scores) were also used to try and teach the model to classify English inputs.




## Results

Accuracy on the test set:

| Language | Accuracy |
| --- | --- |
| all | 88.93% |
| English | 79.20% |
| French | 100% |
| German | 97.73% |
| Italian | 97.83% |
| Portuguese | 100% |
| Spanish | 98.53% |

Confusion Matrix:

![](confusion_matrix.svg)

By Language:

![](confusion_matrix_en.svg)

![](confusion_matrix_fr.svg)

![](confusion_matrix_de.svg)

![](confusion_matrix_it.svg)

![](confusion_matrix_pt.svg)

![](confusion_matrix_es.svg)



## Usage example

```python
from transformers import pipeline

pipe = pipeline("text-classification", model="LenDigLearn/formality-classifier-mdeberta-v3-base")


print("DE:")
texts_de = [
    "Verschwinde", "Nein", "Ja", "vielleicht", "Warum bist du so?",
    "Können Sie mir spontan dabei helfen?", "Bitte senden Sie uns die nötigen Unterlagen zu.", "Dies müssen Sie selbst entscheiden, wenn Sie den entsprechenden Punkt erreicht haben.", "Sie sind also Herr Müller.", "Bitte helfen Sie mir!",
    "Man muss schon wissen, was dann passiert.", "Als nächstes kommen 4g Champignons und 500g Mehl dazu.", "Bananen sind krumm.", "Das ist eine Tatsache, die unumstößlich ist.", "Hilfestellungen sind unter \"Hilfe\" zu finden."
]
for text in texts_de:
    print(pipe(text))

print("-----------\nEN:")
texts_en = [
    "Piss off", "No", "Yes", "maybe", "Why are you like this?",
    "Could you help me spontaneously?", "Please send me the necessary documents.", "You will have to decide this individually as soon as you have reached the relevant point.", "I presume you are Mr. Müller?", "Please offer me your support!",
    "One would have to know what happens then.", "Then, we add 4g Mushrooms and 500g flour.", "Bananas are usually curved.", "That is an irrefutable fact.", "You can find helpful tutorials under \"help\"."
]
for text in texts_en:
    print(pipe(text))
```
