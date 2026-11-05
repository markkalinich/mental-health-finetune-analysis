---
id: CardioNER model --medication
name: CardioNER model --medication
description: Finetuned CardioBERTa.nl model for detection of medication spans. This
  model is a mulilabel model using BCE loss.
license: mit
language: nl
tags:
- span classification
- lexical semantic
- biology
- biomedical
- clinical ner
- science
- bionlp
base_model: UMCU/CardioBERTa.nl_clinical
pipeline_tag: token-classification
---

# Model Card for Cardioner Model --Medication




This a UMCU/CardioBERTa.nl_clinical base model finetuned for span classification. For this model
we used IOB-tagging. Using the IOB-tagging schema facilitates the aggregation of predictions
over sequences. This specific model is trained on a batch of 240 span-labeled documents.

### Expected input and output
The input should be a string with **Dutch** cardio clinical text.

CardioNER model --medication is a muticlass span classification model.
The classes that can be predicted are ['medication'].

#### Extracting span classification from CardioNER model --medication

The following script converts a string of <512 tokens to a list of span predictions.
```python
from transformers import pipeline

le_pipe = pipeline('ner',
                    model=model,
                    tokenizer=model, aggregation_strategy="simple",
                    device=-1)

named_ents = le_pipe(SOME_TEXT)
```

To process a string of arbitrary length you can split the string into sentences or paragraphs
using e.g. pysbd or spacy(sentencizer) and iteratively parse the list of with the span-classification pipe.

Alternatively you might try 
```python
named_ents = le_pipe(SOME_TEXT, stride=256)
```



# Data description

50/50 Train/validation split on CardioCCC, a manually labeled cardiology corpus


# Acknowledgement

This is part of the [DT4H project](https://www.datatools4heart.eu/).

# Doi and reference



For more details about training/eval and other scripts, see CardioNER [github repo](https://github.com/DataTools4Heart/CardioNER).
and for more information on the background, see Datatools4Heart [Huggingface](https://huggingface.co/DT4H)/[Website](https://www.datatools4heart.eu/)


