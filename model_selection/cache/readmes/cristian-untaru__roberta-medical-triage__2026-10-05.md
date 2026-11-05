---
license: mit
language:
- en
datasets:
- cristian-untaru/symcat-medical-triage-dataset
tags:
- medical-triage
- text-classification
- roberta
- healthcare
- symptom-checker
- natural-language-processing
- academic-project
pipeline_tag: text-classification
library_name: transformers
base_model: FacebookAI/roberta-base
model-index:
- name: roberta-medical-triage
  results:
  - task:
      type: text-classification
      name: Medical pre-triage classification
    dataset:
      name: SymCAT Medical Triage Dataset
      type: cristian-untaru/symcat-medical-triage-dataset
    metrics:
    - type: accuracy
      value: 0.6792
      name: Accuracy
    - type: f1
      value: 0.6772
      name: Macro F1
    - type: precision
      value: 0.6908
      name: Macro Precision
    - type: recall
      value: 0.6742
      name: Macro Recall
    - type: roc_auc
      value: 0.8523
      name: Macro AUC OvR
---

# RoBERTa Medical Triage Classifier

## Model Description

This repository contains a fully fine-tuned RoBERTa sequence classification model. Full fine-tuning updates the transformer encoder and the classification head.

The model receives a short English symptom description and predicts one of the following triage-oriented labels:

- `self_monitor`
- `consult_gp`
- `urgent`

This model was developed as part of the **SortMed** academic project, a medical pre-triage assistant prototype built for a bachelor's thesis by **Cristian Untaru** at the **West University of Timișoara, Faculty of Informatics**.

The model is intended for research and educational use. It is not a diagnostic system and is not a certified medical device.

## Intended Use

This model is intended to be used in an academic medical pre-triage prototype for:

- classifying English symptom descriptions into broad urgency categories;
- comparing transformer-based models for medical text classification;
- evaluating full fine-tuning against parameter-efficient fine-tuning methods;
- supporting experimental NLP research in symptom-based medical pre-triage.

Example input:

```text
I have chest pain, shortness of breath, and I feel dizzy.
```

Example output:

```text
urgent
```

## Out-of-Scope Use

This model must not be used as:

- a replacement for professional medical advice;
- a diagnostic system;
- an emergency decision-making tool;
- a certified clinical triage system;
- a standalone healthcare product;
- a tool for non-English medical text without additional validation.

For severe, worsening, or emergency symptoms, users should contact emergency services or a qualified healthcare professional.

## Labels

The model predicts one of three labels:

| Label | Meaning |
|---|---|
| `self_monitor` | Symptoms appear mild and may be monitored, assuming no worsening or additional warning signs. |
| `consult_gp` | A general practitioner or non-emergency medical professional should be consulted. |
| `urgent` | Symptoms may require urgent medical attention or emergency evaluation. |

The label mapping is included in [`label_map.json`](./label_map.json) and in the model configuration.

Expected mapping:

```python
{
    0: "self_monitor",
    1: "consult_gp",
    2: "urgent",
}
```

## Training Data

The model was trained on the [`cristian-untaru/symcat-medical-triage-dataset`](https://huggingface.co/datasets/cristian-untaru/symcat-medical-triage-dataset), a SymCAT-derived dataset prepared for academic experiments in medical pre-triage classification.

The dataset contains English symptom-based text examples labeled into three triage classes:

- `self_monitor`
- `consult_gp`
- `urgent`

Dataset split used for training:

| Split | Examples |
|---|---:|
| Train | 490 |
| Validation | 105 |
| Test | 106 |
| Total | 701 |

The dataset labels were produced using rule-based triage logic for academic experimentation. They are not clinically validated annotations from medical professionals.

MedQuAD was not used to train this classifier. In the broader SortMed system, MedQuAD is used separately for retrieval of related medical information through the [`cristian-untaru/medquad-retrieval-pretriage`](https://huggingface.co/datasets/cristian-untaru/medquad-retrieval-pretriage) dataset.

## Training Procedure

Base checkpoint:

```text
FacebookAI/roberta-base
```

| Parameter | Value |
|---|---:|
| Fine-tuning method | Full Fine-Tuning |
| Maximum sequence length | 128 |
| Epochs | 5 |
| Train batch size | 16 |
| Evaluation batch size | 32 |
| Learning rate | 2e-05 |
| Weight decay | 0.01 |
| Warmup ratio | 0.1 |
| Mixed precision | FP16 |
| Early stopping patience | 2 |
| Best checkpoint metric | f1 |
| Random seed | 42 |

Additional training metadata is available in [`training_config.json`](./training_config.json).

## Evaluation Results

The model was evaluated on the held-out test split.

| Metric | Test Score |
|---|---:|
| Accuracy | 0.6792 |
| Macro Precision | 0.6908 |
| Macro Recall / Sensitivity | 0.6742 |
| Macro Specificity | 0.8355 |
| Macro F1 | 0.6772 |
| Macro AUC OvR | 0.8523 |
| Macro IoU / Jaccard | 0.5181 |
| Test Loss | 0.8294 |

### Per-Class Results

| Class | Precision | Recall / Sensitivity | F1-score | Support |
|---|---:|---:|---:|---:|
| `self_monitor` | 0.68 | 0.70 | 0.69 | 33 |
| `consult_gp` | 0.63 | 0.60 | 0.62 | 40 |
| `urgent` | 0.65 | 0.67 | 0.66 | 33 |

These results should be interpreted in the context of the small dataset size and the academic nature of the experiment.

## How to Use

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

repo_id = "cristian-untaru/roberta-medical-triage"

tokenizer = AutoTokenizer.from_pretrained(repo_id)
model = AutoModelForSequenceClassification.from_pretrained(repo_id)

text = "I have chest pain, shortness of breath, and I feel dizzy."

inputs = tokenizer(
    text,
    return_tensors="pt",
    truncation=True,
    padding=True,
    max_length=128
)

with torch.no_grad():
    outputs = model(**inputs)
    probabilities = torch.softmax(outputs.logits, dim=-1)
    predicted_class_id = torch.argmax(probabilities, dim=-1).item()

predicted_label = model.config.id2label[predicted_class_id]
confidence = probabilities[0][predicted_class_id].item()

print("Predicted label:", predicted_label)
print("Confidence:", round(confidence, 4))
```


This model loads with the standard Transformers API and does not require `trust_remote_code=True`.


To verify the label mapping:

```python
print(model.config.id2label)
```

Expected output:

```python
{0: "self_monitor", 1: "consult_gp", 2: "urgent"}
```

## Repository Files

| File | Description |
|---|---|
| `config.json` | Model architecture, label mapping, and classification configuration. |
| `model.safetensors` | Model weights in SafeTensors format. |
| `tokenizer.json` | Tokenizer vocabulary and processing pipeline. |
| `tokenizer_config.json` | Tokenizer configuration. |
| `training_args.bin` | Hugging Face Trainer arguments saved during training. |
| `training_config.json` | Human-readable training configuration. |
| `label_map.json` | Mapping between numeric class IDs and triage labels. |
| `README.md` | Model card documentation. |
| `.gitattributes` | Git LFS configuration for large model files. |

## Limitations

This model has several important limitations:

- It was trained on a small academic dataset.
- The labels are rule-based and not clinically validated by medical experts.
- It does not perform medical diagnosis.
- It does not consider patient age, sex, medical history, medication history, vital signs, comorbidities, pregnancy status, allergies, or physical examination findings.
- It may produce incorrect predictions for rare, ambiguous, incomplete, severe, or contradictory symptom descriptions.
- It was trained for English text only.
- It should not be used for emergency triage without medical supervision.
- Its predictions depend on the quality and completeness of the user-provided text.

## Ethical and Safety Considerations

Medical pre-triage systems can influence user decisions in sensitive healthcare situations. This model should therefore be used only with clear disclaimers and with safeguards that encourage users to seek professional medical care when appropriate.

Any real-world deployment would require:

- clinical expert review;
- validation on larger and more representative medical datasets;
- safety testing;
- bias and fairness evaluation;
- monitoring for incorrect or unsafe predictions;
- clear user-facing warnings;
- escalation rules for emergency symptoms.

## Medical Disclaimer

This model is intended only for academic, research, and prototype development purposes. It is not a substitute for professional medical advice, diagnosis, treatment, or emergency care.

If symptoms are severe, sudden, worsening, or potentially life-threatening, users should contact emergency services or a qualified healthcare professional immediately.

## Related Datasets

- [`cristian-untaru/symcat-medical-triage-dataset`](https://huggingface.co/datasets/cristian-untaru/symcat-medical-triage-dataset)
- [`cristian-untaru/medquad-retrieval-pretriage`](https://huggingface.co/datasets/cristian-untaru/medquad-retrieval-pretriage)

## Related Models

### Full Fine-Tuned Models

- [`cristian-untaru/distilbert-medical-triage`](https://huggingface.co/cristian-untaru/distilbert-medical-triage)
- [`cristian-untaru/biobert-medical-triage`](https://huggingface.co/cristian-untaru/biobert-medical-triage)
- [`cristian-untaru/roberta-medical-triage`](https://huggingface.co/cristian-untaru/roberta-medical-triage)
- [`cristian-untaru/biomedbert-medical-triage`](https://huggingface.co/cristian-untaru/biomedbert-medical-triage)

### LoRA Models

- [`cristian-untaru/lora-distilbert-medical-triage`](https://huggingface.co/cristian-untaru/lora-distilbert-medical-triage)
- [`cristian-untaru/lora-biobert-medical-triage`](https://huggingface.co/cristian-untaru/lora-biobert-medical-triage)
- [`cristian-untaru/lora-roberta-medical-triage`](https://huggingface.co/cristian-untaru/lora-roberta-medical-triage)
- [`cristian-untaru/lora-biomedbert-medical-triage`](https://huggingface.co/cristian-untaru/lora-biomedbert-medical-triage)

### Bottleneck MLP Adapter Models

- [`cristian-untaru/bottleneck-mlp-distilbert-medical-triage`](https://huggingface.co/cristian-untaru/bottleneck-mlp-distilbert-medical-triage)
- [`cristian-untaru/bottleneck-mlp-biobert-medical-triage`](https://huggingface.co/cristian-untaru/bottleneck-mlp-biobert-medical-triage)
- [`cristian-untaru/bottleneck-mlp-roberta-medical-triage`](https://huggingface.co/cristian-untaru/bottleneck-mlp-roberta-medical-triage)
- [`cristian-untaru/bottleneck-mlp-biomedbert-medical-triage`](https://huggingface.co/cristian-untaru/bottleneck-mlp-biomedbert-medical-triage)

### Frozen Encoder Models

- [`cristian-untaru/frozen-encoder-distilbert-medical-triage`](https://huggingface.co/cristian-untaru/frozen-encoder-distilbert-medical-triage)
- [`cristian-untaru/frozen-encoder-biobert-medical-triage`](https://huggingface.co/cristian-untaru/frozen-encoder-biobert-medical-triage)
- [`cristian-untaru/frozen-encoder-roberta-medical-triage`](https://huggingface.co/cristian-untaru/frozen-encoder-roberta-medical-triage)
- [`cristian-untaru/frozen-encoder-biomedbert-medical-triage`](https://huggingface.co/cristian-untaru/frozen-encoder-biomedbert-medical-triage)
