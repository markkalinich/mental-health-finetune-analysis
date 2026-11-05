---
language:
- es
- it
- ro
- en
- nl
- sv
- cs
license: cc-by-4.0
library_name: transformers
pipeline_tag: token-classification
tags:
- ner
- named-entity-recognition
- token-classification
- clinical-ner
- biomedical-ner
- multilingual
datasets:
- symptemist
- cardioccc
metrics:
- strict precision
- strict recall
- strict f1
- character-level precision
- character-level recall
- character-level f1
base_model: xlm-roberta-base
---

# DT4H_XLM-R_stl_multilingual_symptom

## Model Description

This **multilingual clinical Named Entity Recognition (NER)** model is designed to identify **sign** and **symptom** mentions in biomedical and clinical text. It is based on [`xlm-roberta-base`](https://huggingface.co/FacebookAI/xlm-roberta-base) and fine-tuned on translated variants of the clinical NER datasets **SympTEMIST** and **CardioCCC**, which consist of clinical case reports with manually annotated symptom mentions, following a single-task learning (STL) approach and using the BIO tagging scheme for sequence labeling.

- **Architecture:** Single-task learning (STL)  
- **Training setup:** Multilingual, Monolabel  (SYMPTOM)
- **Supported languages:**
  - Spanish (`es`)
  - Italian (`it`)
  - Romanian (`ro`)
  - English (`en`)
  - Dutch (`nl`)
  - Swedish (`sv`)
  - Czech (`cs`)
- **Base model:** `xlm-roberta-base`  
- **Task:** Token classification (NER)  
- **Label scheme:** BIO

## Training Data

The model is trained on multilingual clinical NER data combining **SympTEMIST** and **CardioCCC** across the supported languages.

The data is part of the **MultiClinNER** subtask of the [**MultiClinAI**](https://temu.bsc.es/MultiClinAI/) shared task, an initiative as part of the DataTools4Heart (DT4H) project, which provides translated and annotation-projected clinical corpora.

Training and test splits correspond to the **MultiClinNER** task at the 11th SMM4H-HeaRD Workshop (ACL 2026).

## How to use

You can load the model using Hugging Face Transformers:

```python
from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline

model_name = "judithrosell/DT4H_XLM-R_stl_multilingual_symptom"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForTokenClassification.from_pretrained(model_name)

ner_pipeline = pipeline("token-classification", model=model, tokenizer=tokenizer)

text = "La paciente presenta empeoramiento clínico, con intensa astenia, somnolencia, hipoperfusión, frialdad cutánea, hipersudoración, dolor abdominal y náuseas."
predictions = ner_pipeline(text)
print(predictions)
```

⚠ **Note:** We recommend pre-tokenizing the input text into words, as this matches the training setup. Providing raw text directly may lead to slightly degraded performance.

The model outputs **token-level predictions**. For evaluation or submission, these predictions should be converted into **character-level spans**.

To facilitate this process, we provide an inference script in a [GitHub repository]() that:

- Loads the model
- Processes .txt files from an input directory
- Extracts disease mentions
- Exports predictions as a TSV file in the format required for the [MultiClinAI evaluation library](https://github.com/nlp4bia-bsc/MultiClinAIEval):

```text
filename                              label      start_span    end_span    text
MultiClinNER-en-test-symptom-59546    SYMPTOM    72            82          chest pain
```

## Limitations and bias

At the time of submission, no formal bias or fairness evaluation has been conducted. We intend to conduct research in these areas in the future, and if completed, this model card will be updated.

## Evaluation

Evaluation was conducted using **strict (exact match)** and **character-level** metrics on the MultiClinNER test set.

| Language | Strict P | Strict R | Strict F1 | Char P | Char R | Char F1 |
|----------|---------:|---------:|----------:|-------:|-------:|--------:|
| es | 0.6175 | 0.6060 | 0.6117 | 0.7750 | 0.7584 | 0.7666 |
| it | 0.6352 | 0.5469 | 0.5877 | 0.7877 | 0.6741 | 0.7265 |
| ro | 0.6829 | 0.5890 | 0.6325 | 0.8137 | 0.7009 | 0.7531 |
| en | 0.6625 | 0.5860 | 0.6219 | 0.8022 | 0.7069 | 0.7515 |
| nl | 0.5974 | 0.5435 | 0.5692 | 0.7438 | 0.6734 | 0.7068 |
| sv | 0.6513 | 0.5990 | 0.6240 | 0.7848 | 0.7171 | 0.7495 |
| cz | 0.6278 | 0.5810 | 0.6035 | 0.7608 | 0.6996 | 0.7289 |
| **Average** |  |  | **0.6072** |  |  | **0.7404** |

## Additional information

### Authors
NLP4BIA team at the Barcelona Supercomputing Center (nlp4bia@bsc.es).

### Contact information
judith.rosell [at] bsc.es

### Funding

This model is part of the DataTools4Heart (DT4H) project, funded by the European Union’s Horizon Europe Framework Under Grant Agreement No. 101057849.