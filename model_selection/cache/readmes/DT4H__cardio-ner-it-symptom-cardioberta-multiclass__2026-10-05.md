---
id: cardio-ner-it-symptom-cardioberta-multiclass
name: cardio-ner-it-symptom-cardioberta-multiclass
description: Finetuned CardioBERTa.it multiclass model for detection of symptom spans
  in Italian cardiology text.
license: mit
language: it
tags:
- biomedical
- clinical ner
- span classification
- cardiology
- italian
base_model: DT4H/CardioBERTa.it
pipeline_tag: token-classification
---

# Model Card for cardio-ner-it-symptom-cardioberta-multiclass

This is a DT4H/CardioBERTa.it base model finetuned for span classification on Italian
cardiology clinical text, using IOB tagging.

### Expected input and output
The input should be a string of **Italian** cardiology clinical text.

cardio-ner-it-symptom-cardioberta-multiclass is a multiclass (single-entity-type) span classification model.
The classes that can be predicted are: SYMPTOM.

#### Extracting span classification from cardio-ner-it-symptom-cardioberta-multiclass

```python
from transformers import pipeline

ner_pipe = pipeline('ner',
                     model="cardio-ner-it-symptom-cardioberta-multiclass",
                     tokenizer="cardio-ner-it-symptom-cardioberta-multiclass",
                     aggregation_strategy="simple",
                     trust_remote_code=True)

named_ents = ner_pipe(SOME_TEXT)
```

For text longer than the model's max sequence length, use a sliding stride:
```python
named_ents = ner_pipe(SOME_TEXT, stride=125)
```

# Data description

10-fold cross-validation on the Italian portion of CardioCCC (DataTools4Heart Cardiology Clinical Case Corpus), batches 1+2, 508 documents, version `1_validated_without_sugs`. The uploaded checkpoint is the arithmetic mean of the 10 per-fold checkpoints ("Run 1"/weight-averaging in the CardioLM paper).

# Acknowledgement

This is part of the [DT4H project](https://www.datatools4heart.eu/).

For more details about training/eval and other scripts, see the CardioNER
[github repo](https://github.com/DataTools4Heart/CardioNER) and for more
information on the background, see DataTools4Heart's
[Huggingface](https://huggingface.co/DT4H)/[Website](https://www.datatools4heart.eu/).
