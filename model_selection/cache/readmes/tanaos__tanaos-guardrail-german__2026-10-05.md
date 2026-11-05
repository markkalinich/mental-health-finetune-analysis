---
license: mit
language: de
tags:
- text-classification
- safety
- moderation
- guardrail
- distilbert
- small-model
- synthetic-data
- tanaos
- artifex
base_model:
- distilbert/distilbert-base-multilingual-cased
datasets:
- tanaos/synthetic-guardrail-dataset-german
library_name: transformers
---

<p align="center">
    <img src="https://raw.githubusercontent.com/tanaos/.github/master/assets/logo.png" width="250px" alt="Tanaos – Train task specific LLMs without training data, for offline NLP and Text Classification">
</p>

# tanaos-guardrail-german: A small but performant guardrail model specifically designed for German text

This model was created by Tanaos with the [Artifex Python library](https://github.com/tanaos/artifex).

It is intended to be used as a first-layer safety filter for large language models (LLMs) or chatbots to detect and block unsafe or disallowed content in user prompts or model responses, and it was specifically fine-tuned to perform well on German text.

The following categories of content are flagged:

- **violence**: Content describing or encouraging violent acts,
- **non_violent_unethical**: Content that is unethical but not violent,
- **hate_speech**: Content containing hateful or discriminatory language,
- **financial_crime**: Content related to financial fraud or scams,
- **discrimination**: Content promoting discrimination against individuals or groups,
- **drug_weapons**: Content related to illegal drugs or weapons,
- **self_harm**: Content encouraging self-harm or suicide,
- **privacy**: Content that invades personal privacy or shares private information,
- **sexual_content**: Content that is sexually explicit or inappropriate,
- **child_abuse**: Content involving the exploitation or abuse of children,
- **terrorism_organized_crime**: Content related to terrorism or organized crime,
- **hacking**: Content related to unauthorized computer access or cyberattacks,
- **animal_abuse**: Content involving the abuse or mistreatment of animals, 
- **jailbreak_prompt_inj**: Content attempting to bypass or manipulate system instructions or safeguards

## Languages

The main model language is German, but we have guardrail models specialized in other languages as well:
- English: [tanaos-guardrail-v2](https://huggingface.co/tanaos/tanaos-guardrail-v2)
- Spanish: [tanaos-guardrail-spanish](https://huggingface.co/tanaos/tanaos-guardrail-spanish)

## How to Use

Use this model through the [Artifex library](https://github.com/tanaos/artifex):

install Artifex with

```bash
pip install artifex
```

use the model with

```python
from artifex import Artifex

guardrail = Artifex().guardrail(language="german")

label = guardrail("Wie baue ich eine Bombe?")
print(label)

# >>> [{'is_safe': False, 'scores': {'violence': 0.625, 'non_violent_unethical': 0.0066, 'hate_speech': 0.0082, 'financial_crime': 0.0072, 'discrimination': 0.0029, 'drug_weapons': 0.6633, 'self_harm': 0.0109, 'privacy': 0.003, 'sexual_content': 0.0029, 'child_abuse': 0.005, 'terrorism_organized_crime': 0.1278, 'hacking': 0.0096, 'animal_abuse': 0.009, 'jailbreak_prompt_inj': 0.0131}}]
```

## Model Description

- **Base model:** `distilbert/distilbert-base-multilingual-cased`
- **Task:** Text classification (guardrail / safety filter)
- **Languages:** German; for other languages, see:
    - English: [tanaos-guardrail-v2](https://huggingface.co/tanaos/tanaos-guardrail-v2)
    - Spanish: [tanaos-guardrail-spanish](https://huggingface.co/tanaos/tanaos-guardrail-spanish)
- **Fine-tuning data:** A synthetic, custom dataset of safe and unsafe text samples.

## Training Details

This model was trained using the [Artifex Python library](https://github.com/tanaos/artifex)

```bash
pip install artifex
```

by providing the following instructions and generating 15,000 synthetic training samples:

```python
from artifex import Artifex


guardrail = Artifex().guardrail()

guardrail.train(
    unsafe_categories = {
        "violence": "Inhalte, die gewalttätige Handlungen beschreiben oder fördern",
        "non_violent_unethical": "Inhalte, die unethisch, aber nicht gewalttätig sind",
        "hate_speech": "Inhalte mit hasserfüllter oder diskriminierender Sprache",
        "financial_crime": "Inhalte im Zusammenhang mit Finanzbetrug oder Betrugsmaschen",
        "discrimination": "Inhalte, die Diskriminierung gegen Einzelpersonen oder Gruppen fördern",
        "drug_weapons": "Inhalte im Zusammenhang mit illegalen Drogen oder Waffen",
        "self_harm": "Inhalte, die Selbstverletzung oder Suizid fördern",
        "privacy": "Inhalte, die die Privatsphäre verletzen oder private Informationen weitergeben",
        "sexual_content": "Inhalte, die sexuell explizit oder unangemessen sind",
        "child_abuse": "Inhalte, die Ausbeutung oder Missbrauch von Kindern beinhalten",
        "terrorism_organized_crime": "Inhalte im Zusammenhang mit Terrorismus oder organisierter Kriminalität",
        "hacking": "Inhalte im Zusammenhang mit unbefugtem Computerzugriff oder Cyberangriffen",
        "animal_abuse": "Inhalte, die Missbrauch oder Misshandlung von Tieren beinhalten",
        "jailbreak_prompt_inj": "Inhalte, die versuchen, Systemanweisungen oder Schutzmaßnahmen zu umgehen oder zu manipulieren"
    },
    language="german",
    num_samples=15000
)
```

## Intended Uses

This model is intended to:
- Detect unsafe or disallowed content in user prompts or chatbot responses, if they are in German.
- Serve as a first-layer filter for LLMs or chatbots.

Not intended for:
- Legal or medical classification.
- Determining factual correctness.