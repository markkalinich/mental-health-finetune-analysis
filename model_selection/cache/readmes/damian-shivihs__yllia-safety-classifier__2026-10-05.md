---
license: apache-2.0
language:
- pl
library_name: transformers
base_model:
- PKOBP/polish-roberta-8k
pipeline_tag: text-classification
tags:
- text-classification
- safety
- triage
- polish
- mental-health
- crisis-detection
- psychiatric-chatbot
metrics:
- accuracy
- f1
- matthews_correlation
---

# Yllia Safety Classifier

Yllia Safety Classifier is a Polish-language encoder model for first-line safety classification and message routing in mental-health conversational systems.

It classifies a single user message into one of five categories:

- `ATTACK`
- `CRISIS`
- `MEDICAL_SENSITIVE`
- `OFFTOPIC`
- `OK`

The model is based on `PKOBP/polish-roberta-8k` and was fine-tuned as a five-class sequence classifier.

This release is a research checkpoint and an early step toward a broader safety architecture for Polish-language AI systems.

---

## Purpose

The model is intended to support the first stage of message triage.

Its role is to help determine whether an incoming message:

- may be handled as a routine inquiry,
- contains medically sensitive content,
- may indicate a crisis,
- is unrelated to the intended domain,
- or contains adversarial, abusive, or manipulative content.

The model is designed as an additional safety layer, not as a standalone clinical system.

It should be combined with:

- rule-based safeguards,
- secondary review,
- confidence thresholds,
- human escalation paths,
- and explicit crisis procedures.

---

## Labels

| ID | Label | Description |
|---:|---|---|
| 0 | `ATTACK` | Prompt injection, jailbreak attempts, instruction manipulation, abusive language, and spam |
| 1 | `CRISIS` | Suicidal thoughts or plans, self-harm, acute psychosis, command hallucinations, and violence |
| 2 | `MEDICAL_SENSITIVE` | Medication dosing, adverse effects, interactions, requests for diagnosis, and interpretation of medical results |
| 3 | `OFFTOPIC` | Topics unrelated to the psychiatric or psychological practice |
| 4 | `OK` | Routine logistics, appointments, pricing, address, services, treatment inquiries, and other ordinary intake messages |

The checkpoint performs flat single-label classification.

Any routing hierarchy, for example prioritizing `CRISIS` over `MEDICAL_SENSITIVE`, must be implemented at the application level.

---

## Dataset

The project is based on **1,369 original questions written by people**.

The examples were designed to reflect messages that may realistically be sent to a psychiatric or psychological practice.

They include:

- routine organizational questions,
- requests involving medical information,
- crisis-related messages,
- unrelated content,
- abusive or adversarial inputs.

All original examples were reviewed and assigned labels by people involved in the project.

Synthetic variants were created only after the original examples had been prepared and labelled.

The augmentation process included:

- short paraphrases,
- emotionally intensified variants,
- spelling-error variants,
- more verbose variants.

Synthetic data was used to expand linguistic diversity, but evaluation on original human-written examples is reported separately.

The dataset split was performed using the original source question as the grouping key. Synthetic variants derived from the same source question were kept within the same split.

---

## Evaluation

### Independent Test Set — Original Human-Written Questions

The primary evaluation subset contains **206 original questions** and does not include synthetic variants.

| Category | Precision | Recall | F1 | Support |
|---|---:|---:|---:|---:|
| `ATTACK` | 0.8462 | 0.5789 | 0.6875 | 19 |
| `CRISIS` | 0.6562 | 0.7241 | 0.6885 | 29 |
| `MEDICAL_SENSITIVE` | 0.6719 | 0.7679 | 0.7167 | 56 |
| `OFFTOPIC` | 0.8125 | 0.4333 | 0.5652 | 30 |
| `OK` | 0.7160 | 0.8056 | 0.7582 | 72 |
| **Macro average** | **0.7406** | **0.6620** | **0.6832** | **206** |
| Weighted average | 0.7217 | 0.7087 | 0.7025 | 206 |

**Accuracy: 0.7087**

**Macro-F1: 0.6832**

**MCC: 0.6099**

The most operationally relevant recall values are:

- `CRISIS`: **0.7241**
- `MEDICAL_SENSITIVE`: **0.7679**
- `OK`: **0.8056**

These results show that the model can serve as a useful first classification layer, while still requiring additional safeguards for high-risk cases.

---

### Full Test Set — Original and Synthetic Examples

The full test set contains **637 examples**:

- 206 original human-written examples,
- 431 synthetic variants.

**Accuracy: 0.8038**

**Macro-F1: 0.8079**

**MCC: 0.7507**

Performance on synthetic variants is higher than on original human-written questions. For this reason, the independent original-only test subset should be treated as the primary estimate of real-world generalization.

---

## Confusion Matrix

Confusion matrix for the independent original-only test subset.

Rows represent true labels and columns represent predicted labels.

| True \ Predicted | ATTACK | CRISIS | MEDICAL_SENSITIVE | OFFTOPIC | OK |
|---|---:|---:|---:|---:|---:|
| **ATTACK** | 11 | 2 | 1 | 1 | 4 |
| **CRISIS** | 0 | 21 | 5 | 0 | 3 |
| **MEDICAL_SENSITIVE** | 0 | 5 | 43 | 0 | 8 |
| **OFFTOPIC** | 2 | 3 | 4 | 13 | 8 |
| **OK** | 0 | 1 | 11 | 2 | 58 |

---

## Training Details

| Parameter | Value |
|---|---|
| Base model | `PKOBP/polish-roberta-8k` |
| Architecture | `RobertaForSequenceClassification` |
| Number of labels | 5 |
| Training method | Full fine-tuning |
| Learning rate | `3e-6` |
| Batch size | `32` |
| Maximum sequence length | `256` |
| Hidden dropout | `0.25` |
| Attention dropout | `0.25` |
| Classifier dropout | `0.25` |
| Configured epochs | `12` |
| Optimizer epsilon | `1e-8` |
| Precision | FP32 |

Training run:

```text
polish_roberta_8k_bs32_len256_do0p25_lr3e_06
```

The training history suggests the beginning of overfitting in later epochs. Raw softmax probabilities should therefore not be interpreted as calibrated confidence estimates.

Calibration methods such as temperature scaling are recommended before using probability thresholds in a production system.

---

## Usage

```python
import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer

MODEL_ID = "damian-shivihs/yllia-safety-classifier"

tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_ID)
model.eval()


def classify(text: str) -> dict:
    inputs = tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        max_length=256,
    )

    with torch.inference_mode():
        logits = model(**inputs).logits

    probabilities = torch.softmax(logits, dim=-1)[0]
    predicted_id = int(probabilities.argmax())

    return {
        "label": model.config.id2label[predicted_id],
        "score": float(probabilities[predicted_id]),
    }


print(classify("Czy mogę umówić wizytę u psychiatry?"))
```

You can also use the Transformers pipeline:

```python
from transformers import pipeline

classifier = pipeline(
    "text-classification",
    model="damian-shivihs/yllia-safety-classifier",
    top_k=None,
)

print(classifier("Czy mogę umówić wizytę u psychiatry?"))
```

The returned scores are raw softmax values and are not calibrated.

---

## Intended Uses

The model may be useful for:

- first-line triage of messages sent to a psychiatric or psychological chatbot,
- routing messages to safer handling paths,
- detecting messages that may require crisis escalation,
- separating routine questions from medically sensitive requests,
- research on Polish-language safety classification,
- experimentation with safety layers for mental-health AI systems.

---

## Limitations

### Crisis Detection

`CRISIS` recall on the independent original-only test set is **0.7241**.

This means that some crisis-related messages are still assigned to other categories.

The model must not be used as the only crisis-detection mechanism.

### OFFTOPIC Performance

`OFFTOPIC` remains the weakest class, with recall of **0.4333** on the original-only test subset.

### Broad ATTACK Category

`ATTACK` combines several different types of content:

- prompt injection,
- jailbreak attempts,
- abusive language,
- manipulation,
- spam.

Future versions may benefit from separating these behaviors into more precise categories.

### Boundary Between OK and MEDICAL_SENSITIVE

The distinction between a routine service question and a request for medical information can be subtle.

Small wording changes may change the correct label.

### Narrow Domain

The model was trained on short Polish-language messages intended for a psychiatric or psychological practice.

Its behavior on long documents, social-media content, medical records, or unrelated domains has not been established.

### Uncalibrated Probabilities

The confidence scores returned by the model are not calibrated and may be overconfident.

---

## Out-of-Scope Uses

The model is not intended for:

- medical diagnosis,
- psychiatric diagnosis,
- individual suicide-risk assessment,
- medication recommendations,
- clinical decision-making,
- replacing human review,
- use as the only safety layer in a mental-health system.

This is not a clinical product and has not undergone regulatory or prospective clinical validation.

---

## Collaboration

The dataset was prepared and evaluated in cooperation with the **AI4BUSINESS Student Research Group**.

The following people contributed to the creation, collection, evaluation, organization, and description of the dataset:

- **Katarzyna Jurczak**
- **Agnieszka Ruszczak**
- **Wojciu**
- **Grzegorz Borkowski**
- **Katarzyna Surmacka**
- **Differ3nt**
- and other members of the team involved in the project

Academic support and acknowledgement:

- **Professor Iwona Chomiak-Orsa**
- **Professor Krzysztof Piontek**

Wroclaw University of Economics and Business.

---

## Project Lead

**Damian Siwicki**

Psychiatrist and computer science engineer based in Wrocław, Poland.

---

## Future Development

This release is only the beginning.

Planned directions include:

- collecting more original human-written examples,
- improving `CRISIS` recall,
- reviewing ambiguous labels,
- calibrating confidence scores,
- splitting broad categories into more precise subtypes,
- testing hierarchical and multi-label approaches,
- integrating the classifier into the broader Yllia system,
- transferring the experience gained from this encoder to Polish generative models,
- further work with models from the **Bielik** family,
- developing psychologically safer Polish-language AI systems.

---

## Model Status

This release should be considered a **research and development checkpoint**.

The model is public so that it can be tested, reviewed, criticized, and improved.

---

## Model Card

https://huggingface.co/damian-shivihs/yllia-safety-classifier

---

## Citation

```bibtex
@misc{siwicki2026yllia,
  title        = {Yllia Safety Classifier: Polish Encoder-Based Safety and Triage Model},
  author       = {Siwicki, Damian},
  year         = {2026},
  howpublished = {\url{https://huggingface.co/damian-shivihs/yllia-safety-classifier}}
}
```
