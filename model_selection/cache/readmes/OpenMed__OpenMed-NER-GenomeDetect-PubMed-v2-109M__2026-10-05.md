---
widget:
- text: "The EGFR gene mutation was identified in lung cancer patients."
- text: "Overexpression of HER2 protein correlates with poor prognosis."
- text: "The TP53 gene encodes a tumor suppressor protein."
- text: "The BRAF V600E mutation is a common driver in melanoma."
- text: "Insulin receptor signaling is essential for glucose homeostasis."
tags:
- token-classification
- named-entity-recognition
- biomedical-nlp
- transformers
- gene-recognition
- protein-recognition
- genomics
- molecular-biology
- gene/protein
language:
- en
license: apache-2.0
---

# 🧬 [OpenMed-NER-GenomeDetect-PubMed-109M](https://huggingface.co/OpenMed/OpenMed-NER-GenomeDetect-PubMed-109M)

**Specialized model for Gene/Protein Entity Recognition - Gene and protein mentions**

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)]()
[![Transformers](https://img.shields.io/badge/🤗-Transformers-yellow)]()
[![OpenMed](https://img.shields.io/badge/🏥-OpenMed-green)](https://huggingface.co/OpenMed)

## 📋 Model Overview

This model is a **state-of-the-art** fine-tuned transformer engineered to deliver **enterprise-grade accuracy** for gene/protein entity recognition - gene and protein mentions. This specialized model excels at identifying and extracting biomedical entities from clinical texts, research papers, and healthcare documents, enabling applications such as **drug interaction detection**, **medication extraction from patient records**, **adverse event monitoring**, **literature mining for drug discovery**, and **biomedical knowledge graph construction** with **production-ready reliability** for clinical and research applications.

### 🎯 Key Features
- **High Precision**: Optimized for biomedical entity recognition
- **Domain-Specific**: Trained on curated BC2GM dataset
- **Production-Ready**: Validated on clinical benchmarks
- **Easy Integration**: Compatible with Hugging Face Transformers ecosystem

### 🏷️ Supported Entity Types

This model can identify and classify the following biomedical entities:

- `B-GENE/PROTEIN`
- `I-GENE/PROTEIN`

## 📊 Dataset

BC2GM corpus targets gene and protein mention recognition from the BioCreative II Gene Mention task.

The BC2GM (BioCreative II Gene Mention) corpus is a foundational dataset for gene and protein name recognition in biomedical literature, created for the BioCreative II challenge. This corpus contains thousands of sentences from MEDLINE abstracts with manually annotated gene and protein mentions, serving as a critical benchmark for genomics and molecular biology NER systems. The dataset addresses the challenging task of identifying gene names, which often have complex nomenclature and ambiguous boundaries. It has been instrumental in advancing automated gene recognition systems used in functional genomics research, gene expression analysis, and molecular biology text mining. The corpus continues to be widely used for training and evaluating biomedical NER models.


## 📊 Performance Metrics

### Current Model Performance
- **F1 Score**: `0.89`
- **Precision**: `0.89`
- **Recall**: `0.89`
- **Accuracy**: `0.97`

### 🏆 Comparative Performance on BC2GM Dataset

| Rank | Model | F1 Score | Precision | Recall | Accuracy |
|------|-------|----------|-----------|--------|-----------|
| 🥇 1 | [OpenMed-NER-GenomeDetect-SuperClinical-434M](https://huggingface.co/OpenMed/OpenMed-NER-GenomeDetect-SuperClinical-434M) | **0.9010** | 0.8954 | 0.9066 | 0.9683 |
| 🥈 2 | [OpenMed-NER-GenomeDetect-PubMed-335M](https://huggingface.co/OpenMed/OpenMed-NER-GenomeDetect-PubMed-335M) | **0.8963** | 0.8924 | 0.9002 | 0.9719 |
| 🥉 3 | [OpenMed-NER-GenomeDetect-BioMed-335M](https://huggingface.co/OpenMed/OpenMed-NER-GenomeDetect-BioMed-335M) | **0.8943** | 0.8887 | 0.8999 | 0.9704 |
|  4 | [OpenMed-NER-GenomeDetect-MultiMed-335M](https://huggingface.co/OpenMed/OpenMed-NER-GenomeDetect-MultiMed-335M) | **0.8905** | 0.8870 | 0.8940 | 0.9631 |
|  5 | [OpenMed-NER-GenomeDetect-PubMed-109M](https://huggingface.co/OpenMed/OpenMed-NER-GenomeDetect-PubMed-109M) | **0.8894** | 0.8850 | 0.8937 | 0.9706 |
|  6 | [OpenMed-NER-GenomeDetect-BioPatient-108M](https://huggingface.co/OpenMed/OpenMed-NER-GenomeDetect-BioPatient-108M) | **0.8865** | 0.8850 | 0.8881 | 0.9590 |
|  7 | [OpenMed-NER-GenomeDetect-SuperMedical-355M](https://huggingface.co/OpenMed/OpenMed-NER-GenomeDetect-SuperMedical-355M) | **0.8852** | 0.8802 | 0.8902 | 0.9668 |
|  8 | [OpenMed-NER-GenomeDetect-BioClinical-108M](https://huggingface.co/OpenMed/OpenMed-NER-GenomeDetect-BioClinical-108M) | **0.8851** | 0.8767 | 0.8937 | 0.9582 |
|  9 | [OpenMed-NER-GenomeDetect-MultiMed-568M](https://huggingface.co/OpenMed/OpenMed-NER-GenomeDetect-MultiMed-568M) | **0.8834** | 0.8770 | 0.8898 | 0.9671 |
|  10 | [OpenMed-NER-GenomeDetect-PubMed-109M](https://huggingface.co/OpenMed/OpenMed-NER-GenomeDetect-PubMed-109M) | **0.8833** | 0.8781 | 0.8886 | 0.9706 |


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
# Model: https://huggingface.co/OpenMed/OpenMed-NER-GenomeDetect-PubMed-109M
model_name = "OpenMed/OpenMed-NER-GenomeDetect-PubMed-109M"

# Create a pipeline
medical_ner_pipeline = pipeline(
    model=model_name,
    aggregation_strategy="simple"
)

# Example usage
text = "The EGFR gene mutation was identified in lung cancer patients."
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
    "The EGFR gene mutation was identified in lung cancer patients.",
    "Overexpression of HER2 protein correlates with poor prognosis.",
    "The TP53 gene encodes a tumor suppressor protein.",
    "The BRAF V600E mutation is a common driver in melanoma.",
    "Insulin receptor signaling is essential for glucose homeostasis.",
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

- **Dataset**: BC2GM
- **Description**: Gene/Protein Entity Recognition - Gene and protein mentions

### Training Details
- **Base Model**: BiomedNLP-BiomedBERT-base-uncased-abstract
- **Training Framework**: Hugging Face Transformers
- **Optimization**: AdamW optimizer with learning rate scheduling
- **Validation**: Cross-validation on held-out test set

## 🔬 Model Architecture

- **Base Architecture**: BiomedNLP-BiomedBERT-base-uncased-abstract
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