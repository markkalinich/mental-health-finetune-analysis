---
widget:
- text: "Escherichia coli bacteria were found in the water samples."
- text: "The study included specimens from Homo sapiens and Mus musculus."
- text: "Saccharomyces cerevisiae is commonly used in biotechnology applications."
- text: "The venom of the black mamba, Dendroaspis polylepis, is highly neurotoxic."
- text: "Canis lupus familiaris has been domesticated for thousands of years."
tags:
- token-classification
- named-entity-recognition
- biomedical-nlp
- transformers
- species-recognition
- taxonomy
- organism-identification
- biology
- species
language:
- en
license: apache-2.0
---

# 🧬 [OpenMed-NER-SpeciesDetect-TinyMed-135M](https://huggingface.co/OpenMed/OpenMed-NER-SpeciesDetect-TinyMed-135M)

**Specialized model for Species Entity Recognition - Species and organism names**

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)]()
[![Transformers](https://img.shields.io/badge/🤗-Transformers-yellow)]()
[![OpenMed](https://img.shields.io/badge/🏥-OpenMed-green)](https://huggingface.co/OpenMed)

## 📋 Model Overview

This model is a **state-of-the-art** fine-tuned transformer engineered to deliver **enterprise-grade accuracy** for species entity recognition - species and organism names. This specialized model excels at identifying and extracting biomedical entities from clinical texts, research papers, and healthcare documents, enabling applications such as **drug interaction detection**, **medication extraction from patient records**, **adverse event monitoring**, **literature mining for drug discovery**, and **biomedical knowledge graph construction** with **production-ready reliability** for clinical and research applications.

### 🎯 Key Features
- **High Precision**: Optimized for biomedical entity recognition
- **Domain-Specific**: Trained on curated LINNAEUS dataset
- **Production-Ready**: Validated on clinical benchmarks
- **Easy Integration**: Compatible with Hugging Face Transformers ecosystem

### 🏷️ Supported Entity Types

This model can identify and classify the following biomedical entities:

- `B-SPECIES`
- `I-SPECIES`

## 📊 Dataset

Linnaeus corpus is designed for species name identification and taxonomic entity recognition in biomedical literature.

The Linnaeus corpus is a specialized biomedical NER dataset focused on species name identification and organism recognition in scientific literature. Named after Carl Linnaeus who established modern taxonomic nomenclature, this corpus contains annotations for species mentions that are normalized to NCBI Taxonomy identifiers. The dataset is crucial for biodiversity informatics, ecological research, and biological literature mining where accurate organism identification is essential. It supports the development of text mining systems for taxonomic studies, species distribution research, and comparative genomics applications. The corpus addresses the challenge of recognizing both scientific names and common names of organisms across diverse biological texts.


## 📊 Performance Metrics

### Current Model Performance
- **F1 Score**: `0.94`
- **Precision**: `0.93`
- **Recall**: `0.94`
- **Accuracy**: `0.99`

### 🏆 Comparative Performance on LINNAEUS Dataset

| Rank | Model | F1 Score | Precision | Recall | Accuracy |
|------|-------|----------|-----------|--------|-----------|
| 🥇 1 | [OpenMed-NER-SpeciesDetect-PubMed-335M](https://huggingface.co/OpenMed/OpenMed-NER-SpeciesDetect-PubMed-335M) | **0.9649** | 0.9582 | 0.9718 | 0.9967 |
| 🥈 2 | [OpenMed-NER-SpeciesDetect-PubMed-109M](https://huggingface.co/OpenMed/OpenMed-NER-SpeciesDetect-PubMed-109M) | **0.9543** | 0.9422 | 0.9667 | 0.9956 |
| 🥉 3 | [OpenMed-NER-SpeciesDetect-BioMed-335M](https://huggingface.co/OpenMed/OpenMed-NER-SpeciesDetect-BioMed-335M) | **0.9539** | 0.9441 | 0.9638 | 0.9957 |
|  4 | [OpenMed-NER-SpeciesDetect-SuperClinical-434M](https://huggingface.co/OpenMed/OpenMed-NER-SpeciesDetect-SuperClinical-434M) | **0.9534** | 0.9369 | 0.9704 | 0.9959 |
|  5 | [OpenMed-NER-SpeciesDetect-PubMed-109M](https://huggingface.co/OpenMed/OpenMed-NER-SpeciesDetect-PubMed-109M) | **0.9502** | 0.9317 | 0.9695 | 0.9951 |
|  6 | [OpenMed-NER-SpeciesDetect-MultiMed-335M](https://huggingface.co/OpenMed/OpenMed-NER-SpeciesDetect-MultiMed-335M) | **0.9479** | 0.9286 | 0.9680 | 0.9955 |
|  7 | [OpenMed-NER-SpeciesDetect-MultiMed-568M](https://huggingface.co/OpenMed/OpenMed-NER-SpeciesDetect-MultiMed-568M) | **0.9460** | 0.9312 | 0.9613 | 0.9957 |
|  8 | [OpenMed-NER-SpeciesDetect-SuperMedical-355M](https://huggingface.co/OpenMed/OpenMed-NER-SpeciesDetect-SuperMedical-355M) | **0.9433** | 0.9221 | 0.9655 | 0.9953 |
|  9 | [OpenMed-NER-SpeciesDetect-SuperClinical-141M](https://huggingface.co/OpenMed/OpenMed-NER-SpeciesDetect-SuperClinical-141M) | **0.9406** | 0.9290 | 0.9525 | 0.9950 |
|  10 | [OpenMed-NER-SpeciesDetect-ModernClinical-395M](https://huggingface.co/OpenMed/OpenMed-NER-SpeciesDetect-ModernClinical-395M) | **0.9385** | 0.9379 | 0.9392 | 0.9940 |


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
# Model: https://huggingface.co/OpenMed/OpenMed-NER-SpeciesDetect-TinyMed-135M
model_name = "OpenMed/OpenMed-NER-SpeciesDetect-TinyMed-135M"

# Create a pipeline
medical_ner_pipeline = pipeline(
    model=model_name,
    aggregation_strategy="simple"
)

# Example usage
text = "Escherichia coli bacteria were found in the water samples."
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
    "Escherichia coli bacteria were found in the water samples.",
    "The study included specimens from Homo sapiens and Mus musculus.",
    "Saccharomyces cerevisiae is commonly used in biotechnology applications.",
    "The venom of the black mamba, Dendroaspis polylepis, is highly neurotoxic.",
    "Canis lupus familiaris has been domesticated for thousands of years.",
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

- **Dataset**: LINNAEUS
- **Description**: Species Entity Recognition - Species and organism names

### Training Details
- **Base Model**: distilbert-base-multilingual-cased
- **Training Framework**: Hugging Face Transformers
- **Optimization**: AdamW optimizer with learning rate scheduling
- **Validation**: Cross-validation on held-out test set

## 🔬 Model Architecture

- **Base Architecture**: distilbert-base-multilingual-cased
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