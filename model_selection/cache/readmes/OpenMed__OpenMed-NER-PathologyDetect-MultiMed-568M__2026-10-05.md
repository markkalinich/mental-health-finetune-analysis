---
widget:
- text: "Early detection of breast cancer improves survival rates."
- text: "The patient exhibited symptoms consistent with Parkinson's disease."
- text: "Genetic testing revealed predisposition to Huntington's disease."
- text: "Malaria is a life-threatening disease caused by parasites transmitted through mosquito bites."
- text: "Multiple sclerosis affects the central nervous system, leading to a range of symptoms."
tags:
- token-classification
- named-entity-recognition
- biomedical-nlp
- transformers
- disease-entity-recognition
- medical-diagnosis
- ncbi
- pathology
- disease
language:
- en
license: apache-2.0
---

# 🧬 [OpenMed-NER-PathologyDetect-MultiMed-568M](https://huggingface.co/OpenMed/OpenMed-NER-PathologyDetect-MultiMed-568M)

**Specialized model for Disease Entity Recognition - Disease entities from the NCBI dataset**

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)]()
[![Transformers](https://img.shields.io/badge/🤗-Transformers-yellow)]()
[![OpenMed](https://img.shields.io/badge/🏥-OpenMed-green)](https://huggingface.co/OpenMed)

## 📋 Model Overview

This model is a **state-of-the-art** fine-tuned transformer engineered to deliver **enterprise-grade accuracy** for disease entity recognition - disease entities from the ncbi dataset. This specialized model excels at identifying and extracting biomedical entities from clinical texts, research papers, and healthcare documents, enabling applications such as **drug interaction detection**, **medication extraction from patient records**, **adverse event monitoring**, **literature mining for drug discovery**, and **biomedical knowledge graph construction** with **production-ready reliability** for clinical and research applications.

### 🎯 Key Features
- **High Precision**: Optimized for biomedical entity recognition
- **Domain-Specific**: Trained on curated NCBI_DISEASE dataset
- **Production-Ready**: Validated on clinical benchmarks
- **Easy Integration**: Compatible with Hugging Face Transformers ecosystem

### 🏷️ Supported Entity Types

This model can identify and classify the following biomedical entities:

- `B-Disease`
- `I-Disease`

## 📊 Dataset

NCBI Disease corpus is a comprehensive resource for disease name recognition and concept normalization.

The NCBI Disease corpus is a gold-standard dataset containing 793 PubMed abstracts with 6,892 disease mentions mapped to 790 unique disease concepts from Medical Subject Headings (MeSH) and Online Mendelian Inheritance in Man (OMIM). Developed by the National Center for Biotechnology Information, this corpus provides both mention-level and concept-level annotations for disease entity recognition and normalization. The dataset is extensively used for developing clinical NLP systems, medical diagnosis support tools, and biomedical text mining applications. It serves as a critical benchmark for evaluating disease name recognition systems in healthcare informatics and medical literature analysis.


## 📊 Performance Metrics

### Current Model Performance
- **F1 Score**: `0.88`
- **Precision**: `0.87`
- **Recall**: `0.89`
- **Accuracy**: `0.97`

### 🏆 Comparative Performance on NCBI_DISEASE Dataset

| Rank | Model | F1 Score | Precision | Recall | Accuracy |
|------|-------|----------|-----------|--------|-----------|
| 🥇 1 | [OpenMed-NER-PathologyDetect-PubMed-109M](https://huggingface.co/OpenMed/OpenMed-NER-PathologyDetect-PubMed-109M) | **0.9110** | 0.8918 | 0.9310 | 0.9792 |
| 🥈 2 | [OpenMed-NER-PathologyDetect-PubMed-335M](https://huggingface.co/OpenMed/OpenMed-NER-PathologyDetect-PubMed-335M) | **0.9086** | 0.8913 | 0.9266 | 0.9781 |
| 🥉 3 | [OpenMed-NER-PathologyDetect-BioMed-335M](https://huggingface.co/OpenMed/OpenMed-NER-PathologyDetect-BioMed-335M) | **0.9052** | 0.8867 | 0.9244 | 0.9780 |
|  4 | [OpenMed-NER-PathologyDetect-SuperClinical-434M](https://huggingface.co/OpenMed/OpenMed-NER-PathologyDetect-SuperClinical-434M) | **0.9035** | 0.8772 | 0.9314 | 0.9760 |
|  5 | [OpenMed-NER-PathologyDetect-PubMed-109M](https://huggingface.co/OpenMed/OpenMed-NER-PathologyDetect-PubMed-109M) | **0.9022** | 0.8825 | 0.9227 | 0.9769 |
|  6 | [OpenMed-NER-PathologyDetect-ElectraMed-335M](https://huggingface.co/OpenMed/OpenMed-NER-PathologyDetect-ElectraMed-335M) | **0.8977** | 0.8884 | 0.9073 | 0.9719 |
|  7 | [OpenMed-NER-PathologyDetect-ElectraMed-560M](https://huggingface.co/OpenMed/OpenMed-NER-PathologyDetect-ElectraMed-560M) | **0.8950** | 0.8749 | 0.9161 | 0.9747 |
|  8 | [OpenMed-NER-PathologyDetect-MultiMed-335M](https://huggingface.co/OpenMed/OpenMed-NER-PathologyDetect-MultiMed-335M) | **0.8903** | 0.8749 | 0.9063 | 0.9692 |
|  9 | [OpenMed-NER-PathologyDetect-SnowMed-568M](https://huggingface.co/OpenMed/OpenMed-NER-PathologyDetect-SnowMed-568M) | **0.8903** | 0.8684 | 0.9133 | 0.9731 |
|  10 | [OpenMed-NER-PathologyDetect-SuperClinical-141M](https://huggingface.co/OpenMed/OpenMed-NER-PathologyDetect-SuperClinical-141M) | **0.8894** | 0.8633 | 0.9172 | 0.9744 |


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
# Model: https://huggingface.co/OpenMed/OpenMed-NER-PathologyDetect-MultiMed-568M
model_name = "OpenMed/OpenMed-NER-PathologyDetect-MultiMed-568M"

# Create a pipeline
medical_ner_pipeline = pipeline(
    model=model_name,
    aggregation_strategy="simple"
)

# Example usage
text = "Early detection of breast cancer improves survival rates."
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
    "Early detection of breast cancer improves survival rates.",
    "The patient exhibited symptoms consistent with Parkinson's disease.",
    "Genetic testing revealed predisposition to Huntington's disease.",
    "Malaria is a life-threatening disease caused by parasites transmitted through mosquito bites.",
    "Multiple sclerosis affects the central nervous system, leading to a range of symptoms.",
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

- **Dataset**: NCBI_DISEASE
- **Description**: Disease Entity Recognition - Disease entities from the NCBI dataset

### Training Details
- **Base Model**: bge-m3
- **Training Framework**: Hugging Face Transformers
- **Optimization**: AdamW optimizer with learning rate scheduling
- **Validation**: Cross-validation on held-out test set

## 🔬 Model Architecture

- **Base Architecture**: bge-m3
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