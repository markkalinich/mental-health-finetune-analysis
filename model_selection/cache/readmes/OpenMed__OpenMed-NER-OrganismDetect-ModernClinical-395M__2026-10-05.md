---
widget:
- text: "Caenorhabditis elegans is a model organism for genetic studies."
- text: "The research focused on Drosophila melanogaster development."
- text: "Arabidopsis thaliana serves as a model for plant biology."
- text: "The zebrafish, Danio rerio, is widely used for studying vertebrate development."
- text: "Neurospora crassa is a type of red bread mold used in genetic research."
tags:
- token-classification
- named-entity-recognition
- biomedical-nlp
- transformers
- species-recognition
- taxonomy
- organism-identification
- biodiversity
- species
language:
- en
license: apache-2.0
---

# 🧬 [OpenMed-NER-OrganismDetect-ModernClinical-395M](https://huggingface.co/OpenMed/OpenMed-NER-OrganismDetect-ModernClinical-395M)

**Specialized model for Species Entity Recognition - Species names from the Species-800 dataset**

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)]()
[![Transformers](https://img.shields.io/badge/🤗-Transformers-yellow)]()
[![OpenMed](https://img.shields.io/badge/🏥-OpenMed-green)](https://huggingface.co/OpenMed)

## 📋 Model Overview

This model is a **state-of-the-art** fine-tuned transformer engineered to deliver **enterprise-grade accuracy** for species entity recognition - species names from the species-800 dataset. This specialized model excels at identifying and extracting biomedical entities from clinical texts, research papers, and healthcare documents, enabling applications such as **drug interaction detection**, **medication extraction from patient records**, **adverse event monitoring**, **literature mining for drug discovery**, and **biomedical knowledge graph construction** with **production-ready reliability** for clinical and research applications.

### 🎯 Key Features
- **High Precision**: Optimized for biomedical entity recognition
- **Domain-Specific**: Trained on curated SPECIES800 dataset
- **Production-Ready**: Validated on clinical benchmarks
- **Easy Integration**: Compatible with Hugging Face Transformers ecosystem

### 🏷️ Supported Entity Types

This model can identify and classify the following biomedical entities:

- `B-SPECIES`
- `I-SPECIES`

## 📊 Dataset

Species800 is a corpus for species recognition and taxonomy classification in biomedical texts.

The Species800 corpus is a manually annotated dataset designed for species recognition and taxonomic classification in biomedical literature. This corpus contains 800 abstracts with comprehensive annotations for organism mentions, supporting biodiversity informatics and biological taxonomy research. The dataset includes both scientific names and common names of species, making it valuable for developing NER systems that can handle the complexity of biological nomenclature. It serves as a benchmark for evaluating species identification models used in ecological studies, conservation biology, and systematic biology research. The corpus is particularly useful for text mining applications in biodiversity databases and biological literature analysis.


## 📊 Performance Metrics

### Current Model Performance
- **F1 Score**: `0.79`
- **Precision**: `0.79`
- **Recall**: `0.78`
- **Accuracy**: `0.96`

### 🏆 Comparative Performance on SPECIES800 Dataset

| Rank | Model | F1 Score | Precision | Recall | Accuracy |
|------|-------|----------|-----------|--------|-----------|
| 🥇 1 | [OpenMed-NER-OrganismDetect-BioMed-335M](https://huggingface.co/OpenMed/OpenMed-NER-OrganismDetect-BioMed-335M) | **0.8639** | 0.8557 | 0.8722 | 0.9715 |
| 🥈 2 | [OpenMed-NER-OrganismDetect-PubMed-335M](https://huggingface.co/OpenMed/OpenMed-NER-OrganismDetect-PubMed-335M) | **0.8550** | 0.8370 | 0.8737 | 0.9698 |
| 🥉 3 | [OpenMed-NER-OrganismDetect-PubMed-109M](https://huggingface.co/OpenMed/OpenMed-NER-OrganismDetect-PubMed-109M) | **0.8458** | 0.8287 | 0.8637 | 0.9690 |
|  4 | [OpenMed-NER-OrganismDetect-MultiMed-335M](https://huggingface.co/OpenMed/OpenMed-NER-OrganismDetect-MultiMed-335M) | **0.8441** | 0.8352 | 0.8532 | 0.9670 |
|  5 | [OpenMed-NER-OrganismDetect-SuperClinical-434M](https://huggingface.co/OpenMed/OpenMed-NER-OrganismDetect-SuperClinical-434M) | **0.8435** | 0.8291 | 0.8585 | 0.9670 |
|  6 | [OpenMed-NER-OrganismDetect-PubMed-109M](https://huggingface.co/OpenMed/OpenMed-NER-OrganismDetect-PubMed-109M) | **0.8349** | 0.8082 | 0.8634 | 0.9685 |
|  7 | [OpenMed-NER-OrganismDetect-MultiMed-568M](https://huggingface.co/OpenMed/OpenMed-NER-OrganismDetect-MultiMed-568M) | **0.8313** | 0.8053 | 0.8592 | 0.9703 |
|  8 | [OpenMed-NER-OrganismDetect-ElectraMed-335M](https://huggingface.co/OpenMed/OpenMed-NER-OrganismDetect-ElectraMed-335M) | **0.8288** | 0.8176 | 0.8404 | 0.9631 |
|  9 | [OpenMed-NER-OrganismDetect-BioPatient-108M](https://huggingface.co/OpenMed/OpenMed-NER-OrganismDetect-BioPatient-108M) | **0.8154** | 0.8140 | 0.8169 | 0.9591 |
|  10 | [OpenMed-NER-OrganismDetect-ElectraMed-33M](https://huggingface.co/OpenMed/OpenMed-NER-OrganismDetect-ElectraMed-33M) | **0.8121** | 0.7772 | 0.8503 | 0.9600 |


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
# Model: https://huggingface.co/OpenMed/OpenMed-NER-OrganismDetect-ModernClinical-395M
model_name = "OpenMed/OpenMed-NER-OrganismDetect-ModernClinical-395M"

# Create a pipeline
medical_ner_pipeline = pipeline(
    model=model_name,
    aggregation_strategy="simple"
)

# Example usage
text = "Caenorhabditis elegans is a model organism for genetic studies."
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
    "Caenorhabditis elegans is a model organism for genetic studies.",
    "The research focused on Drosophila melanogaster development.",
    "Arabidopsis thaliana serves as a model for plant biology.",
    "The zebrafish, Danio rerio, is widely used for studying vertebrate development.",
    "Neurospora crassa is a type of red bread mold used in genetic research.",
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

- **Dataset**: SPECIES800
- **Description**: Species Entity Recognition - Species names from the Species-800 dataset

### Training Details
- **Base Model**: BioClinical-ModernBERT-large
- **Training Framework**: Hugging Face Transformers
- **Optimization**: AdamW optimizer with learning rate scheduling
- **Validation**: Cross-validation on held-out test set

## 🔬 Model Architecture

- **Base Architecture**: BioClinical-ModernBERT-large
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