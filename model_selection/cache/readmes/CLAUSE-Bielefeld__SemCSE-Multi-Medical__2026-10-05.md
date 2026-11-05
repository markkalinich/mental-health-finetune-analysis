---
library_name: transformers
tags:
- embedding
- scientific
- abstract
license: mit
language:
- en
base_model:
- KISTI-AI/Scideberta-full
pipeline_tag: feature-extraction
---

# SemCSE-Multi-Medical Model Card

SemCSE-multi is a multifaceted embedding model that predicts multiple, aspect-specific embeddings for a given scientific text.
This version of the model is targeted to the medical domain. It encodes the aspects: Disease, Patient Group, Methodology

The individual aspect-specific embeddings can then be used to evaluate the similarity of two studies with regards to just that aspect in isolation.
For details, please see [our paper](https://arxiv.org/abs/2510.11599).

## Model Details

### Model Description

- **Developed by:** CLAUSE group at Bielefeld University
- **Model type:** DeBERTa
- **Languages:** English
- **Finetuned from model:** [KISTI-AI/Scideberta-full](https://huggingface.co/KISTI-AI/Scideberta-full) with additional projection heads

### Model Sources

- **Repository:** [github.com/inas-argumentation/SemCSE-Multi](https://github.com/inas-argumentation/SemCSE-Multi)
- **Paper:** [https://arxiv.org/abs/2510.11599](https://arxiv.org/abs/2510.11599)

## How to Get Started with the Model

Minimal example on how to create embeddings with our model:
```
from transformers import AutoTokenizer, AutoModel

model = AutoModel.from_pretrained("CLAUSE-Bielefeld/SemCSE-Multi-Medical", trust_remote_code=True)
tokenizer = AutoTokenizer.from_pretrained("CLAUSE-Bielefeld/SemCSE-Multi-Medical")

text = "This is a scientific abstract from the medical domain."
batch = tokenizer([text], return_tensors='pt')

# Get the embedding for the "disease" aspect. Other options are: "patient_group" and "methodology".
output = model(**batch)["disease"]

# The resulting embeddings can be used for similarity assessments using cosine similarity.
```

## Training Details

This model was trained on a dataset of summaries for 15000 scientific abstracts from from the medical domain (PubMed).
We used a contrastive loss to encourage summaries of the same abstract to be placed nearby in the embedding space. This is done for each aspect separately, and the individual models are then distilled into a single, multifaceted embedding model. 
The dataset and exact training procedure can be found in our [GitHub repo](https://github.com/inas-argumentation/SemCSE-Multi).

## Evaluation

Our model achieves state-of-the-art scores for performing precise, apsect-specific similarity assessments. The evaluations are included in [our paper](https://arxiv.org/abs/2510.11599).

## Citation

**BibTeX:**

```bibtex
@misc{brinner2025semcsemultimultifaceteddecodableembeddings,
      title={SemCSE-Multi: Multifaceted and Decodable Embeddings for Aspect-Specific and Interpretable Scientific Domain Mapping}, 
      author={Marc Brinner and Sina Zarrieß},
      year={2025},
      eprint={2510.11599},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2510.11599}, 
}
```
