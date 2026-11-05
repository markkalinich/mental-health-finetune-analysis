---
language: 
  - es
tags:
  - biomedical
  - clinical
  - EHR
  - spanish
  - NER
  - named-entity-recognition
  - temporal
  - temporality
  - timex
license: cc-by-4.0
metrics:
- precision
- recall
- f1
base_model:
- PlanTL-GOB-ES/bsc-bio-ehr-es
pipeline_tag: token-classification
model-index:
- name: BSC-NLP4BIA/bsc-bio-ehr-es-temporalidad
  results:
    - task:
        type: token-classification
      dataset:
        name: temporalidad-ner
        type: temporalidad-ner
      metrics:
        - name: precision (micro)
          type: precision
          value: 0.8866
        - name: recall (micro)
          type: recall
          value: 0.9107
        - name: f1 (micro)
          type: f1
          value: 0.8985
widget:
  - text: Paciente de 67 años que acude por dolor torácico de 3 días de evolución. Se cita para revisión en 2 semanas.
  - text: Refiere fiebre de hasta 38.5ºC desde hace una semana, con tos nocturna que se repite cada 4 horas.
  - text: Antecedente de infarto agudo de miocardio en 2018. Tratamiento crónico desde entonces, con controles mensuales.
---


# bsc-bio-ehr-es-temporalidad

## Table of contents
<details>
<summary>Click to expand</summary>

- [Model description](#model-description)
- [How to use](#how-to-use)
- [Evaluation](#evaluation)
- [Limitations and bias](#limitations-and-bias)
- [Additional information](#additional-information)
  - [Authors](#authors)
  - [Contact information](#contact-information)
  - [Funding](#funding)
  - [Citing information](#citing-information)
  - [Disclaimer](#disclaimer)

</details>

## Model description
A fine-tuned version of the [bsc-bio-ehr-es](https://huggingface.co/PlanTL-GOB-ES/bsc-bio-ehr-es) model for the recognition of temporal expressions (TIMEX-style) in Spanish clinical text and electronic health records. The model labels the following entity classes:

| Label      | Description                                                        |
|------------|--------------------------------------------------------------------|
| `AGE`      | Age expressions (e.g. *67 años*).                                  |
| `DATE`     | Calendar dates and references to a point in time (e.g. *en 2018*). |
| `DURATION` | Durations / spans of time (e.g. *3 días de evolución*).           |
| `SET`      | Recurring or periodic expressions (e.g. *cada 4 horas*, *mensuales*). |
| `TIME`     | Times of day (e.g. *por la noche*).                               |

Labels follow the BIO tagging scheme (`B-`, `I-`, `O`).

### Training data
The model was trained on an internal Spanish clinical corpus (`temporalidad-ner`) annotated for temporal expressions following a TIMEX-style scheme.

### Training procedure
The model was selected through a **Weights & Biases hyperparameter sweep** (up to 50 runs), keeping the configuration that maximized validation micro-F1 (`eval/f1`) over the [bsc-bio-ehr-es](https://huggingface.co/PlanTL-GOB-ES/bsc-bio-ehr-es) base model. The search space explored was:

| Hyperparameter        | Search space                                       |
|-----------------------|----------------------------------------------------|
| Base model            | `PlanTL-GOB-ES/bsc-bio-ehr-es`                     |
| Epochs                | 15                                                 |
| Batch size            | {8, 16, 32}                                         |
| Learning rate         | log-uniform, 1e-7 – 1e-3                           |
| Classifier dropout    | uniform, 0.1 – 0.8 (step 0.1)                      |
| Weight decay          | {0, 1e-5, 1e-4, 1e-3, 0.01, 0.1}                  |
| Warmup ratio          | {0, 0.1}                                            |
| Class weight strategy | none                                               |
| Evaluation strategy   | per epoch                                          |

## How to use

⚠ We recommend pre-tokenizing the input text into words instead of providing it directly to the model, as this is how the model was trained. Otherwise, the results and performance might get affected.

A usage example can be found [here](https://github.com/nlp4bia-bsc/hugging-face-pipeline/blob/main/simple_inference.py).

## Evaluation

Strict (same class, exact boundaries) and overlapping (same class, some boundary overlap) precision / recall / F-score on the test set.

| Label     | Precision | Recall | F-Score | Ov. Precision | Ov. Recall | Ov. F-Score |
|-----------|-----------|--------|---------|---------------|------------|-------------|
| AGE       | 0.9426    | 0.9287 | 0.9356  | 0.9596        | 0.9455     | 0.9525      |
| DATE      | 0.9093    | 0.9167 | 0.9130  | 0.9469        | 0.9546     | 0.9508      |
| DURATION  | 0.9013    | 0.9129 | 0.9071  | 0.9384        | 0.9505     | 0.9444      |
| SET       | 0.8466    | 0.9096 | 0.8770  | 0.8886        | 0.9548     | 0.9205      |
| TIME      | 0.6323    | 0.7656 | 0.6926  | 0.7097        | 0.8594     | 0.7774      |
| micro avg | 0.8866    | 0.9107 | 0.8985  | 0.9241        | 0.9492     | 0.9365      |

## Limitations and bias
At the time of submission, no measures have been taken to estimate the bias embedded in the model. However, we are well aware that our models may be biased since the corpora have been collected using crawling techniques on multiple web sources. We intend to conduct research in these areas in the future, and if completed, this model card will be updated.

## Additional information

### Authors
NLP4BIA team at the Barcelona Supercomputing Center (nlp4bia@bsc.es).

### Contact information
jan.rodriguez [at] bsc.es

### Funding

More information will be available soon.

### Citing information

Please cite the following works:

```bibtex




```

### Disclaimer

The models published in this repository are intended for a generalist purpose and are available to third parties. These models may have bias and/or any other undesirable distortions.

When third parties deploy or provide systems and/or services to other parties using any of these models (or using systems based on these models) or become users of the models, they should note that it is their responsibility to mitigate the risks arising from their use and, in any event, to comply with applicable regulations, including regulations regarding the use of artificial intelligence.

---
Los modelos publicados en este repositorio tienen una finalidad generalista y están a disposición de terceros. Estos modelos pueden tener sesgos y/u otro tipo de distorsiones indeseables.

Cuando terceros desplieguen o proporcionen sistemas y/o servicios a otras partes usando alguno de estos modelos (o utilizando sistemas basados en estos modelos) o se conviertan en usuarios de los modelos, deben tener en cuenta que es su responsabilidad mitigar los riesgos derivados de su uso y, en todo caso, cumplir con la normativa aplicable, incluyendo la normativa en materia de uso de inteligencia artificial.
