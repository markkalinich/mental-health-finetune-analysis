---
license: mit
datasets:
- ncbi/pubmed
language:
- en
tags:
- biomedical-text
- nlp
- biomedical-nlp
- discharge-notes
- healthcare
- pubmed
pipeline_tag: feature-extraction
base_model:
- answerdotai/ModernBERT-base
library_name: transformers
---

# Clinical ModernBERT

Clinical ModernBERT is a state-of-the-art encoder-based transformer tailored specifically for biomedical and clinical text handling context length up to **8192 tokens**. Building on the innovations introduced by ModernBERT, this model extends the context window to 8,192 tokens and incorporates domain-specific vocabulary refinements. It is designed to produce semantically rich representations that capture both the nuanced syntax of biomedical literature and the intricate semantics of clinical narratives.

## Usage

Pretrained model weights and tokenizer artifacts are provided to facilitate easy integration with your downstream biomedical NLP tasks:

```python
from transformers import AutoModel, AutoTokenizer

model = AutoModel.from_pretrained('Simonlee711/Clinical_ModernBERT')
tokenizer = AutoTokenizer.from_pretrained('Simonlee711/Clinical_ModernBERT')
```

## Model Overview

Below is a table summarizing ModernBERT's key architectural components and their benefits:

| **Feature**                  | **Description**                                                                                           | **Benefit**                                                                                                      |
|------------------------------|-----------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|
| Extended Context Length      | Processes sequences up to **8,192 tokens**.                                                                   | Captures long-range dependencies and full document contexts, essential for complex linguistic tasks.             |
| GeGLU Activation             | Uses the GeGLU activation, a gated variant of GeLU.                                                       | Enhances non-linear representation and model stability by allowing controlled information flow.                   |
| Rotary Positional Embeddings | Implements RoPE to encode relative positional information.                                               | Provides robust handling of positional data, especially beneficial for extended contexts.                         |
| Flash Attention              | Employs Flash Attention to compute self-attention blockwise.                                             | Reduces memory overhead from quadratic to near-linear complexity, enabling efficient processing of long sequences. |

This model leverages a suite of modern architectural advancements including rotary positional embeddings (RoPE), Flash Attention for near-linear memory usage with extended contexts, and GeGLU activation layers that enhance representational capacity by integrating smooth gating mechanisms. By initializing from a ModernBERT-base checkpoint and applying domain-specific pre-training on approximately 40 million PubMed abstracts combined with MIMIC-IV clinical notes, Clinical ModernBERT is optimized to serve in tasks such as retrieval-augmented generation, fine-grained text classification, and domain-specific entity extraction.

## Pre-training Optimizations

| **Parameter**            | **Value**           | **Description**                                                     |
|--------------------------|---------------------|---------------------------------------------------------------------|
| Total Tokens             | 13,004,002,816      | Total number of tokens in the unified pre-training corpus           |
| Pre-training Corpus      | PubMed + MIMIC-IV + Medical Codes & Descriptions  | Combination of approximately 40M PubMed abstracts and MIMIC-IV Clinical notes and medical code and description pairs (ICD 9 Code 250.00: Diabetes mellitus without mention of complication, type II or unspecified type, not stated as uncontrolled.)  |
| Training Steps           | 150,000           | Total number of masked language modeling (MLM) training steps       |
| Batch Size               | 128                 | Batch size used during training                                     |


## Masked Language Modeling (MLM) Setup

Clinical ModernBERT is pre-trained using a multi-phase masked language modeling (MLM) strategy. A custom collator dynamically adjusts the masking probability—beginning at 30% and decreasing to 15% over the course of training—to emphasize medically relevant tokens (e.g., drug names, procedural codes). The MLM objective is defined as

$$
\mathcal{L}_{\text{MLM}} = - \sum_{i \in \mathcal{M}} \log p_\theta(x_i \mid \tilde{x}),
$$

where the model predicts masked tokens given their context. The table below summarizes the MLM evaluation framework without detailing specific metric scores:

| **Metric**       | **Top-1 Accuracy** | **Top-5 Accuracy** | **Top-10 Accuracy** | **Top-25 Accuracy** |
|------------------|--------------------|--------------------|---------------------|---------------------|
| **Value (%)**    | 63.31                | 79.67                | 83.33                | 88.10                |

This structure captures the granularity at which the model’s recovery of masked tokens is evaluated, with the understanding that higher top-\(k\) values reflect a broader lexical recall, and the model consistently ranks clinically appropriate tokens among its predictions.


## Intended Use

Clinical ModernBERT is ideally suited for tasks that demand an in-depth understanding of biomedical language. It is particularly valuable for clinical information retrieval, narrative classification, and structured medical coding. Researchers and practitioners may fine-tune this model for specialized downstream applications such as electronic health record analysis, clinical decision support systems, and evidence-based medical literature retrieval.

## Citations and Pre-training Source Code

The source code can be found here: [Clinical ModernBERT Github](https://github.com/Simonlee711/Clinical_ModernBERT)

Citing Model
```
@misc{simon_lee_2025,
	author       = { Simon A. Lee },
	title        = { Clinical_ModernBERT (Revision 24e72d6) },
	year         = 2025,
	url          = { https://huggingface.co/Simonlee711/Clinical_ModernBERT },
	doi          = { 10.57967/hf/4999 },
	publisher    = { Hugging Face }
}
```

Citing Paper
```
@article{lee2025clinical,
  title={Clinical ModernBERT: An efficient and long context encoder for biomedical text},
  author={Lee, Simon A and Wu, Anthony and Chiang, Jeffrey N},
  journal={arXiv preprint arXiv:2504.03964},
  year={2025}
}
```

## Questions

email (simonlee711@g.ucla.edu)