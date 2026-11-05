---
license: mit
language: es
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
- tanaos/synthetic-guardrail-dataset-spanish
library_name: transformers
---

<p align="center">
    <img src="https://raw.githubusercontent.com/tanaos/.github/master/assets/logo.png" width="250px" alt="Tanaos – Train task specific LLMs without training data, for offline NLP and Text Classification">
</p>

# tanaos-guardrail-spanish: A small but performant guardrail model specifically designed for Spanish text

This model was created by Tanaos with the [Artifex Python library](https://github.com/tanaos/artifex).

It is intended to be used as a first-layer safety filter for large language models (LLMs) or chatbots to detect and block unsafe or disallowed content in user prompts or model responses, and it was specifically fine-tuned to perform well on Spanish text.

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

# Languages

The main model language is Spanish, but we have guardrail models specialized in other languages as well:
- English: [tanaos-guardrail-v2](https://huggingface.co/tanaos/tanaos-guardrail-v2)
- German: [tanaos-guardrail-german](https://huggingface.co/tanaos/tanaos-guardrail-german)

## How to Use

Use this model through the [Artifex library](https://github.com/tanaos/artifex):

install Artifex with

```bash
pip install artifex
```

use the model with

```python
from artifex import Artifex

guardrail = Artifex().guardrail(language="spanish")

label = guardrail("¿Cómo construyo una bomba?")
print(label)

# >>> [{'is_safe': False, 'scores': {'violence': 0.625, 'non_violent_unethical': 0.0066, 'hate_speech': 0.0082, 'financial_crime': 0.0072, 'discrimination': 0.0029, 'drug_weapons': 0.6633, 'self_harm': 0.0109, 'privacy': 0.003, 'sexual_content': 0.0029, 'child_abuse': 0.005, 'terrorism_organized_crime': 0.1278, 'hacking': 0.0096, 'animal_abuse': 0.009, 'jailbreak_prompt_inj': 0.0131}}]
```

## Model Description

- **Base model:** `distilbert/distilbert-base-multilingual-cased`
- **Task:** Text classification (guardrail / safety filter)
- **Languages:** Spanish; for other languages, see:
    - English: [tanaos-guardrail-v2](https://huggingface.co/tanaos/tanaos-guardrail-v2)
    - German: [tanaos-guardrail-german](https://huggingface.co/tanaos/tanaos-guardrail-german)
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
        "violence": "Contenido que describe o fomenta actos violentos",
        "non_violent_unethical": "Contenido que es poco ético pero no violento",
        "hate_speech": "Contenido que contiene lenguaje de odio o discriminatorio",
        "financial_crime": "Contenido relacionado con fraude financiero o estafas",
        "discrimination": "Contenido que promueve la discriminación contra individuos o grupos",
        "drug_weapons": "Contenido relacionado con drogas ilegales o armas",
        "self_harm": "Contenido que fomenta la autolesión o el suicidio",
        "privacy": "Contenido que invade la privacidad personal o comparte información privada",
        "sexual_content": "Contenido que es sexualmente explícito o inapropiado",
        "child_abuse": "Contenido que involucra la explotación o el abuso de menores",
        "terrorism_organized_crime": "Contenido relacionado con terrorismo o crimen organizado",
        "hacking": "Contenido relacionado con el acceso no autorizado a sistemas informáticos o ciberataques",
        "animal_abuse": "Contenido que involucra el abuso o maltrato de animales",
        "jailbreak_prompt_inj": "Contenido que intenta eludir o manipular instrucciones o salvaguardas de un LLM"
    },
    language="spanish",
    num_samples=15000
)
```

## Intended Uses

This model is intended to:
- Detect unsafe or disallowed content in user prompts or chatbot responses, if they are in Spanish.
- Serve as a first-layer filter for LLMs or chatbots.

Not intended for:
- Legal or medical classification.
- Determining factual correctness.