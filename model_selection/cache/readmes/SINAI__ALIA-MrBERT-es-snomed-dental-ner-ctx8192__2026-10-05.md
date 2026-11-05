---
license: apache-2.0
library_name: transformers
pipeline_tag: token-classification
language:
- es
base_model:
- BSC-LT/MrBERT-es
tags:
- biomedical
- spanish
- dental
- dentistry
- ner
- token-classification
- snomed-ct
- medical-entities
---

# ALIA MrBERT-es Snomed Dental NER Model (Context 8192)

This repository contains **ALIA-MrBERT-es-snomed-dental-ner-ctx8192**, a Spanish dentistry domain Named Entity Recognition (NER) model. It is built upon [MrBERT-es](https://huggingface.co/BSC-LT/MrBERT-es), a bilingual (Spanish-English) foundational language model based on the ModernBERT architecture, and fine-tuned on dentistry-specific clinical data. 

The model is trained to recognize clinical entities corresponding to approximately **400 unique SNOMED CT codes**, serving as the extraction phase (NER) of a clinical entity linking/normalization pipeline in dentistry.

> [!WARNING]
> **DISCLAIMER:** This model is a domain-specific proof-of-concept designed to demonstrate entity recognition capabilities in the Spanish dentistry domain.
> While optimized for identifying dental clinical terms, results should be verified by qualified dental professionals and clinical experts. The model should not be used for automated diagnostic decisions without human expert validation.

---

## Model Details

### Model Lineage

```
ModernBERT (architecture)
       ↓
  MrBERT-es (BSC-LT)
  Bilingual ES/EN encoder
  150M parameters
       ↓
  ALIA-MrBERT-es-snomed-dental-ner-ctx8192 (UJA)
  Dentistry Named Entity Recognition fine-tuning
  ~400 SNOMED CT clinical codes
```

### Key Features

- 🦷 **Domain**: Spanish dental and dentistry clinical texts.
- 📐 **Architecture**: ModernBERT adapted for Token Classification.
- 📏 **Long context**: Up to 8,192 tokens, allowing processing of entire clinical reports or patient histories without truncation.
- 🏷️ **Labels**: Specially trained to identify clinical entities corresponding to approximately 400 unique SNOMED CT codes (e.g., anatomical structures, pathologies, treatments, and devices).
- 🔗 **Downstream Task**: Designed as the foundational extraction layer (NER) for subsequent medical entity linking and terminology mapping.

### Architecture

This model utilizes the ModernBERT architecture, extended with a token classification linear layer on top of the hidden states:

|                              |               |
|------------------------------|:--------------|
| **Base Architecture**        | ModernBERT    |
| **Total Parameters**         | ~150M         |
| **Hidden size**              | 768           |
| **Intermediate size**        | 1,152         |
| **Attention heads**          | 12            |
| **Hidden layers**            | 22            |
| **Context length**           | 8,192 tokens  |
| **Vocabulary size**          | 51,200        |
| **Precision**                | bfloat16      |
| **Positional encoding**      | RoPE          |
| **Activation function**      | GeLU          |
| **Attention type**           | Mixed (global every 3 layers + sliding window) |
| **Classification Head**      | Token Classification (Linear + Softmax) |

---

## Training

### Training Data

The model was fine-tuned on a specialized dentistry corpus containing clinical dialogues, patient summaries, and dental reports. The training set is annotated at the token level using BIO-tagging formats for dental medical entities. 

The entity classes map to approximately **400 distinct SNOMED CT concepts**, including:
- **Pathologies and conditions**: *caries*, *abrasión dental*, *apiñamiento*, *atrofia ósea*, *anquilosis*, *ameloblastoma*.
- **Anatomical structures**: *canino*, *cámara pulpar*, *bifurcación radicular*, *canal mandibular*, *ápice*.
- **Treatments and procedures**: *búsqueda de conducto*, *biopsia*, *cierre*.
- **Clinical findings/devices**: *brecha edéntula*, *corona conservada*, *agregado óseo*.

### Training Strategy

The model was trained using supervised fine-tuning (SFT) for token classification. The loss function optimized during training is Cross-Entropy Loss at the token level, ignoring padding tokens.

### Final Training Hyperparameters

| Hyperparameter | Value | Description |
|----------------|:-----:|:------------|
| **Learning Rate** | 3×10⁻⁵ | Nominal learning rate for token classification |
| **Batch Size** | 32 | Global batch size |
| **Warmup Ratio** | 0.1 | Linear LR warmup at the start of training |
| **Weight Decay** | 0.01 | L2 regularization |
| **Optimizer** | AdamW | Standard HuggingFace Trainer optimizer |
| **Precision** | bf16 | Bfloat16 for Ampere+ architectures |
| **Max Sequence Length** | 8,192 | Maximum tokens processed |
| **Loss Function** | CrossEntropyLoss | Token-level classification loss |

---

## Intended Use

### Direct Use

This model is designed for token extraction and Named Entity Recognition (NER) in the **Spanish dentistry domain**. Primary use cases include:
- **Clinical Entity Extraction**: Identifying dental conditions, anatomical sites, and procedures in clinical notes.
- **Pre-annotation for Entity Linking**: Automatically extracting candidate spans to be resolved to SNOMED CT codes.
- **Dental Record Structuring**: Structuring unstructured dental text into tabular or graph representations.

### Out-of-Scope Use

- General-domain Named Entity Recognition.
- Non-Spanish clinical texts.
- Use as a text-generation model (this is an encoder-only model).
- Automatic clinical diagnosis or treatment planning without human expert review.

---

## How to Use

### With HuggingFace `pipeline`

```python
from transformers import pipeline

# Load the token classification pipeline
ner_pipeline = pipeline(
    "token-classification",
    model="SINAI/ALIA-MrBERT-es-snomed-dental-ner-ctx8192",
    aggregation_strategy="simple"
)

# Example text from a dentistry clinical note
clinical_text = "El paciente presenta una caries severa en el canino inferior y una brecha edéntula en el primer molar."

# Run inference
entities = ner_pipeline(clinical_text)
for entity in entities:
    print(f"Entity: {entity['word']} | Class: {entity['entity_group']} | Score: {entity['score']:.4f}")
```

### With `transformers` (Manual Inference)

```python
import torch
from transformers import AutoTokenizer, AutoModelForTokenClassification

model_name = "SINAI/ALIA-MrBERT-es-snomed-dental-ner-ctx8192"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForTokenClassification.from_pretrained(model_name)

text = "Paciente acude por apiñamiento dental y requiere reconstrucción de corona."
inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=8192)

with torch.no_grad():
    outputs = model(**inputs)

predictions = torch.argmax(outputs.logits, dim=-1)
tokens = tokenizer.convert_ids_to_tokens(inputs["input_ids"][0])

for token, prediction in zip(tokens, predictions[0].tolist()):
    if prediction != 0:  # Assuming 0 is the 'O' (Outside) label
        label = model.config.id2label[prediction]
        print(f"Token: {token:12} -> Label: {label}")
```

---

## Evaluation

The model was evaluated using a train/test split containing **80% training** and **20% testing** data, representing a total of **6,022 entities** in the test set.

### Metrics

The Named Entity Recognition (NER) span-level performance on the test set is as follows:

| Metric | Value |
|:---|:---:|
| **Precision (Spans)** | 96.61% (5,818 / 6,022) |

---

## Limitations and Biases

### Known Limitations

- **Domain Specificity**: The model is highly specialized in dental and oral medicine terminology. Performance will degrade significantly if applied to other medical specialties (e.g., cardiology, oncology) or general text.
- **Language Constraint**: The model is fine-tuned specifically for Spanish clinical narratives.
- **Ambiguous Terms**: Certain abbreviations or short words common in clinical jargon might be misclassified if context is insufficient.

### Biases

- The training distribution reflects the clinical practices, vocabulary, and dialects of the training data providers. Performance may vary across different Spanish-speaking regions or distinct clinical writing styles.

---

## Additional Information

### License
[Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0)

### Citation

If you use this model in your research, please cite:

```bibtex
@misc{ALIA-MrBERT-es-snomed-dental-ner-ctx8192,
  title        = {ALIA MrBERT-es Snomed Dental NER Model},
  author       = {SINAI Research Group, Universidad de Jaén},
  year         = {2026},
  publisher    = {HuggingFace},
  howpublished = {\url{https://huggingface.co/SINAI/ALIA-MrBERT-es-snomed-dental-ner-ctx8192}}
}
```

Please also cite the base model:

```bibtex
@misc{tamayo2026mrbertmodernmultilingualencoders,
      title={MrBERT: Modern Multilingual Encoders via Vocabulary, Domain, and Dimensional Adaptation}, 
      author={Daniel Tamayo and Iñaki Lacunza and Paula Rivera-Hidalgo and Severino Da Dalt and Javier Aula-Blasco and Aitor Gonzalez-Agirre and Marta Villegas},
      year={2026},
      eprint={2602.21379},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2602.21379}, 
}
```

### Funding
This work is funded by the Ministerio para la Transformación Digital y de la Función Pública - Funded by EU – NextGenerationEU within the framework of the project [ALIA](https://alia.gob.es).

### Acknowledgments
This dataset has been generated thanks to [CEATIC](https://www.ujaen.es/centros/ceatic/) (Centro de Estudios Avanzados en Tecnologías de la Información y de la Comunicación) – [UJA](http://www.ujaen.es/) (Universidad de Jaén) which provided the needed computational resources on its clusters.

---

**Contact:** [ALIA Project](https://www.alia.gob.es/) - [SINAI Research Group](https://sinai.ujaen.es) - [Universidad de Jaén](https://www.ujaen.es/)

**More Information:** [SINAI Research Group](https://sinai.ujaen.es) | [ALIA-UJA Project](https://github.com/sinai-uja/ALIA-UJA)
