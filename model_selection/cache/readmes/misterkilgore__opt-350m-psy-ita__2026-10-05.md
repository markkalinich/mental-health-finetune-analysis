---
language: 
  - it
thumbnail: "url to a thumbnail used in social sharing"
tags:
- psychology
- distilgpt2
widget:
- text: "Il cognitivismo"
- text: "Parliamo di attaccamento"
- text: "Le cause del disturbo d'ansia nei bambini sono"
---

# Italian Psychology opt-350m

This model is a fine-tuned version of the Meta OPT-350M language model, trained on a dataset of Italian psychology articles. 
It is capable of generating human-like text on topics related to psychology and mental health in Italian language.

## Model details

The base model used for fine-tuning is the Meta OPT-350M, with a transformer architecture and 350M parameters. 
The fine-tuning dataset consists of approximately 10,000 Italian psychology articles.

## Example usage

```python
from transformers import pipeline

nlp = pipeline("text-generation", model="misterkilgore/opt-350m-psy-ita")

generated_text = nlp("Le cause del disturbo d'ansia nei bambini sono", max_length=100)
print(generated_text)
```

## Limitations and bias
This model has been trained on a dataset of Italian psychology articles and may not perform well on other types of text or in other languages. 
Additionally, the dataset used to fine-tune the model may contain biases and limitations, which will be reflected in the generated text.

## Dataset
The dataset used to fine-tune this model is composed of Italian psychology articles. 
It contains various topics on mental health and psychology, but some limitations and biases may be present. This model is meant to be used only for research and educational purposes.

## Training data
The training data is composed of Italian psychology articles. 
Fine-tuning was performed on this dataset to adapt the base OPT-350m model to the specific topic of psychology and mental health in Italian language.