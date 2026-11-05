---
widget:
- text: "The BRCA2 gene is associated with hereditary breast cancer."
- text: "Mutations in the CFTR gene cause cystic fibrosis."
- text: "The APOE gene variant affects Alzheimer's disease risk."
- text: "The HTT gene provides instructions for making a protein called huntingtin."
- text: "Sickle cell disease is caused by a mutation in the HBB gene."
tags:
- token-classification
- named-entity-recognition
- biomedical-nlp
- transformers
- gene-recognition
- genetics
- genomics
- molecular-biology
- cell-line-name
language:
- en
license: apache-2.0
---

# 🧬 [OpenMed-NER-GenomicDetect-ElectraMed-109M](https://huggingface.co/OpenMed/OpenMed-NER-GenomicDetect-ElectraMed-109M)

**Specialized model for Gene Entity Recognition - Gene-related entities**

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)]()
[![Transformers](https://img.shields.io/badge/🤗-Transformers-yellow)]()
[![OpenMed](https://img.shields.io/badge/🏥-OpenMed-green)](https://huggingface.co/OpenMed)

## 📋 Model Overview

This model is a **state-of-the-art** fine-tuned transformer engineered to deliver **enterprise-grade accuracy** for gene entity recognition - gene-related entities. This specialized model excels at identifying and extracting biomedical entities from clinical texts, research papers, and healthcare documents, enabling applications such as **drug interaction detection**, **medication extraction from patient records**, **adverse event monitoring**, **literature mining for drug discovery**, and **biomedical knowledge graph construction** with **production-ready reliability** for clinical and research applications.

### 🎯 Key Features
- **High Precision**: Optimized for biomedical entity recognition
- **Domain-Specific**: Trained on curated GELLUS dataset
- **Production-Ready**: Validated on clinical benchmarks
- **Easy Integration**: Compatible with Hugging Face Transformers ecosystem

### 🏷️ Supported Entity Types

This model can identify and classify the following biomedical entities:

- `B-Cell-line-name`
- `I-Cell-line-name`

## 📊 Dataset

Gellus corpus targets gene recognition and genetics entities for genomics and molecular biology applications.

The Gellus corpus is a biomedical NER dataset specifically designed for gene recognition and genetics entity extraction in molecular biology literature. This corpus contains comprehensive annotations for gene names, genetic variants, and genomics-related entities that are essential for genetic research and genomics applications. The dataset supports the development of automated systems for gene mention identification, genetic association studies, and genomics text mining. It is particularly valuable for identifying genes involved in hereditary diseases, genetic disorders, and molecular genetics research. The corpus serves as a benchmark for evaluating NER models used in genetics research, personalized medicine, and genomics informatics, contributing to advances in precision medicine and genetic counseling applications.


## 📊 Performance Metrics

### Current Model Performance
- **F1 Score**: `0.97`
- **Precision**: `1.00`
- **Recall**: `0.94`
- **Accuracy**: `0.99`

### 🏆 Comparative Performance on GELLUS Dataset

| Rank | Model | F1 Score | Precision | Recall | Accuracy |
|------|-------|----------|-----------|--------|-----------|
| 🥇 1 | [OpenMed-NER-GenomicDetect-SnowMed-568M](https://huggingface.co/OpenMed/OpenMed-NER-GenomicDetect-SnowMed-568M) | **0.9976** | 0.9977 | 0.9975 | 0.9989 |
| 🥈 2 | [OpenMed-NER-GenomicDetect-SuperMedical-355M](https://huggingface.co/OpenMed/OpenMed-NER-GenomicDetect-SuperMedical-355M) | **0.9970** | 0.9960 | 0.9981 | 0.9986 |
| 🥉 3 | [OpenMed-NER-GenomicDetect-BigMed-560M](https://huggingface.co/OpenMed/OpenMed-NER-GenomicDetect-BigMed-560M) | **0.9968** | 0.9967 | 0.9969 | 0.9986 |
|  4 | [OpenMed-NER-GenomicDetect-MultiMed-568M](https://huggingface.co/OpenMed/OpenMed-NER-GenomicDetect-MultiMed-568M) | **0.9967** | 0.9974 | 0.9960 | 0.9985 |
|  5 | [OpenMed-NER-GenomicDetect-PubMed-109M](https://huggingface.co/OpenMed/OpenMed-NER-GenomicDetect-PubMed-109M) | **0.9964** | 0.9957 | 0.9970 | 0.9992 |
|  6 | [OpenMed-NER-GenomicDetect-PubMed-335M](https://huggingface.co/OpenMed/OpenMed-NER-GenomicDetect-PubMed-335M) | **0.9963** | 0.9961 | 0.9965 | 0.9991 |
|  7 | [OpenMed-NER-GenomicDetect-PubMed-109M](https://huggingface.co/OpenMed/OpenMed-NER-GenomicDetect-PubMed-109M) | **0.9951** | 0.9948 | 0.9953 | 0.9991 |
|  8 | [OpenMed-NER-GenomicDetect-BioMed-109M](https://huggingface.co/OpenMed/OpenMed-NER-GenomicDetect-BioMed-109M) | **0.9941** | 0.9934 | 0.9949 | 0.9988 |
|  9 | [OpenMed-NER-GenomicDetect-TinyMed-82M](https://huggingface.co/OpenMed/OpenMed-NER-GenomicDetect-TinyMed-82M) | **0.9940** | 0.9997 | 0.9884 | 0.9961 |
|  10 | [OpenMed-NER-GenomicDetect-SuperMedical-125M](https://huggingface.co/OpenMed/OpenMed-NER-GenomicDetect-SuperMedical-125M) | **0.9934** | 0.9999 | 0.9870 | 0.9958 |


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
# Model: https://huggingface.co/OpenMed/OpenMed-NER-GenomicDetect-ElectraMed-109M
model_name = "OpenMed/OpenMed-NER-GenomicDetect-ElectraMed-109M"

# Create a pipeline
medical_ner_pipeline = pipeline(
    model=model_name,
    aggregation_strategy="simple"
)

# Example usage
text = "The BRCA2 gene is associated with hereditary breast cancer."
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
    "The BRCA2 gene is associated with hereditary breast cancer.",
    "Mutations in the CFTR gene cause cystic fibrosis.",
    "The APOE gene variant affects Alzheimer's disease risk.",
    "The HTT gene provides instructions for making a protein called huntingtin.",
    "Sickle cell disease is caused by a mutation in the HBB gene.",
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

- **Dataset**: GELLUS
- **Description**: Gene Entity Recognition - Gene-related entities

### Training Details
- **Base Model**: e5-base-v2
- **Training Framework**: Hugging Face Transformers
- **Optimization**: AdamW optimizer with learning rate scheduling
- **Validation**: Cross-validation on held-out test set

## 🔬 Model Architecture

- **Base Architecture**: e5-base-v2
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