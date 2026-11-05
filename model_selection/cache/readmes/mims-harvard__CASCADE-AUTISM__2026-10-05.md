---
license: mit
tags:
  - single-cell
  - transcriptomics
  - biology
  - pytorch
---

<p align="center">
  <a href="https://valegiunchiglia.github.io/cascade-website/">
    <img src="banner.png" alt="CASCADE — Cross-System, Multi-Scale Single-Cell Foundation Model with Clinical Applications" width="100%">
  </a>
</p>

<h1 align="center">CASCADE: context-aware single-cell modelling links cellular programmes to patient-level disease phenotypes</h1>

<table align="center" border="0" cellspacing="0" cellpadding="4" style="border-collapse: collapse; border: none; background: transparent; margin-left: auto; margin-right: auto;">
  <tr>
    <td style="border: none; background: transparent;"><a href="https://mims-harvard.github.io/CASCADE-website/"><img src="https://img.shields.io/badge/Website-4CAF50?logo=googlechrome&logoColor=white" alt="Website"></a></td>
    <td style="border: none; background: transparent;"><a href="https://github.com/mims-harvard/CASCADE"><img src="https://img.shields.io/badge/Code-181717?logo=github&logoColor=white" alt="Code"></a></td>
    <td style="border: none; background: transparent;"><img src="https://img.shields.io/badge/Paper-coming%20soon-b31b1b?logo=arxiv&logoColor=white" alt="Paper (coming soon)"></td>
    <td style="border: none; background: transparent;"><img src="https://img.shields.io/badge/%F0%9F%A4%97%20Dataset-AUTISM-FFD21E" alt="Dataset: AUTISM"></td>
  </tr>
</table>

## Model Card

This repository contains a CASCADE checkpoint pre-trained on an autism spectrum disorder single-cell cohort.

## Introduction

CASCADE integrates contextual information into both input representation and pre-training
objectives, allowing the same cell to be interpreted through multiple biologically meaningful
axes and enabling patient-level phenotype prediction from single-cell profiles.

**1. Context-aware tokenisation.** Each cell is encoded as context-dependent up- and
down-regulated genes relative to a biologically defined reference group, producing multiple
representations per cell across disease, tissue, cell type, and treatment contexts.

**2. Context-specific representation learning.** Shared cell embeddings are projected through
separate context-specific projectors (disease, tissue, cell type, treatment), learning how
molecular programmes vary across biologically meaningful contexts via contrastive objectives.

**3. Patient representation & explainability.** Cell-level embeddings are aggregated across all
cells from a donor to produce a patient-level representation for multiscale phenotype
prediction. CASCADE-Explainer identifies the cell types and genes most responsible for each
prediction.

- Code: https://github.com/mims-harvard/CASCADE
- Project page: https://mims-harvard.github.io/CASCADE-website/
- Source dataset: https://cells.ucsc.edu/?ds=autism

## Training Data

- **Disease states** (2): ASD, Control
- **Tissues** (2): ACC, PFC
- **Cell types** (14): identified by Cell Ontology (CL) ID — CL:0000099, CL:0000115, CL:0000128, CL:0000129, CL:0000540, CL:0002453, CL:4023016, CL:4023017, CL:4023018, CL:4030059, .... Look up terms at https://www.ebi.ac.uk/ols4/ontologies/cl.

## Model Architecture

CASCADE's encoder (`TransformerGenerator`) is a shared transformer over context-aware gene
token sequences, followed by context-specific projection heads (one per context in the table
below) trained with a context-specific contrastive objective.

### Model Hyperparameters

| Hyperparameter | Value |
|---|---|
| Embedding dim (`d_model`) | 384 |
| Attention heads (`nhead`) | 6 |
| Transformer layers (`nlayers`) | 12 |
| Feedforward dim (`dim_embedding`) | 384 |
| Dropout | 0.1 |
| Vocabulary size | 17028 |
| Cell embedding style | `avg-pool` |
| Contexts | disease, cell_type, tissue |
| Context-specific projections | True |
| Domain adaptation (Sinkhorn) | True |

### Files Included

| File | Purpose |
|---|---|
| `model.safetensors` | Model weights only (stripped of optimizer/scheduler/scaler state) |
| `config.json` | Architecture hyperparameters needed to reconstruct `TransformerGenerator` |
| `tokenizer_dictionary_AUTISM.pkl` | Gene/context vocabulary (17028 tokens) used by the context-aware tokenizer |
| `metadata_dictionary_AUTISM.pkl` | Obs-column metadata mapping preserved from the source AnnData |
| `median_genes_*_all_AUTISM.pkl` | Per-context median expression reference used to derive up-/down-regulated gene tokens at tokenization time |

## Usage Instructions

The model architecture (`TransformerGenerator`) is not a standard `transformers` class, so
loading it requires the `cascade` package from the GitHub repo rather than `AutoModel`:

```bash
pip install git+https://github.com/mims-harvard/CASCADE
```

```python
import json, pickle
from huggingface_hub import hf_hub_download
from safetensors.torch import load_file
from cascade.model.cascade_model import TransformerGenerator

repo_id = "<your-org>/CASCADE-AUTISM"

config = json.load(open(hf_hub_download(repo_id, "config.json")))
vocab = pickle.load(open(hf_hub_download(repo_id, f"tokenizer_dictionary_AUTISM.pkl"), "rb"))
weights = load_file(hf_hub_download(repo_id, "model.safetensors"))

model = TransformerGenerator(
    d_model=config["d_model"],
    nhead=config["nhead"],
    ntoken=config["vocab_size"],
    dim_embedding=config["dim_embedding"],
    nlayers=config["nlayers"],
    vocab=vocab,
    nclass=config["nclass"],
    dropout=config["dropout"],
    pad_token=config["pad_token"],
    cell_emb_style=config["cell_emb_style"],
    context_specific_projections=config["context_specific_projections"],
    constant_ctx=config["constant_ctx"],
    only_contrastive=config["only_contrastive"],
    DA=config["DA"],
    lambda_sinkhorn=config["lambda_sinkhorn"],
    merged_contexts=config["merged_contexts"],
)
model.load_state_dict(weights)
model.eval()
```

To tokenize new raw data for this model, see `cascade/data/tokenizer.py` in the GitHub repo,
using the `tokenizer_dictionary_AUTISM.pkl` and `median_genes_*_all_AUTISM.pkl` files
from this repo as the vocab and per-context median reference respectively.

## Citation

Paper coming soon — see the [project page](https://mims-harvard.github.io/CASCADE-website/)
for updates.

## Contact

For any questions or feedback, please open an issue in the [GitHub repository](https://github.com/mims-harvard/CASCADE)
or contact [Valentina Giunchiglia](mailto:v.giunchiglia20@imperial.ac.uk) and
[Marinka Zitnik](mailto:marinka@hms.harvard.edu).
