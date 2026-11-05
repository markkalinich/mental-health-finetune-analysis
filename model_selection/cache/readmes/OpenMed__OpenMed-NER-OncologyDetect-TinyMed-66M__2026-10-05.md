---
widget:
- text: "Mutations in KRAS gene drive oncogenic transformation."
- text: "The tumor suppressor p53 pathway was disrupted."
- text: "EGFR amplification promotes cancer cell proliferation."
- text: "Loss of function of the PTEN gene is common in many cancers."
- text: "The PI3K/AKT/mTOR pathway is a critical regulator of cell growth."
tags:
- token-classification
- named-entity-recognition
- biomedical-nlp
- transformers
- cancer-genetics
- oncology
- gene-regulation
- cancer-research
- amino_acid
- anatomical_system
- cancer
- cell
- cellular_component
- developing_anatomical_structure
- gene_or_gene_product
- immaterial_anatomical_entity
- multi-tissue_structure
- organ
- organism
- organism_subdivision
- organism_substance
- pathological_formation
- simple_chemical
- tissue
language:
- en
license: apache-2.0
---

# 🧬 [OpenMed-NER-OncologyDetect-TinyMed-66M](https://huggingface.co/OpenMed/OpenMed-NER-OncologyDetect-TinyMed-66M)

**Specialized model for Cancer Genetics - Cancer-related genetic entities**

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)]()
[![Transformers](https://img.shields.io/badge/🤗-Transformers-yellow)]()
[![OpenMed](https://img.shields.io/badge/🏥-OpenMed-green)](https://huggingface.co/OpenMed)

## 📋 Model Overview

This model is a **state-of-the-art** fine-tuned transformer engineered to deliver **enterprise-grade accuracy** for cancer genetics - cancer-related genetic entities. This specialized model excels at identifying and extracting biomedical entities from clinical texts, research papers, and healthcare documents, enabling applications such as **drug interaction detection**, **medication extraction from patient records**, **adverse event monitoring**, **literature mining for drug discovery**, and **biomedical knowledge graph construction** with **production-ready reliability** for clinical and research applications.

### 🎯 Key Features
- **High Precision**: Optimized for biomedical entity recognition
- **Domain-Specific**: Trained on curated BIONLP2013_CG dataset
- **Production-Ready**: Validated on clinical benchmarks
- **Easy Integration**: Compatible with Hugging Face Transformers ecosystem

### 🏷️ Supported Entity Types

This model can identify and classify the following biomedical entities:

- `B-Amino_acid`
- `B-Anatomical_system`
- `B-Cancer`
- `B-Cell`
- `B-Cellular_component`

<details>
<summary>See 27 more entity types...</summary>

- `B-Developing_anatomical_structure`
- `B-Gene_or_gene_product`
- `B-Immaterial_anatomical_entity`
- `B-Multi-tissue_structure`
- `B-Organ`
- `B-Organism`
- `B-Organism_subdivision`
- `B-Organism_substance`
- `B-Pathological_formation`
- `B-Simple_chemical`
- `B-Tissue`
- `I-Amino_acid`
- `I-Anatomical_system`
- `I-Cancer`
- `I-Cell`
- `I-Cellular_component`
- `I-Developing_anatomical_structure`
- `I-Gene_or_gene_product`
- `I-Immaterial_anatomical_entity`
- `I-Multi-tissue_structure`
- `I-Organ`
- `I-Organism`
- `I-Organism_subdivision`
- `I-Organism_substance`
- `I-Pathological_formation`
- `I-Simple_chemical`
- `I-Tissue`
</details>

## 📊 Dataset

BioNLP 2013 CG corpus targets cancer genetics entities for oncology research and cancer genomics.

The BioNLP 2013 CG (Cancer Genetics) corpus is a specialized dataset focusing on cancer genetics entities and gene regulation in oncology research. This corpus contains annotations for genes, proteins, and molecular processes specifically related to cancer biology and tumor genetics. Developed for the BioNLP Shared Task 2013, it supports the development of text mining systems for cancer research, oncological studies, and precision medicine applications. The dataset is particularly valuable for identifying cancer-related biomarkers, tumor suppressor genes, oncogenes, and therapeutic targets mentioned in cancer research literature. It serves as a benchmark for evaluating NER systems used in cancer genomics, personalized medicine, and oncology informatics.


## 📊 Performance Metrics

### Current Model Performance
- **F1 Score**: `0.77`
- **Precision**: `0.76`
- **Recall**: `0.77`
- **Accuracy**: `0.91`

### 🏆 Comparative Performance on BIONLP2013_CG Dataset

| Rank | Model | F1 Score | Precision | Recall | Accuracy |
|------|-------|----------|-----------|--------|-----------|
| 🥇 1 | [OpenMed-NER-OncologyDetect-SuperMedical-355M](https://huggingface.co/OpenMed/OpenMed-NER-OncologyDetect-SuperMedical-355M) | **0.8990** | 0.8926 | 0.9056 | 0.9416 |
| 🥈 2 | [OpenMed-NER-OncologyDetect-ElectraMed-560M](https://huggingface.co/OpenMed/OpenMed-NER-OncologyDetect-ElectraMed-560M) | **0.8841** | 0.8788 | 0.8895 | 0.9390 |
| 🥉 3 | [OpenMed-NER-OncologyDetect-SnowMed-568M](https://huggingface.co/OpenMed/OpenMed-NER-OncologyDetect-SnowMed-568M) | **0.8801** | 0.8774 | 0.8828 | 0.9366 |
|  4 | [OpenMed-NER-OncologyDetect-PubMed-335M](https://huggingface.co/OpenMed/OpenMed-NER-OncologyDetect-PubMed-335M) | **0.8782** | 0.8834 | 0.8730 | 0.9539 |
|  5 | [OpenMed-NER-OncologyDetect-MultiMed-568M](https://huggingface.co/OpenMed/OpenMed-NER-OncologyDetect-MultiMed-568M) | **0.8766** | 0.8749 | 0.8784 | 0.9351 |
|  6 | [OpenMed-NER-OncologyDetect-SuperClinical-434M](https://huggingface.co/OpenMed/OpenMed-NER-OncologyDetect-SuperClinical-434M) | **0.8684** | 0.8602 | 0.8768 | 0.9495 |
|  7 | [OpenMed-NER-OncologyDetect-BioMed-335M](https://huggingface.co/OpenMed/OpenMed-NER-OncologyDetect-BioMed-335M) | **0.8660** | 0.8540 | 0.8783 | 0.9516 |
|  8 | [OpenMed-NER-OncologyDetect-PubMed-109M](https://huggingface.co/OpenMed/OpenMed-NER-OncologyDetect-PubMed-109M) | **0.8606** | 0.8604 | 0.8608 | 0.9503 |
|  9 | [OpenMed-NER-OncologyDetect-BigMed-560M](https://huggingface.co/OpenMed/OpenMed-NER-OncologyDetect-BigMed-560M) | **0.8556** | 0.8582 | 0.8530 | 0.9250 |
|  10 | [OpenMed-NER-OncologyDetect-ModernClinical-395M](https://huggingface.co/OpenMed/OpenMed-NER-OncologyDetect-ModernClinical-395M) | **0.8471** | 0.8465 | 0.8476 | 0.9411 |


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
# Model: https://huggingface.co/OpenMed/OpenMed-NER-OncologyDetect-TinyMed-66M
model_name = "OpenMed/OpenMed-NER-OncologyDetect-TinyMed-66M"

# Create a pipeline
medical_ner_pipeline = pipeline(
    model=model_name,
    aggregation_strategy="simple"
)

# Example usage
text = "Mutations in KRAS gene drive oncogenic transformation."
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
    "Mutations in KRAS gene drive oncogenic transformation.",
    "The tumor suppressor p53 pathway was disrupted.",
    "EGFR amplification promotes cancer cell proliferation.",
    "Loss of function of the PTEN gene is common in many cancers.",
    "The PI3K/AKT/mTOR pathway is a critical regulator of cell growth.",
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

- **Dataset**: BIONLP2013_CG
- **Description**: Cancer Genetics - Cancer-related genetic entities

### Training Details
- **Base Model**: distilbert-base-uncased
- **Training Framework**: Hugging Face Transformers
- **Optimization**: AdamW optimizer with learning rate scheduling
- **Validation**: Cross-validation on held-out test set

## 🔬 Model Architecture

- **Base Architecture**: distilbert-base-uncased
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