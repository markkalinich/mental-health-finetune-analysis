---
widget:
- text: "The patient was administered acetylsalicylic acid for pain relief."
- text: "Treatment with doxorubicin showed significant improvement in tumor regression."
- text: "The compound benzylpenicillin demonstrated strong antimicrobial activity."
- text: "Further studies are needed to understand the effects of methotrexate on rheumatoid arthritis."
- text: "The synthesis of vancomycin remains a significant challenge in organic chemistry."
tags:
- token-classification
- named-entity-recognition
- biomedical-nlp
- transformers
- chemical-entity-recognition
- drug-discovery
- pharmacology
- chemistry
- chem
language:
- en
license: apache-2.0
---

# 🧬 [OpenMed-NER-ChemicalDetect-BigMed-560M](https://huggingface.co/OpenMed/OpenMed-NER-ChemicalDetect-BigMed-560M)

**Specialized model for Chemical Entity Recognition - Identifies chemical compounds and substances in biomedical literature**

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)]()
[![Transformers](https://img.shields.io/badge/🤗-Transformers-yellow)]()
[![OpenMed](https://img.shields.io/badge/🏥-OpenMed-green)](https://huggingface.co/OpenMed)

## 📋 Model Overview

This model is a **state-of-the-art** fine-tuned transformer engineered to deliver **enterprise-grade accuracy** for chemical entity recognition - identifies chemical compounds and substances in biomedical literature. This specialized model excels at identifying and extracting biomedical entities from clinical texts, research papers, and healthcare documents, enabling applications such as **drug interaction detection**, **medication extraction from patient records**, **adverse event monitoring**, **literature mining for drug discovery**, and **biomedical knowledge graph construction** with **production-ready reliability** for clinical and research applications.

### 🎯 Key Features
- **High Precision**: Optimized for biomedical entity recognition
- **Domain-Specific**: Trained on curated BC4CHEMD dataset
- **Production-Ready**: Validated on clinical benchmarks
- **Easy Integration**: Compatible with Hugging Face Transformers ecosystem

### 🏷️ Supported Entity Types

This model can identify and classify the following biomedical entities:

- `B-CHEM`
- `I-CHEM`

## 📊 Dataset

BC4CHEMD is a biomedical NER corpus for chemical entity recognition from the BioCreative IV challenge.

The BC4CHEMD (BioCreative IV Chemical Entity Mention) corpus is a manually annotated dataset designed for chemical entity recognition in biomedical literature. Created for the BioCreative IV challenge, this corpus contains abstracts from PubMed with chemical entities annotated according to Chemical Entities of Biological Interest (ChEBI) guidelines. The dataset is specifically designed to advance automated chemical name recognition systems for drug discovery, pharmacology, and chemical biology applications. It serves as a benchmark for evaluating named entity recognition models in identifying chemical compounds, drugs, and other chemical substances mentioned in scientific literature.


## 📊 Performance Metrics

### Current Model Performance
- **F1 Score**: `0.95`
- **Precision**: `0.94`
- **Recall**: `0.95`
- **Accuracy**: `0.99`

### 🏆 Comparative Performance on BC4CHEMD Dataset

| Rank | Model | F1 Score | Precision | Recall | Accuracy |
|------|-------|----------|-----------|--------|-----------|
| 🥇 1 | [OpenMed-NER-ChemicalDetect-PubMed-335M](https://huggingface.co/OpenMed/OpenMed-NER-ChemicalDetect-PubMed-335M) | **0.9540** | 0.9498 | 0.9582 | 0.9902 |
| 🥈 2 | [OpenMed-NER-ChemicalDetect-PubMed-109M](https://huggingface.co/OpenMed/OpenMed-NER-ChemicalDetect-PubMed-109M) | **0.9490** | 0.9447 | 0.9534 | 0.9891 |
| 🥉 3 | [OpenMed-NER-ChemicalDetect-PubMed-109M](https://huggingface.co/OpenMed/OpenMed-NER-ChemicalDetect-PubMed-109M) | **0.9487** | 0.9418 | 0.9557 | 0.9892 |
|  4 | [OpenMed-NER-ChemicalDetect-SnowMed-568M](https://huggingface.co/OpenMed/OpenMed-NER-ChemicalDetect-SnowMed-568M) | **0.9485** | 0.9469 | 0.9502 | 0.9891 |
|  5 | [OpenMed-NER-ChemicalDetect-ElectraMed-560M](https://huggingface.co/OpenMed/OpenMed-NER-ChemicalDetect-ElectraMed-560M) | **0.9480** | 0.9455 | 0.9505 | 0.9890 |
|  6 | [OpenMed-NER-ChemicalDetect-SuperClinical-434M](https://huggingface.co/OpenMed/OpenMed-NER-ChemicalDetect-SuperClinical-434M) | **0.9469** | 0.9427 | 0.9512 | 0.9881 |
|  7 | [OpenMed-NER-ChemicalDetect-SuperMedical-355M](https://huggingface.co/OpenMed/OpenMed-NER-ChemicalDetect-SuperMedical-355M) | **0.9462** | 0.9418 | 0.9507 | 0.9875 |
|  8 | [OpenMed-NER-ChemicalDetect-MultiMed-335M](https://huggingface.co/OpenMed/OpenMed-NER-ChemicalDetect-MultiMed-335M) | **0.9460** | 0.9435 | 0.9485 | 0.9857 |
|  9 | [OpenMed-NER-ChemicalDetect-MultiMed-568M](https://huggingface.co/OpenMed/OpenMed-NER-ChemicalDetect-MultiMed-568M) | **0.9459** | 0.9437 | 0.9481 | 0.9885 |
|  10 | [OpenMed-NER-ChemicalDetect-BigMed-560M](https://huggingface.co/OpenMed/OpenMed-NER-ChemicalDetect-BigMed-560M) | **0.9454** | 0.9376 | 0.9534 | 0.9888 |


*Rankings based on F1-score performance across all models trained on this dataset.*

![OpenMed (open-source) vs. latest closed-source SOTA](https://huggingface.co/spaces/OpenMed/README/resolve/main/openmed_vs_sota_performance.png)

*Figure: OpenMed (Open-Source) vs. Latest SOTA (Closed-Source) performance comparison across biomedical NER datasets.*

## 🚀 Quick Start

### Installation

```bash
pip install transformers torch
```

### Usage

```python
from transformers import pipeline

# Load the model and tokenizer
# Model: https://huggingface.co/OpenMed/OpenMed-NER-ChemicalDetect-BigMed-560M
model_name = "OpenMed/OpenMed-NER-ChemicalDetect-BigMed-560M"

# Create a pipeline
medical_ner_pipeline = pipeline(
    model=model_name,
    aggregation_strategy="simple"
)

# Example usage
text = "The patient was administered acetylsalicylic acid for pain relief."
entities = medical_ner_pipeline(text)

print(entities)

token = entities[0]
print(text[token["start"] : token["end"]])
```

NOTE: The `aggregation_strategy` parameter defines how token predictions are grouped into entities. For a detailed explanation, please refer to the [Hugging Face documentation](https://huggingface.co/docs/transformers/en/main_classes/pipelines#transformers.TokenClassificationPipeline.aggregation_strategy).

Here is a summary of the available strategies:
- **`none`**: Returns raw token predictions without any aggregation.
- **`simple`**: Groups adjacent tokens with the same entity type (e.g., `B-LOC` followed by `I-LOC`).
- **`first`**: For word-based models, if tokens within a word have different entity tags, the tag of the first token is assigned to the entire word.
- **`average`**: For word-based models, this strategy averages the scores of tokens within a word and applies the label with the highest resulting score.
- **`max`**: For word-based models, the entity label from the token with the highest score within a word is assigned to the entire word.

### Batch Processing

For efficient processing of large datasets, use proper batching with the `batch_size` parameter:

```python
texts = [
    "The patient was administered acetylsalicylic acid for pain relief.",
    "Treatment with doxorubicin showed significant improvement in tumor regression.",
    "The compound benzylpenicillin demonstrated strong antimicrobial activity.",
    "Further studies are needed to understand the effects of methotrexate on rheumatoid arthritis.",
    "The synthesis of vancomycin remains a significant challenge in organic chemistry.",
]

# Efficient batch processing with optimized batch size
# Adjust batch_size based on your GPU memory (typically 8, 16, 32, or 64)
results = medical_ner_pipeline(texts, batch_size=8)

for i, entities in enumerate(results):
    print(f"Text {i+1} entities:")
    for entity in entities:
        print(f"  - {entity['word']} ({entity['entity_group']}): {entity['score']:.4f}")
```

### Large Dataset Processing

For processing large datasets efficiently:

```python
from transformers.pipelines.pt_utils import KeyDataset
from datasets import Dataset
import pandas as pd

# Load your data
# Load a medical dataset from Hugging Face
from datasets import load_dataset

# Load a public medical dataset (using a subset for testing)
medical_dataset = load_dataset("BI55/MedText", split="train[:100]")  # Load first 100 examples
data = pd.DataFrame({"text": medical_dataset["Completion"]})
dataset = Dataset.from_pandas(data)

# Process with optimal batching for your hardware
batch_size = 16  # Tune this based on your GPU memory
results = []

for out in medical_ner_pipeline(KeyDataset(dataset, "text"), batch_size=batch_size):
    results.extend(out)

print(f"Processed {len(results)} texts with batching")

```

### Performance Optimization

**Batch Size Guidelines:**
- **CPU**: Start with batch_size=1-4
- **Single GPU**: Try batch_size=8-32 depending on GPU memory
- **High-end GPU**: Can handle batch_size=64 or higher
- **Monitor GPU utilization** to find the optimal batch size for your hardware

**Memory Considerations:**
```python
# For limited GPU memory, use smaller batches
medical_ner_pipeline = pipeline(
    model=model_name,
    aggregation_strategy="simple",
    device=0  # Specify GPU device
)

# Process with memory-efficient batching
for batch_start in range(0, len(texts), batch_size):
    batch = texts[batch_start:batch_start + batch_size]
    batch_results = medical_ner_pipeline(batch, batch_size=len(batch))
    results.extend(batch_results)
```

## 📚 Dataset Information

- **Dataset**: BC4CHEMD
- **Description**: Chemical Entity Recognition - Identifies chemical compounds and substances in biomedical literature

### Training Details
- **Base Model**: xlm-roberta-large
- **Training Framework**: Hugging Face Transformers
- **Optimization**: AdamW optimizer with learning rate scheduling
- **Validation**: Cross-validation on held-out test set

## 🔬 Model Architecture

- **Base Architecture**: xlm-roberta-large
- **Task**: Token Classification (Named Entity Recognition)
- **Labels**: Dataset-specific entity types
- **Input**: Tokenized biomedical text
- **Output**: BIO-tagged entity predictions

## 💡 Use Cases

This model is particularly useful for:
- **Clinical Text Mining**: Extracting entities from medical records
- **Biomedical Research**: Processing scientific literature
- **Drug Discovery**: Identifying chemical compounds and drugs
- **Healthcare Analytics**: Analyzing patient data and outcomes
- **Academic Research**: Supporting biomedical NLP research

## 📜 License

Licensed under the Apache License 2.0. See [LICENSE](https://www.apache.org/licenses/LICENSE-2.0) for details.

## 🤝 Contributing

We welcome contributions of all kinds! Whether you have ideas, feature requests, or want to join our mission to advance open-source Healthcare AI, we'd love to hear from you.

Follow [OpenMed Org](https://huggingface.co/OpenMed) on Hugging Face 🤗 and click "Watch" to stay updated on our latest releases and developments.

## Citation

If you use this model in your research or applications, please cite the following paper:

```latex
@misc{panahi2025openmedneropensourcedomainadapted,
      title={OpenMed NER: Open-Source, Domain-Adapted State-of-the-Art Transformers for Biomedical NER Across 12 Public Datasets},
      author={Maziyar Panahi},
      year={2025},
      eprint={2508.01630},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2508.01630},
}
```

Proper citation helps support and acknowledge my work. Thank you!