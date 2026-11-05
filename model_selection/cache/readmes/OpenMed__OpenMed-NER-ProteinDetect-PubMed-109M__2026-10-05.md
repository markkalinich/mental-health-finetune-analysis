---
widget:
- text: "The Maillard reaction is responsible for the browning of many foods."
- text: "Casein micelles are the primary protein component of milk."
- text: "Starch gelatinization is a key process in cooking pasta and rice."
- text: "Polyphenols in green tea have antioxidant properties."
- text: "Omega-3 fatty acids are essential fats found in fish oil."
tags:
- token-classification
- named-entity-recognition
- biomedical-nlp
- transformers
- protein-interactions
- molecular-biology
- biochemistry
- systems-biology
- protein
- protein_complex
- protein_enum
- protein_familiy_or_group
- protein_variant
language:
- en
license: apache-2.0
---

# 🧬 [OpenMed-NER-ProteinDetect-PubMed-109M](https://huggingface.co/OpenMed/OpenMed-NER-ProteinDetect-PubMed-109M)

**Specialized model for Biomedical Entity Recognition - Various biomedical entities**

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)]()
[![Transformers](https://img.shields.io/badge/🤗-Transformers-yellow)]()
[![OpenMed](https://img.shields.io/badge/🏥-OpenMed-green)](https://huggingface.co/OpenMed)

## 📋 Model Overview

This model is a **state-of-the-art** fine-tuned transformer engineered to deliver **enterprise-grade accuracy** for biomedical entity recognition - various biomedical entities. This specialized model excels at identifying and extracting biomedical entities from clinical texts, research papers, and healthcare documents, enabling applications such as **drug interaction detection**, **medication extraction from patient records**, **adverse event monitoring**, **literature mining for drug discovery**, and **biomedical knowledge graph construction** with **production-ready reliability** for clinical and research applications.

### 🎯 Key Features
- **High Precision**: Optimized for biomedical entity recognition
- **Domain-Specific**: Trained on curated FSU dataset
- **Production-Ready**: Validated on clinical benchmarks
- **Easy Integration**: Compatible with Hugging Face Transformers ecosystem

### 🏷️ Supported Entity Types

This model can identify and classify the following biomedical entities:

- `B-protein`
- `B-protein_complex`
- `B-protein_enum`
- `B-protein_familiy_or_group`
- `B-protein_variant`

<details>
<summary>See 5 more entity types...</summary>

- `I-protein`
- `I-protein_complex`
- `I-protein_enum`
- `I-protein_familiy_or_group`
- `I-protein_variant`
</details>

## 📊 Dataset

FSU corpus focuses on protein interactions and molecular biology entities for systems biology research.

The FSU (Florida State University) corpus is a biomedical NER dataset designed for protein interaction recognition and molecular biology entity extraction. This corpus contains annotations for proteins, protein complexes, protein families, protein variants, and molecular interaction entities relevant to systems biology and biochemistry research. The dataset supports the development of text mining systems for protein-protein interaction extraction, molecular pathway analysis, and systems biology applications. It is particularly valuable for identifying protein entities involved in cellular processes, signal transduction pathways, and molecular mechanisms. The corpus serves as a benchmark for evaluating NER systems used in proteomics research, drug discovery, and molecular biology informatics.


## 📊 Performance Metrics

### Current Model Performance
- **F1 Score**: `0.93`
- **Precision**: `0.92`
- **Recall**: `0.94`
- **Accuracy**: `0.98`

### 🏆 Comparative Performance on FSU Dataset

| Rank | Model | F1 Score | Precision | Recall | Accuracy |
|------|-------|----------|-----------|--------|-----------|
| 🥇 1 | [OpenMed-NER-ProteinDetect-SnowMed-568M](https://huggingface.co/OpenMed/OpenMed-NER-ProteinDetect-SnowMed-568M) | **0.9609** | 0.9576 | 0.9642 | 0.9803 |
| 🥈 2 | [OpenMed-NER-ProteinDetect-ElectraMed-560M](https://huggingface.co/OpenMed/OpenMed-NER-ProteinDetect-ElectraMed-560M) | **0.9609** | 0.9581 | 0.9636 | 0.9802 |
| 🥉 3 | [OpenMed-NER-ProteinDetect-MultiMed-568M](https://huggingface.co/OpenMed/OpenMed-NER-ProteinDetect-MultiMed-568M) | **0.9579** | 0.9564 | 0.9595 | 0.9788 |
|  4 | [OpenMed-NER-ProteinDetect-BigMed-560M](https://huggingface.co/OpenMed/OpenMed-NER-ProteinDetect-BigMed-560M) | **0.9549** | 0.9520 | 0.9578 | 0.9778 |
|  5 | [OpenMed-NER-ProteinDetect-SuperMedical-355M](https://huggingface.co/OpenMed/OpenMed-NER-ProteinDetect-SuperMedical-355M) | **0.9547** | 0.9517 | 0.9576 | 0.9749 |
|  6 | [OpenMed-NER-ProteinDetect-EuroMed-212M](https://huggingface.co/OpenMed/OpenMed-NER-ProteinDetect-EuroMed-212M) | **0.9482** | 0.9482 | 0.9482 | 0.9770 |
|  7 | [OpenMed-NER-ProteinDetect-BigMed-278M](https://huggingface.co/OpenMed/OpenMed-NER-ProteinDetect-BigMed-278M) | **0.9466** | 0.9434 | 0.9499 | 0.9738 |
|  8 | [OpenMed-NER-ProteinDetect-SuperMedical-125M](https://huggingface.co/OpenMed/OpenMed-NER-ProteinDetect-SuperMedical-125M) | **0.9465** | 0.9423 | 0.9507 | 0.9714 |
|  9 | [OpenMed-NER-ProteinDetect-SuperClinical-434M](https://huggingface.co/OpenMed/OpenMed-NER-ProteinDetect-SuperClinical-434M) | **0.9412** | 0.9351 | 0.9474 | 0.9802 |
|  10 | [OpenMed-NER-ProteinDetect-TinyMed-82M](https://huggingface.co/OpenMed/OpenMed-NER-ProteinDetect-TinyMed-82M) | **0.9398** | 0.9331 | 0.9467 | 0.9680 |


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
# Model: https://huggingface.co/OpenMed/OpenMed-NER-ProteinDetect-PubMed-109M
model_name = "OpenMed/OpenMed-NER-ProteinDetect-PubMed-109M"

# Create a pipeline
medical_ner_pipeline = pipeline(
    model=model_name,
    aggregation_strategy="simple"
)

# Example usage
text = "The Maillard reaction is responsible for the browning of many foods."
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
    "The Maillard reaction is responsible for the browning of many foods.",
    "Casein micelles are the primary protein component of milk.",
    "Starch gelatinization is a key process in cooking pasta and rice.",
    "Polyphenols in green tea have antioxidant properties.",
    "Omega-3 fatty acids are essential fats found in fish oil.",
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

- **Dataset**: FSU
- **Description**: Biomedical Entity Recognition - Various biomedical entities

### Training Details
- **Base Model**: BiomedNLP-BiomedBERT-base-uncased-abstract-fulltext
- **Training Framework**: Hugging Face Transformers
- **Optimization**: AdamW optimizer with learning rate scheduling
- **Validation**: Cross-validation on held-out test set

## 🔬 Model Architecture

- **Base Architecture**: BiomedNLP-BiomedBERT-base-uncased-abstract-fulltext
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