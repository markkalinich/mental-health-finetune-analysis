---
widget:
- text: "The p53 protein plays a crucial role in tumor suppression."
- text: "Expression of BRCA1 gene was significantly upregulated in breast tissue."
- text: "The NF-kB pathway regulates inflammatory responses."
- text: "Activation of the STAT3 signaling pathway is observed in many cancers."
- text: "The experiment involved transfecting HeLa cells with a plasmid containing the target gene."
tags:
- token-classification
- named-entity-recognition
- biomedical-nlp
- transformers
- protein-recognition
- gene-recognition
- molecular-biology
- genomics
- dna
- rna
- cell_line
- cell_type
- protein
language:
- en
license: apache-2.0
---

# 🧬 [OpenMed-NER-DNADetect-BigMed-278M](https://huggingface.co/OpenMed/OpenMed-NER-DNADetect-BigMed-278M)

**Specialized model for Biomedical Entity Recognition - Proteins, DNA, RNA, cell lines, and cell types**

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)]()
[![Transformers](https://img.shields.io/badge/🤗-Transformers-yellow)]()
[![OpenMed](https://img.shields.io/badge/🏥-OpenMed-green)](https://huggingface.co/OpenMed)

## 📋 Model Overview

This model is a **state-of-the-art** fine-tuned transformer engineered to deliver **enterprise-grade accuracy** for biomedical entity recognition - proteins, dna, rna, cell lines, and cell types. This specialized model excels at identifying and extracting biomedical entities from clinical texts, research papers, and healthcare documents, enabling applications such as **drug interaction detection**, **medication extraction from patient records**, **adverse event monitoring**, **literature mining for drug discovery**, and **biomedical knowledge graph construction** with **production-ready reliability** for clinical and research applications.

### 🎯 Key Features
- **High Precision**: Optimized for biomedical entity recognition
- **Domain-Specific**: Trained on curated JNLPBA dataset
- **Production-Ready**: Validated on clinical benchmarks
- **Easy Integration**: Compatible with Hugging Face Transformers ecosystem

### 🏷️ Supported Entity Types

This model can identify and classify the following biomedical entities:

- `B-DNA`
- `B-RNA`
- `B-cell_line`
- `B-cell_type`
- `B-protein`

<details>
<summary>See 5 more entity types...</summary>

- `I-DNA`
- `I-RNA`
- `I-cell_line`
- `I-cell_type`
- `I-protein`
</details>

## 📊 Dataset

JNLPBA corpus focuses on biomedical named entity recognition for protein, DNA, RNA, cell line, and cell type entities.

The JNLPBA (Joint Workshop on Natural Language Processing in Biomedicine and its Applications) corpus is a widely-used biomedical NER dataset derived from the GENIA corpus for the 2004 bio-entity recognition task. It contains annotations for five entity types: protein, DNA, RNA, cell line, and cell type, making it essential for molecular biology and genomics research applications. The corpus consists of MEDLINE abstracts annotated with biomedical entities relevant to gene and protein recognition tasks. It has been extensively used as a benchmark for evaluating biomedical NER systems and continues to be a standard evaluation dataset for developing machine learning models in computational biology and bioinformatics.


## 📊 Performance Metrics

### Current Model Performance
- **F1 Score**: `0.80`
- **Precision**: `0.75`
- **Recall**: `0.85`
- **Accuracy**: `0.93`

### 🏆 Comparative Performance on JNLPBA Dataset

| Rank | Model | F1 Score | Precision | Recall | Accuracy |
|------|-------|----------|-----------|--------|-----------|
| 🥇 1 | [OpenMed-NER-DNADetect-SuperClinical-434M](https://huggingface.co/OpenMed/OpenMed-NER-DNADetect-SuperClinical-434M) | **0.8188** | 0.7778 | 0.8643 | 0.9320 |
| 🥈 2 | [OpenMed-NER-DNADetect-SuperMedical-355M](https://huggingface.co/OpenMed/OpenMed-NER-DNADetect-SuperMedical-355M) | **0.8177** | 0.7716 | 0.8697 | 0.9318 |
| 🥉 3 | [OpenMed-NER-DNADetect-MultiMed-568M](https://huggingface.co/OpenMed/OpenMed-NER-DNADetect-MultiMed-568M) | **0.8157** | 0.7758 | 0.8599 | 0.9354 |
|  4 | [OpenMed-NER-DNADetect-BigMed-560M](https://huggingface.co/OpenMed/OpenMed-NER-DNADetect-BigMed-560M) | **0.8134** | 0.7723 | 0.8591 | 0.9346 |
|  5 | [OpenMed-NER-DNADetect-BioClinical-108M](https://huggingface.co/OpenMed/OpenMed-NER-DNADetect-BioClinical-108M) | **0.8071** | 0.7632 | 0.8562 | 0.9147 |
|  6 | [OpenMed-NER-DNADetect-MultiMed-335M](https://huggingface.co/OpenMed/OpenMed-NER-DNADetect-MultiMed-335M) | **0.8069** | 0.7642 | 0.8547 | 0.9185 |
|  7 | [OpenMed-NER-DNADetect-PubMed-335M](https://huggingface.co/OpenMed/OpenMed-NER-DNADetect-PubMed-335M) | **0.8056** | 0.7611 | 0.8556 | 0.9344 |
|  8 | [OpenMed-NER-DNADetect-SuperClinical-184M](https://huggingface.co/OpenMed/OpenMed-NER-DNADetect-SuperClinical-184M) | **0.8053** | 0.7548 | 0.8630 | 0.9259 |
|  9 | [OpenMed-NER-DNADetect-BioPatient-108M](https://huggingface.co/OpenMed/OpenMed-NER-DNADetect-BioPatient-108M) | **0.8052** | 0.7605 | 0.8555 | 0.9137 |
|  10 | [OpenMed-NER-DNADetect-SuperMedical-125M](https://huggingface.co/OpenMed/OpenMed-NER-DNADetect-SuperMedical-125M) | **0.8044** | 0.7589 | 0.8557 | 0.9284 |


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
# Model: https://huggingface.co/OpenMed/OpenMed-NER-DNADetect-BigMed-278M
model_name = "OpenMed/OpenMed-NER-DNADetect-BigMed-278M"

# Create a pipeline
medical_ner_pipeline = pipeline(
    model=model_name,
    aggregation_strategy="simple"
)

# Example usage
text = "The p53 protein plays a crucial role in tumor suppression."
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
    "The p53 protein plays a crucial role in tumor suppression.",
    "Expression of BRCA1 gene was significantly upregulated in breast tissue.",
    "The NF-kB pathway regulates inflammatory responses.",
    "Activation of the STAT3 signaling pathway is observed in many cancers.",
    "The experiment involved transfecting HeLa cells with a plasmid containing the target gene.",
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

- **Dataset**: JNLPBA
- **Description**: Biomedical Entity Recognition - Proteins, DNA, RNA, cell lines, and cell types

### Training Details
- **Base Model**: xlm-roberta-base
- **Training Framework**: Hugging Face Transformers
- **Optimization**: AdamW optimizer with learning rate scheduling
- **Validation**: Cross-validation on held-out test set

## 🔬 Model Architecture

- **Base Architecture**: xlm-roberta-base
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