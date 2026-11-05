---
license: apache-2.0
language:
- en
- fr
- de
- es
- pt
- it
- sl
- el
- nl
library_name: gliner
pipeline_tag: token-classification
datasets:
- E3-JSI/synthetic-multi-pii-ner-v1
base_model:
- urchade/gliner_multi_pii-v1
---


# GLiNER Multi PII Domains

GLiNER is a Named Entity Recognition (NER) model capable of identifying any entity type using a bidirectional transformer encoder (BERT-like). It provides a practical alternative to traditional NER models, which are limited to predefined entities, and Large Language Models (LLMs) that, despite their flexibility, are costly and large for resource-constrained scenarios.

This model has been trained by fine-tuning [urchade/gliner_multi_pii-v1](https://huggingface.co/urchade/gliner_multi_pii-v1) on the synthetic dataset [E3-JSI/synthetic-multi-pii-ner-v1](https://huggingface.co/datasets/E3-JSI/synthetic-multi-pii-ner-v1).

This model is capable of recognizing various types of *personally identifiable information* (PII), including but not limited to these entity types: `person`, `organization`, `phone number`, `address`, `passport number`, `email`, `credit card number`, `social security number`, `health insurance id number`, `date of birth`, `mobile phone number`, `bank account number`, `medication`, `cpf`, `driver's license number`, `tax identification number`, `medical condition`, `identity card number`, `national id number`, `ip address`, `email address`, `iban`, `credit card expiration date`, `username`, `health insurance number`, `registration number`, `student id number`, `insurance number`, `flight number`, `landline phone number`, `blood type`, `cvv`, `reservation number`, `digital signature`, `social media handle`, `license plate number`, `cnpj`, `postal code`, `passport number`, `serial number`, `vehicle registration number`, `credit card brand`, `fax number`, `visa number`, `insurance company`, `identity document number`, `transaction number`, `national health insurance number`, `cvc`, `birth certificate number`, `train ticket number`, `passport expiration date`, and `social security number`.


## Usage

To use the model, one must use the [GLiNER](https://github.com/urchade/GLiNER) library. Once installed, the user can load the model and use it to discern the entities within the text.

```bash
pip install gliner
```

What follows are some examples of its intended use.


### Extract entities from English medical text
  
```python
from gliner import GLiNER

# initialize the GLiNER using this model
model = GLiNER.from_pretrained("E3-JSI/gliner-multi-pii-domains-v1")

# prepare the text for entity extraction
text = """
Medical Record

Patient Name: John Doe
Date of Birth: 15-01-1985
Date of Examination: 20-05-2024
Social Security Number: 123-45-6789

Examination Procedure:
John Doe underwent a routine physical examination. The procedure included measuring vital signs (blood pressure, heart rate, temperature), a comprehensive blood panel, and a cardiovascular stress test. The patient also reported occasional headaches and dizziness, prompting a neurological assessment and an MRI scan to rule out any underlying issues.

Medication Prescribed:

Ibuprofen 200 mg: Take one tablet every 6-8 hours as needed for headache and pain relief.
Lisinopril 10 mg: Take one tablet daily to manage high blood pressure.
Next Examination Date:
15-11-2024
"""

# prepare the labels/entities to be extracted
# this model should work best when entity types are in lowercase
labels = ["name", "social security number", "date of birth", "date"]

# perform entity extraction
entities = model.predict_entities(text, labels, threshold=0.5)

# display predicted entities and their labels
for entity in entities:
    print(entity["text"], "=>", entity["label"])
```

**Expected output**

```text
John Doe => name
15-01-1985 => date of birth
20-05-2024 => date
123-45-6789 => social security number
John Doe => name
15-11-2024 => date
```



### Extract entities from Dutch medical text

```python
from gliner import GLiNER

# initialize the GLiNER using this model
model = GLiNER.from_pretrained("E3-JSI/gliner-multi-pii-domains-v1")

# prepare the text for entity extraction
text = """
Medisch dossier

Naam patiënt: Jan de Vries
Geboortedatum: 15-01-1985
Datum van onderzoek: 20-05-2024
Burgerservicenummer: 987-65-4321

Onderzoeksprocedure:
Jan de Vries onderging een routine lichamelijk onderzoek. De procedure omvatte het meten van de vitale functies (bloeddruk, hartslag, temperatuur), een uitgebreid bloedonderzoek en een cardiovasculaire inspanningstest. De patiënt meldde ook af en toe hoofdpijn en duizeligheid, wat aanleiding gaf tot een neurologische beoordeling en een MRI-scan om eventuele onderliggende problemen uit te sluiten.

Voorgeschreven medicatie:

Paracetamol 500 mg: Neem één tablet elke 6-8 uur indien nodig voor hoofdpijn en pijnverlichting.
Amlodipine 5 mg: Neem één tablet dagelijks om hoge bloeddruk te beheersen.

Volgende onderzoekdatum:
15-11-2024
"""

# prepare the labels/entities to be extracted
# this model should work best when entity types are in lowercase
labels = ["naam", "bmurgerservicenummer", "geboortedatum", "datum"]

# perform entity extraction
entities = model.predict_entities(text, labels, threshold=0.2)

# display predicted entities and their labels
for entity in entities:
    print(entity["text"], "=>", entity["label"])
```

**Expected output**

```text
Jan de Vries => naam
15-01-1985 => geboortedatum
20-05-2024 => datum
987-65-4321 => bmurgerservicenummer
Jan de Vries => naam
15-11-2024 => datum
```

## Aknowledgements

Funded by the European Union. UK participants in Horizon Europe Project [PREPARE](https://prepare-rehab.eu/) are supported by UKRI grant number 10086219 (Trilateral Research). Views and opinions expressed are however those of the author(s) only and do not necessarily reflect those of the European Union or European Health and Digital Executive Agency (HADEA) or UKRI. Neither the European Union nor the granting authority nor UKRI can be held responsible for them. Grant Agreement 101080288 PREPARE HORIZON-HLTH-2022-TOOL-12-01.