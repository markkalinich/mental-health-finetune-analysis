---
license: apache-2.0
datasets:
- clarin-pl/kpwr-ner
language:
- pl
- en
metrics:
- f1
base_model:
- PKOBP/polish-roberta-8k
pipeline_tag: token-classification
tags:
- ner
---
# Polish PII Classification Model

This model is a fine-tuned version of **polish-roberta-8k**, specifically designed for
**Named Entity Recognition (NER)** focused on identifying **Personally Identifiable Information (PII)** in Polish text.

The model identifies entities such as names, locations, organizations, and contact numbers, making it ideal for
anonymization pipelines and data privacy tasks.

## Model Details

- **Architecture**: `RobertaForTokenClassification`
- **Base Model**: [polish-roberta-8k](https://huggingface.co/PKOBP/polish-roberta-8k)
- **Language**: Polish
- **Task**: Token Classification (NER)
- **Context Length**: Up to 8192 tokens (inherited from base model)

### Label Mapping

The model classifies tokens into the following 9 categories:

| ID | Label          | Description                        |
|----|----------------|------------------------------------|
| 0  | `O`            | Outside any entity                 |
| 1  | `CONTACT/NUM`  | Phone numbers, emails, etc.        |
| 2  | `EVENT`        | Named events                       |
| 3  | `FACILITY`     | Buildings, airports, bridges, etc. |
| 4  | `LOCATION`     | Cities, countries, regions         |
| 5  | `ORGANIZATION` | Companies, institutions, groups    |
| 6  | `OTHER`        | Miscellaneous PII                  |
| 7  | `PERSON`       | People's names                     |
| 8  | `PRODUCT`      | Brand names, products              |

## Training Data

The model was trained on a generalized version of the **KPWr-NER**
dataset ([clarin-pl/kpwr-ner](https://huggingface.co/datasets/clarin-pl/kpwr-ner)).

Fine-grained labels from the original dataset were mapped to the general categories listed above using a custom mapping
process to improve the model's robustness and utility for general anonymization.

## Training Hyperparameters

| Hyperparameter          | Value      |
|-------------------------|------------|
| Epochs                  | 5          |
| Batch Size (Train/Eval) | 16 / 16    |
| Learning Rate           | 5e-5       |
| Weight Decay            | 0.01       |
| Max Sequence Length     | 128        |
| Seed                    | 42         |
| Optimization Metric     | `f1_macro` |

## Evaluation Results

The model achieved the following results on the evaluation set:

| Metric             | Value      |
|--------------------|------------|
| **F1 Macro**       | **0.8430** |
| **F1 Weighted**    | **0.9784** |
| Precision Macro    | 0.8480     |
| Precision Weighted | 0.9786     |
| Recall Macro       | 0.8461     |
| Recall Weighted    | 0.9787     |
| Eval Loss          | 0.1099     |

## Usage

### 1. Standard Transformers Pipeline

You can use the model directly via the Hugging Face `transformers` library:

```python
from transformers import pipeline

# Load the model and tokenizer

model_id = "radlab/pii-pl-v1.0"
pii_pipeline = pipeline("ner", model=model_id, tokenizer=model_id, aggregation_strategy="simple")

text = "Jan Kowalski z firmy PKO BP mieszka w Warszawie i dowiedza ciocię Jadzię w Warszawie razem z synem Dominikiem."
results = pii_pipeline(text)

for entity in results:
    print(f"Entity: {entity['word']} | Label: {entity['entity_group']} | Score: {entity['score']:.4f}")
```

**expected output**
```text
Entity: Jan Kowalski | Label: PERSON | Score: 0.9981
Entity: PKO BP | Label: ORGANIZATION | Score: 0.9959
Entity: Warszawie | Label: LOCATION | Score: 0.9974
Entity: Jadzię | Label: PERSON | Score: 0.9955
Entity: Warszawie | Label: LOCATION | Score: 0.9974
Entity: Dominikiem | Label: PERSON | Score: 0.9942
```

### 2. Using the `pii_classification` Inference Wrapper

For advanced features like punctuation cleaning, sub-token merging, and full anonymization, use the `AnonPredictor` from
the official repository.

**Installation:**

```bash
git clone https://github.com/radlab-dev-group/anonymizer-model.git
cd anonymizer-model
pip install . --break-system-packages
```

**Inference Code:**

```python
from pii_classification.inference.inference import AnonPredictor

# Initialize predictor
predictor = AnonPredictor(model_path="radlab/pii-pl-v1.0")

text = "Jan Kowalski z firmy PKO BP mieszka w Warszawie i dowiedza ciocię Jadzię w Warszawie razem z synem Dominikiem."

# 1. Get detailed predictions (merged entities)
predictions = predictor.predict(
    text, clean_punct=True, merge_entities=True, handle_gaps=True
)
print(predictions)

# 2. Full anonymization
anonymized = predictor.predict_and_anonymize(text)
print(f"Anonymized Text: {anonymized['text']}")
print(f"Mappings: {anonymized['mappings']}")
```

**expected output**
```text
{'0': 'O', '1': 'CONTACT/NUM', '2': 'EVENT', '3': 'FACILITY', '4': 'LOCATION', '5': 'ORGANIZATION', '6': 'OTHER', '7': 'PERSON', '8': 'PRODUCT'}
[{'word': 'Jan Kowalski', 'label': 'PERSON'}, {'word': ' ', 'label': 'O'}, {'word': 'z', 'label': 'O'}, {'word': ' ', 'label': 'O'}, {'word': 'firmy', 'label': 'O'}, {'word': ' ', 'label': 'O'}, {'word': 'PKO BP', 'label': 'ORGANIZATION'}, {'word': ' ', 'label': 'O'}, {'word': 'mieszka', 'label': 'O'}, {'word': ' ', 'label': 'O'}, {'word': 'w', 'label': 'O'}, {'word': ' ', 'label': 'O'}, {'word': 'Warszawie', 'label': 'LOCATION'}, {'word': ' ', 'label': 'O'}, {'word': 'i', 'label': 'O'}, {'word': ' ', 'label': 'O'}, {'word': 'dowiedza', 'label': 'O'}, {'word': ' ', 'label': 'O'}, {'word': 'ciocię', 'label': 'O'}, {'word': ' ', 'label': 'O'}, {'word': 'Jadzię', 'label': 'PERSON'}, {'word': ' ', 'label': 'O'}, {'word': 'w', 'label': 'O'}, {'word': ' ', 'label': 'O'}, {'word': 'Warszawie', 'label': 'LOCATION'}, {'word': ' ', 'label': 'O'}, {'word': 'razem', 'label': 'O'}, {'word': ' ', 'label': 'O'}, {'word': 'z', 'label': 'O'}, {'word': ' ', 'label': 'O'}, {'word': 'synem', 'label': 'O'}, {'word': ' ', 'label': 'O'}, {'word': 'Dominikiem', 'label': 'PERSON'}, {'word': '.', 'label': 'O'}]
predictions= [{'word': 'Jan Kowalski', 'label': 'PERSON'}, {'word': ' ', 'label': 'O'}, {'word': 'z', 'label': 'O'}, {'word': ' ', 'label': 'O'}, {'word': 'firmy', 'label': 'O'}, {'word': ' ', 'label': 'O'}, {'word': 'PKO BP', 'label': 'ORGANIZATION'}, {'word': ' ', 'label': 'O'}, {'word': 'mieszka', 'label': 'O'}, {'word': ' ', 'label': 'O'}, {'word': 'w', 'label': 'O'}, {'word': ' ', 'label': 'O'}, {'word': 'Warszawie', 'label': 'LOCATION'}, {'word': ' ', 'label': 'O'}, {'word': 'i', 'label': 'O'}, {'word': ' ', 'label': 'O'}, {'word': 'dowiedza', 'label': 'O'}, {'word': ' ', 'label': 'O'}, {'word': 'ciocię', 'label': 'O'}, {'word': ' ', 'label': 'O'}, {'word': 'Jadzię', 'label': 'PERSON'}, {'word': ' ', 'label': 'O'}, {'word': 'w', 'label': 'O'}, {'word': ' ', 'label': 'O'}, {'word': 'Warszawie', 'label': 'LOCATION'}, {'word': ' ', 'label': 'O'}, {'word': 'razem', 'label': 'O'}, {'word': ' ', 'label': 'O'}, {'word': 'z', 'label': 'O'}, {'word': ' ', 'label': 'O'}, {'word': 'synem', 'label': 'O'}, {'word': ' ', 'label': 'O'}, {'word': 'Dominikiem', 'label': 'PERSON'}, {'word': '.', 'label': 'O'}]
Anonymized Text: {PERSON_1776877218745866_1} z firmy {ORGANIZATION_1776877218745866_2} mieszka w {LOCATION_1776877218745866_3} i dowiedza ciocię {PERSON_1776877218745866_4} w {LOCATION_1776877218745866_5} razem z synem {PERSON_1776877218745866_6}.
Mappings: {'PERSON_1776877218745866_1': 'Jan Kowalski', 'ORGANIZATION_1776877218745866_2': 'PKO BP', 'LOCATION_1776877218745866_3': 'Warszawie', 'PERSON_1776877218745866_4': 'Jadzię', 'LOCATION_1776877218745866_5': 'Warszawie', 'PERSON_1776877218745866_6': 'Dominikiem'}
```


## Repository and Code

The full training pipeline, data conversion scripts, and inference API are available here:
👉 [https://github.com/radlab-dev-group/anonymizer-model](https://github.com/radlab-dev-group/anonymizer-model)

## Licensing

- **Model Weights**: [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0)
- **Base Model (`polish-roberta-8k`)**: [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0)
- **Dataset (`kpwr-ner`)**: [Creative Commons Attribution 3.0 (CC-BY-3.0)](https://creativecommons.org/licenses/by/3.0/)