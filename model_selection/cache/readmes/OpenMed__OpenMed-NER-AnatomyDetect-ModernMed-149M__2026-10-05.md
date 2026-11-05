---
widget:
- text: "The patient complained of pain in the left ventricle region."
- text: "Examination revealed inflammation of the hippocampus."
- text: "The liver showed signs of fatty infiltration."
- text: "An MRI of the cerebrum showed no signs of abnormalities."
- text: "The procedure involved an incision near the femoral artery."
tags:
- token-classification
- named-entity-recognition
- biomedical-nlp
- transformers
- anatomical-entity-recognition
- medical-terminology
- anatomy
- healthcare
- anatomy
language:
- en
license: apache-2.0
---

# 🧬 [OpenMed-NER-AnatomyDetect-ModernMed-149M](https://huggingface.co/OpenMed/OpenMed-NER-AnatomyDetect-ModernMed-149M)

**Specialized model for Anatomical Entity Recognition - Anatomical structures and body parts**

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)]()
[![Transformers](https://img.shields.io/badge/🤗-Transformers-yellow)]()
[![OpenMed](https://img.shields.io/badge/🏥-OpenMed-green)](https://huggingface.co/OpenMed)

## 📋 Model Overview

This model is a **state-of-the-art** fine-tuned transformer engineered to deliver **enterprise-grade accuracy** for anatomical entity recognition - anatomical structures and body parts. This specialized model excels at identifying and extracting biomedical entities from clinical texts, research papers, and healthcare documents, enabling applications such as **drug interaction detection**, **medication extraction from patient records**, **adverse event monitoring**, **literature mining for drug discovery**, and **biomedical knowledge graph construction** with **production-ready reliability** for clinical and research applications.

### 🎯 Key Features
- **High Precision**: Optimized for biomedical entity recognition
- **Domain-Specific**: Trained on curated ANATOMY dataset
- **Production-Ready**: Validated on clinical benchmarks
- **Easy Integration**: Compatible with Hugging Face Transformers ecosystem

### 🏷️ Supported Entity Types

This model can identify and classify the following biomedical entities:

- `B-Anatomy`
- `I-Anatomy`

## 📊 Dataset

Anatomy corpus focuses on anatomical entity recognition for medical terminology and healthcare applications.

The Anatomy corpus is a specialized biomedical NER dataset designed for recognizing anatomical entities and medical terminology in clinical and biomedical texts. This corpus contains annotations for anatomical structures, body parts, organs, and physiological systems mentioned in medical literature. It is essential for developing clinical NLP systems, medical education tools, and healthcare informatics applications where accurate anatomical entity identification is crucial. The dataset supports the development of automated systems for medical coding, clinical decision support, and anatomical knowledge extraction from medical records and literature. It serves as a valuable resource for training NER models used in medical imaging, surgical planning, and clinical documentation.


## 📊 Performance Metrics

### Current Model Performance
- **F1 Score**: `0.81`
- **Precision**: `0.83`
- **Recall**: `0.79`
- **Accuracy**: `0.97`

### 🏆 Comparative Performance on ANATOMY Dataset

| Rank | Model | F1 Score | Precision | Recall | Accuracy |
|------|-------|----------|-----------|--------|-----------|
| 🥇 1 | [OpenMed-NER-AnatomyDetect-ElectraMed-560M](https://huggingface.co/OpenMed/OpenMed-NER-AnatomyDetect-ElectraMed-560M) | **0.9063** | 0.9083 | 0.9044 | 0.9825 |
| 🥈 2 | [OpenMed-NER-AnatomyDetect-PubMed-335M](https://huggingface.co/OpenMed/OpenMed-NER-AnatomyDetect-PubMed-335M) | **0.9063** | 0.8995 | 0.9131 | 0.9851 |
| 🥉 3 | [OpenMed-NER-AnatomyDetect-SuperClinical-434M](https://huggingface.co/OpenMed/OpenMed-NER-AnatomyDetect-SuperClinical-434M) | **0.9024** | 0.9040 | 0.9008 | 0.9836 |
|  4 | [OpenMed-NER-AnatomyDetect-ElectraMed-335M](https://huggingface.co/OpenMed/OpenMed-NER-AnatomyDetect-ElectraMed-335M) | **0.9020** | 0.9024 | 0.9016 | 0.9787 |
|  5 | [OpenMed-NER-AnatomyDetect-MultiMed-568M](https://huggingface.co/OpenMed/OpenMed-NER-AnatomyDetect-MultiMed-568M) | **0.9012** | 0.8977 | 0.9048 | 0.9812 |
|  6 | [OpenMed-NER-AnatomyDetect-PubMed-109M](https://huggingface.co/OpenMed/OpenMed-NER-AnatomyDetect-PubMed-109M) | **0.9004** | 0.8941 | 0.9067 | 0.9844 |
|  7 | [OpenMed-NER-AnatomyDetect-SuperMedical-355M](https://huggingface.co/OpenMed/OpenMed-NER-AnatomyDetect-SuperMedical-355M) | **0.9002** | 0.8974 | 0.9029 | 0.9815 |
|  8 | [OpenMed-NER-AnatomyDetect-BigMed-560M](https://huggingface.co/OpenMed/OpenMed-NER-AnatomyDetect-BigMed-560M) | **0.8980** | 0.9007 | 0.8954 | 0.9814 |
|  9 | [OpenMed-NER-AnatomyDetect-BioMed-335M](https://huggingface.co/OpenMed/OpenMed-NER-AnatomyDetect-BioMed-335M) | **0.8961** | 0.8941 | 0.8982 | 0.9830 |
|  10 | [OpenMed-NER-AnatomyDetect-BioClinical-108M](https://huggingface.co/OpenMed/OpenMed-NER-AnatomyDetect-BioClinical-108M) | **0.8961** | 0.8960 | 0.8962 | 0.9768 |


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
# Model: https://huggingface.co/OpenMed/OpenMed-NER-AnatomyDetect-ModernMed-149M
model_name = "OpenMed/OpenMed-NER-AnatomyDetect-ModernMed-149M"

# Create a pipeline
medical_ner_pipeline = pipeline(
    model=model_name,
    aggregation_strategy="simple"
)

# Example usage
text = "The patient complained of pain in the left ventricle region."
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
    "The patient complained of pain in the left ventricle region.",
    "Examination revealed inflammation of the hippocampus.",
    "The liver showed signs of fatty infiltration.",
    "An MRI of the cerebrum showed no signs of abnormalities.",
    "The procedure involved an incision near the femoral artery.",
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

- **Dataset**: ANATOMY
- **Description**: Anatomical Entity Recognition - Anatomical structures and body parts

### Training Details
- **Base Model**: ModernBERT-base
- **Training Framework**: Hugging Face Transformers
- **Optimization**: AdamW optimizer with learning rate scheduling
- **Validation**: Cross-validation on held-out test set

## 🔬 Model Architecture

- **Base Architecture**: ModernBERT-base
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