---
datasets:
- ai4privacy/pii-masking-400k
language:
- de
base_model:
- iiiorg/piiranha-v1-detect-personal-information
pipeline_tag: token-classification
tags:
- named-entity-recognition
- ner
- pii
- datenschutz
- dsg
- dsgvo
- german
---


# 🛡️ PII Sensitive NER – German

Ein feinjustiertes Modell zur **Erkennung schützenswerter und besonders schützenswerter Personendaten** nach **DSGVO** und **Schweizer DSG**. Das Modell basiert auf `iiiorg/piiranha-v1-detect-personal-information` und wurde auf deutschsprachigen Beispielen trainiert.

## 🔍 Anwendungsfall

Das Modell erkennt personenbezogene Daten in Texten – insbesondere verschiedene Kategorien von **besonders schützenswerten Personendaten** gemäss Art. 9 DSGVO wie:

- `REL`: Religion (z. B. *Weihnachten*, *islamisch*, *Konfirmation*)
- `ETHN`: Ethnische Zugehörigkeit (z. B. *türkischstämmig*, *asiatisch*)
- `SOR`: Sexuelle Orientierung (z. B. *homosexuell*, *bisexuell*)

Zusätzlich werden Standard-Entitäten aus dem [Piiranha-Modell](https://huggingface.co/iiiorg/piiranha-v1-detect-personal-information) wie `EMAIL`, `TELEPHONENUM`, `DATEOFBIRTH`, `IDCARDNUM` etc. erkannt.


## 📊 Training

Das Modell wurde mit einer Kombination aus:

- dem deutschen Teil des [ai4privacy/pii-masking-400k](https://huggingface.co/datasets/ai4privacy/pii-masking-400k) Datensatzes
- synthetisch generierten Beispielen für die Labels `REL`, `ETHN` und `SOR`

fine-getuned.


## ⚠️ Disclaimer

Dieses Modell wurde auf synthetisch erzeugten Daten validiert und evaluiert. Obwohl bei der Generierung auf hohe Variation und realitätsnahe Formulierungen geachtet wurde, kann die tatsächliche Leistung im Einsatz mit echten, unstrukturierten Texten abweichen.

Das Modell befindet sich in einem frühen Entwicklungsstadium und ist nicht frei von Fehlern. Insbesondere bei mehrdeutigen oder komplex verschachtelten Sätzen kann es zu Fehlklassifikationen oder unvollständiger Erkennung kommen. Eine manuelle Nachprüfung der Ergebnisse wird ausdrücklich empfohlen.

Die Weiterentwicklung und Evaluierung des Modells auf echten Anwendungsdaten ist vorgesehen, konnte im Rahmen dieser Version jedoch noch nicht erfolgen.

**Es wird keine Haftung für die Funktionsweise, Genauigkeit oder Vollständigkeit des Modells übernommen. Die Nutzung erfolgt auf eigene Verantwortung.**


## 📦 Verwendung

```python
from transformers import pipeline

model = pipeline(
    "token-classification",
    model="HuggingLil/pii-sensitive-ner-german",
    aggregation_strategy="simple" 
)

text = "Elena Petrov ist Kosovarin und hat die Emailadresse elena.petrov@uni-berlin.de angegeben."
output = model(text)
print(output)

